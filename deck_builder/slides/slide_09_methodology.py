"""
Slide 9: Proposed Methodology Builder
"""
from pptx.util import Emu
from pptx.enum.text import PP_ALIGN
from deck_builder.config import (
    C_INDIGO, C_DARK, C_WHITE, C_MUTED, C_GREEN, C_AMBER, C_CRIMSON
)
from deck_builder.helpers import (
    clear_tf, set_slide_title, write_header_bullet, write_bullet,
    add_para, add_textbox
)

def build_slide_9(slide):
    set_slide_title(slide, "Text Box 34", "Proposed Methodology: AegisMAS Defense-in-Depth")
    for shape in slide.shapes:
        if shape.name == "TextBox 4":
            tf = clear_tf(shape)
            write_header_bullet(
                tf, "◈  3-Tier Active Immune Architecture:", "",
                label_color=C_INDIGO, body_color=C_DARK, size=13, first=True, space_after=1
            )
            write_bullet(
                tf, "Layer 1 — System-1 Non-Autoregressive Decision Gate (Cloudflare Clef / ConvAI Laya):",
                level=1, bold=True, size=12, color=C_DARK, space_after=1
            )
            write_bullet(
                tf, "Single-pass forward inference in ~30–50ms on State-Drift Vector. Routes: 🟢 Green (Nominal) → allow | 🟡 Amber (Drift) → System-2 | 🔴 Red (Viral) → Quarantine + HITL.",
                level=2, size=11, color=C_DARK, space_after=2
            )
            write_bullet(
                tf, "Layer 2 — System-2 Deliberative Trajectory Reasoning Engine (Deep LLM):",
                level=1, bold=True, size=12, color=C_DARK, space_after=1
            )
            write_bullet(
                tf, "Activated only on Amber traffic (<15%). Performs multi-turn trajectory audit, goal-invariant checking, and sandboxed counterfactual tool-call simulation.",
                level=2, size=11, color=C_DARK, space_after=2
            )
            write_bullet(
                tf, "Layer 3 — Containment, Quarantine & Human-in-the-Loop (HITL):",
                level=1, bold=True, size=12, color=C_DARK, space_after=1
            )
            write_bullet(
                tf, "Red-path: Immediate communication severance, sandbox isolation, and real-time administrator alert on HITL dashboard.",
                level=2, size=11, color=C_DARK, space_after=3
            )
            
            add_para(tf, level=0, space_after=1)
            write_header_bullet(
                tf, "◈  Asynchronous Co-Evolutionary Red-Team (Digital Twin):", "",
                label_color=C_INDIGO, body_color=C_DARK, size=13, space_after=1
            )
            write_bullet(
                tf, "Offline shadow sandbox fuzzed via Crescendo & AutoInject RL continuously extracts new bypass signatures and updates System-1 decision boundaries without adding runtime latency.",
                level=1, size=11, color=C_DARK, space_after=1
            )

    # Visual Architecture Flow Diagram at bottom of Slide 9
    diag_y = Emu(4900000)
    diag_h = Emu(1400000)

    # Station 1: Inter-Agent Message
    add_textbox(
        slide, Emu(1100000), diag_y, Emu(1800000), diag_h,
        "Inter-Agent\nMessage\n(RPC / Tool Call)",
        size=11, bold=True, color=C_WHITE, bg_color=C_MUTED, align=PP_ALIGN.CENTER
    )

    # Arrow 1
    add_textbox(
        slide, Emu(2950000), diag_y + Emu(400000), Emu(450000), Emu(500000),
        "➔", size=20, bold=True, color=C_INDIGO, align=PP_ALIGN.CENTER
    )

    # Station 2: System-1 Gate
    add_textbox(
        slide, Emu(3450000), diag_y, Emu(2200000), diag_h,
        "Layer 1\nSystem-1 Gate\n(<50ms Clef/Laya)\n[State-Drift]",
        size=11, bold=True, color=C_WHITE, bg_color=C_INDIGO, align=PP_ALIGN.CENTER
    )

    # Arrow 2
    add_textbox(
        slide, Emu(5700000), diag_y + Emu(400000), Emu(450000), Emu(500000),
        "➔", size=20, bold=True, color=C_INDIGO, align=PP_ALIGN.CENTER
    )

    # Station 3: 3-Way Triage Stack
    add_textbox(
        slide, Emu(6200000), diag_y, Emu(2400000), Emu(420000),
        "🟢 Green: Allow (>85%)", size=10, bold=True, color=C_WHITE, bg_color=C_GREEN, align=PP_ALIGN.CENTER
    )
    add_textbox(
        slide, Emu(6200000), diag_y + Emu(490000), Emu(2400000), Emu(420000),
        "🟡 Amber: Escalate (<15%)", size=10, bold=True, color=C_WHITE, bg_color=C_AMBER, align=PP_ALIGN.CENTER
    )
    add_textbox(
        slide, Emu(6200000), diag_y + Emu(980000), Emu(2400000), Emu(420000),
        "🔴 Red: Quarantine + HITL", size=10, bold=True, color=C_WHITE, bg_color=C_CRIMSON, align=PP_ALIGN.CENTER
    )

    # Arrow 3 (from Amber)
    add_textbox(
        slide, Emu(8650000), diag_y + Emu(400000), Emu(450000), Emu(500000),
        "➔", size=20, bold=True, color=C_AMBER, align=PP_ALIGN.CENTER
    )

    # Station 4: System-2 LLM
    add_textbox(
        slide, Emu(9150000), diag_y, Emu(2600000), diag_h,
        "Layer 2: System-2\nDeliberation Engine\n(Trajectory Audit &\nSandbox Simulation)",
        size=11, bold=True, color=C_WHITE, bg_color=C_INDIGO, align=PP_ALIGN.CENTER
    )
