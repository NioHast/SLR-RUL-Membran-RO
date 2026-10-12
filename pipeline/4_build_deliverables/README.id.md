> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# 4_build_deliverables/ - Membangun Deliverable (Laporan, Excel, Artikel)

Folder ini mengubah data korpus + sintesis menjadi deliverable akhir: laporan Word,
spreadsheet Excel, dan artikel jurnal 2 kolom.

## Alur (order of execution)

```
fill_report.py  ->  build_docx.py        ->  SLR_Laporan.docx
      |                                          
 report_filled.md                               

build_xlsx.py          ->  SLR_Korpus.xlsx
build_article_docx.py  ->  SLR_Artikel_Jurnal.docx
```

1. `fill_report.py` - isi marker di `report.md` -> `report_filled.md`.
2. `build_docx.py` - `report_filled.md` -> `SLR_Laporan.docx`.
3. `build_xlsx.py` - korpus + sintesis -> `SLR_Korpus.xlsx`.
4. `build_article_docx.py` - `article.md` -> `SLR_Artikel_Jurnal.docx`.

## File skrip

### `fill_report.py`
- **Tujuan:** Mengganti marker HTML di `report.md` (`<!-- PRISMA -->`, `<!-- PILAR -->`, `<!-- DIMENSI -->`, `<!-- TABLES -->`, `<!-- SINTESIS -->`, `<!-- GAP -->`) dengan tabel/teks berisi angka nyata.
- **INPUT:** `BASE/corpus_*.json`, `BASE/harvest_stats.json`, `BASE/synthesis.json`, `BASE/report.md`.
- **OUTPUT:** `BASE/report_filled.md`.
- **Menjalankan:** `python3 fill_report.py`

### `build_xlsx.py`
- **Tujuan:** Membangun `SLR_Korpus.xlsx` 6 sheet (Korpus, Ringkasan & Status, Matriks Konsep, Sintesis & Gap, Peta Teori, Konsep Kunci); urut kuartil lalu tahun, sorot paper acuan (Gao), matriks centang D1-D8.
- **INPUT:** `BASE/corpus_*.json`, `BASE/harvest_stats.json`, `BASE/synthesis.json`.
- **OUTPUT:** `/home/nioha/Downloads/SLR_Korpus.xlsx`.
- **Menjalankan:** `python3 build_xlsx.py`

### `build_docx.py`
- **Tujuan:** Mengonversi laporan Markdown menjadi `SLR_Laporan.docx` (Times New Roman 12, margin 4-4-3-3 cm, spasi 1,5, tabel tanpa fill).
- **INPUT:** `report_filled.md` (fallback `report.md`).
- **OUTPUT:** `/home/nioha/Downloads/SLR_Laporan.docx`.
- **Menjalankan:** `python3 build_docx.py`

### `build_article_docx.py`
- **Tujuan:** Membangun artikel jurnal 2 kolom `.docx`: front matter 1 kolom, body 2 kolom (dipisah penanda `<!--BODY-->`).
- **INPUT:** `BASE/article.md`.
- **OUTPUT:** `/home/nioha/Downloads/SLR_Artikel_Jurnal.docx`.
- **Menjalankan:** `python3 build_article_docx.py`

## Sumber teks/data (bukan skrip)
- `report.md` - template laporan berisi marker (diisi oleh `fill_report.py`).
- `synthesis.json` - sintesis naratif per dimensi + research gap + teori + konsep.
- `article.md` - naskah artikel jurnal (dipisah `<!--BODY-->`).
- `presentation_brief.md` - brief materi presentasi.
- `assets/` - berkas reveal.js (`reveal.js`, `reveal.css`, `notes.js`) untuk slideshow.

> **NOTE:** Skrip di folder ini memakai path **ABSOLUT**. `BASE="/tmp/opencode/slr"`
> dan `OUT="/home/nioha/Downloads/..."` WAJIB kamu ubah ke lokasi kerjamu sendiri
> sebelum menjalankan.
