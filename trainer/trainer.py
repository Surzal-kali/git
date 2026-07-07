"""Persistent training loop that survives session disconnects."""

from __future__ import annotations

import os
import time
import threading
from pathlib import Path
from typing import Callable, Optional

import torch
import torch.nn as nn
import torch.optim as optim

from trainer.checkpoint import CheckpointManager


class PersistentTrainer:
    """Training loop with checkpoint/resume capability.
    
    The loop runs in a background thread and can be started/stopped/restarted
    from any endpoint (WebUI, terminal) via the FastAPI API.
    """

    def __init__(
        self,
        model: nn.Module,
        train_loader,
        criterion: nn.Module,
        checkpoint_dir: str | Path = "/workspace/checkpoints",
        save_interval_epochs: int = 5,
        device: Optional[torch.device] = None,
    ):
        self.model = model.to(device or torch.device("cpu"))
        self.train_loader = train_loader
        self.criterion = criterion
        self.optimizer = optim.Adam(self.model.parameters(), lr=1e-3)
        self.checkpoint_mgr = CheckpointManager(checkpoint_dir)

        self.save_interval = save_interval_epochs
        self.epoch = 0
        self.running = False
        self._thread: Optional[threading.Thread] = None
        self._stop_event = threading.Event()
        self.device = device or torch.device("cpu")

        # Training stats
        self.loss_history: list[float] = []
        self.epoch_losses: list[tuple[int, float]] = []

    def _train_epoch(self) -> float:
        """Train for one epoch. Returns average loss."""
        self.model.train()
        total_loss = 0.0
        num_batches = 0

        for batch_idx, (data, target) in enumerate(self.train_loader):
            data, target = data.to(self.device), target.to(self.device)

            self.optimizer.zero_grad()
            output = self.model(data)
            loss = self.criterion(output, target)
            loss.backward()
            self.optimizer.step()

            total_loss += loss.item()
            num_batches += 1

        avg_loss = total_loss / max(num_batches, 1)
        return avg_loss

    def train(self, epochs: int = 100, start_epoch: int = 0):
        """Run the training loop in a background thread."""
        if self.running:
            raise RuntimeError("Training is already running. Stop it first.")

        self.running = True
        self._stop_event.clear()
        self.epoch = start_epoch

        def _run():
            try:
                for i in range(start_epoch, start_epoch + epochs):
                    if self._stop_event.is_set():
                        print(f"[trainer] Stopped at epoch {i}")
                        break

                    epoch_loss = self._train_epoch()
                    self.epoch_losses.append((i, epoch_loss))
                    self.loss_history.append(epoch_loss)
                    self.epoch = i + 1

                    if (i + 1) % self.save_interval == 0:
                        ckpt = self.checkpoint_mgr.save(
                            self.model, self.optimizer, i + 1, epoch_loss
                        )
                        print(f"[trainer] Epoch {i+1}/{start_epoch+epochs} | "
                              f"Loss: {epoch_loss:.4f} | Checkpoint saved: {ckpt.name}")

                    # Print progress every 10 epochs
                    if (i + 1) % 10 == 0:
                        print(f"[trainer] Epoch {i+1}/{start_epoch+epochs} | "
                              f"Loss: {epoch_loss:.4f}")

            except Exception as e:
                print(f"[trainer] Error during training: {e}")
            finally:
                self.running = False

        self._thread = threading.Thread(target=_run, daemon=True)
        self._thread.start()
        print(f"[trainer] Training started: {epochs} epochs from epoch {start_epoch}")

    def stop(self):
        """Stop the training loop gracefully."""
        if not self.running:
            return
        self._stop_event.set()
        # Save final checkpoint
        if self.epoch_losses:
            last_epoch, last_loss = self.epoch_losses[-1]
            ckpt = self.checkpoint_mgr.save(
                self.model, self.optimizer, last_epoch + 1, last_loss
            )
            print(f"[trainer] Final checkpoint saved: {ckpt.name}")

    def resume(self, epochs: int = 50):
        """Resume training from the latest checkpoint."""
        state = self.checkpoint_mgr.load_latest()
        if state is None:
            raise RuntimeError("No checkpoint found to resume from.")

        # Restore model and optimizer state
        self.model.load_state_dict(state["model_state_dict"])
        self.optimizer.load_state_dict(state["optimizer_state_dict"])

        start_epoch = state["epoch"]
        print(f"[trainer] Resuming from epoch {start_epoch} (last loss: {state['loss']:.4f})")
        self.train(epochs=epochs, start_epoch=start_epoch)

    def status(self) -> dict:
        """Return current training status."""
        return {
            "running": self.running,
            "epoch": self.epoch,
            "total_epochs_trained": len(self.epoch_losses),
            "latest_loss": self.epoch_losses[-1][1] if self.epoch_losses else None,
            "checkpoint_status": self.checkpoint_mgr.status(),
        }
