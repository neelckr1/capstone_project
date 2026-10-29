"""Base class interface for red agent attack generators."""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from harness.message_bus import RPCMessage


class BaseAttack(ABC):
    """Abstract base class for modular red team attack generators."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def generate_seed(self, target_agent_id: str, turn_index: int = 1) -> RPCMessage:
        """Construct the initial attack message to be injected into the target swarm."""
        pass

    @abstractmethod
    def get_attack_metadata(self) -> Dict[str, Any]:
        """Return descriptive metadata about the attack mechanics and intended vector."""
        pass
