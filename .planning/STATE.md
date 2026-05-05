# USDR workspace state

Authoritative checklist for humans and agents. Update after each merged PR.

## Last updated

- 2026-05-04 — **bio-ph harvest** + 2 missing hypotheses + quantum-biology bridge + Kleiber unknown (PR #16, this session)
- 2026-05-04 — **Dashboard** stat deck updated: bridges card added, counts refreshed (PR #15)
- 2026-05-04 — **2 hypotheses closed gaps**: h-grokking-criticality-universality, h-cardiac-arrhythmia-phase-transition + u-cortical-folding-topology (PR #14)
- 2026-05-04 — **nlin harvest**: b-grokking-criticality bridge (AI↔statistical-physics), u-cardiac-criticality-synchronization, u-grokking-phase-transition, h-topological-defect-morphogenesis (PR #13)
- 2026-05-04 — **physics:cond-mat:stat-mech harvest**: u-active-matter-percolation, u-topological-morphogenesis, b-topology-morphogenesis, bridge-discovery prompt (PR #12)
- 2026-05-04 — **Cross-domain bridge system**: schemas/bridge.yaml, validate_schemas.py extended, 4 initial bridges (b-percolation-oncology, b-criticality-neuroscience, b-glymphatic-aging, b-lichen-astrobiology) (PR #11)
- 2026-05-04 — **Hypotheses**: h-criticality-conscious-integration, h-glymphatic-amyloid-clearance-rate, h-adaptive-therapy-percolation-threshold, h-lichen-consortium-metabolic-coupling (PR #10)
- 2026-05-04 — **arXiv q-bio harvest**: 4 unknowns seeded (u-brain-criticality-function, u-amyloid-progression-trajectory, u-tumor-containment-percolation, u-synthetic-lichen-biofabrication) (PR #9)
- 2026-05-04 — GitHub Pages live + dashboard deployed at [kr8zysho3.github.io/…/dashboard/](https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/)
- 2026-05-03 — Contributor hub visual refresh, CI green, all docs wired.

## Catalog state

| Type | Count | Directory |
|------|-------|-----------|
| Unknowns | 12 | `unknowns-catalog/` |
| Hypotheses | 11 | `hypotheses/active/` |
| Bridges | 7 | `cross-domain/` |
| Schemas | 3 | `schemas/` (unknown, hypothesis, bridge) |

### Bridge network (cross-domain connections)

| Bridge | Fields | Status |
|--------|--------|--------|
| b-percolation-oncology | statistical-physics ↔ oncology | proposed |
| b-criticality-neuroscience | condensed-matter ↔ neuroscience | proposed |
| b-glymphatic-aging | sleep-medicine ↔ neurology ↔ geroscience | proposed |
| b-lichen-astrobiology | synthetic-biology ↔ astrobiology | proposed |
| b-topology-morphogenesis | mathematics/topology ↔ developmental-biology | proposed |
| b-grokking-criticality | AI/machine-learning ↔ statistical-physics | proposed |
| b-quantum-biology-navigation | quantum-mechanics ↔ sensory-biology | **established** |

## Current focus

- **Content seeding**: running arXiv harvests (q-bio, cond-mat:stat-mech, nlin, bio-ph) to seed unknowns, hypotheses, and bridges.
- **Bridge discovery**: every harvest is checked against the bridge-discovery prompt in `docs/prompts/bridge_discovery.md`.
- **Contributor discoverability**: GitHub Issues to be created from open unknowns (next action).
- **Schema discipline**: all YAML validated by `scripts/validate_schemas.py` on every PR.

## Active git branches / PRs

- `main` — default; all PRs squash-merged here; CI: validate-schemas + mkdocs + markdown-link-check.
- Any active feature branch: `feat/...` — check GitHub Pull Requests tab.

## Shipped in this session (2026-05-04)

- **Bridge system** (schemas, validator, 7 bridges) — the core anti-tunnel-vision primitive.
- **11 unknowns + 11 hypotheses** — seeded from 4 arXiv harvests.
- **3 prompt templates** (literature synthesis, hypothesis comparison, falsification, bridge discovery).
- **Developer dashboard** updated with bridge stat card and current counts.
- **GitHub Pages** live at [kr8zysho3.github.io/Universal-Science-Discovery/](https://kr8zysho3.github.io/Universal-Science-Discovery/).

## Blocked / needs human

- None.

## Next actions (max 5)

- Create GitHub Issues from the most compelling open unknowns for contributor discoverability.
- Write `u-quantum-biology-decoherence` — the open question raised by b-quantum-biology-navigation.
- Run a `q-bio:q-bio:TO` (tissues and organs) harvest to seed the topology-morphogenesis bridge further.
- Update the developer dashboard stat counts after each PR that adds catalog entries.
- Keep `schemas/unknown.yaml`, `schemas/hypothesis.yaml`, `schemas/bridge.yaml` in sync when adding new optional fields.
