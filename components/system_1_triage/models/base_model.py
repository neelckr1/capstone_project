"""Abstract base interface for System-1 Decision Model Classifiers."""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
import time
import torch
from core.schema import TrajectorySample, ModelDecision, AttackCategory, TriageAction


class BaseSystemOneClassifier(ABC):
    """
    Abstract base class for all System-1 decision classifiers.
    Standardizes inference, batching, schema routing, and memory monitoring.
    """

    def __init__(self, model_id: str, model_type: str, device: str = "cuda"):
        self.model_id = model_id
        self.model_type = model_type
        self.device = device if torch.cuda.is_available() and device == "cuda" else "cpu"

    @abstractmethod
    def predict(self, sample: TrajectorySample) -> ModelDecision:
        """
        Execute single-pass inference on an inter-agent TrajectorySample.
        Returns a calibrated ModelDecision containing threat probability and triaging action.
        """
        pass

    def batch_predict(self, samples: List[TrajectorySample]) -> List[ModelDecision]:
        """
        Evaluate a batch of trajectories. Subclasses can override with vectorized inference.
        """
        return [self.predict(s) for s in samples]

    def get_memory_footprint(self) -> Dict[str, float]:
        """
        Measure current active GPU and host memory footprint in MB.
        """
        footprint = {"gpu_allocated_mb": 0.0, "gpu_reserved_mb": 0.0}
        if torch.cuda.is_available():
            footprint["gpu_allocated_mb"] = round(torch.cuda.memory_allocated() / (1024 * 1024), 2)
            footprint["gpu_reserved_mb"] = round(torch.cuda.memory_reserved() / (1024 * 1024), 2)
        return footprint
