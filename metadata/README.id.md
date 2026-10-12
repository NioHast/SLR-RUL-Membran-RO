> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# metadata/ - Data Antara & Pemetaan

JSON untuk menjalankan pipeline & dokumentasi korpus:
- `corpus_a.json` - **korpus master** (101 artikel): no, pilar, judul, penulis, tahun, jurnal, klasifikasi (kuartil),
  relevansi, kualitas, dimensi d1-d8, ringkasan, kontribusi.
- `issn_map.json` - pemetaan DOI -> ISSN jurnal.
- `scopus_official.json` - kuartil resmi SCImago (SJR Best Quartile) per DOI.
- `scopus_check.json` - kuartil estimasi (SJR 2024) per DOI.
- `harvest_stats.json` - statistik pencarian (angka PRISMA).
- `pool.json`, `ranked.json`, `selected*.json`, `replacement_pool.json`, `oa_*.json`, `core_*.json` - kandidat & proses seleksi.
- `phase5_gugur.json` - daftar paper gugur (final: kosong).
