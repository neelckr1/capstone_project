# Adaptive Defense for Multi-Agent Systems

This repository documents a capstone research project focused on defending autonomous Multi-Agent Systems (MAS) against adversarial prompt injection, self-propagating malicious instructions, and goal-subversion attacks commonly described as "mind viruses."

This README is intentionally written to be easy for AI systems such as Gemini to understand quickly and accurately.

## TL;DR

This project is not a traditional application repository with a web app or API. Instead, it is a research and design repository for a security architecture that protects AI agents from adversarial communication and cross-agent contamination.

The central idea is simple:

- AI agents increasingly collaborate with one another.
- Those interactions create a new attack surface.
- Malicious or deceptive instructions can propagate from one agent to another.
- Existing standard filters are often insufficient because attacks are semantic, multi-turn, and adaptive.

The project proposes a layered defense-in-depth system:

- System-1 triage layer for fast filtering and routing
- System-2 deliberative reasoning for ambiguous or suspicious cases
- Quarantine and escalation for high-risk behaviors
- Continuous adversarial red-team testing to improve robustness over time

## Problem Statement

Modern LLM-based systems are moving from single-model chatbots to interconnected agent ecosystems. In those multi-agent settings, one compromised or malicious agent can influence others through shared messages, tool calls, memory, or instructions.

This creates a class of threats known as "mind viruses": malicious ideas, instructions, or behavioral drift that spread across agents and alter their objectives or tool usage.

The research focuses on questions such as:

- How do malicious instructions spread across agent networks?
- Which message patterns or decision trajectories indicate infection or drift?
- How can a system detect risky exchanges before they escalate?
- How can we keep latency and cost low while preserving strong security?

## Core Research Vision

The project proposes an adaptive defense architecture designed for agent-to-agent environments.

At a high level, the system works as follows:

1. Incoming inter-agent traffic is first screened by a lightweight triage layer.
2. Low-risk communication is allowed quickly.
3. Ambiguous or suspicious traffic is escalated to deeper reasoning.
4. High-risk or confirmed malicious communication is blocked and quarantined.
5. The system continuously tests itself against adversarial prompt-injection strategies.

This design mirrors defense-in-depth principles and zero-trust assumptions: assume the environment is hostile, validate each step, and reduce trust in unverified agent outputs.

## High-Level Architecture

The project describes a layered model similar to the following:

- Layer 1: System-1 triage gate
  - Fast, low-latency decision model
  - Flags nominal, suspicious, or critical behavior
  - Routes traffic efficiently

- Layer 2: System-2 deliberative reasoning
  - Deep inspection of suspicious trajectories
  - Compares agent goals against expected invariants
  - Performs sandboxed simulation before execution

- Layer 3: Containment and escalation
  - Quarantines compromised agents
  - Surfaces issues to human reviewers
  - Prevents propagation across the system

- Continuous red-teaming engine
  - Uses adversarial prompting, mutation, and reinforcement-learning-based attacks
  - Strengthens the defense over time

## Research Objectives

The capstone evaluates whether this defense architecture can:

- detect prompt injection and behavioral drift reliably
- suppress spread of malicious instructions across agent networks
- reduce latency and compute overhead compared to heavy monolithic guardrails
- maintain practical utility while improving security

The project also measures performance using concepts such as:

- detection accuracy
- false positive rate
- propagation suppression
- system latency
- cost efficiency
- resilience to multi-turn and adaptive attacks

## Repository Structure

```text
.
├── README.md                      # Project overview and AI-readable summary
├── AGENTS.md                      # Collaboration and git sync instructions
├── vision.md                      # Main design/vision document
├── training_pipeline.jpeg          # Training/defense pipeline diagram
├── reports/
│   ├── ai_agent_marketplaces_report.md
│   └── multi_turn_prompt_injection_report.md
├── research_papers/              # Key anchor research papers
│   ├── Mind Viruses- Self-Propagating Ideas in Multi-Agent LLM Systems.pdf
│   ├── OpenAI-Hugging Face Incident-Technical-Report.pdf
│   ├── RLredAgent_promptInjection.pdf
│   └── civic_shield.pdf
├── lit_review/                   # Supporting literature review materials
│   ├── README.md
│   ├── Prompt_Infection_LLM_to_LLM_in_MAS.pdf
│   ├── Morris_II_AI_Worm_Self_Replicating_Prompts.pdf
│   ├── Beyond_Single_Model_Injection_Threat_Model_MAS.pdf
│   ├── Crescendo_Multi_Turn_Jailbreak_Attack.pdf
│   ├── AgentDojo_Benchmark_Attacks_Defenses_LLM_Agents.pdf
│   ├── InjecAgent_Benchmarking_Indirect_Prompt_Injections.pdf
│   ├── PAIR_Jailbreaking_Black_Box_LLMs_Twenty_Queries.pdf
│   ├── TAP_Tree_of_Attacks_Automated_Jailbreaking.pdf
│   ├── Multi_Agent_LLM_Defense_Pipeline_Prompt_Injection.pdf
│   ├── Llama_Guard_Input_Output_Safeguard.pdf
│   └── NeMo_Guardrails_Toolkit_Safe_LLM_Applications.pdf
└── review_1/                     # Draft or earlier review artifacts
```

## Recommended Reading Order

For a human or AI agent trying to understand the repo quickly, this is the ideal order:

1. README.md
2. vision.md
3. lit_review/README.md
4. reports/
5. research_papers/

This order gives the high-level concept first, then the architectural reasoning, then the actual evidence base.

## Important Context for AI Readers

This repository should be interpreted as a research, security architecture, and literature review project rather than a code application.

Important assumptions:

- The project is focused on agent security, not generic software engineering.
- The primary threat model is adversarial communication between autonomous agents.
- The solution is architecture-oriented and conceptual, supported by research literature.
- There is no conventional software setup or app runtime in this repo by default.

## Key Terms

- MAS: Multi-Agent System
- Mind Virus: a self-propagating malicious idea or instruction that changes agent behavior
- Prompt Injection: adversarial instruction embedded in input or tool output
- System-1: fast triage model
- System-2: deeper reasoning and deliberation
- HITL: Human-in-the-loop escalation
- Red Teaming: proactive adversarial testing of the system
- Defense-in-Depth: layered security rather than single-point protection

## Research Themes Covered

This project synthesizes several major themes:

- prompt injection in agent workflows
- multi-agent propagation risks
- security of tool-calling and autonomous action loops
- red-team attack generation and benchmarking
- layered defense architectures for LLM systems
- zero-trust assumptions for agent communication

## Suggested Use

This repository is useful for:

- capstone research documentation
- literature review synthesis
- idea generation for defending LLM agents
- architecture discussions and presentations
- security experimentation design

## Notes for Future Development

The repo is structured to support future extensions such as:

- attack simulation environments
- benchmark harnesses for injection scenarios
- detection model experiments
- quarantine and escalation dashboards
- comparative evaluation across agent topologies

## Summary

This project explores how to build an adaptive immune system for autonomous AI agents. The long-term goal is not just to block single attacks, but to create a robust, scalable defense model that can detect malicious intent, limit propagation, and maintain system safety in dynamic multi-agent environments.

For Gemini or any other AI reader, the essential idea is:

This is a research repository about defending multi-agent AI systems against self-replicating adversarial instructions using a layered, adaptive security architecture.

---

If you want, I can also produce a second version of the README tailored specifically for:

- GitHub presentation quality
- academic capstone submission
- AI/LLM readability
- a more concise executive-summary version
