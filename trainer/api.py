"""FastAPI endpoints for the persistent trainer."""

from __future__ import annotations


from contextlib import asynccontextmanager
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from trainer.trainer import PersistentTrainer
from trainer.checkpoint import CheckpointManager


# Global trainer instance (initialized on first request)
_trainer: Optional[PersistentTrainer] = None


def get_trainer() -> PersistentTrainer:
    global _trainer
    if _trainer is None:
        raise RuntimeError("Trainer not initialized. Call /init first.")
    return _trainer


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: nothing yet — trainer initializes on demand
    yield
    # Shutdown: stop training gracefully
    if _trainer and _trainer.running:
        _trainer.stop()


app = FastAPI(title="Homelab Neural Network Trainer", lifespan=lifespan)


# --- Request/Response models ---

class InitRequest(BaseModel):
    model_class: str  # e.g., "SimpleNet"
    epochs: int = 100
    save_interval: int = 5
    checkpoint_dir: str = "/workspace/checkpoints"


class TrainRequest(BaseModel):
    epochs: int = 50


class StopRequest(BaseModel):
    pass


# --- Endpoints ---

@app.get("/status")
def status():
    """Get current training status."""
    trainer = get_trainer()
    return trainer.status()


@app.post("/init")
def init(req: InitRequest):
    """Initialize the trainer with a model.
    
    This is where you'd define your model architecture.
    For now, we use a placeholder — replace with your actual model.
    """
    global _trainer
    
    # If _trainer already exists and is training...
    # The old one gets garbage collected but its thread keeps running!
    
    _trainer = PersistentTrainer(
        model=None,
        train_loader=None,
        criterion=None,
        checkpoint_dir=req.checkpoint_dir,
        save_interval_epochs=req.save_interval,
    )
    
    return {"message": "Trainer initialized", "model": req.model_class}


@app.post("/train")
def train(req: TrainRequest):
    """Start training."""
    trainer = get_trainer()
    try:
        trainer.train(epochs=req.epochs)
        return {"message": f"Training started for {req.epochs} epochs"}
    except RuntimeError as e:  # ← caught!
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/resume")
def resume(req: TrainRequest):
    """Resume training from latest checkpoint."""
    trainer = get_trainer()
    try:
        trainer.resume(epochs=req.epochs)  # raises RuntimeError if no checkpoint
        return {"message": f"Training resumed for {req.epochs} epochs"}
    except RuntimeError as e:  # ← this IS caught, so actually fine!



            @app.post("/stop")
            def stop():
                """Stop training and save final checkpoint."""
                trainer = get_trainer()  # ← if _trainer is None, this CRASHES
                trainer.stop()
                return {"message": "Training stopped"}


@app.get("/checkpoints")
def list_checkpoints():
    """List all saved checkpoints."""
    trainer = get_trainer()  # ← same crash
    return trainer.checkpoint_mgr.status()
