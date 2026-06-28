#!/usr/bin/env python3
"""
PD Media Preprocessor — watches a directory for new video files and processes them
through an FFmpeg pipeline (deinterlace → denoise → upscale → audio normalize).

Usage: Drop this into any folder, run it, then drop/download videos there.
       Finished files appear in ./output/ ready for OBS.
"""

import os
import sys
import json
import shutil
import subprocess
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

# ─── Configuration ──────────────────────────────────────────────
OUTPUT_DIR = "output"  # where finished files land (relative to script dir)
WORKING_DIR = ".processing"  # temp staging area, deleted on completion
LOG_FILE = None  # set to a path like "process.log" if you want file logging

# Video extensions to watch for. Add/remove as needed.
WATCH_EXTENSIONS = [
    "*.mkv", "*.mp4", "*.avi", "*.mov", "*.flv", "*.wmv",
    "*.webm", "*.ogv", "*.ts", "*.m2ts"
]

# Target output resolution height (width auto-scaled to preserve aspect ratio)
TARGET_HEIGHT = 720

# Bitrate for video (adjust based on your network/GPU encoding headroom)
VIDEO_BITRATE = "4M"

# Audio loudnorm settings (EBU R128 compliant, good for streaming consistency)
AUDIO_LOUDNORM_I = -16       # Integrated target loudness in LUFS
AUDIO_LOUDNORM_LRA = 11     # Loudness Range target
AUDIO_LOUDNORM_TP = -1.5    # True Peak ceiling

# Hardware acceleration: set to 'auto' for auto-detect, or a specific pixel format like 'cuda', 'vaapi', etc.
HARDWARE_ACCEL = "auto"  # Set to empty string "" to force software decoding only

# ─── End Configuration ────────────────────────────────────────


def log(msg: str):
    """Print and optionally write to a log file."""
    print(f"[{Path(__file__).stem.upper()}] {msg}")
    if LOG_FILE:
        with open(LOG_FILE, "a") as f:
            f.write(f"{msg}\n")


def get_ffmpeg_hw_flags() -> list[str]:
    """Detect available hardware acceleration and return FFmpeg flags."""
    hw = HARDWARE_ACCEL

    # If user forced software only
    if not hw or hw == "none":
        log("Info: Hardware acceleration disabled (software decoding).")
        return []

    candidates = ["cuda", "vaapi", "vdpau"]
    if hw != "auto":
        candidates = [hw]  # user specified one explicitly

    for accel in candidates:
        try:
            result = subprocess.run(
                ["ffmpeg", "-hide_banner", "-init_hw_device", accel],
                capture_output=True, timeout=5
            )
            if result.returncode == 0 or "hwdevice" not in result.stderr.decode().lower():
                log(f"Info: Using {accel.upper()} hardware acceleration.")
                hw = accel
                break
        except Exception:
            continue

    else:
        # Nothing found, fall back to software
        log("Warning: No hardware acceleration detected. Falling back to software decoding.")
        return []

    if hw == "cuda":
        pix_fmt_out = "yuv420p"
        extra_hw_args = ["-hwaccel_output_format", "rawvideo"]
    elif hw == "vaapi":
        pix_fmt_out = "nv12_vaapi|nv12"
        # VAAPI handles its own output format in the filter chain
        return [f"-init_hw_device", f"{hw}=gpu:/dev/dri/renderD128"] + \
               ["-vf", f"format=nv12|vaapi, hwupload,scale_vaapi=h={TARGET_HEIGHT}:-2:format=yuv420p,hwdownload"]

    else:
        pix_fmt_out = "yuv420p"

    return [f"-hwaccel", hw] + extra_hw_args


def probe_video(filepath: Path) -> dict | None:
    """Use ffprobe to get video/audio stream info."""
    try:
        result = subprocess.run(
            ["ffprobe", "-v", "quiet", "-print_format", "json",
             "-show_streams", "-show_format", str(filepath)],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode != 0:
            log(f"Warning: ffprobe failed for {filepath.name}")
            return None

        data = json.loads(result.stdout)
        # Find the first video stream
        video_stream = next(
            (s for s in data.get("streams", []) if s["codec_type"] == "video"),
            None
        )
        audio_stream = next(
            (s for s in data.get("streams", []) if s["codec_type"] == "audio"),
            None
        )

        info = {
            "has_video": video_stream is not None,
            "has_audio": audio_stream is not None,
            "width": int(video_stream["width"]) if video_stream else 0,
            "height": int(video_stream["height"]) if video_stream else 0,
            "codec_name": video_stream.get("codec_name", "?") if video_stream else "?",
            "sample_rate": int(audio_stream["sample_rate"]) if audio_stream and "sample_rate" in audio_stream else 48000,
        }

        # Detect interlaced content from side data or codec hints
        info["interlaced"] = False
        if video_stream:
            field_order = video_stream.get("field_order", "")
            if any(x in str(field_order).lower() for x in ["tb", "bt", "tff", "bff", "interlace"]):
                info["interlaced"] = True

        return info

    except Exception as e:
        log(f"Error probing {filepath.name}: {e}")
        return None


def build_ffmpeg_command(src: Path, dst: Path) -> list[str]:
    """Build the FFmpeg command for processing this file."""
    probe = probe_video(src) or {}

    cmd = ["ffmpeg", "-y"]  # -y to overwrite without prompting

    # Hardware acceleration flags (prepend before input)
    hw_flags = get_ffmpeg_hw_flags()
    if hw_flags:
        cmd.extend(hw_flags)

    cmd.append("-i")
    cmd.append(str(src))

    # ── Video Filter Chain ────────────────────────────────
    vf_parts = []

    # 1. Deinterlace (only for interlaced or SD content — height < 720 is a good heuristic)
    if probe.get("interlaced") or probe.get("height", 480) <= 576:
        log(f"Info: {src.name} detected as interlaced/SD → deinterlacing with yadif.")
        vf_parts.append("yadif=0:-1:0")

    # 2. Denoise (light temporal + spatial denoise — conservative to preserve detail)
    vf_parts.append(
        "hqdn3d=strong=0.5:fast=0.5:dark_mode=1"
    )

    # 3. Scale to target height, maintain aspect ratio, ensure even dimensions (H.264 requirement)
    vf_parts.append(f"scale=-2:{TARGET_HEIGHT}")

    # 4. Color space normalization → Rec.709 for streaming compatibility
    vf_parts.append("format=yuv420p")

    video_filter = ",".join(vf_parts)

    cmd.extend(["-vf", video_filter])

    # ── Audio Filter Chain ────────────────────────────────
    af_parts = []

    if probe.get("has_audio"):
        sr = max(probe.get("sample_rate", 48000), 44100)
        target_sr = min(sr, 48000)  # Cap at 48kHz for streaming efficiency

        af_parts.append(f"aresample={target_sr}")

        # Two-pass loudnorm: first pass measures, second applies (simplified single-pass here)
        af_parts.append(
            f"loudnorm=I={AUDIO_LOUDNORM_I}:LRA={AUDIO_LOUDNORM_LRA}:"
            f"TP={AUDIO_LOUDNORM_TP}"
        )

    else:
        # No audio stream — generate silence to avoid FFmpeg errors in some players/OBS
        af_parts.append("anullsrc=channel_layout=stereo:sample_rate=48000")

    if af_parts:
        cmd.extend(["-af", ",".join(af_parts)])

    # ── Output Encoding Settings ────────────────────────────
    # Video codec — use hardware encoder if available, fall back to libx264
    try:
        result = subprocess.run(
            ["ffmpeg", "-encoders"], capture_output=True, text=True, timeout=5
        )
        encoders_available = set(result.stdout.split())

        hw_encoder_map = {
            "h264_nvenc": ("cuda"),
            "vaapi_h264": ("vaapi"),
        }

        encoder_used = None
        for enc, req in hw_encoder_map.items():
            if enc in encoders_available:
                cmd.extend(["-c:v", f"{req}_h264" if req != "cuda" else "h264_nvenc"])
                # For NVIDIA NVENC with hardware accel input, need extra flags
                encoder_used = enc

        if not encoder_used and "libx265" in encoders_available:
            cmd.extend(["-c:v", "libx265", "-crf", "28"])  # x265 at higher CRF for speed/size balance
        elif not encoder_used and "libx264" in encoders_available:
            cmd.extend(["-c:v", "libx264", "-preset", "fast", "-crf", "23"])

    except Exception as e:
        log(f"Warning: Could not detect available encoders ({e}). Using libx264.")
        # Final fallback — this should almost always exist if ffmpeg is installed at all
        cmd.extend(["-c:v", "libx264", "-preset", "fast", "-crf", "23"])

    # Audio codec (AAC, streaming standard)
    if probe.get("has_audio"):
        cmd.extend([
            "-c:a", "aac",
            "-b:a", "192k",
            "-movflags", "+faststart"  # Web-friendly: moov atom at front for fast seeking
        ])

    # Container settings
    cmd.extend(["-f", "mp4"])
    cmd.append(str(dst))

    return cmd


def process_file(filepath: Path):
    """Main processing function — runs the FFmpeg pipeline."""
    name = filepath.name
    stem = filepath.stem

    log(f"Processing started for {name}")

    # Create working output dir if needed
    out_dir = OUTPUT_DIR_PATH / stem.replace(" ", "_")
    work_dir = WORKING_DIR_PATH / stem.replace(" ", "_")

    try:
        os.makedirs(out_dir, exist_ok=True)

        # Build command and run FFmpeg (two-pass loudnorm for best results)
        dst_path = out_dir / f"{stem}_processed.mp4"

        if dst_path.exists():
            log(f"Skipping {name} — already processed at {dst_path.name}")
            return True

        cmd = build_ffmpeg_command(filepath, dst_path)
        log(f"Running FFmpeg for {name}...")

        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=None
        )

        if result.returncode != 0:
            # Extract the last few lines of stderr as they usually contain the error
            errors = "\n".join(result.stderr.strip().split("\n")[-15:])
            log(f"ERROR processing {name}: FFmpeg exited with code {result.returncode}")
            log(f"FFmpeg output: {errors[:500]}...")

            # Save a copy of full stderr for debugging if needed
            err_log = out_dir / f"{stem}_ffmpeg_error.log"
            err_log.write_text(result.stderr)
            return False

        else:
            file_size_mb = dst_path.stat().st_size / (1024 * 1024)
            log(f"✅ {name} → {dst_path.name} ({file_size_mb:.1f} MB)")
            return True

    except subprocess.TimeoutExpired:
        # This shouldn't happen since timeout=None, but just in case
        pass
    except Exception as e:
        log(f"FATAL error processing {name}: {e}")
        return False


# ─── Watchdog Handler ──────────────────────────────────────────

SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR_PATH = SCRIPT_DIR / OUTPUT_DIR
WORKING_DIR_PATH = SCRIPT_DIR / WORKING_DIR


class ProcessHandler(PatternMatchingEventHandler):
    """Handles new files appearing in the watched directory."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, patterns=WATCH_EXTENSIONS, ignore_directories=True, case_sensitive=False)
        self._processing = set()  # Track what we're currently working on

    def process_created(self, event: object):
        """Called when a new file is created."""
        filepath = Path(event.src_path)
        if not filepath.is_file():
            return
        key = (filepath.absolute(), "created")
        self._processing.add(key)
        try:
            process_file(filepath)
        finally:
            self._processing.discard(key)

    def on_created(self, event):
        """Watchdog callback for new files."""
        if not hasattr(event.src_path, "") or Path(event.src_path).is_dir():
            return  # Ignore directories and weird events
        filepath = Path(event.src_path)
        self.process_created(event)


def scan_existing_files(directory: Path):
    """Process any matching video files already present in the directory on startup."""
    found = False
    for ext_group in WATCH_EXTENSIONS:
        matches = list(directory.glob(ext_group))
        for filepath in sorted(matches):
            # Skip our own output/ and .processing directories
            if OUTPUT_DIR_PATH.name in str(filepath) or WORKING_DIR_PATH.name in str(filepath):
                continue
            found = True
            process_file(filepath)

    return found


# ─── Main Entry Point ──────────────────────────────────────


def main():
    log("=" * 60)
    log("PD Media Preprocessor")
    log(f"Watching: {SCRIPT_DIR}")
    log(f"Output dir: {OUTPUT_DIR_PATH}")
    log(f"Extensions tracked: {', '.join(WATCH_EXTENSIONS)}")
    log(f"Target resolution height: {TARGET_HEIGHT}p")

    if HARDWARE_ACCEL != "none":
        try:
            ffmpeg_check = subprocess.run(
                ["ffmpeg", "-version"], capture_output=True, text=True, timeout=5
            )
            if ffmpeg_check.returncode == 0:
                version_line = ffmpeg_check.stdout.split("\n")[0]
                log(f"FFmpeg found: {version_line.strip()}")
            else:
                sys.exit("ERROR: FFmpeg is not installed or not in PATH. Run: sudo apt install -y ffmpeg")
        except FileNotFoundError:
            sys.exit("FATAL: 'ffmpeg' command not found. Install it with: sudo apt install -y ffmpeg")

    # Create output directory upfront so we can verify write access works
    try:
        os.makedirs(OUTPUT_DIR_PATH, exist_ok=True)
        test_file = OUTPUT_DIR_PATH / ".write_test"
        test_file.touch()
        test_file.unlink()  # Clean up immediately to avoid confusion with actual media files
    except PermissionError as e:
        sys.exit(f"FATAL: Cannot write to output directory {OUTPUT_DIR_PATH}: {e}")

    log("Scanning for existing video files...")
    found = scan_existing_files(SCRIPT_DIR)

    if not found:
        log("No matching videos found. Drop any into this folder and they'll be processed.")

    # Set up the observer to watch new arrivals going forward
    event_handler = ProcessHandler()
    observer = Observer(timeout=10)  # Polling interval in seconds for Linux (inotify doesn't need polling but watchdog normalizes cross-platform behavior here anyway)
    observer.schedule(event_handler, str(SCRIPT_DIR), recursive=False)

    log("Observer started. Press Ctrl+C to stop.")
    try:
        observer.start()
        while True:
            import time
            time.sleep(10)  # Main thread sleep; watchdog handles events in its own threads
    except KeyboardInterrupt:
        log("\nStopping...")
        observer.stop()

    observer.join()
    log("Done.")


if __name__ == "__main__":
    main()