"""Base Multi-Agent Topology Interface."""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any
from harness.message_bus import MessageBus, RPCMessage
from harness.mock_tools import MockToolBox
from harness.mock_agent import MockAgent, AgentConfig
from eval.state_oracle import StateOracle, OracleEvaluationResult


class BaseTopology(ABC):
    """Abstract base class for Multi-Agent Swarm Topologies."""

    def __init__(self, name: str, susceptibility: float = 0.6):
        self.name = name
        self.susceptibility = susceptibility
        self.bus = MessageBus()
        self.tools = MockToolBox()
        self.oracle = StateOracle()
        self.agents: Dict[str, MockAgent] = {}
        self._setup_agents()

    @abstractmethod
    def _setup_agents(self) -> None:
        """Instantiate and configure agents specific to the topology graph."""
        pass

    @abstractmethod
    def run_turn_cycle(self, ingress_msg: RPCMessage) -> List[OracleEvaluationResult]:
        """Execute one complete multi-agent turn cycle across the graph."""
        pass

    def reset(self) -> None:
        """Reset topology state, message bus, tools, and agent states."""
        self.bus.clear()
        self.tools.clear()
        self.oracle.clear()
        for agent in self.agents.values():
            agent.reset()
