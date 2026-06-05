

# Universal Science Discovery Repository

**The open-source knowledge engine for scientific unknowns and cross-domain discovery**

[![Bridges](https://img.shields.io/badge/bridges-1123-6366f1?style=flat-square)](cross-domain/)
[![Unknowns](https://img.shields.io/badge/unknowns-1408-22c55e?style=flat-square)](unknowns-catalog/)
[![Hypotheses](https://img.shields.io/badge/hypotheses-1274-f59e0b?style=flat-square)](hypotheses/)
[![Graph Nodes](https://img.shields.io/badge/graph_nodes-3857-ec4899?style=flat-square)](docs/knowledge_graph.json)
[![License: CC BY 4.0](https://img.shields.io/badge/catalog-CC%20BY%204.0-blue?style=flat-square)](LICENSE)
[![License: MIT](https://img.shields.io/badge/code-MIT-green?style=flat-square)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/KR8ZYSHO3/Universal-Science-Discovery/validate.yml?style=flat-square&label=CI)](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/actions)

**[Live Dashboard](https://usdr.science/dashboard/) · [Knowledge Graph](https://usdr.science/dashboard/#knowledge-graph) · [Preprint](docs/preprint/usdr_preprint.md) · [Contribute**](CONTRIBUTING.md) (github.io mirror: https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/)

> **🚀 June 2026 Launch Sprint** — 1,123 cross-domain bridges • 1,408 open unknowns • 1,274 hypotheses • 0 orphans • Automation live. First external contributors wanted.



---

## The Problem

Science has extraordinary infrastructure for recording what is *known* — 200M+ indexed papers, citation graphs, semantic search. It has almost no infrastructure for recording what is *unknown*.

The frontier of human knowledge — the open problems, the cross-domain connections that haven't been made, the experiments that haven't been run — exists only in review article background sections, grant application paragraphs, and the informal knowledge of domain experts. It is not indexed. It is not version-controlled. It is not findable.

This means:

- A graduate student entering a field invests years to understand which problems are genuinely open
- Two fields independently study the same mathematical phenomenon for decades without recognizing the connection
- The most important questions in science are the hardest to find

**USDR is built to fix this.**

---

## What We've Built

A git-native, schema-validated, community-governed catalog of scientific unknowns, hypotheses, and cross-domain mathematical bridges — currently containing:


| Metric                     | Count     | Notes                                                           |
| -------------------------- | --------- | --------------------------------------------------------------- |
| **Cross-domain bridges**   | **1,123** | Mathematical connections between fields that rarely communicate |
| **Open unknowns**          | **1,408** | Named, structured research gaps across 55+ disciplines          |
| **Falsifiable hypotheses** | **1,274** | Testable claims linked to specific unknowns                     |
| **Knowledge graph nodes**  | **3,857** | Interconnected across 4,517 edges (`docs/knowledge_graph.json`) |
| **Pioneer profiles**       | **18**    | `pioneers/*.yaml` — lineage context for seeded bridges            |
| **Breakthrough gaps**      | **24**    | `breakthrough-gaps/bg-*.yaml` — stewarded high-impact gaps      |
| **Phenomenology records**  | **10**    | Pre-formal observations (`phenomenology/**/p-*.yaml`)           |
| **Orphan unknowns**        | **0**     | `scripts/find_orphan_unknowns.py` — none disconnected in graph  |
| **Schema errors**          | **0**     | All entries pass CI validation on every PR                      |

*Headline catalog totals (bridges, unknowns, hypotheses, phenomenology) and graph node/edge counts are checked by **`python scripts/verify_dashboard_consistency.py`** against YAML globs and `docs/knowledge_graph.json` meta.*

Entries are YAML and schema-validated in CI; bridges and many records cite primary literature (DOIs/arXiv where applicable — see per-record `references`). The knowledge graph is rebuilt deterministically from source files on every push.

---

## What Makes a Bridge

A USDR bridge is not a metaphor. It requires a **term-by-term mathematical mapping** between two fields — the same differential equation, order parameter, or information-theoretic quantity governing phenomena in both domains.

**Example: Percolation Theory ↔ Ecological Fragmentation**


| Statistical physics                    | Conservation biology                                   |
| -------------------------------------- | ------------------------------------------------------ |
| Site percolation threshold p_c         | Critical habitat coverage fraction (~59%)              |
| Giant connected component              | Connected habitat network enabling population rescue   |
| Finite-size scaling correction         | Threshold shift in smaller landscape patches           |
| Correlation length ξ (diverges at p_c) | Mean dispersal distance to maintain connectivity       |
| Universality class (2D, ν = 4/3)       | Spatial connectivity independent of landscape geometry |


The conservation biology literature has used percolation as a simulation tool since 1987. The exact analytical machinery — finite-size scaling, critical exponents, universality class proofs — has not crossed over. **That gap is what USDR makes explicit and actionable.**

---

## Discovery Engine

USDR ships tooling that turns the knowledge graph into an active bridge-discovery system:

```bash
# Find cross-domain papers from OpenAlex (250M+ papers)
python scripts/harvesters/harvest_openalex.py --bridge-scan

# Find the highest-priority domain pairs with no bridge yet
python scripts/propose_bridges.py --top 15

# Find unknowns with no connections — prime contribution targets
python scripts/find_orphan_unknowns.py

# Audit catalog quality
python scripts/audit_quality.py
```

The `harvest_openalex.py` script queries OpenAlex for papers that cite **two specific concept domains simultaneously** — the core primitive for automated bridge discovery at scale. PubMed and Semantic Scholar harvesters are also included.

### Wave Factory mode

Wave Factory mode converts harvested candidates into schema-safe draft triples at scale:

```bash
# Stage ranked bridge + unknown + hypothesis drafts
python scripts/harvesters/wave_factory.py \
  --top 30 \
  --min-citations 50 \
  --sources openalex,pubmed,semantic_scholar \
  --output drafts/wave_factory

# Validate staged records before promotion
python scripts/harvesters/promote_wave_factory_batch.py --stage drafts/wave_factory
```

Drafts are intentionally staged (not auto-promoted) so human review remains the merge gate.

---

## Quick Start

```bash
git clone https://github.com/KR8ZYSHO3/Universal-Science-Discovery.git
cd Universal-Science-Discovery

# View the live dashboard locally (path: dashboard/index.html — URL in dashboard/README.md)
python -m http.server 8765

# Validate the entire catalog
pip install pyyaml jsonschema
python scripts/validate_schemas.py

# Rebuild the knowledge graph
pip install pyyaml networkx
python scripts/build_graph.py
```

---

## Catalog Structure

```
cross-domain/{domain-a}-{domain-b}/b-*.yaml   ← 1123 bridges
unknowns-catalog/{domain}/u-*.yaml            ← 1408 unknowns
hypotheses/active|validated|archived/h-*.yaml ← 1274 hypotheses
pioneers/pioneer-*.yaml                       ← 18 pioneer profiles
breakthrough-gaps/bg-*.yaml                   ← 24 breakthrough gaps
phenomenology/p-*.yaml                        ← pre-formal observations
schemas/                                      ← JSON Schema definitions
scripts/                                      ← tooling and harvesters
scripts/harvesters/                           ← OpenAlex, PubMed, Semantic Scholar
dashboard/                                    ← interactive D3 dashboard
api/v1/                                       ← static JSON API
```

---

## Contributing

The simplest contribution is a new **unknown** — a named, structured research gap in your field. No code required, just YAML.

```yaml
id: u-your-unknown-id
title: "What mechanism allows X to Y without Z?"
status: open
summary: "A brief description of the gap and why it matters."
disciplines: [your-field, adjacent-field]
priority: high
references:
  - doi: "10.XXXX/XXXXX"
    note: "Paper that defines the boundary of current knowledge"
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for full instructions and [docs/QUICK_START_CONTRIBUTING.md](docs/QUICK_START_CONTRIBUTING.md) for a 30-minute first-contribution guide.

**Open issues labeled `[good first issue](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/issues?q=is%3Aopen+label%3A%22good+first+issue%22)`** include bridge stubs, domain unknowns, and documentation tasks across 8 scientific domains.

---

## Roadmap


| Phase                                        | Timeline  | Goal                                                                                       |
| -------------------------------------------- | --------- | ------------------------------------------------------------------------------------------ |
| **Phase 0: Foundation** *(complete)*         | 2026      | Governance · schemas · CI · seeded catalog · knowledge graph · contributor hub · automation |
| **Phase 1: Discovery & adoption** *(active)* | 2026–2027 | arXiv DOI · public launch & outreach · first contributors · hackathon · custom domain       |
| **Phase 2: Momentum**                        | 2027–2028 | 10,000+ entries · institutional partners · AI co-pilot · 500 contributors              |
| **Phase 3: Acceleration**                    | 2029–2031 | 100,000+ entries · autonomous discovery agents · global research labs                      |
| **Phase 4: Transformation**                  | 2032–2035 | The default interface through which researchers interact with the open frontier of science |


---

## Governance & Ethics

- **Speculation is labeled.** `status: proposed` means plausible but unvalidated. `status: established` requires a published cross-disciplinary recognition.
- **No fabricated citations.** All references must include a verifiable DOI or arXiv ID.
- **Unknowns ≠ findings.** The system enforces terminological separation between what is known and what is not.
- **Human review gates all merges.** CI catches schema errors; human domain expertise catches scientific errors.

See [GOVERNANCE.md](GOVERNANCE.md), [ETHICS.md](ETHICS.md), and [docs/ETHICS_REPRODUCIBILITY_AND_DATA.md](docs/ETHICS_REPRODUCIBILITY_AND_DATA.md).

---

## Citation

If you use USDR in research, please cite:

> Shoemaker, B. and Contributors. *Universal Science Discovery Repository: Open Infrastructure for Tracking Scientific Unknowns and Cross-Domain Mathematical Bridges.* v1.1, May 2026. [https://github.com/KR8ZYSHO3/Universal-Science-Discovery](https://github.com/KR8ZYSHO3/Universal-Science-Discovery)

A preprint is available at [docs/preprint/usdr_preprint.md](docs/preprint/usdr_preprint.md).

---

## License

- **Catalog content** (YAML entries, documentation): [CC BY 4.0](LICENSE)
- **Code** (scripts, dashboard, CI): [MIT](LICENSE)

© 2026 Brandon Shoemaker and USDR Contributors