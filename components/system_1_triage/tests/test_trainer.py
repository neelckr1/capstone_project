"""TDD Unit Tests for SystemOneTrainer."""

import os
import pytest
from train.trainer import SystemOneTrainer


def test_trainer_initialization():
    """Verify trainer parameter initialization and default model IDs."""
    trainer = SystemOneTrainer(model_type="modernbert")
    assert trainer.model_id == "answerdotai/ModernBERT-base"
    assert trainer.batch_size == 8

    trainer_llama = SystemOneTrainer(model_type="llama_1b")
    assert trainer_llama.model_id == "Qwen/Qwen2.5-1.5B"

    trainer_clef = SystemOneTrainer(model_type="clef_flash")
    assert trainer_clef.model_id == "Cloudflare/clef-flash"


def test_trainer_dry_run_execution(tmp_path):
    """Verify dry_run simulation execution and checkpoint generation."""
    out_dir = str(tmp_path / "checkpoints")
    trainer = SystemOneTrainer(
        model_type="modernbert",
        output_dir=out_dir,
        epochs=1,
    )
    result = trainer.train(dry_run=True)
    assert result["status"] == "success"
    assert result["epochs_completed"] == 1
    assert os.path.exists(result["checkpoint_path"])
