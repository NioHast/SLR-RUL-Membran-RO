# Prompt: aggregate thematic synthesis (post-extraction)

> Status: reconstructed from the executed plan (`docs/PLAN_PHASE5.txt`, section F) and the
> `synthesis.json` structure. Prompt body is in English (agent-facing); output narrative is in
> Bahasa Indonesia.

| Field | Value |
|---|---|
| **Purpose** | Turn the 101 per-paper extractions into a thematically coded synthesis + research gap |
| **Model** | LLM subagent (OpenCode) |
| **Version / Date** | v1 - executed 2026-10-12 |
| **Params** | not recorded (see `docs/AI_USAGE.md`) |
| **Input** | `metadata/corpus_a.json` (updated by `phase5_merge.py`), per-paper `extraction.json`/`analysis.txt` |
| **Output** | `pipeline/4_build_deliverables/synthesis.json`; consumed by `fill_report.py` and `build_xlsx.py` |
| **Human check** | author review; numbers cross-checked against the corpus |

## Instructions

You synthesize an **already-extracted** corpus (no new full-text reading here). Do not invent
numbers - every count must be recomputable from `metadata/corpus_a.json`.

Produce `synthesis.json` with these keys:
1. `per_dimensi` - for each D1-D8: the main findings, the count of articles, and the gap.
2. `gap_final` - the single headline research gap (the Method x Domain intersection, "Opsi C"
   tier `Inti-Metode+Domain`, is the core gap - state it plainly).
3. `sintesis_kualitatif` - **SWiM**-style narrative synthesis (no meta-analysis; engineering
   studies are heterogeneous, no pooled effect size).
4. `peta_teori` - theory/concept map to dimensions.
5. `konsep_kunci` - key concepts of the model.

Also produce/refresh the descriptive layer: distribution by year, pillar (A-G), venue, quartile.

Rules:
- Kitchenham/SE norms, not medical (no GRADE/RoB2).
- Cite concrete article counts, never hardcode stale totals - read them from the corpus.
- Output narrative in **Bahasa Indonesia** with English technical terms; **no em dash** (`—`).
- Keep it concise; this data feeds the report, the Excel "Sintesis & Gap Final" sheet, and the article.
