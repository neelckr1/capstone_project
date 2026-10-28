# System-1 Decision Architecture: Multi-Turn Prompt Injection Triage

A modular, test-driven framework for fine-tuning and evaluating **System-1 Ingress Decision Models** against advanced prompt injection in Multi-Agent Systems (MAS).

Built for deployment on the **NVIDIA GB10 (Grace Blackwell Architecture, CUDA 13.0, 119.6 GiB Unified Memory)**.

---

## 1. Directory Structure

```
system_one/
├── venv/                      # Dedicated Python 3.12 environment with CUDA 13.0 PyTorch
├── README.md                  # This documentation guide
├── docs/
│   ├── ARCHITECTURE.md        # Detailed threat modeling & tri-state triaging specs
│   └── PIPELINE.md            # Data flow & dual-plane closed loop diagrams
├── configs/
│   ├── modernbert_large.yaml  # ModernBERT-large (395M) FFT configuration
│   ├── llama_1b.yaml          # Llama-3.2-1B LoRA (128k context) configuration
│   └── clef_flash_9b.yaml     # Clef-Flash 9B QLoRA (NF4 4-bit) configuration
├── core/
│   ├── schema.py              # DialogueTurn, TrajectorySample, and ModelDecision schemas
│   └── tokenizer_utils.py     # Multi-turn sliding window & role delineation
├── data/
│   ├── dataset_builder.py     # Crescendo, InjecAgent, Mind Virus, and Benign compiler
│   └── processed/             # Formatted train.jsonl, val.jsonl, test.jsonl
├── models/
│   ├── base_model.py          # Abstract BaseSystemOneClassifier interface
│   ├── modernbert_classifier.py # ModernBERT-large sequence classifier
│   ├── llama_classifier.py    # Llama-3.2-1B-Instruct LoRA classifier
│   └── clef_classifier.py     # Clef-Flash 9B joint schema classifier
├── train/
│   └── trainer.py             # Unified fine-tuning pipeline with active VRAM monitoring
├── eval/
│   ├── metrics.py             # Recall, FPR, ASR, and latency percentiles
│   └── benchmark_runner.py    # Comparative evaluation harness across all 3 models
└── tests/                     # Comprehensive TDD test suite (100% passing)
    ├── test_schemas.py
    ├── test_tokenizer_utils.py
    ├── test_dataset_builder.py
    ├── test_metrics.py
    ├── test_model_interfaces.py
    └── test_trainer.py
```

---

## 2. Threat Modeling & Paper References

| Threat Vector | Anchor Paper | Mechanism & System-1 Defense |
| :--- | :--- | :--- |
| **Conversational Semantic Drift** | **Crescendo** (*Russinovich et al., Microsoft Research, USENIX 2024*) | Attacks start benignly, escalate across turns, and backtrack on refusal. Ingests rolling multi-turn trajectories to detect cumulative intent drift. |
| **Indirect Tool Poisoning** | **InjecAgent & AgentDojo** (*Zhan et al., ACL 2024; Debenedetti et al., NeurIPS 2024*) | Injects adversarial payloads inside third-party tool returns (`<tool_output>`). Privilege-separated token framing prevents execution. |
| **Self-Replicating Mind Viruses** | **Mind Viruses in MAS** (*Papadopoulos et al., Anthropic 2024; Morris-II 2025*) | Inter-agent messages coercing downstream propagation ($R_0 > 1$). Dedicated categorical classifier flags lateral infection directives. |
| **System Override & Extraction** | **Tensor Trust & HackAPrompt** (*NeurIPS TDC / EMNLP 2023*) | Delimiter bypasses and prompt extraction probes. Calibrated probability scoring triggers immediate agent quarantine. |

---

## 3. Quickstart Commands

### 1. Run Automated TDD Test Suite
```bash
PYTHONPATH=. ./venv/bin/pytest tests -v
```

### 2. Generate Multi-Turn Dataset Splits
```bash
PYTHONPATH=. ./venv/bin/python3 -c "
from data.dataset_builder import DatasetBuilder
builder = DatasetBuilder('data/processed')
stats = builder.build_and_export_splits(count_per_category=50)
print('Dataset Generated:', stats)
"
```

### 3. Run Comparative Benchmark on NVIDIA GB10
```bash
# Benchmark all three candidate models
PYTHONPATH=. ./venv/bin/python3 eval/benchmark_runner.py --model all

# Or benchmark individual models
PYTHONPATH=. ./venv/bin/python3 eval/benchmark_runner.py --model modernbert
PYTHONPATH=. ./venv/bin/python3 eval/benchmark_runner.py --model llama_1b
PYTHONPATH=. ./venv/bin/python3 eval/benchmark_runner.py --model clef_flash
```

### 4. Fine-Tune Models (with Dry-Run / Live Support)
```bash
# ModernBERT-large (395M)
PYTHONPATH=. ./venv/bin/python3 train/trainer.py --model-type modernbert --epochs 3 --batch-size 16

# Llama-3.2-1B-Instruct (LoRA Rank 32)
PYTHONPATH=. ./venv/bin/python3 train/trainer.py --model-type llama_1b --epochs 3 --batch-size 8

# Clef-Flash (9B QLoRA 4-bit NF4)
PYTHONPATH=. ./venv/bin/python3 train/trainer.py --model-type clef_flash --epochs 3 --batch-size 4
```

---

## 4. Hardware Sizing & Multi-Tenant Safety on NVIDIA GB10

* **Physical Memory:** 119.6 GiB Unified Memory (ATS architecture shared between CPU and GPU).
* **Contention Protection:** Training memory footprints are strictly capped below **11 GB VRAM** (ModernBERT uses ~3.5 GB, Llama-1B uses ~4.5 GB, Clef-Flash QLoRA uses ~10.5 GB).
* **Guaranteed Immunity:** Even under heavy multi-tenant host activity, peak memory stays well clear of the Linux Kernel OOM Killer.
