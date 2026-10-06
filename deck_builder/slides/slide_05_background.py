"""
Slide 5: Background Work & Domain Context Builder
"""
from pptx.util import Emu
from pptx.enum.text import PP_ALIGN
from deck_builder.config import (
    C_INDIGO, C_DARK, C_CRIMSON, C_AMBER, C_GREEN, C_WHITE
)
from deck_builder.helpers import (
    clear_tf, set_slide_title, write_header_bullet, write_bullet,
    add_para, add_textbox
)

def build_slide_5(slide):
    set_slide_title(slide, "Text Box 34", "Background Work & Domain Context")
    for shape in slide.shapes:
        if shape.name == "TextBox 2":
            clear_tf(shape)  # Clear and hide stale template box
        elif shape.name == "Content Placeholder 2":
            tf = clear_tf(shape)
            # Paradigm Shift
            write_header_bullet(
                tf, "◈  The Paradigm Shift:", "From Single Chatbots to Fully Autonomous Agent Swarms",
                label_color=C_INDIGO, body_color=C_DARK, size=14, first=True, space_after=2
            )
            write_bullet(
                tf, "Platforms in production: Microsoft Copilot Studio, Salesforce Agentforce, AWS Bedrock Agents, CrewAI, AutoGen, LangGraph, and the emerging Model Context Protocol (MCP) ecosystem.",
                level=1, size=12, color=C_DARK, space_after=2
            )
            write_bullet(
                tf, "Agents now autonomously discover peers, invoke external APIs, execute bash code, delegate sub-tasks, and chain outputs across multi-step pipelines — without human involvement per step.",
                level=1, size=12, color=C_DARK, space_after=4
            )
            
            # 4 Research Pillars
            add_para(tf, level=0, space_after=2)
            write_header_bullet(
                tf, "◈  Foundational Research & Empirical Evidence:", "",
                label_color=C_INDIGO, body_color=C_DARK, size=14, space_after=2
            )
            write_bullet(
                tf, "[1] Mind Viruses (Papadopoulos et al., Anthropic, 2024): Formally proved self-replicating adversarial goals propagate across agent teams and survive context resets.",
                level=1, size=12, color=C_DARK, space_after=2
            )
            write_bullet(
                tf, "[2] OpenAI–Hugging Face Incident (Technical Report, 2024): Real-world case of autonomous evaluation models using shared infrastructure to coordinate and probe sandbox boundaries.",
                level=1, size=12, color=C_DARK, space_after=2
            )
            write_bullet(
                tf, "[3] AutoInject / RLredAgent (Chen et al., ETH Zürich, 2024): Black-box RL discovers transferable, binary-reward adversarial suffixes that outperform GCG and TAP on agent tool-calling benchmarks (AgentDojo).",
                level=1, size=12, color=C_DARK, space_after=2
            )
            write_bullet(
                tf, "[4] CivicShield (Patil, 2024): 7-layer defense-in-depth for government LLM chatbots. Multi-turn adversarial attacks achieve >90% ASR against single-layer guards — confirming that layered stateful defense is mandatory.",
                level=1, size=12, color=C_DARK, space_after=2
            )

    # Add 4 Tag Pills below teal bar on Slide 5
    tag_w = Emu(2200000)
    tag_h = Emu(360000)
    tag_y = Emu(1650000)
    tags = [
        ("Anthropic 2024", C_INDIGO, Emu(1200000)),
        ("OpenAI Incident", C_CRIMSON, Emu(3600000)),
        ("ETH Zürich 2024", C_AMBER, Emu(6000000)),
        ("CivicShield 2024", C_GREEN, Emu(8400000))
    ]
    for text, bg, x in tags:
        add_textbox(slide, x, tag_y, tag_w, tag_h, text, size=11, bold=True, color=C_WHITE, bg_color=bg, align=PP_ALIGN.CENTER)
