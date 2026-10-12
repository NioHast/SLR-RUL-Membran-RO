> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# metadata/ - Intermediate Data & Mapping

JSON for running the pipeline & documenting the corpus:
- `corpus_a.json` - **master corpus** (101 articles): no, pillar, title, authors, year, journal, classification (quartile),
  relevance, quality, dimensions d1-d8, summary, contribution.
- `issn_map.json` - DOI -> journal ISSN mapping.
- `scopus_official.json` - official SCImago quartile (SJR Best Quartile) per DOI.
- `scopus_check.json` - estimated quartile (SJR 2024) per DOI.
- `harvest_stats.json` - search statistics (PRISMA numbers).
- `pool.json`, `ranked.json`, `selected*.json` - candidates & selection funnel.
- `oa_core_filtered.json`, `oa_replacements.json`, `replacement_pool.json`, `core_replacements_detail.json`,
  `core_failed_downloads.json` - OA/replacement candidate sets and their provenance.
  `oa_replacements.json` consolidates the former `oa_core_replacement.json` + `oa_core_replacement2.json` +
  `oa_replacement.json` into one file (deduped by DOI; each row keeps a `batch` field for provenance).
- `phase5_gugur.json` - list of dropped papers (final: empty).
