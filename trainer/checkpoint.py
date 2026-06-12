"""Persistent training loop with checkpoint/resume capability."""

from __future__ import annotations

import json
import os
import time
import threading
from pathlib import Path
from typing import Any, Dict, Optional

import torch
import torch.nn as nn


class CheckpointManager:
    """Save and restore model + optimizer state to disk."""

    def __init__(self, checkpoint_dir: str | Path = "/workspace/checkpoints"):
        self.checkpoint_dir = Path(checkpoint_dir)
        self.checkpoint_dir.mkdir(parents=True, exist_ok=True)
        self.meta_path = self.checkpoint_dir / "meta.json"
        self._lock = threading.Lock()

    def save(
        self,
        model: nn.Module,
        optimizer: torch.optim.Optimizer,
        epoch: int,
        loss: float,
        extra: Optional[Dict[str, Any]] = None,
    ) -> Path:
        """Save a checkpoint and return the path."""
        ts = int(time.time())
        ckpt_name = f"checkpoint_epoch_{epoch}_{ts}.pt"
        ckpt_path = self.checkpoint_dir / ckpt_name

        state = {
            "model_state_dict": model.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
            "epoch": epoch,
            "loss": loss,
            "timestamp": ts,
        }
        if extra:
            state["extra"] = extra

        with self._lock:
            torch.save(state, ckpt_path)

        # Update metadata
        meta = {"latest_checkpoint": str(ckpt_path), "epoch": epoch, "loss": loss}
        with open(self.meta_path, "w") as f:
            json.dump(meta, f, indent=2)

        return ckpt_path

    def load_latest(self) -> Optional[Dict[str, Any]]:
        """Load the latest checkpoint if it exists."""
        if not self.meta_path.exists():
            return None

        with open(self.meta_path) as f:
            meta = json.load(f)

        ckpt_path = Path(meta["latest_checkpoint"])
        if not ckpt_path.exists():
            return None

        return torch.load(ckpt_path, map_location="cpu", weights_only=False)

    def list_checkpoints(self) -> list[Dict[str, Any]]:
        """List all saved checkpoints."""
        pts = sorted(self.checkpoint_dir.glob("checkpoint_epoch_*.pt"))
        return [
            {
                "file": p.name,
                "size_bytes": p.stat().st_size,
                "modified": int(p.stat().st_mtime),
            }
            for p in pts
        ]

    def status(self) -> Dict[str, Any]:
        """Return current checkpoint status."""
        meta = {}
        if self.meta_path.exists():
            with open(self.meta_path) as f:
                meta = json.load(f)
        return {
            "checkpoint_dir": str(self.checkpoint_dir),
            "latest": meta,
            "checkpoints": self.list_checkpoints(),
        }
