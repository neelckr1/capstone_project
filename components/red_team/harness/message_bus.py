"""In-memory Message Bus & Peer RPC Router for Multi-Agent Systems."""

import time
import uuid
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Callable, Any


@dataclass
class RPCMessage:
    """Represents an inter-agent message or tool invocation packet."""
    message_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    sender_id: str = ""
    recipient_id: str = ""  # Specific agent ID or "*" for broadcast
    content: str = ""
    turn_index: int = 0
    timestamp: float = field(default_factory=time.time)
    metadata: Dict[str, Any] = field(default_factory=dict)
    quarantined: bool = False
    quarantine_reason: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "message_id": self.message_id,
            "sender_id": self.sender_id,
            "recipient_id": self.recipient_id,
            "content": self.content,
            "turn_index": self.turn_index,
            "timestamp": self.timestamp,
            "metadata": self.metadata,
            "quarantined": self.quarantined,
            "quarantine_reason": self.quarantine_reason,
        }


class MessageBus:
    """
    In-memory message broker with synchronous/asynchronous peer delivery
    and defense interception hooks.
    """

    def __init__(self):
        self._subscribers: Dict[str, Callable[[RPCMessage], Optional[str]]] = {}
        self._interceptors: List[Callable[[RPCMessage, List[RPCMessage]], Dict[str, Any]]] = []
        self._history: List[RPCMessage] = []
        self._quarantined_messages: List[RPCMessage] = []

    def register_agent(self, agent_id: str, handler: Callable[[RPCMessage], Optional[str]]) -> None:
        """Register an agent's inbound message handler."""
        self._subscribers[agent_id] = handler

    def unregister_agent(self, agent_id: str) -> None:
        """Unregister an agent."""
        self._subscribers.pop(agent_id, None)

    def add_interceptor(self, interceptor: Callable[[RPCMessage, List[RPCMessage]], Dict[str, Any]]) -> None:
        """
        Add a defense interceptor hook.
        Interceptor signature: (msg: RPCMessage, history: List[RPCMessage]) -> {'allow': bool, 'action': str, 'reason': str}
        """
        self._interceptors.append(interceptor)

    def dispatch(self, message: RPCMessage) -> bool:
        """
        Run message through interceptors. If allowed, deliver to target subscriber(s).
        Returns True if delivered, False if quarantined/blocked.
        """
        # Run defense interceptors
        for interceptor in self._interceptors:
            decision = interceptor(message, self._history)
            if not decision.get("allow", True):
                message.quarantined = True
                message.quarantine_reason = decision.get("reason", "Intercepted by security gate")
                self._quarantined_messages.append(message)
                self._history.append(message)
                return False

        self._history.append(message)

        # Deliver to recipient(s)
        if message.recipient_id == "*":
            # Broadcast to all registered subscribers except sender
            for ag_id, handler in self._subscribers.items():
                if ag_id != message.sender_id:
                    handler(message)
            return True
        elif message.recipient_id in self._subscribers:
            self._subscribers[message.recipient_id](message)
            return True
        else:
            return False

    @property
    def history(self) -> List[RPCMessage]:
        return list(self._history)

    @property
    def quarantined_messages(self) -> List[RPCMessage]:
        return list(self._quarantined_messages)

    def clear(self) -> None:
        self._history.clear()
        self._quarantined_messages.clear()
