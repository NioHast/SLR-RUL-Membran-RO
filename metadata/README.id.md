> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# metadata/ - Data Antara & Pemetaan

JSON untuk menjalankan pipeline & dokumentasi korpus:
- `corpus_a.json` - **korpus assessed** (101 record; 79 included): no, pilar, judul, penulis, tahun, jurnal, klasifikasi (kuartil),
  relevansi, kualitas, dimensi d1-d8, ringkasan, kontribusi.
- `issn_map.json` - pemetaan DOI -> ISSN jurnal.
- `scopus_official.json` - kuartil resmi SCImago (SJR Best Quartile) per DOI.
- `scopus_check.json` - kuartil estimasi (SJR 2024) per DOI.
- `harvest_stats.json` - statistik pencarian (angka PRISMA).
- `prisma_flow.json` - rekonstruksi angka PRISMA (sumber tunggal untuk alur).
- `core_papers.json` - skor 101 record (relevansi RQ, kedekatan metode, kualitas), flag core + peran.
- `pool.json`, `ranked.json`, `selected*.json` - kandidat & funnel seleksi.
- `oa_core_filtered.json`, `oa_replacements.json`, `replacement_pool.json`, `core_replacements_detail.json`,
  `core_failed_downloads.json` - set kandidat OA/pengganti & provenansnya.
  `oa_replacements.json` menggabungkan `oa_core_replacement.json` + `oa_core_replacement2.json` +
  `oa_replacement.json` menjadi satu file (dedup per DOI; tiap baris menyimpan field `batch`).
- `phase5_gugur.json` - daftar paper gugur (final: kosong).
