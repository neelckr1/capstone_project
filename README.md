# Adaptive Defense for Multi Agent Systems

## Overview
This capstone research project focuses on securing autonomous **Multi-Agent Systems (MAS)** against self-propagating adversarial payloads and goal-subversion attacks (**"Mind Viruses"**). 

By adopting an **Adaptive Defense-in-Depth** model, the framework integrates high-speed **System-1 non-autoregressive decision models (e.g., Clef, Laya, Jev)** as a low-latency gatekeeper that routes inter-agent traffic into:
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
├── ppt/
│   └── sample.pptx                             # University capstone presentation template
├── reports/
│   ├── multi_turn_prompt_injection_report.md   # Research report on multi-turn attacks & findings
│   └── ai_agent_marketplaces_report.md         # Architecture, security & use cases of agent marketplaces
├── research_papers/                            # Core reference literature
│   ├── Mind Viruses- Self-Propagating Ideas in Multi-Agent LLM Systems.pdf
│   ├── OpenAI-Hugging Face Incident-Technical-Report.pdf
│   ├── RLredAgent_promptInjection.pdf
│   └── civic_shield.pdf
└── lit_review/                                 # Domain peer papers for literature review & comparison
    ├── README.md                               # Mapping of lit review papers to core components
    ├── Prompt_Infection_LLM_to_LLM_in_MAS.pdf
    ├── Morris_II_AI_Worm_Self_Replicating_Prompts.pdf
    ├── Beyond_Single_Model_Injection_Threat_Model_MAS.pdf
    ├── Crescendo_Multi_Turn_Jailbreak_Attack.pdf
    ├── AgentDojo_Benchmark_Attacks_Defenses_LLM_Agents.pdf
    ├── InjecAgent_Benchmarking_Indirect_Prompt_Injections.pdf
    ├── PAIR_Jailbreaking_Black_Box_LLMs_Twenty_Queries.pdf
    ├── TAP_Tree_of_Attacks_Automated_Jailbreaking.pdf
    ├── Multi_Agent_LLM_Defense_Pipeline_Prompt_Injection.pdf
    ├── Llama_Guard_Input_Output_Safeguard.pdf
    └── NeMo_Guardrails_Toolkit_Safe_LLM_Applications.pdf
```

---

## Core Research References
1. **Mind Viruses in Multi-Agent LLM Systems** — Papadopoulos et al. (Anthropic Fellows / EPFL, 2024)
2. **OpenAI – Hugging Face Incident Technical Report** — OpenAI (2024)
3. **Learning to Inject: Automated Prompt Injection via Reinforcement Learning (AutoInject)** — Chen, Zhang, & Tramèr (ETH Zürich, 2024)
4. **CivicShield: A Cross-Domain Defense-in-Depth Framework for Securing AI Chatbots** — Patil (2024)
5. **The Crescendo Multi-Turn LLM Jailbreak Attack** — Russinovich, Salem, & Eldan (Microsoft Research, 2024)
