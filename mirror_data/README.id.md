> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# mirror_data/ - Data SJR/Scopus (SCImago)

Data publik yang dipakai untuk **klasifikasi kuartil jurnal**. Semua file di folder ini adalah
**salinan publik (mirror)** dari data SCImago/Scopus, diunduh agar pipeline SLR bisa berjalan
**otomatis tanpa login/kredensial**. Sumber resmi: **SCImago** (https://www.scimagojr.com) dan
**Scopus** (Elsevier).

> **Atribusi wajib bila dikutip:**
> SCImago. (n.d.). *SJR - SCImago Journal & Country Rank.* Retrieved from https://www.scimagojr.com

## Isi
- `sjr_quart.csv` - SCImago ed. 2022 (kolom **"SJR Best Quartile"**, Q1-Q4).
- `sjr_all.csv` - panel SCImago 1999-2025 (SJR + ISSN).
- `scopus_titles.tsv` - daftar judul Scopus 2021.

## Sumber & Detail Tiap File
**1) `sjr_quart.csv`**
- Isi: peringkat jurnal SCImago + kolom "SJR Best Quartile" (Q1-Q4), ISSN, SJR, H-index, Coverage, Categories, Areas.
- Edisi: **SCImago 2022** | Ukuran: ~8 MB, 27.955 baris.
- Mirror: https://huggingface.co/datasets/inria-soda/carte-benchmark (file `data_raw/journal_sjr.csv`).
- Raw URL: `https://huggingface.co/datasets/inria-soda/carte-benchmark/resolve/main/data_raw/journal_sjr.csv`
- Asal: bagian dari dataset benchmark penelitian tim INRIA (SODA).
- Lisensi: Data SCImago (CC BY-NC; non-komersial, dengan atribusi).

**2) `sjr_all.csv`**
- Isi: panel SCImago 1999-2025 (Title, field, year, SJR, h-index, avg_citations, Issn, Sourceid) - TANPA kolom kuartil.
- Ukuran: ~84 MB, 1.024.562 baris.
- Mirror: https://github.com/Michael-E-Rose/SCImagoJournalRankIndicators
- Raw URL: `https://raw.githubusercontent.com/Michael-E-Rose/SCImagoJournalRankIndicators/master/all.csv`
- Catatan: dipakai untuk (a) mendeteksi jurnal baru, (b) menurunkan kuartil per bidang pada tahun terbaru bila tak ada di `sjr_quart.csv`.
- Lisensi: Data SCImago (CC BY-NC), dikompilasi peneliti pihak ketiga.

**3) `scopus_titles.tsv`**
- Isi: daftar judul Scopus (scopus_id, title_name, ISSN print/electronic, Active or Inactive, Coverage, ASJC, dst).
- Edisi: **Scopus Source List 2021** | Ukuran: ~5,7 MB, 82.234 baris.
- Mirror: https://github.com/dhimmel/scopus (file `data/titles.tsv`).
- Raw URL: `https://raw.githubusercontent.com/dhimmel/scopus/main/data/titles.tsv`
- Catatan: hanya rujukan status terindeks; versi 2021 (lama).
- Lisensi: Data Scopus (Elsevier) - dataset turunan untuk riset.

## Catatan Penting
- Mirror pihak ketiga bisa **kedaluwarsa / tidak lengkap**. Untuk sitasi formal, tetap rujuk sumber aslinya (SCImago/Scopus) + tanggal akses.
- Untuk data 100% resmi Scopus (coverage + status aktif terbaru), perlu "Scopus Source List" (unduh via akun/langganan Scopus) - tidak bisa otomatis.
- Cara mengunduh ulang: `python3 ../pipeline/3_journal_classification/download_mirrors.py`.
- Tanggal unduh mirror pada paket ini: **2026-10-11** (Asia/Jakarta).
