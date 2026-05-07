# Universal Science Discovery Repository (USDR)

Open-source, Git-based knowledge infrastructure for **discovery-first** science: explicit unknowns, testable hypotheses, cross-domain mathematical bridges, and reproducible workflows.

<!-- Project status badges -->
[![Bridges](https://img.shields.io/badge/Bridges-180-4f9cf9?style=flat-square)](cross-domain/)
[![Unknowns](https://img.shields.io/badge/Unknowns-619-f43f5e?style=flat-square)](unknowns-catalog/)
[![Graph Nodes](https://img.shields.io/badge/Graph%20Nodes-1%2C000-22d3b8?style=flat-square)](docs/knowledge_graph.json)
[![License: CC BY 4.0](https://img.shields.io/badge/Content-CC%20BY%204.0-lightgrey?style=flat-square)](LICENSE)
[![License: MIT](https://img.shields.io/badge/Code-MIT-blue?style=flat-square)](LICENSE-CODE)

<!-- CI badges -->
[![Developer Dashboard](https://img.shields.io/badge/Developer%20Dashboard-Live-4f9cf9?style=for-the-badge&logo=github)](https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/)
[![Docs](https://img.shields.io/badge/Documentation-Live-22d3b8?style=for-the-badge&logo=readthedocs)](https://kr8zysho3.github.io/Universal-Science-Discovery/)
[![Validate Catalog](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/actions/workflows/validate.yml/badge.svg)](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/actions/workflows/validate.yml)
[![Knowledge Graph](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/actions/workflows/build-graph.yml/badge.svg)](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/actions/workflows/build-graph.yml)
[![License](https://img.shields.io/github/license/KR8ZYSHO3/Universal-Science-Discovery)](LICENSE)
[![Contributors](https://img.shields.io/github/contributors/KR8ZYSHO3/Universal-Science-Discovery)](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/graphs/contributors)
[![Issues](https://img.shields.io/github/issues/KR8ZYSHO3/Universal-Science-Discovery)](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/issues)

---

## Live Dashboard

**[kr8zysho3.github.io/Universal-Science-Discovery/dashboard/](https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/)**

Interactive D3 knowledge graph · full-text search · pioneer profiles · breakthrough gap tracker · domain pages

---

## Project Status (May 2026 — Wave 10 Complete)

| Metric | Count |
|--------|-------|
| Cross-domain bridges | **180** |
| Open unknowns | **619** |
| Hypotheses | **173** |
| Knowledge graph nodes | **1,000** |
| Knowledge graph edges | **910** |
| Pioneer profiles | **13** |
| Breakthrough gaps | **11** |
| Scientific domains | **41** |
| Pre-formal observations | **4** |

All records pass CI schema validation. arXiv preprint ready (`docs/preprint/usdr_preprint.md`).

---

## New here? (contributors)

1. **Skim this README** (5 min), then **[CONTRIBUTING.md](CONTRIBUTING.md)** — how to participate and what to contribute first.
2. **Contributor hub:** open the **[live dashboard](https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/)** — contributor path, policies, phase progress, CI status, and workstreams. Or run locally: `python -m http.server 8765` and open [localhost:8765/dashboard/](http://localhost:8765/dashboard/) — details in **[dashboard/README.md](dashboard/README.md)**.
3. **Browsing only on GitHub (no clone):** use **[docs/ONBOARDING.md](docs/ONBOARDING.md)** and the links in CONTRIBUTING; the dashboard's **GitHub** links next to each doc open the files in the browser.

Everything under **`dashboard/`** is **tracked in git** and auto-deployed to **[GitHub Pages](https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/)** on every push to `main`.

---

## Quick Start

### View the dashboard locally

```bash
git clone https://github.com/KR8ZYSHO3/Universal-Science-Discovery.git
cd Universal-Science-Discovery
python -m http.server 8765
# Open: http://localhost:8765/dashboard/
```

### Validate the catalog

```bash
pip install pyyaml jsonschema
python scripts/validate_schemas.py
# Expected: OK: all ... YAML files validate.
```

### Run the quality audit

```bash
python scripts/audit_quality.py
# Outputs: docs/quality_report.md
```

### Rebuild the knowledge graph

```bash
python scripts/build_graph.py
# Outputs: docs/knowledge_graph.json
```

### Generate the static API

```bash
python scripts/generate_api.py
# Outputs: api/v1/*.json
```

### Find contribution targets (orphan unknowns)

```bash
python scripts/find_orphan_unknowns.py
# Lists unknowns with no bridge or hypothesis connection — highest-priority targets
```

---

## Catalog Types

USDR organizes scientific knowledge into six catalog types, each with a defined YAML schema:

| Catalog | Directory | Schema | Description |
|---------|-----------|--------|-------------|
| **Bridges** | `cross-domain/` | `schemas/bridge.yaml` | Mathematical/conceptual links between two or more disciplines. Each bridge includes a translation table, status (established/proposed/speculative), DOI-backed references, and open unknowns it addresses. |
| **Unknowns** | `unknowns-catalog/` | `schemas/unknown.yaml` | Explicitly named research gaps — questions science does not yet have good answers to. Organized by domain. Seeded from arXiv harvests and community input. |
| **Hypotheses** | `hypotheses/` | `schemas/hypothesis.yaml` | Testable, falsifiable hypotheses linked to specific unknowns. Include priority, impact score, evidence links, and falsification criteria. |
| **Pioneers** | `pioneers/` | `schemas/pioneer.yaml` | Profiles of researchers whose work spans multiple disciplines. Each pioneer lists the bridge seeds and unknowns their work catalyzes. |
| **Breakthrough Gaps** | `breakthrough-gaps/` | `schemas/breakthrough_gap.yaml` | The 10–20 cross-domain problems whose solutions would most reshape science. Each gap lists required bridges, source domain, and world-reshaping potential. |
| **Pre-formal Observations** | `phenomenology/` | `schemas/phenomenon.yaml` | Raw, pre-theoretical observations and intuitions that do not yet fit an existing unknown or bridge. Triaged into unknowns when mature enough. |

---

## Why this exists

- **Mobilize contributors:** [WHY_CONTRIBUTE.md](WHY_CONTRIBUTE.md)
- **Pitch without unnecessary resistance:** [VISION_COMMUNICATION.md](VISION_COMMUNICATION.md)
- **Full build plan & repo shape:** [universal-science-discovery-repo-blueprint.md](universal-science-discovery-repo-blueprint.md)
- **Strategic roadmap:** [docs/PATH_TO_SUCCESS.md](docs/PATH_TO_SUCCESS.md)

---

## Key documents

| Document | Purpose |
|----------|---------|
| [WHY_CONTRIBUTE.md](WHY_CONTRIBUTE.md) | Case for contributing early and at planetary scale |
| [VISION_COMMUNICATION.md](VISION_COMMUNICATION.md) | Elevator pitches and audience-specific framing |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to add unknowns, hypotheses, bridges, or pioneer profiles |
| [universal-science-discovery-repo-blueprint.md](universal-science-discovery-repo-blueprint.md) | Blueprint: vision, structure, MVP, tooling |
| [INTERFACE.md](INTERFACE.md) | User/system interfaces to USDR (full plan; delivery phased per [ROADMAP.md](ROADMAP.md)) |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Technical / system architecture |
| [ROADMAP.md](ROADMAP.md) | Planned phases and priorities |
| [docs/PATH_TO_SUCCESS.md](docs/PATH_TO_SUCCESS.md) | Strategic roadmap: near/medium/long-term actions for discoverability and community growth |

---

## Governance, ethics, and legal

| Document | Purpose |
|----------|---------|
| [GOVERNANCE.md](GOVERNANCE.md) | Roles, decisions, maintainer expectations |
| [ETHICS.md](ETHICS.md) | Ethical guardrails for content and collaboration |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | Community behavior |
| [LEGAL.md](LEGAL.md) | Copyright, licensing posture, DMCA-style policy |
| [DISCLAIMER.md](DISCLAIMER.md) | Limitation of liability, not medical/legal advice |
| [SECURITY.md](SECURITY.md) | Reporting vulnerabilities or leaked secrets |
| [LICENSE](LICENSE) | Default license for this repository |

---

## Traceability

[DOC_MAP.md](DOC_MAP.md) lists every top-level doc and what it governs.

---

## Content layout

| Path | Role |
|------|------|
| [schemas/](schemas/) | JSON Schemas: hypothesis, unknown, bridge, phenomenon, pioneer, breakthrough_gap (YAML); ingestion envelope v1 (`ingestion-envelope-1.0.0.json`) |
| [templates/](templates/) | PR / issue boilerplate for new records |
| [unknowns-catalog/](unknowns-catalog/) | Global research gaps (`u-...`) — 619 entries across 41 domains |
| [hypotheses/](hypotheses/) | Hypothesis registry (`h-...`; `active` / `validated` / `archived`) — 173 entries |
| [cross-domain/](cross-domain/) | Cross-domain bridge YAMLs (`b-...`) — 180 bridges |
| [pioneers/](pioneers/) | Pioneer profiles (`pioneer-...`) — 13 profiles |
| [breakthrough-gaps/](breakthrough-gaps/) | Breakthrough gap records (`bg-...`) — 11 gaps |
| [phenomenology/](phenomenology/) | Pre-formal observations (`p-...`) — 4 entries |
| [scripts/](scripts/) | Automation: validate, build graph, generate API, quality audit, domain pages |
| [dashboard/](dashboard/) | Static site: D3 graph, Lunr search, domain pages, explainers |
| [docs/](docs/) | Documentation, preprint, outreach materials, reports |
| [api/v1/](api/v1/) | Static JSON API endpoints (auto-generated) |

---

## Scripts reference

| Script | Purpose |
|--------|---------|
| `scripts/validate_schemas.py` | Validate all catalog YAML against schemas; used by CI |
| `scripts/build_graph.py` | Build `docs/knowledge_graph.json` from all catalog entries |
| `scripts/generate_api.py` | Generate static JSON API endpoints under `api/v1/` |
| `scripts/update_dashboard_stats.py` | Patch stat counters in `dashboard/index.html` |
| `scripts/generate_domain_pages.py` | Generate per-domain HTML pages under `dashboard/domains/` |
| `scripts/generate_explainers.py` | Generate bridge explainer HTML pages |
| `scripts/propose_bridges.py` | Propose novel bridge candidates from pioneer seeds, breakthrough gaps, domain gaps |
| `scripts/find_orphan_unknowns.py` | Identify unknowns with no graph connections (prime contribution targets) |
| `scripts/audit_quality.py` | Flag low-quality catalog entries (short titles, missing fields) |
| `scripts/build_citation_index.py` | Extract and rank cross-referenced papers across bridges |

---

## Documentation site (preview)

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

CI runs `mkdocs build --strict` on every PR and push to `main`.

---

## arXiv metadata ingest (Phase B starter)

Package overview: [`packages/ingest/README.md`](packages/ingest/README.md). Compliance-oriented **metadata-only** harvest from arXiv OAI-PMH (no PDFs; see [LEGAL.md](LEGAL.md) and [docs/DATA_PLAN.md](docs/DATA_PLAN.md)):

```bash
pip install -r requirements-ingest.txt
pip install -e ./packages/ingest
usdr-ingest harvest --output records.jsonl --max-records 10 --manifest manifest.json
```

---

## Published documentation (GitHub Pages)

**Live:** [https://kr8zysho3.github.io/Universal-Science-Discovery/](https://kr8zysho3.github.io/Universal-Science-Discovery/) — auto-deploys on every push to `main`.

**Developer dashboard:** [https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/](https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/)

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The simplest contribution is adding a new unknown (a named research gap) or a hypothesis to an existing unknown. Both require only YAML editing — no code needed.

---

## License

Catalog content (YAML entries, documentation): [CC BY 4.0](LICENSE)  
Code (scripts, dashboard): [MIT](LICENSE-CODE)

© 2026 Universal Science Discovery Repository Contributors

---

## AI-assisted work in this repo

Project-specific Cursor guidance is in [cursorrules](cursorrules) (import or symlink into `.cursor/rules/` per your editor setup).
