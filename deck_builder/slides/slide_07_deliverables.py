"""
Slide 7: Expected Deliverables Builder
"""
from deck_builder.config import (
    C_CRIMSON, C_AMBER, C_GREEN, C_DARK
)
from deck_builder.helpers import (
    clear_tf, set_slide_title, write_header_bullet, write_bullet,
    add_para
)

def build_slide_7(slide):
    set_slide_title(slide, "Text Box 34", "Expected Deliverables by Phase")
    for shape in slide.shapes:
        if shape.name == "Content Placeholder 2":
            tf = clear_tf(shape)
            # Capstone I
            write_header_bullet(
                tf, "◉  Capstone-I  |  Foundations & Threat Modeling:", "",
                label_color=C_CRIMSON, body_color=C_DARK, size=14, first=True, space_after=2
            )
            write_bullet(
                tf, "Formal threat model documenting mind virus propagation dynamics across MAS topologies (Sequential, Mesh, Marketplace).",
                level=1, size=12, color=C_DARK, space_after=2
            )
            write_bullet(
                tf, "Baseline MAS simulation testbed: 3-agent sequential pipeline + 1 marketplace agent invocation scenario.",
                level=1, size=12, color=C_DARK, space_after=2
            )
            write_bullet(
                tf, "Red-Agent attack generator: Crescendo multi-turn templates + AutoInject RL adversarial suffix harness.",
                level=1, size=12, color=C_DARK, space_after=2
            )
            write_bullet(
                tf, "Empirical undefended baseline report: R₀ measurement demonstrating viral spread (R₀ > 1).",
                level=1, size=12, color=C_DARK, space_after=4
            )
            
            # Capstone II
            add_para(tf, level=0, space_after=2)
            write_header_bullet(
                tf, "◉  Capstone-II  |  Defender Architecture Build:", "",
                label_color=C_AMBER, body_color=C_DARK, size=14, space_after=2
            )
            write_bullet(
                tf, "System-1 Non-Autoregressive Triage Gate (Cloudflare Clef / ConvAI Laya) operating at <50ms end-to-end latency.",
                level=1, size=12, color=C_DARK, space_after=2
            )
            write_bullet(
                tf, "State-Drift Vector encoder: Computes semantic goal-deviation scores from agent state snapshots.",
                level=1, size=12, color=C_DARK, space_after=2
            )
            write_bullet(
                tf, "System-2 Deliberative Reasoning Engine for multi-turn trajectory inspection and goal-invariant verification.",
                level=1, size=12, color=C_DARK, space_after=2
            )
            write_bullet(
                tf, "Human-in-the-Loop (HITL) quarantine dashboard + asynchronous co-evolutionary red-team feedback loop.",
                level=1, size=12, color=C_DARK, space_after=4
            )
            
            # Capstone III
            add_para(tf, level=0, space_after=2)
            write_header_bullet(
                tf, "◉  Capstone-III  |  Validation, Benchmarks & Paper:", "",
                label_color=C_GREEN, body_color=C_DARK, size=14, space_after=2
            )
            write_bullet(
                tf, "Full benchmark suite: Viral suppression (R₀ < 1), triage latency (<50ms), compute cost reduction (>75%), benign task preservation (>90%).",
                level=1, size=12, color=C_DARK, space_after=2
            )
            write_bullet(
                tf, "Open-source repository, full documentation, and conference/workshop paper draft (IEEE S&P / USENIX Security track).",
                level=1, size=12, color=C_DARK, space_after=2
            )
