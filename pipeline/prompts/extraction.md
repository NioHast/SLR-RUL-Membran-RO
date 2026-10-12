# Prompt: per-paper full-text extraction (Phase 5)

> Status: reconstructed from the executed plan (`docs/PLAN_PHASE5.txt`) and the Phase 5 wave
> notes (`pipeline/6_fulltext_extraction_kaggle/phase5_run_waves.md`). Bahasa Indonesia: lihat
> ringkasan di bawah. Prompt body is in English (agent-facing).

| Field | Value |
|---|---|
| **Purpose** | Read one article's full text and produce `extraction.json` + `analysis.txt` |
| **Model** | LLM subagent (OpenCode, task category `deep-low`) |
| **Version / Date** | v1 - executed 2026-10-11/12 |
| **Params** | not recorded (see `docs/AI_USAGE.md`) |
| **Input** | `papers_analysis/<NNN_...>/text.md` (Marker), selected `figures/*.jpeg`, abstract |
| **Output** | `extraction.json` (structured), `analysis.txt` (narrative, Bahasa Indonesia) |
| **Human check** | rubric calibrated on a 5-paper pilot; dual extraction on a ~15-20 paper sample; author review |

## Instructions

You are extracting structured evidence for a Systematic Literature Review (Kitchenham/SE norms,
**not** medical norms - no GRADE/RoB). Work on **one paper** per run.

1. Read the **full text** `text.md`. Read figures **selectively** (see rule 6).
2. Write `extraction.json` with these fields:
   `no, judul, penulis, tahun, jurnal, doi, kuartil, pilar`,
   `ringkasan` (2-3 sentences, from the full text),
   `kontribusi` (1-2 sentences vs the thesis gap),
   `temuan_kunci` (numbers/metrics when present),
   `dimensi` `{d1..d8}` + `alasan_dimensi` (evidence/phrase for every tick),
   `relevansi` (`Inti`/`Pendukung`/`Konteks` + sub-tag `Metode`/`Domain`/`Metode+Domain` for Inti),
   `kualitas` `{skor 0-10, rincian per Q1-Q8, catatan}`,
   `data_kuantitatif` (dataset, size, metrics RMSE/R2/CI),
   `metode`, `limitasi`, `funding_coi`,
   `status_inklusi` (`diterima` / `gugur` + reason),
   `bukti` (key figure/table/equation), `figur_dibaca` (`[{"file","isi"}]`).
3. Write `analysis.txt`: narrative in **Bahasa Indonesia** - study characteristics, method,
   data, findings, relevance to the thesis, dimension justification, quality, limitations.
4. **Dimensions (strict, evidence required).** Tick `1` only with a supporting phrase, else `""`:
   - D1 Data/sensor: multi-sensor / time-series signal (not just the word "data").
   - D2 Target/failure: defines an RUL/failure/threshold target (not just "degradation").
   - D3 Censoring: actually models/handles censored data (survival/Weibull/hazard/cure).
   - D4 Architecture: uses a specific model (LSTM/CNN/Transformer/Bayesian/RF/SVM/GP).
   - D5 Uncertainty: quantifies uncertainty (CI/posterior/interval).
   - D6 Decision: proposes/analyses a maintenance decision (schedule/cost/DSS).
   - D7 RO domain: membrane/RO/desalination/fouling object.
   - D8 Data scale: explicitly handles small/transfer/hierarchical/all-censored data.
5. **Quality rubric Q1-Q8** (0/0.5/1, total x10/7 -> 0-10): RQ clarity; method/design detail;
   data validity; reproducibility; evaluation; censoring handling; uncertainty reporting;
   decision link. Q6-Q8 may be "N/A" if irrelevant (does not lower the score).
6. **Figures:** read only when needed (architecture diagrams, key result charts, frameworks);
   target ~1-5 important figures per paper; if the caption already suffices, skip.
7. **Inclusion (full-text):** primary study on RUL/prognostics/survival/censoring, or predictive
   maintenance in membrane/water; must have data/method; journal article (not editorial).
   Otherwise set `status_inklusi` = "gugur" + reason (logged to PRISMA).
8. **QA:** no em dash (`—`) in output; consistent numbers; language = Bahasa Indonesia with
   English technical terms.

## Notes
- One agent handled a batch of 8-10 papers; 101 papers ran in ~10-13 groups over parallel waves.
- Token load is high: process per wave with checkpoints.
