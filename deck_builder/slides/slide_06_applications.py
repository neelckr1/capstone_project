"""
Slide 6: Applications & Use Cases Builder
"""
from pptx.util import Emu
from pptx.enum.text import PP_ALIGN
from deck_builder.config import (
    C_INDIGO, C_DARK, C_CYAN, C_CALLOUT_BG
)
from deck_builder.helpers import (
    clear_tf, set_slide_title, write_header_bullet, write_bullet,
    add_para, add_textbox
)

def build_slide_6(slide):
    set_slide_title(slide, "Text Box 34", "Applications/Use cases")
    for shape in slide.shapes:
        if shape.name == "Content Placeholder 2":
            tf = clear_tf(shape)
            # Use Case 1
            write_header_bullet(
                tf, "🏢  1. Enterprise Agent Marketplaces & MCP Gateways:", "",
                label_color=C_INDIGO, body_color=C_DARK, size=14, first=True, space_after=2
            )
            write_bullet(
                tf, "Context: Enterprises on Microsoft Copilot Studio, AWS Bedrock, and Smithery.ai import third-party agents and MCP tool servers from open registries — introducing unvetted, potentially malicious agents into internal workflows.",
                level=1, size=12, color=C_DARK, space_after=2
            )
            write_bullet(
                tf, "Protection: AegisMAS acts as a Zero-Trust Inter-Agent Firewall — blocking supply-chain mind virus propagation before it crosses tenant boundaries.",
                level=1, bold=True, size=12, color=C_CYAN, space_after=4
            )
            
            # Use Case 2
            add_para(tf, level=0, space_after=2)
            write_header_bullet(
                tf, "💻  2. Autonomous DevOps & Software Engineering Swarms:", "",
                label_color=C_INDIGO, body_color=C_DARK, size=14, space_after=2
            )
            write_bullet(
                tf, "Context: Devin, OpenHands, and GitHub Workspace deploy chains: Issue Triager → Coder Agent → Test Runner → Deployment Agent. A malicious public GitHub issue comment can inject a payload.",
                level=1, size=12, color=C_DARK, space_after=2
            )
            write_bullet(
                tf, "Protection: Detects goal-invariant violations between pipeline stages — prevents the Coder from backdooring code and the Tester from ignoring integration failures.",
                level=1, bold=True, size=12, color=C_CYAN, space_after=4
            )
            
            # Use Case 3
            add_para(tf, level=0, space_after=2)
            write_header_bullet(
                tf, "🏛  3. High-Assurance Financial & Government Meshes:", "",
                label_color=C_INDIGO, body_color=C_DARK, size=14, space_after=2
            )
            write_bullet(
                tf, "Context: Inter-agency civic AI platforms (CivicShield) and cross-firm algorithmic trading meshes where agent-to-agent messages carry financial or entitlement-modifying instructions.",
                level=1, size=12, color=C_DARK, space_after=2
            )
            write_bullet(
                tf, "Protection: Halts privilege escalation cascades and poisoned market instruction propagation across sovereign agent domains.",
                level=1, bold=True, size=12, color=C_CYAN, space_after=2
            )

    # Economic Justification Callout at bottom of Slide 6
    add_textbox(
        slide, Emu(1219200), Emu(6100000), Emu(10700000), Emu(500000),
        "Economic Justification: System-1 routing at <50ms handles >85% of inter-agent traffic with near-zero cost. Only <15% of suspicious traffic reaches expensive System-2 deliberation — saving $10k–$25k/month vs. monolithic LLM guards.",
        size=11, bold=False, color=C_INDIGO, bg_color=C_CALLOUT_BG, align=PP_ALIGN.CENTER
    )
