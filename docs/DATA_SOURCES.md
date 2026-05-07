# USDR External Data Sources

This document catalogs all external databases integrated or planned for integration into the Universal Science Discovery Repository.

## Integration Priority Tiers

### Tier 1 — Active (currently integrated)
| Source | Type | Coverage | Integration method |
|--------|------|----------|--------------------|
| arXiv (OAI-PMH) | Preprints | Physics, CS, Math, Biology | `packages/ingest/` — `usdr-ingest harvest` |

### Tier 2 — Planned (next 90 days)
| Source | Type | Coverage | Why it matters for USDR | API endpoint |
|--------|------|----------|------------------------|--------------|
| OpenAlex | Papers + concepts | 250M+ cross-field papers | Best cross-domain concept tagging; query "papers citing both X and Y" | `https://api.openalex.org` |
| Semantic Scholar | Papers + citations | 200M+ papers | AI-extracted concepts, citation influence scores | `https://api.semanticscholar.org/graph/v1` |
| PubMed/NCBI | Biomedical literature | All medicine/biology | Essential for Lyme, neuroscience, pharmacology bridges | `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/` |
| CrossRef | DOI metadata | All fields | Verifies DOIs, extracts reference lists for citation index | `https://api.crossref.org` |

### Tier 3 — Domain-specific (planned)
| Source | Domain | Priority |
|--------|--------|----------|
| NASA ADS | Astronomy/astrophysics | High |
| INSPIRE-HEP | High-energy physics | High |
| bioRxiv/medRxiv | Biology/medicine preprints | High |
| ChemRxiv | Chemistry | Medium |
| SSRN | Social science/economics/law | Medium |
| PhilPapers | Philosophy of science | Medium |
| Wikidata | Structured concept facts | Medium (bridge translation tables) |
| OpenAIRE | European research | Low |

### Tier 4 — Future (Phase 1+)
- **Gene Ontology** — biological process/function ontology for biology bridges
- **ChEMBL** — bioactive molecules for pharmacology/biochemistry bridges
- **PDB (Protein Data Bank)** — protein structure for structural biology bridges
- **ClinicalTrials.gov** — clinical research gaps for medicine unknowns
- **USPTO Patents** — technology gap analysis from patent claims

---

## Integration Architecture

Each external source is integrated via a standardized harvester script in `scripts/harvesters/`:

```
scripts/harvesters/
  harvest_arxiv.py         ← existing (via usdr-ingest)
  harvest_openalex.py      ← NEW (Tier 2)
  harvest_pubmed.py        ← planned
  harvest_semantic_scholar.py ← planned
  harvest_crossref.py      ← planned
```

Each harvester:
1. Queries the API for papers matching cross-domain concept pairs
2. Extracts candidate unknowns (open questions in abstracts/conclusions)
3. Identifies bridge candidates (papers citing both field A and field B)
4. Outputs structured YAML stubs to `drafts/` for human expert review
5. Never writes directly to `unknowns-catalog/` or `cross-domain/` without review

---

## OpenAlex Integration (Active Development)

OpenAlex is the highest-priority integration because:
- Free, no API key required for low-volume queries
- Returns structured **concept tags** on every paper (e.g., "Percolation theory", "Ecology")
- Can query for papers that span **two specific concepts** — the core bridge-discovery primitive
- 250M+ papers across all fields

### Bridge discovery query pattern:
```
GET https://api.openalex.org/works?filter=concepts.id:C12345|C67890&per-page=50
```

### Concept pairs to query (mapped to existing bridges):
- Topology + Condensed Matter → feeds topological insulator bridges
- Information Theory + Evolutionary Biology → feeds Fisher/Shannon bridges
- Percolation Theory + Ecology → extends our percolation-ecology bridge
- Statistical Mechanics + Finance → extends econophysics bridges
- Network Theory + Epidemiology → extends SIR/percolation bridges

---

## Quality and Ethics

All harvested content:
- Is reviewed by a human domain expert before merging to main
- Includes source attribution (DOI, API source, harvest date)
- Does not ingest full paper text — only metadata, abstracts, and structured fields
- Follows `docs/ETHICS_REPRODUCIBILITY_AND_DATA.md` for data handling

See `docs/METHODOLOGY.md` for the harvest-to-unknown pipeline.
