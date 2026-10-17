> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# figures/ - Diagram Penting SLR

Diagram valid dan reproducible yang dipakai laporan, artikel jurnal, dan presentasi.

| Gambar | Isi | Sumber | Dipakai di |
|---|---|---|---|
| `fig01_prisma_flow` | Alur PRISMA 2020 (694 -> 485 -> 72 -> +29 -> 101 assessed -> 79 included) | `src/fig01_prisma_flow.mmd` | Laporan, artikel, deck |
| `fig02_slr_process` | Proses SLR (Kitchenham + PRISMA + Wohlin) | `src/charts.py` | Laporan, deck |
| `fig03_pipeline_dataflow` | Tahap pipeline reproducible 1 -> 3 -> 2+6 -> analisis -> 4 -> 5 | `src/charts.py` | Laporan |
| `fig04_method_architecture` | Bayesian LSTM-SURV + DSS (dua lapis) | `src/charts.py` | Laporan, artikel, deck |
| `fig05_decision_flow` | Aturan keputusan perawatan berbasis biaya | `src/fig05_decision_flow.mmd` | Laporan, deck |
| `fig06_censoring_timeline` | Konsep right-censoring | `src/charts.py` | Laporan, deck |
| `fig07_pillar_distribution` | Artikel per pilar A-G | `src/charts.py` | Laporan, artikel, deck |
| `fig08_dimension_coverage` | Artikel per dimensi D1-D8 | `src/charts.py` | Laporan, artikel, deck |
| `fig09_tier_funnel` | 694 -> 485 -> 101 assessed -> 79 included -> 46 Inti -> 19 core + gap | `src/charts.py` | Laporan, deck |
| `fig10_pillar_dimension_heatmap` | Matriks konsep Webster-Watson (pilar x dimensi) | `src/charts.py` | Laporan, artikel |
| `fig11_year_trend` | Tren publikasi 2015-2026 | `src/charts.py` | Laporan |
| `fig12_quality_distribution` | Sebaran skor kualitas | `src/charts.py` | Laporan |

## Build ulang
```bash
pip install matplotlib
npm install -g @mermaid-js/mermaid-cli
bash src/build_figures.sh
```
Semua chart berbasis data membaca `metadata/corpus_a.json` (sumber tunggal). Sumber
Mermaid disimpan di `src/` dan dirender ke `png/` (300 dpi) dan `svg/`.
