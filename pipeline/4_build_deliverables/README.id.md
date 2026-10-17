> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# 4_build_deliverables/ - Membangun Deliverable

Mengubah data korpus + sintesis menjadi deliverable akhir. Semua keluaran ditulis ke
`docs/` (tanpa path absolut).

## Alur (urutan)

```
docs/figures/src/build_figures.sh   -> docs/figures/png/*.png + svg/*.svg
fill_report.py                      -> report_filled.md
build_docx.py                       -> docs/SLR_Laporan.docx  (+ PDF via LibreOffice)
build_xlsx.py                       -> docs/SLR_Korpus.xlsx   (7 sheet)
build_article_docx.py               -> docs/SLR_Artikel_Jurnal.docx (+ PDF)
build_presentation.py               -> docs/SLR_Presentasi.html (+ PDF via Chrome)
```

## Skrip

| Skrip | Fungsi | Input -> Output |
|---|---|---|
| `fill_report.py` | Isi marker dengan angka dari sumber tunggal | `metadata/corpus_a.json`, `prisma_flow.json`, `core_papers.json`, `synthesis.json`, `report.md` -> `report_filled.md` |
| `build_docx.py` | Laporan gaya tesis (TNR 12, margin 4-4-3-3, spasi 1,5) + gambar | `report_filled.md` -> `docs/SLR_Laporan.docx` |
| `build_xlsx.py` | Workbook 7 sheet (tambah "Paper Inti & Skor") | korpus + sintesis + core -> `docs/SLR_Korpus.xlsx` |
| `build_article_docx.py` | Artikel jurnal 2 kolom + gambar | `article.md` -> `docs/SLR_Artikel_Jurnal.docx` |
| `build_presentation.py` | Validasi (17 slide, offline, angka) + bangun PDF | `docs/SLR_Presentasi.html` -> `docs/SLR_Presentasi.pdf` |

## Penanda gambar
`report.md` dan `article.md` mendukung `{{FIG:file.png|caption|width_cm}}`; berkas diambil
dari `docs/figures/png/` dan dirender dengan caption otomatis `Gambar N.`. Tabel/gambar
lebar pada artikel membentang dua kolom melalui section break.

## Sumber teks/data
- `report.md` - template laporan berisi marker (diisi `fill_report.py`).
- `synthesis.json` - sintesis naratif per dimensi + gap + teori + konsep.
- `article.md` - naskah artikel jurnal (dipisah `<!--BODY-->`).
- Prompt presentasi: [`../prompts/presentation.md`](../prompts/presentation.md).
- Kontrak gaya: [`../prompts/deliverable_style.md`](../prompts/deliverable_style.md).
