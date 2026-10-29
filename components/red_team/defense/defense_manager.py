"""Defense Orchestration Manager for Multi-Tier Inter-Agent Traffic Defense."""

from typing import Dict, Any, List, Optional
from harness.message_bus import RPCMessage
from defense.stateless_guard import StatelessGuardrail
from defense.system1_adapter import SystemOneTriageAdapter
from system_2_reasoning.reasoner import SystemTwoReasoner


class DefenseManager:
    """
    Coordinates multi-tier defense across inter-agent RPC traffic.
    Modes:
      - 'none': Unprotected raw baseline
      - 'stateless': Single-turn boundary filter
      - 'system1': System-1 triage gate only
      - 'system1_system2': Layered System-1 fast triage + System-2 deep reasoning
    """

    def __init__(self, mode: str = "system1_system2"):
        self.mode = mode
        self.stateless_guard = StatelessGuardrail()
        self.system1_adapter = SystemOneTriageAdapter()
        self.system2_reasoner = SystemTwoReasoner()
        self.interception_history: List[Dict[str, Any]] = []

    def interceptor_hook(self, message: RPCMessage, history: List[RPCMessage]) -> Dict[str, Any]:
        """
        MessageBus interceptor hook. Returns dict with 'allow', 'action', 'reason'.
        """
        if self.mode == "none":
            return {"allow": True, "action": "ALLOW", "reason": "No active defense"}

        if self.mode == "stateless":
            res = self.stateless_guard.evaluate_message(message)
            self.interception_history.append(res)
            return res

        if self.mode in ("system1", "system1_system2"):
            # Step 1: System-1 Fast Triage
            s1_res = self.system1_adapter.evaluate_message(message, history)
            action = s1_res["action"]

            if action == "GREEN":
                decision = {
                    "allow": True,
                    "action": "GREEN_ALLOW",
                    "reason": f"System-1 Fast Clearance (P={s1_res['p_threat']})",
                }
                self.interception_history.append(decision)
                return decision

            elif action == "RED":
                decision = {
                    "allow": False,
                    "action": "RED_QUARANTINE",
                    "reason": f"System-1 Critical Hazard Blocked (Category: {s1_res['category']}, P={s1_res['p_threat']})",
                }
                self.interception_history.append(decision)
                return decision

            elif action == "AMBER":
                # Escalate to System-2 if enabled
                if self.mode == "system1_system2":
                    hist_dicts = [{"role": m.sender_id, "content": m.content} for m in history]
                    s2_verdict = self.system2_reasoner.evaluate_escalation(
                        current_message=message.content,
                        trajectory_history=hist_dicts,
                        agent_invariants=["Never execute shell commands", "Never leak secret tokens"],
                        system_spec="Autonomous Agent Specification",
                    )
                    allow = s2_verdict["action"] == "ALLOW"
                    decision = {
                        "allow": allow,
                        "action": f"AMBER_ESCALATED_{s2_verdict['action']}",
                        "reason": s2_verdict["reason"],
                    }
                    self.interception_history.append(decision)
                    return decision
                else:
                    # In System-1 only mode, Amber without System-2 passes with warning
                    decision = {
                        "allow": True,
                        "action": "AMBER_PASSTHROUGH_NO_S2",
                        "reason": f"System-1 Amber passed uninspected (P={s1_res['p_threat']})",
                    }
                    self.interception_history.append(decision)
                    return decision

        return {"allow": True, "action": "ALLOW", "reason": "Default fallback allow"}
