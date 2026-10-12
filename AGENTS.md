# AGENTS.md

Guidance for AI coding agents working in this repository.

## What this is
A Systematic Literature Review (SLR) of 101 articles on **RUL prediction of reverse-osmosis (RO)
membranes** (survival analysis + deep learning with censored data). Research artifact; issues/PRs
may not be monitored. AI-use details: [`docs/AI_USAGE.md`](docs/AI_USAGE.md).

## Layout
| Path | Contents |
|---|---|
| `docs/` | Final deliverables (protocol, corpus `.xlsx`, report/article `.docx`/`.pdf`, presentation, logs). |
| `papers_analysis/` | Per-paper results: `extraction.json`, `analysis.txt` (+ `full_text.*`, `figures/`, `meta.json`, `SOURCE.txt` for OA). |
| `pipeline/1..6/` | Source code per stage. `pipeline/prompts/` = AI prompt templates. |
| `metadata/` | Intermediate JSON: master corpus, ISSN/quartile maps, search stats, selection artifacts. |
| `mirror_data/` | SCImago/SJR mirrors used for quartile classification. |

## Golden rules
1. **Bilingual pairs:** every `README.md` has a `README.id.md` with line 1 exactly
   `> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)`. Same for `RUNBOOK.md`.
2. **Script docstrings:** every `.py` starts with a module docstring with `Purpose / INPUT / OUTPUT / How to run / NOTE`.
3. **Commit style:** Conventional Commits, `type(scope): imperative subject` (types: `docs`, `refactor`, `style`, `feat`, `fix`; scopes: `pipeline`, `metadata`, `readme`, `presentation`, `docs`). English.
4. **Language:** docs/code comments in English; deliverable prose is Bahasa Indonesia (+ English technical terms). **No em dash (`—`).**
5. **Never commit secrets** (Kaggle token lives in `~/.kaggle/access_token`, never in the repo). `.gitignore` is intentionally empty.
6. **Never touch** `papers_analysis/*/full_text.md`, `*.pdf`, or `figures/` - these are copyrighted third-party content.

## How to run (order matters: 1 -> 3 -> 2+6 -> analysis -> 4 -> 5, not numeric)
```bash
# 1. search & select        -> metadata/*.json
python3 pipeline/1_search_and_select/harvest.py && python3 pipeline/1_search_and_select/rank.py && python3 pipeline/1_search_and_select/select.py
# 3. journal classification -> metadata/issn_map.json, open_access_status.json
python3 pipeline/3_journal_classification/download_mirrors.py && python3 pipeline/3_journal_classification/issn.py
# 2 + 6. full-text (Marker on Kaggle GPU)
python3 pipeline/2_get_fulltext/download_fulltext.py
python3 pipeline/6_fulltext_extraction_kaggle/make_kernel.py   # then push kernel/dataset via Kaggle CLI
python3 pipeline/6_fulltext_extraction_kaggle/phase2_assemble.py && python3 pipeline/6_fulltext_extraction_kaggle/phase2_finalize.py
# 4. deliverables (docx/xlsx/pdf)
python3 pipeline/4_build_deliverables/fill_report.py && python3 pipeline/4_build_deliverables/build_xlsx.py && python3 pipeline/4_build_deliverables/build_docx.py
# 5. verify references
python3 pipeline/5_verify_references/verify_refs.py
```
**NOTE:** several scripts use **absolute paths** (`BASE=/tmp/opencode/slr`, `ROOT=/home/nioha/Downloads/SLR`); adjust before running. System deps: LibreOffice (`soffice`), Pandoc, Ghostscript.

## Data flow
`metadata/corpus_a.json` is the **master corpus** (101 articles). `phase5_merge.py` writes analysis
results into it; `synthesis.json` + corpus feed the deliverable builders; `open_access_status.json`
drives which papers get full text.

## Verification (no CI in this repo)
- `python3 -m py_compile <file>` on changed scripts.
- `python3 -c "import json; json.load(open('<file>'))"` for changed JSON / notebooks.
- Stage 5 (`verify_refs.py`) + `verify_scopus.py` for data integrity.
- Bilingual pairs complete; no leftover em dash; no secrets.

## License
Code = **MIT-0** (`LICENSE`); author content = **CC0** (`LICENSE-CONTENT`); third-party data/articles
keep their own licenses (`NOTICE`; SCImago = CC BY-NC).
