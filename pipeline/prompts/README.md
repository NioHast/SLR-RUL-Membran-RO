> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# prompts/ - Versioned AI Prompt Templates

Prompt templates used to produce the analysis and deliverables. These document **intent**;
they do not guarantee reproduction (LLM output is non-deterministic). See
[`docs/AI_USAGE.md`](../../docs/AI_USAGE.md) for what AI was used for.

| File | Stage | Output | Model / date |
|---|---|---|---|
| `extraction.md` | Phase 5 - per-paper full-text extraction | `papers_analysis/*/extraction.json` + `analysis.txt` | LLM subagent (`deep-low`), 2026-10-11/12 |
| `synthesis.md` | Aggregate thematic synthesis | `pipeline/4_build_deliverables/synthesis.json` | LLM subagent, 2026-10-12 |
| `presentation.md` | Presentation deck | `SLR_Presentasi.html` (+ PDF) | LLM subagent, 2026-10-12 |
| `deliverable_style.md` | (cross-cutting) | style contract for docx/xlsx/deck | reference (not a task prompt) |

## How to use
- Fill the placeholders (e.g. `{PAPER_TEXT}`) with your inputs.
- Record the **model / version / date / parameters** in the header table before running.
- The deterministic build scripts (`pipeline/4_build_deliverables/*.py`) remain the **source of truth**
  for formatting; keep `deliverable_style.md` in sync with them (no drift).
- Deliverable prose is Bahasa Indonesia with English technical terms; **no em dash** (`—`).
