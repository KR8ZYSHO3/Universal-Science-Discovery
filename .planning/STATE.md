# USDR workspace state

Authoritative checklist for humans and agents. Update after each merged PR.

## Last updated

- 2026-05-07 - **Waves 17–35 complete — 470 bridges, 2,000+ graph nodes**: Overnight build session added ~220 bridges (from ~250 to 470), hitting the 300-, 350-, and 400-bridge milestones along the way. Final session counts: **470 bridges, 817 unknowns, 681 hypotheses, 1,982 graph nodes, 2,069 edges, 0 orphan unknowns**. Dashboard updated with 400-bridge gold milestone banner. Lyme disease breakthrough-gap cluster added (breakthrough-gaps now at 12). 13 pioneer profiles. Preprint updated. All schemas validate clean.

- 2026-05-06 - **Wave 29 — THE 400-BRIDGE MILESTONE**: 12 new bridges (399-410) covering stochastic gene expression noise, scientific method epistemological foundations (capstone bridge 400), electrophysiology/action potential, thermodynamics convex analysis, complexity economics, neuromuscular control biomechanics, topological condensed matter, allelopathy chemical ecology, computational psychiatry, order-book microstructure, population vector motor cortex, secondary metabolites drug discovery. 12 unknowns + 12 hypotheses. Dashboard: 400-bridge gold milestone banner added. **Running totals: 413 bridges, 790 unknowns, 657 hypotheses, 1,887 nodes, 1,984 edges.**

- 2026-05-06 - **Wave 24 — THE 350-BRIDGE MILESTONE**: 12 new bridges (340-351) covering superconductivity cooper pairs, network formation games, lipid bilayer membrane transport, FEM/PDE, oceanic turbulence mixing, neural field theory brain waves, optimal control cancer treatment, prediction markets, molecular dynamics, organ-on-chip, Standard Model unity, sleep memory consolidation. 12 unknowns + 12 hypotheses. **Running totals: 350+ bridges, ~689 unknowns, ~556 hypotheses, ~1,700+ nodes.**

- 2026-05-06 - **Wave 20 — THE 300-BRIDGE MILESTONE**: 14 new bridges (287-300) covering glymphatic CSF fluid dynamics, Wasserstein optimal transport for cell differentiation, biomimetic SLIP locomotion, Li-ion electrochemistry, network centrality and social influence, dislocation mechanics, loss aversion evolutionary psychology, geometric measure theory minimal surfaces, ecosystem fold bifurcation, Goemans-Williamson SDP, SNARE neurotransmitter pharmacology, Daubechies wavelet/JPEG-2000, urban scaling laws, complex systems emergence. Dashboard updated with 300-bridge milestone banner. 14 unknowns + 14 hypotheses.

- 2026-05-06 - **Comprehensive audit + PATH_TO_SUCCESS strategic roadmap**: Python script audit (10 scripts), 5 HIGH severity fixes applied. Schema validation: all 1,000+ records PASS. Quality audit: 0 errors, 0 warnings. Created CODE_AUDIT.md, PATH_TO_SUCCESS.md. Updated README.md and DOC_MAP.md.

- 2026-05-06 - **Wave 10 — 1000-node milestone, 13 pioneers, bridges 171-180**: 1,000 nodes reached. 10 new bridges (b-171 to b-180). Added Einstein and Lovelace pioneer profiles (13 total). 11 breakthrough gaps. Dashboard health fixes. Knowledge graph: 1,000 nodes, 910 edges.

## Catalog state (as of 2026-05-07)

| Type | Count | Directory |
|------|-------|-----------|
| Bridges | **470** | `cross-domain/` |
| Unknowns | **817** | `unknowns-catalog/` |
| Hypotheses | **681** | `hypotheses/active/` |
| Pioneers | **13** | `pioneers/` |
| Breakthrough gaps | **12** | `breakthrough-gaps/` |
| Pre-formal observations | **4** | `phenomenology/` |
| Knowledge graph nodes | **1,982** | `docs/knowledge_graph.json` |
| Knowledge graph edges | **2,069** | `docs/knowledge_graph.json` |
| Schemas | **6** | `schemas/` (unknown, hypothesis, bridge, phenomenon, pioneer, breakthrough_gap) |
| Scientific domains | **55+** | `unknowns-catalog/` subdirs + `dashboard/domains/` |

### Data quality
- Orphan unknowns: **0**
- Schema errors: **0**
- CI status: green

## Current milestone

**Wave 35+ complete — 470 bridges, 1,982 graph nodes**

The repository has crossed 470 cross-domain mathematical bridges and 1,982 graph nodes. The overnight build session added ~220 bridges hitting the 300, 350, and 400 milestones. Next major target: **500 bridges**.

## Current focus

- **500-bridge push**: 30 more bridges to reach the next milestone. Run `python scripts/propose_bridges.py` to identify high-value orphan connections.
- **D3 graph on GitHub Pages**: interactive graph fails to load on Pages; fix `dashboard/graph.html` CSP/CORS or switch to static pre-rendered JSON approach.
- **arXiv preprint**: `docs/preprint/usdr_preprint.md` is ready; next step is PDF conversion (Pandoc + LaTeX) and submission to cs.DL + cross-list q-bio.QM, physics.soc-ph.
- **Expand breakthrough-gaps**: 12 entries, target 25+; Lyme cluster added; next clusters: Long COVID, Alzheimer's causation, consciousness, dark matter.
- **More pioneers**: 13 profiles; add 5 more (Turing, Ramanujan, Curie, Feynman, Noether).

## Active git branches / PRs

- `main` — default; all PRs squash-merged here; CI: validate-schemas + mkdocs + markdown-link-check.
- Any active feature branch: `feat/...` — check GitHub Pull Requests tab.

## Blocked / needs human

- None.

## Next actions (max 5)

1. **Hit 500 bridges** — 30 more; run `python scripts/propose_bridges.py` and batch next wave. Focus on under-connected domains (geology, linguistics, medicine).
2. **Fix D3 graph on GitHub Pages** — interactive graph not loading; debug CSP headers, or convert to static pre-rendered embed.
3. **Submit arXiv preprint** — convert `docs/preprint/usdr_preprint.md` to PDF via Pandoc; submit to cs.DL + cross-list q-bio.QM, physics.soc-ph.
4. **Expand breakthrough-gaps catalog** — target 25+ entries; add Long COVID, Alzheimer's causation, consciousness hard problem, dark matter identity clusters.
5. **Add more pioneer profiles** — add Turing, Ramanujan, Curie, Feynman, Noether to `pioneers/` (currently 13).
