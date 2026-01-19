# LLM Basics (Python)

This repository provides a **foundational, hands-on introduction** to working with
Large Language Models (LLMs) from Python.

The goal is to help users understand and practice the **core technical building blocks**
required for *any* LLM-based application, including:

- setting up a local Python environment,
- connecting securely to an LLM via an API,
- sending prompts and receiving responses,
- structuring code and repositories for reproducibility.

This repository focuses on **infrastructure and fundamentals**, not on a specific
application or domain. Concrete use cases (e.g. translation, classification, embeddings,
search, qualitative analysis) are introduced later as examples built on top of the same
foundation.

👉 **Start here:** `docs/session_01_setup.md`

---

## Repository structure

```text
.
├── docs/            # Conceptual notes and session guides
├── src/             # Reusable Python code (LLM client, helpers)
├── examples/        # Minimal, runnable examples
├── data/            # Small, non-sensitive sample inputs
├── Justfile         # Common commands to simplify setup
├── pyproject.toml   # Project configuration and dependencies
└── README.md        # You are here
