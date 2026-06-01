#!/usr/bin/env python3
"""Lightweight smoke-check for MainGit

Performs safe import/runtime checks for core modules without requiring heavy external deps.
Exit code 0 on success, 2 on partial/complete failure.
"""

from __future__ import annotations

import importlib
import importlib.util
import sys
import traceback
from pathlib import Path
from types import ModuleType

REPO_ROOT = Path(__file__).resolve().parent


def _load_module_from_path(path: Path, name: str | None = None) -> ModuleType:
    """Load a module from a file path without requiring it to be a package."""
    if not path.exists():
        raise FileNotFoundError(f"Module file not found: {path}")
    name = name or path.stem
    spec = importlib.util.spec_from_file_location(name, str(path))
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not create module spec for {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[arg-type]
    return module


def run_check(name: str, fn):
    try:
        ok, msg = fn()
    except Exception as exc:
        tb = traceback.format_exc()
        print(f"[FAIL] {name}: Exception: {exc}\n{tb}")
        return False
    else:
        if ok:
            print(f"[OK]   {name}: {msg}")
            return True
        else:
            print(f"[FAIL] {name}: {msg}")
            return False


# --- checks ---

def check_mgscripts_load_env():
    try:
        mod = importlib.import_module("MGScripts.bootstrap")
    except Exception as exc:
        return False, f"Import failed: {exc}"

    if not hasattr(mod, "load_env"):
        return False, "MGScripts.bootstrap missing load_env"

    try:
        ns = mod.load_env()
        required = ["speak", "reload_all", "add_script"]
        present = [k for k in required if k in ns]
        if not present:
            return False, f"load_env returned a namespace but missing keys: {required}"
        return True, f"load_env OK; keys present: {present}"
    except Exception as exc:
        return False, f"load_env() raised: {exc}"


def check_documents_build_namespace():
    try:
        path = REPO_ROOT / "Documents" / "bootstrap.py"
        mod = _load_module_from_path(path, "documents_bootstrap")
    except Exception as exc:
        return False, f"Import failed: {exc}"

    if not hasattr(mod, "build_namespace"):
        return False, "Documents.bootstrap missing build_namespace"

    try:
        ns = mod.build_namespace()
        keys = ["DOCUMENTS_ROOT", "NOTES_ROOT", "open_notes"]
        present = [k for k in keys if k in ns]
        if not present:
            return False, f"build_namespace returned but missing keys: expected {keys}, got {present}"
        return True, f"build_namespace OK; keys present: {present}"
    except Exception as exc:
        return False, f"build_namespace() raised: {exc}"


def check_computerspeak():
    try:
        path = REPO_ROOT / "Documents" / "SurzsEnviro" / "computerspeak.py"
        mod = _load_module_from_path(path, "computerspeak")
    except Exception as exc:
        return False, f"Import failed: {exc}"

    if not hasattr(mod, "ComputerSpeak"):
        return False, "computerspeak missing ComputerSpeak"

    try:
        cls = getattr(mod, "ComputerSpeak")
        inst = cls()
        note = inst.speak("smoke-check")
        return True, f"ComputerSpeak.speak() returned: {note!r}"
    except Exception as exc:
        return False, f"ComputerSpeak usage raised: {exc}"


def check_packet_sniffer_importable():
    try:
        path = REPO_ROOT / "Documents" / "SurzsEnviro" / "catchingpackets.py"
        mod = _load_module_from_path(path, "catchingpackets")
    except Exception as exc:
        return False, f"Import failed: {exc}"

    if not hasattr(mod, "PacketSniffer"):
        return False, "catchingpackets missing PacketSniffer"

    return True, "PacketSniffer importable (no runtime capture started)"


def check_target_config():
    try:
        path = REPO_ROOT / "Documents" / "SurzsEnviro" / "target_config.py"
        mod = _load_module_from_path(path, "target_config")
    except Exception as exc:
        return False, f"Import failed: {exc}"

    present = []
    for name in ("prompt_for_missing", "get_runtime_scope"):
        if hasattr(mod, name):
            present.append(name)
    if not present:
        return False, "target_config missing expected helpers"
    return True, f"target_config has helpers: {present}"


def main():
    checks = [
        ("MGScripts.load_env", check_mgscripts_load_env),
        ("Documents.build_namespace", check_documents_build_namespace),
        ("ComputerSpeak", check_computerspeak),
        ("PacketSniffer(import)", check_packet_sniffer_importable),
        ("target_config", check_target_config),
    ]

    ok = 0
    total = len(checks)
    for name, fn in checks:
        if run_check(name, fn):
            ok += 1

    print(f"\n{ok}/{total} checks passed.")
    sys.exit(0 if ok == total else 2)


if __name__ == "__main__":
    main()
