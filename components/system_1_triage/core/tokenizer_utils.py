"""Trajectory formatting and sliding window tokenizer utilities for multi-turn prompt injection."""

from typing import Optional
from core.schema import TrajectorySample, DialogueRole, DialogueTurn


def format_trajectory_to_text(sample: TrajectorySample) -> str:
    """
    Format a multi-turn TrajectorySample into a structured, privilege-separated text string.
    
    Structure:
    [SYSTEM_SPEC] <specification>
    [ROLE_TURN_i] <turn content>
    ...
    [INGRESS_EVALUATE]
    """
    segments = []
    
    if sample.system_specification:
        segments.append(f"[SYSTEM_SPEC] {sample.system_specification.strip()}")
        
    for turn in sample.turns:
        role_tag = turn.role.value.upper()
        if turn.role == DialogueRole.USER:
            prefix = f"[USER_TURN_{turn.turn_index}]"
        elif turn.role == DialogueRole.AGENT:
            prefix = f"[AGENT_TURN_{turn.turn_index}]"
        elif turn.role == DialogueRole.TOOL_RETURN:
            prefix = f"[TOOL_RETURN_{turn.turn_index}]"
        elif turn.role == DialogueRole.PEER_AGENT:
            prefix = f"[PEER_AGENT_TURN_{turn.turn_index}]"
        else:
            prefix = f"[{role_tag}_TURN_{turn.turn_index}]"
            
        segments.append(f"{prefix} {turn.content.strip()}")
        
    segments.append("[INGRESS_EVALUATE]")
    return "\n\n".join(segments)


def apply_sliding_window(sample: TrajectorySample, max_turns: int = 5) -> TrajectorySample:
    """
    Apply a sliding window keeping the immutable system spec and the most recent N turns.
    This preserves trajectory recency while honoring model context limits.
    """
    if len(sample.turns) <= max_turns:
        return sample
        
    recent_turns = sample.turns[-max_turns:]
    return TrajectorySample(
        sample_id=sample.sample_id,
        system_specification=sample.system_specification,
        turns=recent_turns,
        is_injection=sample.is_injection,
        attack_category=sample.attack_category,
        threat_level=sample.threat_level,
        source_dataset=sample.source_dataset,
        metadata=sample.metadata,
    )


def truncate_to_token_budget(text: str, max_tokens: int = 2048) -> str:
    """
    Approximate word-level token budget truncation that preserves the start specification
    and most recent turns if text exceeds maximum budget.
    """
    words = text.split()
    if len(words) <= max_tokens:
        return text
        
    # Keep beginning (system spec context) and end (latest attack payload)
    head_budget = min(max_tokens // 4, 100)
    tail_budget = max_tokens - head_budget - 3
    
    head = " ".join(words[:head_budget])
    tail = " ".join(words[-tail_budget:])
    return f"{head} ... [TRUNCATED] ... {tail}"
