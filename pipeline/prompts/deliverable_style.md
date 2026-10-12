# Deliverable style contract (single source of truth)

> Shared reference for humans **and** AI agents producing deliverables. The build scripts
> (`build_xlsx.py`, `build_docx.py`, `build_article_docx.py`, `fill_report.py`) are the
> **enforcers**; this file documents the contract. Never let the two drift: if you change a
> rule here, change the script too (and vice versa). Prompt body/notes in English; deliverable
> prose is in Bahasa Indonesia (+ English technical terms).

## Global
- **Language:** Bahasa Indonesia, with English technical terms kept in English. **No em dash (`—`)**; use `:` or `,`.
- **Numbers:** always read the real counts from `metadata/corpus_a.json`; never hardcode stale totals.
- **No external images** that could fail to load (offline-safe). Prefer tables, CSS/Chart.js bars.
- **Citations:** author-year; include DOI where available.

## DOCX - report (`SLR_Laporan.docx`)
- Font **Times New Roman 12**; line spacing **1.5**; margins **4-4-3-3 cm** (top-right-bottom-left).
- Tables: no fill/shading; header row bold; borders minimal.
- Headings hierarchical; figures/tables numbered + captioned.

## DOCX - journal article (`SLR_Artikel_Jurnal.docx`)
- Front matter = 1 column; body = **2 columns**; the split is marked by `<!--BODY-->` in `article.md`.
- Keep to journal-style section order (Abstract, Introduction, Method, Results, Discussion, Conclusion, References).

## XLSX - corpus (`SLR_Korpus.xlsx`)
- Sheets: `SLR - Korpus Jurnal`, `Ringkasan & Status`, `Matriks Konsep (Webster-Watson)`,
  `Sintesis & Gap Final`, `Peta Teori ke Dimensi`, `Konsep Kunci Model`.
- Corpus columns: No, Pilar, Judul, Penulis, Tahun, Jurnal, Klasifikasi, **Relevansi**, **Kualitas**, DOI, Ringkasan, Kontribusi.
- Sort by quartile then year; highlight the reference paper (Gao); D1-D8 as a checkmark matrix.

## Presentation (`SLR_Presentasi.html` + PDF)
- **reveal.js 5.x** (CDN or local `assets/`), **16:9**, dark academic theme (not plain default).
- Palette: deep blue `#1F4E78`, gray, orange accent. Font: Inter/Arial (sans-serif).
- Progress bar + slide numbers; smooth transitions; keyboard navigation; offline-safe.
- Every slide has short **speaker notes** in `<aside class="notes">`; <= 6 points per slide.
- Charts: simple and robust (Chart.js via CDN or CSS bars).

## Accessibility & size
- Sufficient contrast; readable font sizes; no color-only encoding.
- Keep files offline-openable (no build step required to view).
