# Map the unknowns

Science is excellent at recording what is *known*. It barely records what is *not*.

This catalog names open questions, claimed links between fields, and tests you can run. No account.

**[Open the catalog](https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/) · [Run this test](https://kr8zysho3.github.io/Universal-Science-Discovery/repro/p-b-habitat-percolation-ecology-fss/index.html) · [See how two fields connect](https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/#/map) · [How to use](docs/USE.md) · [Why](docs/WHY.md)**

[![Claimed links](https://img.shields.io/badge/claimed_links-1124-6366f1?style=flat-square)](cross-domain/)
[![Open questions](https://img.shields.io/badge/open_questions-1411-22c55e?style=flat-square)](unknowns-catalog/)
[![Testable ideas](https://img.shields.io/badge/testable_ideas-1275-f59e0b?style=flat-square)](hypotheses/)
[![License: CC BY 4.0](https://img.shields.io/badge/catalog-CC%20BY%204.0-blue?style=flat-square)](LICENSE)

Building until a researcher in the room can use it. Public launch is parked — [ROADMAP.md](ROADMAP.md).

---

## Start here

1. **Run this test** — habitat loss and percolation are the same math. In the browser. If it says INCONCLUSIVE, the demo is small, not that the idea is false.
2. **Map** — pick two fields. The path is from this catalog, not a guess.
3. **Add an open question** — only if you have one. A person reads it first.

Plain language: [docs/USE.md](docs/USE.md). If you operate the site: [docs/OPERATE.md](docs/OPERATE.md).

[![What you are looking at](docs/figures/what-usdr-is.svg)](https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/)

[Open questions](https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/#/search) · [Map](https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/#/map) · [Run this test](https://kr8zysho3.github.io/Universal-Science-Discovery/repro/p-b-habitat-percolation-ecology-fss/index.html)

[![Run the test, see how two fields connect, add an open question](docs/figures/use-three-doors.svg)](https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/#start)

---

## The problem

The open problems, the unmade connections, the unrun experiments live in review-article asides, grant paragraphs, and people’s heads. They are not findable.

- A student spends years learning which questions are actually open.
- Two fields study the same math for decades without noticing.
- The most important questions are the hardest to search.

**USDR is built to fix that.** Why — science, reuse, not policy — is in [docs/WHY.md](docs/WHY.md).

---

## What is in here

| What                         | Count     | In one sentence                                                 |
| ---------------------------- | --------- | --------------------------------------------------------------- |
| **Claimed links**            | **1,124** | Two fields share the same math                                  |
| **Open questions**           | **1,411** | Named research gaps                                             |
| **Testable ideas**           | **1,275** | Claims you can try to falsify                                   |
| **Records on the map**       | **3,863** | Linked by 4,522 connections                                     |
| **Pioneer notes**            | **18**    | Lineage for seeded links                                        |
| **Breakthrough gaps**        | **24**    | High-impact stalls                                              |
| **Early notes**              | **11**    | Pre-formal observations                                         |

A claimed link is not a metaphor. It needs a term-by-term mapping — the same equation, order parameter, or information quantity in both fields.

---

## What a claimed link is

A claimed link is not a metaphor. It requires a **term-by-term mathematical mapping** between two fields — the same differential equation, order parameter, or information-theoretic quantity governing phenomena in both domains.

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

## Tests (Crosscheck)

USDR maps what connects; a **test** tries to prove or break that claim. Four seed tests are gated on every change. A short browser demo may say INCONCLUSIVE because it is small — that is not a finding.

**[How tests work](docs/CROSSCHECK.md)** · [Run the habitat test](https://kr8zysho3.github.io/Universal-Science-Discovery/repro/p-b-habitat-percolation-ecology-fss/index.html)

---

## Add an open question

The simplest contribution is a named research gap from your field. No programming required. A person reads it before it joins the catalog.

Walkthrough: [docs/HAPPY_PATH_FIRST_RECORDS.md](docs/HAPPY_PATH_FIRST_RECORDS.md) · [CONTRIBUTING.md](CONTRIBUTING.md)

<details>
<summary>Record format (only when you add one)</summary>

Records are short structured notes. Copy a similar file and change the title, summary, and a paper that marks the edge of what is known.

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

</details>

---

## If you operate or build on this

One ordered list: [docs/OPERATE.md](docs/OPERATE.md). Long appendix: [docs/DEV_DASHBOARD.md](docs/DEV_DASHBOARD.md).

<details>
<summary>Local preview and checks</summary>

```bash
git clone https://github.com/KR8ZYSHO3/Universal-Science-Discovery.git
cd Universal-Science-Discovery
python -m http.server 8765
# then open http://localhost:8765/dashboard/

pip install pyyaml jsonschema networkx
python scripts/validate_schemas.py
```

</details>

<details>
<summary>Harvest and draft tools (not auto-merged)</summary>

Drafts stay staged. A human still promotes bridges.

```bash
python scripts/harvesters/harvest_openalex.py --bridge-scan
python scripts/propose_bridges.py --top 15
python scripts/find_orphan_unknowns.py
python scripts/harvesters/wave_factory.py --top 30 --min-citations 50 --output drafts/wave_factory
```

</details>

---

## Roadmap


| Stage | Status | Goal |
| ----- | ------ | ---- |
| **Phase 0: Foundation** | Complete | Governance · schemas · CI · seeded catalog · knowledge graph · contributor hub |
| **v1.1 Core Development** | Shipped 2026-08-26 | 4/4 seed Crosscheck CONFIRMED · generate/promote path · CI trust · hub recommendations |
| **v1.3 University-ready** | **Now** | Closed-loop Crosscheck · hub first-visit · one maintainer command list · catalog-batch runbook |
| **v1.2 Public launch** | Parked | arXiv submit · outreach · custom domain — [LAUNCH_PLAYBOOK.md](LAUNCH_PLAYBOOK.md) |
| **Later (2027–2035)** | After the product is the argument | Institutional partners · citeable papers · richer interface |

Canonical path: **[ROADMAP.md](ROADMAP.md)**. GSD execution list: [`.planning/ROADMAP.md`](.planning/ROADMAP.md).


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

- **Catalog content** (records and documentation): [CC BY 4.0](LICENSE)
- **Code** (scripts, site, checks): [MIT](LICENSE)

© 2026 Brandon Shoemaker and USDR Contributors