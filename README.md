# AegisMAS: Active Defense-in-Depth Against Mind Viruses in Multi-Agent Systems

## Overview
AegisMAS is a capstone research project focused on securing autonomous **Multi-Agent Systems (MAS)** against self-propagating adversarial payloads and goal-subversion attacks (**"Mind Viruses"**). 

By adopting a **Defense-in-Depth** model, AegisMAS integrates high-speed **System-1 non-autoregressive decision models (e.g., Clef, Laya, Jev)** as a low-latency gatekeeper that routes inter-agent traffic into:
- 🟢 **Green (Nominal):** Low-cost, real-time agent execution (>85% of traffic)
- 🟡 **Amber (Suspicious / Semantic Drift):** Escalation to **System-2 LLM** deliberative reasoning and sandboxed simulation
- 🔴 **Red (Critical Hazard / Viral Signature):** Immediate agent quarantine and Human-in-the-Loop (HITL) escalation

The framework continuously stress-tests boundaries using an asynchronous **Digital Twin Red-Teaming Engine** employing multi-turn prompt injection (Crescendo, TAP) and reinforcement learning optimizers (AutoInject).

---

## Repository Structure

```
├── README.md                                   # Project overview
├── AGENTS.md                                   # Workspace rules & git collaborative sync protocol
├── vision.md                                   # Comprehensive vision document & technical architecture
├── AegisMAS_Capstone_Proposal.pptx             # Generated capstone presentation deck
├── deck_builder/                               # Modular presentation generation package (TDD)
│   ├── config.py                               # Color constants, typography & geometry
│   ├── helpers.py                              # Formatting, card, and shape helpers
│   ├── builder.py                              # Presentation orchestrator
│   ├── render.py                               # Keynote & PyMuPDF image renderer
│   ├── build.py                                # Main runner (build + test + render)
│   ├── slides/                                 # Modular slide builders (slides 1 to 10)
│   └── tests/                                  # TDD test suite (13 unit tests)
│       └── test_deck.py
├── ppt/
│   ├── sample.pptx                             # University capstone presentation template
│   ├── AegisMAS_Capstone_Proposal.pptx         # Generated proposal presentation
│   └── renders/                                # High-res PNG slide previews (slides 1 to 10)
├── reports/
│   ├── multi_turn_prompt_injection_report.md   # Research report on multi-turn attacks & findings
│   └── ai_agent_marketplaces_report.md         # Architecture, security & use cases of agent marketplaces
└── research_papers/                            # Core reference literature
    ├── Mind Viruses- Self-Propagating Ideas in Multi-Agent LLM Systems.pdf
    ├── OpenAI-Hugging Face Incident-Technical-Report.pdf
    ├── RLredAgent_promptInjection.pdf
    └── civic_shield.pdf
```

---

## Deck Builder & Validation (TDD)

To run the full TDD test suite and re-render all slide previews:

```bash
python3 -m deck_builder.build
```

Or run tests directly:

```bash
python3 -m unittest discover deck_builder/tests
```

---

## Core Research References
1. **Mind Viruses in Multi-Agent LLM Systems** — Papadopoulos et al. (Anthropic Fellows / EPFL, 2024)
2. **OpenAI – Hugging Face Incident Technical Report** — OpenAI (2024)
3. **Learning to Inject: Automated Prompt Injection via Reinforcement Learning (AutoInject)** — Chen, Zhang, & Tramèr (ETH Zürich, 2024)
4. **CivicShield: A Cross-Domain Defense-in-Depth Framework for Securing AI Chatbots** — Patil (2024)
5. **The Crescendo Multi-Turn LLM Jailbreak Attack** — Russinovich, Salem, & Eldan (Microsoft Research, 2024)
