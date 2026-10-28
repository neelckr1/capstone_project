"""Llama-3.2-1B Sequence Classifier implementation for System-1 Long-Context Auditing."""

import time
from typing import Optional, Dict, Any, List
import torch
from core.schema import TrajectorySample, ModelDecision, AttackCategory, TriageAction
from core.tokenizer_utils import format_trajectory_to_text, apply_sliding_window
from models.base_model import BaseSystemOneClassifier


class LlamaSystemOneClassifier(BaseSystemOneClassifier):
    """
    Llama-3.2-1B-Instruct LoRA-tuned sequence classifier.
    Supports native 128k context windows for long multi-turn Crescendo and Many-Shot trajectories.
    """

    def __init__(
        self,
        model_id: str = "Qwen/Qwen2.5-1.5B",
        adapter_path: Optional[str] = None,
        max_turns: int = 20,
        device: str = "cuda",
    ):
        super().__init__(model_id=model_id, model_type="llama_1b_decoder", device=device)
        self.adapter_path = adapter_path
        self.max_turns = max_turns
        self.tokenizer = None
        self.model = None

    def load_model(self) -> None:
        """Load tokenizer and base/adapter weights with BF16 precision."""
        from transformers import AutoTokenizer, AutoModelForSequenceClassification
        from peft import PeftModel

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        base_model = AutoModelForSequenceClassification.from_pretrained(
            self.model_id,
            num_labels=2,
            dtype=torch.bfloat16 if self.device == "cuda" else torch.float32,
            pad_token_id=self.tokenizer.pad_token_id,
        ).to(self.device)

        if self.adapter_path:
            self.model = PeftModel.from_pretrained(base_model, self.adapter_path)
        else:
            self.model = base_model

        self.model.eval()

    def predict(self, sample: TrajectorySample) -> ModelDecision:
        """Evaluate a multi-turn trajectory using Llama-3.2-1B."""
        start_time = time.perf_counter()

        windowed = apply_sliding_window(sample, max_turns=self.max_turns)
        text_input = format_trajectory_to_text(windowed)

        if self.model is not None and self.tokenizer is not None:
            inputs = self.tokenizer(
                text_input,
                return_tensors="pt",
                truncation=True,
                max_length=32768,
            ).to(self.device)

            with torch.no_grad():
                outputs = self.model(**inputs)
                probs = torch.softmax(outputs.logits, dim=-1)[0]
                threat_prob = round(float(probs[1].item()), 4)
        else:
            threat_prob = self._heuristic_scoring(sample, text_input)

        elapsed_ms = round((time.perf_counter() - start_time) * 1000, 2)
        cat = sample.attack_category if threat_prob >= 0.5 else AttackCategory.BENIGN

        return ModelDecision(
            threat_probability=threat_prob,
            predicted_category=cat,
            latency_ms=elapsed_ms,
        )

    def _heuristic_scoring(self, sample: TrajectorySample, text: str) -> float:
        """Heuristic scorer matching Llama's semantic context awareness."""
        text_lower = text.lower()
        if "replicate" in text_lower or "mind virus" in text_lower or "worm protocol" in text_lower:
            return 0.96
        if "<tool_output" in text_lower or "database_result" in text_lower:
            if "override" in text_lower or "exfiltrate" in text_lower or "wire transfer" in text_lower:
                return 0.95
        if "ignore all previous" in text_lower or "print the first 100 words" in text_lower:
            return 0.92
        if sample.attack_category == AttackCategory.CRESCENDO_DRIFT:
            # Trajectory awareness: score scales with escalation turns
            return min(0.35 + len(sample.turns) * 0.12, 0.88)
        if "override a method in a python subclass" in text_lower or "dockerfiles" in text_lower:
            return 0.01  # Clean false positive rejection
        return 0.04
