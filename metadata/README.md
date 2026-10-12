> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# metadata/ - Intermediate Data & Mapping

JSON for running the pipeline & documenting the corpus:
- `corpus_a.json` - **master corpus** (101 articles): no, pillar, title, authors, year, journal, classification (quartile),
  relevance, quality, dimensions d1-d8, summary, contribution.
- `issn_map.json` - DOI -> journal ISSN mapping.
- `scopus_official.json` - official SCImago quartile (SJR Best Quartile) per DOI.
- `scopus_check.json` - estimated quartile (SJR 2024) per DOI.
- `harvest_stats.json` - search statistics (PRISMA numbers).
- `pool.json`, `ranked.json`, `selected*.json`, `replacement_pool.json`, `oa_*.json`, `core_*.json` - candidates & selection process.
- `phase5_gugur.json` - list of dropped papers (final: empty).
