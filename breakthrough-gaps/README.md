# Breakthrough Gaps Catalog

The `breakthrough-gaps/` directory catalogs world-reshaping technological breakthroughs that
are scientifically plausible but currently blocked by specific cross-domain gaps — engineering,
materials, economic, or mathematical barriers that the Universal Science Discovery Repository
is positioned to help bridge.

## Purpose

Breakthrough gap entries do three things:

1. **Name the breakthrough** with honest Technology Readiness Level (TRL) assessment.
2. **Map the blocking gaps** — the specific scientific or engineering barriers preventing
   deployment, with domain attribution.
3. **Link to required bridges** — cross-domain connections (`b-*` entries) whose resolution
   would directly unblock the breakthrough.

## Schema

All entries validate against `schemas/breakthrough_gap.yaml`.

Fields:
- `id` — stable identifier, pattern `bg-[a-z0-9-]+`
- `title` — short name of the breakthrough
- `breakthrough_description` — what the world looks like if this is achieved
- `source_domain` — primary scientific domain
- `current_trl` — Technology Readiness Level 1–9 (1 = basic principles, 9 = operational)
- `world_reshaping_potential` — `transformative`, `significant`, or `moderate`
- `blocking_gaps` — list of specific barriers, each with:
  - `gap_title`, `gap_description`, `blocking_domain`
  - `gap_type`: `materials`, `economic`, `engineering`, `biological`, `mathematical`,
    `social`, or `regulatory`
- `required_bridges` — bridge IDs (`b-*`) whose resolution would unblock this
- `references` — primary literature, review articles, or landmark papers

## TRL Reference

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

## Current entries

| ID | Title | TRL | Potential |
|----|-------|-----|-----------|
| bg-hydrogen-water-splitting | Low-temperature water splitting catalyst | 4 | transformative |
| bg-quantum-computing-fault-tolerant | Fault-tolerant quantum computation | 3 | transformative |
| bg-room-temperature-superconductivity | Ambient superconductivity | 2 | transformative |
| bg-mrna-programmable-medicine | Programmable mRNA therapeutics beyond vaccines | 6 | transformative |
| bg-carbon-direct-air-capture | Economically viable direct air capture | 7 | transformative |

## Adding new entries

1. Copy an existing entry as a template.
2. Validate: `python scripts/validate_schemas.py`
3. Run `python scripts/build_graph.py` to update the knowledge graph.
4. Submit a PR following `CONTRIBUTING.md`.
