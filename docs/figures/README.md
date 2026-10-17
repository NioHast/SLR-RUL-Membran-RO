> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# figures/ - Essential SLR Diagrams

Valid, reproducible diagrams used by the report, journal article, and presentation.

| Figure | Content | Source | Used in |
|---|---|---|---|
| `fig01_prisma_flow` | PRISMA 2020 flow (694 -> 485 -> 72 -> +29 -> 101 assessed -> 79 included) | `src/fig01_prisma_flow.mmd` | Report, article, deck |
| `fig02_slr_process` | SLR process (Kitchenham + PRISMA + Wohlin) | `src/charts.py` | Report, deck |
| `fig03_pipeline_dataflow` | Reproducible pipeline stages 1 -> 3 -> 2+6 -> analysis -> 4 -> 5 | `src/charts.py` | Report |
| `fig04_method_architecture` | Bayesian LSTM-SURV + DSS (two layers) | `src/charts.py` | Report, article, deck |
| `fig05_decision_flow` | Cost-based maintenance decision rule | `src/fig05_decision_flow.mmd` | Report, deck |
| `fig06_censoring_timeline` | Right-censoring concept | `src/charts.py` | Report, deck |
| `fig07_pillar_distribution` | Articles per pillar A-G | `src/charts.py` | Report, article, deck |
| `fig08_dimension_coverage` | Articles per dimension D1-D8 | `src/charts.py` | Report, article, deck |
| `fig09_tier_funnel` | 694 -> 485 -> 101 assessed -> 79 included -> 46 Inti -> 19 core + gap | `src/charts.py` | Report, deck |
| `fig10_pillar_dimension_heatmap` | Webster-Watson concept matrix (pillar x dimension) | `src/charts.py` | Report, article |
| `fig11_year_trend` | Publication trend 2015-2026 | `src/charts.py` | Report |
| `fig12_quality_distribution` | Quality score distribution | `src/charts.py` | Report |

## Rebuild
```bash
pip install matplotlib
npm install -g @mermaid-js/mermaid-cli
bash src/build_figures.sh
```
All data-driven charts read `metadata/corpus_a.json` (single source of truth). The
Mermaid sources are versioned in `src/` and rendered to `png/` (300 dpi) and `svg/`.

> Note: the presentation deck now uses **native dark-theme visuals** (HTML/CSS/SVG) instead of these PNGs, so it stays fully offline. The PNG/SVG files are used by the report and journal article.
