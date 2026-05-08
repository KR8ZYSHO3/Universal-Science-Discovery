# USDR External Data Sources

This document catalogs all external databases integrated or planned for integration into the Universal Science Discovery Repository.

## Integration Priority Tiers

### Tier 1 — Active (currently integrated)
| Source | Type | Coverage | Integration method |
|--------|------|----------|--------------------|
| arXiv (OAI-PMH) | Preprints | Physics, CS, Math, Biology | `packages/ingest/` — `usdr-ingest harvest` |

### Tier 2 — Active harvesters
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
  harvest_arxiv.py                    ← existing (via usdr-ingest)
  harvest_openalex.py                 ← active
  harvest_pubmed.py                   ← active
  harvest_semantic_scholar.py         ← active
  wave_factory.py                     ← ranking + draft triple generation
  promote_wave_factory_batch.py       ← staged validation + promotion helper
  harvest_crossref.py                 ← planned
```

Wave Factory pipeline:
1. Queries the API for papers matching cross-domain concept pairs
2. Normalizes harvested candidates into `drafts/*_candidates.json`
3. Ranks candidates by citation impact, recency, and domain-pair novelty
4. Stages schema-safe bridge/unknown/hypothesis triples under `drafts/wave_factory/`
5. Validates staged records before optional promotion to canonical catalogs
6. Never writes to canonical folders without explicit promotion (`--apply`)

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

## Automated Harvest + Wave Factory Pipeline

The cadence workflow (`.github/workflows/harvest-openalex.yml`) runs twice weekly (Monday + Thursday, 6am UTC):

1. Harvests fresh candidates from OpenAlex, PubMed, and Semantic Scholar
2. Runs `wave_factory.py` dry-run for ranking visibility
3. Stages a batch into `drafts/wave_factory/`
4. Runs `promote_wave_factory_batch.py` in dry-run validation mode
5. Runs schema validation (`python scripts/validate_schemas.py`)
6. Opens/updates an automation PR with staged artifacts (no direct push to protected branches)

This creates a continuous pipeline: literature → ranked candidates → staged triples → reviewed promotion.

Wave Factory can also be run locally:

```bash
python scripts/harvesters/wave_factory.py \
    --top 20 \
    --min-citations 50 \
    --sources openalex,pubmed,semantic_scholar \
    --output drafts/wave_factory
```

---

## Quality and Ethics

All harvested content:
- Is reviewed by a human domain expert before merging to main
- Includes source attribution (DOI, API source, harvest date)
- Does not ingest full paper text — only metadata, abstracts, and structured fields
- Follows `docs/ETHICS_REPRODUCIBILITY_AND_DATA.md` for data handling

See `docs/METHODOLOGY.md` for the harvest-to-unknown pipeline.
