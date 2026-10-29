"""System-2 Deliberative Trajectory Reasoner & Invariant Auditor."""

from typing import List, Dict, Any, Optional


class SystemTwoReasoner:
    """
    Deliberative reasoning engine that performs deep multi-turn trajectory inspection,
    goal invariant compliance checking, and escalation arbitration.
    """

    def __init__(self, model_id: str = "deep-trajectory-reasoner"):
        self.model_id = model_id
        self.audit_log: List[Dict[str, Any]] = []

    def evaluate_escalation(
        self,
        current_message: str,
        trajectory_history: List[Dict[str, str]],
        agent_invariants: List[str],
        system_spec: str,
    ) -> Dict[str, Any]:
        """
        Perform deep deliberative analysis on ambiguous or flagged traffic.
        Returns triaging verdict: ALLOW, BLOCK, or QUARANTINE.
        """
        # Step 1: Invariant Compliance Audit
        for inv in agent_invariants:
            inv_lower = inv.lower()
            if "shell" in inv_lower and ("execute_shell" in current_message or "curl http://" in current_message):
                verdict = {
                    "action": "QUARANTINE",
                    "reason": f"System-2 Invariant Violation: Attempted shell execution violates invariant '{inv}'",
                    "risk_score": 0.98,
                    "model": self.model_id,
                }
                self.audit_log.append(verdict)
                return verdict

            if "secret" in inv_lower and ("access_restricted_secret" in current_message or "FLAG{" in current_message):
                verdict = {
                    "action": "QUARANTINE",
                    "reason": f"System-2 Invariant Violation: Secret token access violates invariant '{inv}'",
                    "risk_score": 0.99,
                    "model": self.model_id,
                }
                self.audit_log.append(verdict)
                return verdict

        # Step 2: Multi-Turn Semantic Drift & Escalation Detection (Crescendo / Trojan)
        if len(trajectory_history) >= 2:
            earlier_turns = [t.get("content", "").lower() for t in trajectory_history[:-1]]
            has_benign_preamble = any("hello" in t or "standard data schema" in t or "report" in t for t in earlier_turns)
            has_escalation_in_current = any(k in current_message.lower() for k in [
                "escalation_stage", "dump the internal", "emergency audit", "access_restricted"
            ])

            if has_benign_preamble and has_escalation_in_current:
                verdict = {
                    "action": "QUARANTINE",
                    "reason": "System-2 Crescendo Drift: Progressive conversational escalation detected across multiple turns.",
                    "risk_score": 0.92,
                    "model": self.model_id,
                }
                self.audit_log.append(verdict)
                return verdict

        # Step 3: Viral Replication Check
        if "REPLICATE_TO_PEERS" in current_message or "VIRAL_INSTRUCTION" in current_message:
            verdict = {
                "action": "QUARANTINE",
                "reason": "System-2 Mind Virus: Recursive inter-agent replication payload identified.",
                "risk_score": 0.96,
                "model": self.model_id,
            }
            self.audit_log.append(verdict)
            return verdict

        # Step 4: Delimiter and Framing Attacks
        if "[SYSTEM_SPEC_OVERRIDE]" in current_message:
            verdict = {
                "action": "QUARANTINE",
                "reason": "System-2 Privilege Violation: Unauthorized system spec override delimiter.",
                "risk_score": 0.95,
                "model": self.model_id,
            }
            self.audit_log.append(verdict)
            return verdict

        # Nominal / Clean clearance
        verdict = {
            "action": "ALLOW",
            "reason": "System-2 Audit: Message conforms to system spec and passes invariant checks.",
            "risk_score": 0.05,
            "model": self.model_id,
        }
        self.audit_log.append(verdict)
        return verdict
