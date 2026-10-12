> 🇬🇧 [English](AI_USAGE.md) | 🇮🇩 [Bahasa Indonesia](AI_USAGE.id.md)

# AI Usage Disclosure

This repository is a Systematic Literature Review (SLR) research artifact. Generative AI
(LLM) tools assisted **specific, documented stages**; **all study-selection decisions, quality
appraisal, and final content were made and reviewed by the human author**. Prompt templates are
versioned in [`pipeline/prompts/`](../pipeline/prompts/README.md).

## What AI was used for
| Stage | AI role | Tool / model | Human check |
|---|---|---|---|
| Phase 5 - per-paper extraction | Read each article's full text (`text.md` from Marker) + selected figures; write `extraction.json` + `analysis.txt` (summary, key findings, dimension tags + evidence, Q1-Q8 quality, tier) | LLM subagents (`deep-low`) in parallel waves | 5-paper rubric pilot + dual extraction on a sample + author review |
| Aggregate synthesis | Thematic synthesis (D1-D8), research gap, theory/concept map | LLM subagent | author review; counts cross-checked vs corpus |
| Narrative deliverables | Drafting report / journal-article narrative | LLM-assisted | author review |
| Presentation | Build the reveal.js deck from `pipeline/prompts/presentation.md` | LLM subagent | author review |
| Repo housekeeping | READMEs, docs, formatting, commit messages | LLM coding agent | author review |

## What AI did NOT do (deterministic code or human)
- Record search & selection (`pipeline/1_search_and_select/`), journal/quartile classification
  (`pipeline/3_journal_classification/`), reference verification (`pipeline/5_verify_references/`).
- Full-text conversion: **Marker** (`marker-pdf==1.10.2`) - a machine-learning PDF-to-Markdown
  pipeline (layout/OCR models), not a generative LLM; invoked deterministically.
- Deliverable construction: `build_xlsx.py`, `build_docx.py`, `build_article_docx.py`, `fill_report.py`.
- Final corpus of 101 articles, the quartile policy, and every inclusion/exclusion call.
- The keyword-based dimension heuristic in `phase2_assemble.py` was **cancelled** (too loose);
  official dimensions come from the Phase 5 review.

## Model & environment
- AI steps ran as **LLM subagents (OpenCode, task category `deep-low`)** in timestamped parallel
  waves on **2026-10-11/12**.
- The exact backing LLM name/version was **not recorded** in this repo. `[FILL IN if known]`
- Full-text extraction: `marker-pdf==1.10.2` on a Kaggle GPU (NVIDIA T4).
- No API keys/tokens are stored in this repository.

## Limitations & responsibility
- LLM output is **non-deterministic**: prompts document intent, not guaranteed reproduction.
- AI-generated fields were spot-checked; residual errors remain the author's responsibility.
- Each prompt records model/version/date/parameters in its header.

## Disclosure statement (ready to paste)
> Generative AI (LLM) tools were used to assist with full-text data extraction, thematic synthesis,
> drafting, and repository documentation. All study-selection decisions, quality appraisal, and final
> content were reviewed and approved by the author, who takes full responsibility for the work.

Cite as: Hastungkoro, M. N. (2026). *SLR: RUL Prediction of Reverse Osmosis Membranes*.
GitHub. https://github.com/NioHast/SLR-RUL-Membran-RO - see `docs/AI_USAGE.md`.
