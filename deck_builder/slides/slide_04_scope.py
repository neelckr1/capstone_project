"""
Slide 4: Scope and Feasibility Study Builder
"""
from pptx.util import Emu
from pptx.enum.text import PP_ALIGN
from deck_builder.config import (
    C_INDIGO, C_DARK, C_MUTED, C_AMBER, C_GREEN, C_CALLOUT_BG
)
from deck_builder.helpers import (
    clear_tf, set_slide_title, write_header_bullet, write_bullet,
    add_para, add_textbox
)

def build_slide_4(slide):
    set_slide_title(slide, "Text Box 34", "Scope and Feasibility Study")
    for shape in slide.shapes:
        if shape.name == "Content Placeholder 2":
            tf = clear_tf(shape)
            # Scope
            write_header_bullet(
                tf, "◈  In-Scope Deliverables:", "",
                label_color=C_INDIGO, body_color=C_DARK, size=14, first=True, space_after=2
            )
            write_bullet(
                tf, "Topologies: 3-stage Sequential Pipeline + Peer Mesh + Agent Marketplace Tool Invocation testbeds.",
                level=1, size=12, color=C_DARK, space_after=2
            )
            write_bullet(
                tf, "Defender Layers: System-1 Non-Autoregressive Gate (Clef / Laya) + System-2 Deliberative Trajectory LLM.",
                level=1, size=12, color=C_DARK, space_after=2
            )
            write_bullet(
                tf, "Red-Team Engine: Multi-Turn Crescendo fuzzer + AutoInject RL adversarial suffix harness.",
                level=1, size=12, color=C_DARK, space_after=2
            )
            write_bullet(
                tf, "Boundaries (Out-of-Scope): Hardware side-channels; pre-training foundation models; non-LLM agents.",
                level=1, size=11, color=C_MUTED, space_after=4
            )
            
            # Challenges & Mitigations
            add_para(tf, level=0, space_after=2)
            write_header_bullet(
                tf, "⚡  Challenge 1 — Context Window vs. Latency:", "",
                label_color=C_AMBER, body_color=C_DARK, size=14, space_after=2
            )
            write_bullet(
                tf, "Problem: Small models (~500M–1.5B params) cannot process 8,000 raw chat-history tokens in 30ms.",
                level=1, bold=True, size=12, color=C_DARK, space_after=2
            )
            write_bullet(
                tf, "✓ Mitigation: System-1 receives a pre-computed State-Drift Vector — a compact numeric embedding of semantic goal deviation — instead of raw conversational tokens. Single-pass inference remains sub-50ms.",
                level=2, size=12, color=C_GREEN, space_after=4
            )
            
            write_header_bullet(
                tf, "⚡  Challenge 2 — The Guardrail Curse (False Positives):", "",
                label_color=C_AMBER, body_color=C_DARK, size=14, space_after=2
            )
            write_bullet(
                tf, "Problem: A 5% false-positive rate across a 10-hop pipeline yields <60% legitimate workflow completion — unusable in production.",
                level=1, bold=True, size=12, color=C_DARK, space_after=2
            )
            write_bullet(
                tf, "✓ Mitigation: Calibrate triage thresholds against benign task suites (AgentBench / GAIA). Maintain >90% benign workflow completion rate as a hard acceptance criterion.",
                level=2, size=12, color=C_GREEN, space_after=2
            )

    # Callout box at bottom of Slide 4
    add_textbox(
        slide, Emu(1295400), Emu(6050000), Emu(10000000), Emu(550000),
        "Key Insight: The feasibility of AegisMAS rests on one architectural innovation — routing System-1 on State-Drift embeddings, not raw token streams. This collapses the latency problem entirely.",
        size=11, bold=True, color=C_INDIGO, bg_color=C_CALLOUT_BG, align=PP_ALIGN.CENTER
    )
