> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# papers_analysis/ - Analisis per Paper

Satu subfolder per artikel (101 folder). Nama folder:
`NNN_PenulisPertama_Tahun_Kuartil_Judul` (NNN = nomor urut sesuai kolom "No" di `docs/SLR_Korpus.xlsx`).

## Isi tiap folder
Berlaku untuk semua folder:
- `extraction.json` - ekstraksi terstruktur dari **full-text**: identitas, pilar, ringkasan,
  kontribusi, temuan kunci, **dimensi D1-D8 + alasan (bukti)**, **tingkat relevansi**,
  **skor kualitas (Q1-Q8)**, data kuantitatif, metode, limitasi, funding/COI, status inklusi.
- `analysis.txt` - analisis naratif (Bahasa Indonesia) dari isi penuh.

**HANYA untuk artikel Open Access berlisensi Creative Commons** (77 folder) ditambahkan:
- `full_text.pdf` - salinan PDF full-text (artikel asli).
- `full_text.md` - hasil ekstraksi teks penuh via **Marker**: teks sadar-kolom + **rumus dalam LaTeX** + tabel Markdown.
- `figures/` - figur/gambar hasil ekstraksi dari artikel.
- `meta.json` - metadata keluaran Marker (jumlah halaman, statistik, dll).
- `SOURCE.txt` - keterangan DOI + lisensi + **atribusi wajib**.

## Kebijakan Full-Text (MENGAPA ada yang ada, ada yang tidak)
Repositori ini menyertakan full-text **hanya untuk artikel yang Open Access DAN berlisensi
Creative Commons (CC)** - diizinkan untuk didistribusikan ulang (dengan atribusi).

- **77 dari 101 artikel** berstatus **OA + CC** -> `fulltext.pdf` **disertakan**.
- **24 artikel** lainnya **tidak disertakan** `fulltext.pdf`-nya karena:
  - **closed** (berlangganan) -> tidak boleh didistribusikan ulang, atau
  - **bronze / tanpa lisensi / "other-oa"** -> gratis dibaca tapi **tanpa izin redistribusi**.
  Untuk artikel-artikel ini hanya tersedia **hasil analisis** (`extraction.json`, `analysis.txt`) + **DOI**.

Atribusi: setiap `fulltext.pdf` tetap milik penulis/penerbit aslinya; lisensi CC mewajibkan
pencantuman atribusi (lihat `SOURCE.txt` di tiap folder).

## Cara mengecek status OA/legalitas
Skrip: `../pipeline/3_journal_classification/check_open_access.py` (memakai API Unpaywall).
Hasil lengkap (status OA, lisensi, termasuk/tidak): `../metadata/open_access_status.json`.
