# Pioneers Catalog

The `pioneers/` directory contains structured biographical and scientific profiles of foundational
scientific figures whose work seeds cross-domain bridges in the Universal Science Discovery
Repository (USDR).

## Purpose

Pioneer entries serve three functions:

1. **Historical attribution** — credit ideas to their originators with accurate status labeling
   (established vs. speculative vs. vindicated-posthumously).
2. **Bridge seeding** — each entry lists `bridge_seeds`: IDs of cross-domain bridges that the
   pioneer's work directly underpins or motivates.
3. **Underappreciated work triage** — each entry catalogues work that was dismissed, stalled,
   or misattributed during the pioneer's lifetime, with honest assessment of current status.

## Schema

All entries validate against `schemas/pioneer.yaml`.

Fields:
- `id` — stable identifier, pattern `pioneer-[a-z0-9-]+`
- `name` — full name
- `birth_year` / `death_year` — integers; `death_year: null` for living scientists
- `primary_domains` — list of disciplines
- `core_contributions` — list of titled contributions with description, mathematical form, and
  status (`established`, `proposed`, `speculative`, `open_question`)
- `bridge_seeds` — list of bridge IDs (`b-*`) whose cross-domain connection traces to this
  pioneer's work
- `underappreciated_work` — contributions dismissed or stalled during the pioneer's lifetime,
  with `current_status` (`vindicated`, `open_question`, `speculative`, `partially_vindicated`)
  and `why_stalled`
- `key_references` — primary sources (books, papers, patents)

## Status labeling policy

Status labels in `core_contributions` follow USDR methodology:
- `established` — accepted by the relevant scientific community, textbook-level consensus
- `proposed` — published and taken seriously but not yet consensus
- `speculative` — intriguing but lacking rigorous experimental support
- `open_question` — physics/math is sound but engineering or scientific feasibility at scale
  is genuinely unknown

Do **not** conflate `open_question` or `speculative` with `established`. The goal is honest
intellectual accounting, not hagiography.

## Current entries

| ID | Name | Domains |
|----|------|---------|
| pioneer-nikola-tesla | Nikola Tesla | electrical-engineering, electromagnetism, fluid-dynamics |
| pioneer-james-clerk-maxwell | James Clerk Maxwell | electromagnetism, statistical-mechanics, optics, thermodynamics |
| pioneer-ludwig-boltzmann | Ludwig Boltzmann | statistical-mechanics, thermodynamics, kinetic-theory |
| pioneer-emmy-noether | Emmy Noether | mathematics, theoretical-physics, abstract-algebra |
| pioneer-claude-shannon | Claude Shannon | information-theory, mathematics, electrical-engineering |

## Adding new entries

1. Copy an existing entry as a template.
2. Validate: `python scripts/validate_schemas.py`
3. Run `python scripts/build_graph.py` to update the knowledge graph with new bridge seeds.
4. Submit a PR following `CONTRIBUTING.md`.
