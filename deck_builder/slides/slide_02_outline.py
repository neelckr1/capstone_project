"""
Slide 2: Outline Slide Builder
"""
from pptx.util import Emu
from pptx.enum.text import PP_ALIGN
from deck_builder.config import (
    C_CYAN, C_DARK, C_INDIGO, C_CALLOUT_BG
)
from deck_builder.helpers import (
    clear_tf, set_slide_title, write_header_bullet, add_textbox
)

def build_slide_2(slide):
    set_slide_title(slide, "Text Box 34", "Presentation Outline")
    for shape in slide.shapes:
        if shape.name == "Content Placeholder 2":
            tf = clear_tf(shape)
            write_header_bullet(
                tf, "01 ›", "Problem Statement  —  Autonomous Goal Subversion & Mind Virus Cascades",
                label_color=C_CYAN, body_color=C_DARK, size=15, first=True, space_after=6
            )
            write_header_bullet(
                tf, "02 ›", "Scope & Feasibility  —  The Context-Latency Tradeoff & Our Mitigation Strategy",
                label_color=C_CYAN, body_color=C_DARK, size=15, space_after=6
            )
            write_header_bullet(
                tf, "03 ›", "Background Work  —  Anthropic Mind Viruses, OpenAI Incident & AutoInject",
                label_color=C_CYAN, body_color=C_DARK, size=15, space_after=6
            )
            write_header_bullet(
                tf, "04 ›", "Applications & Use Cases  —  Enterprise MCP Gateways, DevOps Swarms, Financial Meshes",
                label_color=C_CYAN, body_color=C_DARK, size=15, space_after=6
            )
            write_header_bullet(
                tf, "05 ›", "Expected Deliverables  —  Phase I, II, III Milestones",
                label_color=C_CYAN, body_color=C_DARK, size=15, space_after=6
            )
            write_header_bullet(
                tf, "06 ›", "Project Timeline  —  16-Week Gantt & Team Responsibility Matrix",
                label_color=C_CYAN, body_color=C_DARK, size=15, space_after=6
            )
            write_header_bullet(
                tf, "07 ›", "Proposed Methodology  —  3-Tier Defender Architecture + Digital Twin Red-Team Engine",
                label_color=C_CYAN, body_color=C_DARK, size=15, space_after=6
            )

    # Callout strip at bottom of Slide 2
    add_textbox(
        slide, Emu(1066800), Emu(6150000), Emu(10600000), Emu(420000),
        "Option 3: Dual-Anchor Hybrid — Template-compliant slide order; solution seeded from Slide 4",
        size=11, bold=False, color=C_INDIGO, bg_color=C_CALLOUT_BG, align=PP_ALIGN.CENTER
    )
