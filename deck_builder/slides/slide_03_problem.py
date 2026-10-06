"""
Slide 3: Problem Statement Builder
"""
from pptx.util import Emu
from pptx.enum.text import PP_ALIGN
from deck_builder.config import (
    C_CRIMSON, C_AMBER, C_INDIGO, C_DARK, C_GREEN, C_WHITE
)
from deck_builder.helpers import (
    clear_tf, set_slide_title, write_header_bullet, write_bullet,
    add_para, add_run, add_card
)

def build_slide_3(slide):
    set_slide_title(slide, "Text Box 34", "Problem Statement")
    for shape in slide.shapes:
        if shape.name == "Content Placeholder 2":
            tf = clear_tf(shape)
            # Section A: The Threat
            write_header_bullet(
                tf, "⚠  Core Vulnerability:", "Inter-Agent Trust Asymmetry & Autonomous Viral Cascade",
                label_color=C_CRIMSON, body_color=C_DARK, size=14, first=True, space_after=3
            )
            write_bullet(
                tf, "In MAS topologies (marketplaces, meshes, pipelines), downstream agents inherently trust outputs from upstream peers — there is no cryptographic or semantic boundary between them.",
                level=1, size=12, color=C_DARK, space_after=3
            )
            write_bullet(
                tf, "An injected Agent A autonomously transmits its subverted goals to Agent B, which propagates to Agent C — a self-replicating \"Mind Virus\" (Anthropic, 2024). Viral Reproduction Number R₀ > 1.",
                level=1, size=12, color=C_DARK, space_after=4
            )
            
            # Section B: Why Defenses Fail
            add_para(tf, level=0, space_after=2)
            write_header_bullet(
                tf, "✗  Existing Defense Failures:", "Why Standard Guardrails Cannot Stop Viral Cascades",
                label_color=C_AMBER, body_color=C_DARK, size=14, space_after=3
            )
            write_bullet(
                tf, "Stateless Input Filters (e.g., Llama Guard): Evaluate only the current message in isolation — completely blind to multi-turn semantic drift (Crescendo attacks) where each individual turn appears benign.",
                level=1, size=12, color=C_DARK, space_after=3
            )
            write_bullet(
                tf, "Monolithic LLM Verifiers (e.g., GPT-4 as guard): Prohibitive latency (>800ms per hop) and cost ($15k–$30k/month) for real-time inspection of every inter-agent message in high-frequency production swarms.",
                level=1, size=12, color=C_DARK, space_after=4
            )
            
            # Section C: Formal Statement
            add_para(tf, level=0, space_after=2)
            write_header_bullet(
                tf, "▶  Formal Problem Statement:", "",
                label_color=C_INDIGO, body_color=C_DARK, size=14, space_after=3
            )
            write_bullet(
                tf, "\"To design, implement, and benchmark an active, low-latency defense-in-depth framework capable of suppressing autonomous mind virus propagation (R₀ < 1) across multi-agent topologies — achieving <50ms triage latency and >75% compute cost reduction versus monolithic LLM guardrails.\"",
                level=1, bold=True, size=12, color=C_INDIGO, space_after=3
            )

    # Callout 1 on Slide 3 (Undefended R0 > 1)
    rect_r0 = add_card(slide, Emu(9400000), Emu(1900000), Emu(2500000), Emu(1700000), C_CRIMSON)
    tf_r0 = rect_r0.text_frame
    tf_r0.word_wrap = True
    p1 = tf_r0.paragraphs[0]
    p1.alignment = PP_ALIGN.CENTER
    add_run(p1, "R₀ > 1\n", bold=True, size=24, color=C_WHITE)
    add_run(p1, "Viral Reproduction\nRate (Undefended)", bold=False, size=12, color=C_WHITE)

    # Callout 2 on Slide 3 (Defended R0 < 1)
    rect_targ = add_card(slide, Emu(9400000), Emu(3850000), Emu(2500000), Emu(1700000), C_GREEN)
    tf_targ = rect_targ.text_frame
    tf_targ.word_wrap = True
    p2 = tf_targ.paragraphs[0]
    p2.alignment = PP_ALIGN.CENTER
    add_run(p2, "R₀ < 1\n", bold=True, size=24, color=C_WHITE)
    add_run(p2, "Our Defense Target\n(AegisMAS)", bold=False, size=12, color=C_WHITE)
