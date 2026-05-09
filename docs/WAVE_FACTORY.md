# Wave Factory Mode

Wave Factory mode automates high-throughput bridge draft production from harvested candidate feeds while keeping outputs schema-safe and review-ready.

## Goals

- Rank harvested candidates from OpenAlex, PubMed, and Semantic Scholar.
- Deduplicate against existing bridge IDs/titles.
- Stage draft triples (bridge + unknown + hypothesis) for expert review.
- Keep promotion to canonical folders explicit and collision-checked.

## Inputs

Wave Factory reads these candidate sources when present:

- `drafts/openalex_candidates.json`
- `drafts/pubmed_candidates.json`
- `drafts/semantic_scholar_candidates.json`

Missing source files are skipped safely.

## Script 1: Orchestrate and stage drafts

`scripts/harvesters/wave_factory.py`

### Core behavior

- Weighted ranking using:
  - citation strength
  - recency
  - domain-pair novelty
- Deduplication against existing bridge IDs and existing bridge titles.
- Output staging tree (default):
  - `drafts/wave_factory/cross-domain/**/b-*.yaml`
  - `drafts/wave_factory/unknowns-catalog/**/u-*.yaml`
  - `drafts/wave_factory/hypotheses/active/h-*.yaml`
- **`drafts/wave_factory/` is gitignored** — it is machine-local staging only. Regenerate with `wave_factory.py` when needed; **promote** reviewed triples into canonical folders with `promote_wave_factory_batch.py`.
- Low-confidence records are explicitly tagged `SPECULATIVE` in generated bridge/hypothesis text.

### CLI examples

```bash
# Preview only (no files written)
python scripts/harvesters/wave_factory.py --dry-run --top 20 --min-citations 50

# Stage top 30 from all supported sources
python scripts/harvesters/wave_factory.py \
  --top 30 \
  --min-citations 50 \
  --sources openalex,pubmed,semantic_scholar \
  --output drafts/wave_factory
```

## Script 2: Validate and promote staged batch

`scripts/harvesters/promote_wave_factory_batch.py`

### Core behavior

- Validates staged YAML records against `schemas/bridge.yaml`, `schemas/unknown.yaml`, and `schemas/hypothesis.yaml`.
- Checks collisions before promotion.
- Moves records into canonical locations only with `--apply`.

### CLI examples

```bash
# Dry-run validation + promotion plan
python scripts/harvesters/promote_wave_factory_batch.py --stage drafts/wave_factory

# Apply promotion into canonical folders
python scripts/harvesters/promote_wave_factory_batch.py --stage drafts/wave_factory --apply
```

## Safety notes

- Wave Factory output is **candidate material**, not findings.
- Generated claims remain `status: proposed` (bridges) and `status: open` (unknowns).
- Hypotheses remain test-oriented and explicitly mark speculative confidence when score is low.
- Promotion is intentionally separate to preserve a human review gate.
