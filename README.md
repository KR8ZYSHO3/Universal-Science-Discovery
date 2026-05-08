

# Universal Science Discovery Repository

**The open-source knowledge engine for scientific unknowns and cross-domain discovery**

[Bridges](cross-domain/)
[Unknowns](unknowns-catalog/)
[Hypotheses](hypotheses/)
[Graph Nodes](docs/knowledge_graph.json)
[License: CC BY 4.0](LICENSE)
[License: MIT](LICENSE)
[CI](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/actions)

**[Live Dashboard](https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/) · [Knowledge Graph](https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/#knowledge-graph) · [Preprint](docs/preprint/usdr_preprint.md) · [Contribute**](CONTRIBUTING.md)



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
| **Cross-domain bridges**   | **1,038** | Mathematical connections between fields that rarely communicate |
| **Open unknowns**          | **1,323** | Named, structured research gaps across 55+ disciplines          |
| **Falsifiable hypotheses** | **1,189** | Testable claims linked to specific unknowns                     |
| **Knowledge graph nodes**  | **3,602** | Interconnected across 4,092 edges                               |
| **Pioneer profiles**       | **18**    | Scientists whose work seeded cross-domain bridges               |
| **Breakthrough gaps**      | **24**    | High-priority problems that would reshape entire fields         |
| **Orphan unknowns**        | **0**     | All unknowns connected to bridges or hypotheses                 |
| **Schema errors**          | **0**     | All entries pass CI validation on every PR                      |


Every entry is YAML, schema-validated, DOI-linked, and version-controlled. The knowledge graph is rebuilt deterministically from source files on every push.

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

---

## Quick Start

```bash
git clone https://github.com/KR8ZYSHO3/Universal-Science-Discovery.git
cd Universal-Science-Discovery

# View the live dashboard locally
python -m http.server 8765
# → http://localhost:8765/dashboard/

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
cross-domain/{domain-a}-{domain-b}/b-*.yaml   ← 1038 bridges
unknowns-catalog/{domain}/u-*.yaml            ← 1323 unknowns
hypotheses/active|validated|archived/h-*.yaml ← 1189 hypotheses
pioneers/pioneer-*.yaml                       ← 18 pioneer profiles
breakthrough-gaps/bg-*.yaml                   ← 12 breakthrough gaps
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


| Phase                              | Timeline  | Goal                                                                                       |
| ---------------------------------- | --------- | ------------------------------------------------------------------------------------------ |
| **Phase 0: Foundation** *(active)* | 2026      | 1,000+ bridges · first 50 contributors · arXiv preprint · Hackathon                        |
| **Phase 1: Momentum**              | 2027–2028 | 10,000+ entries · institutional partners · AI co-pilot · 500 contributors                  |
| **Phase 2: Acceleration**          | 2029–2031 | 100,000+ entries · autonomous discovery agents · global research labs                      |
| **Phase 3: Transformation**        | 2032–2035 | The default interface through which researchers interact with the open frontier of science |


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