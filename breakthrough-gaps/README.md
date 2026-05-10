# Breakthrough Gaps Catalog

The `breakthrough-gaps/` directory catalogs world-reshaping technological breakthroughs that
are scientifically plausible but currently blocked by specific cross-domain gaps — engineering,
materials, economic, regulatory, or mathematical barriers that USDR is positioned to map.

**Steward guide (priorities, regeneration, quality bar):** [docs/BREAKTHROUGH_GAPS.md](../docs/BREAKTHROUGH_GAPS.md)

## Purpose

Breakthrough gap entries do three things:

1. **Name the breakthrough** with honest Technology Readiness Level (TRL) assessment.
2. **Map the blocking gaps** — specific barriers preventing deployment, with domain attribution.
3. **Link to required bridges** — cross-domain connections (`b-*` entries) whose resolution would unblock the breakthrough.

## Schema

All entries validate against `schemas/breakthrough_gap.yaml`.

Fields:

- `id` — stable identifier, pattern `bg-[a-z0-9-]+`
- `title` — short name of the breakthrough
- `breakthrough_description` — what the world looks like if this is achieved
- `source_domain` — primary scientific domain
- `current_trl` — Technology Readiness Level 1–9 (1 = basic principles, 9 = operational)
- `world_reshaping_potential` — `transformative`, `significant`, or `moderate`
- `blocking_gaps` — list of barriers, each with `gap_title`, `gap_description`, `blocking_domain`, and `gap_type` (`materials`, `economic`, `engineering`, `biological`, `mathematical`, `social`, `regulatory`, `scientific`, `algorithmic`, `control`)
- `required_bridges` — bridge IDs (`b-*`) whose resolution would unblock this catalog entry
- `references` — primary literature, reviews, or landmark papers (verifiable IDs/URLs only)

## TRL reference

| TRL | Meaning |
|-----|---------|
| 1 | Basic principles observed |
| 2 | Technology concept formulated |
| 3 | Experimental proof of concept |
| 4 | Technology validated in lab |
| 5 | Technology validated in relevant environment |
| 6 | Technology demonstrated in relevant environment |
| 7 | System prototype demonstrated in operational environment |
| 8 | System complete and qualified |
| 9 | Actual system proven in operational environment |

## Contributor hub & API

- Hub cards are **generated** by `scripts/render_breakthrough_gaps_hub.py` from **all** `bg-*.yaml` files.
- JSON summaries: `api/v1/breakthrough_gaps.json` via `scripts/generate_api.py`.

## Adding or updating entries

1. Copy an existing `bg-*.yaml` as a template.
2. Validate: `python scripts/validate_schemas.py`
3. Regenerate hub fragment locally if needed: `python scripts/render_breakthrough_gaps_hub.py --apply`
4. Regenerate API: `python scripts/generate_api.py`
5. Open a PR following `CONTRIBUTING.md` (ship hub/API updates in the same PR when possible).
