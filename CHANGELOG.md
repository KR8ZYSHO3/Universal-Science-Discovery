# Changelog

All notable changes to the Universal Science Discovery Repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added (2026-05-04 session — Kuramoto and Fisher information bridges)
- **`cross-domain/physics-engineering-neuroscience/b-kuramoto-synchronization.yaml`** — 13th bridge: Kuramoto model unifies neural gamma oscillations, cardiac AF, power grid stability, and laser arrays. The spectral-gap formula for K_c (derived for power grids) predicts sinoatrial node AF threshold. Includes h-kuramoto-af-spectral-gap: pacemaker stimulation protocol from laser engineering.
- **`hypotheses/active/h-kuramoto-af-spectral-gap.yaml`** — AF vulnerability = inverse spectral gap of sinoatrial coupling Laplacian; laser noise-robust phase-locking protocol → novel pacemaker design.
- **`cross-domain/statistics-evolution/b-fisher-information-evolution.yaml`** — 14th bridge: Fisher information I(theta) = additive genetic variance V_A. Fisher's two 1925/1930 theorems are one. Natural selection = natural gradient ascent = TRPO/NPG in deep RL. Connects to h-quantum-compass-precision (quantum Fisher info).
- **`unknowns-catalog/biology/u-fisher-natural-gradient-evolution.yaml`** — Does natural selection saturate the Fisher-information speed limit? Does the G-matrix encode the natural gradient direction?
- **`hypotheses/active/h-fisher-speed-limit-selection.yaml`** — Artificial selection efficiency R/(V_A*beta) near 1.0 in large populations, drops with 1/(2*Ne*s); Illinois maize long-term experiment as test case.
- **GitHub Issues #29-31** — Kuramoto AF spectral gap, Fisher speed limit, habitat percolation SLOSS resolution.
- **`dashboard/index.html`** — Updated counts: 20 unknowns · 20 hypotheses · 14 bridges.
- **`.planning/STATE.md`** — Bridge network table updated to 14 bridges.

### Added (2026-05-04 session — ecology and information-evolution bridges)
- **`cross-domain/physics-ecology/b-habitat-percolation-ecology.yaml`** — 11th bridge: completes the percolation trilogy (oncology, epidemiology, ecology). The ~60% habitat threshold at which forest-interior species collapse is the 2D site percolation threshold p_c=0.593. FSS corrections predict how this threshold shifts in finite landscapes. Resolves the 50-year SLOSS debate analytically.
- **`unknowns-catalog/biology/u-habitat-fragmentation-threshold.yaml`** — Has the 2D percolation FSS exponent nu=4/3 ever been measured from real species-persistence data? No.
- **`hypotheses/active/h-habitat-percolation-critical-density.yaml`** — FSS-corrected threshold p_c(A)=0.593+c*A^(-3/4) measurable from Sentinel-2 satellite data; early-warning indicators of approaching threshold derivable from cluster-size power law.
- **`cross-domain/information-evolution/b-error-threshold-information.yaml`** — 12th bridge: Eigen's quasispecies error threshold and Shannon's channel capacity theorem are the same mathematical result. RNA viruses operate near the Shannon limit. Coronavirus nsp14 proofreading is a capacity-expansion adaptation.
- **`unknowns-catalog/biology/u-error-threshold-genome-size.yaml`** — Has the Shannon bound C=1-H(mu) ever been fitted to the (mu, L) distribution across all domains of life?
- **`hypotheses/active/h-viral-proofreading-shannon-optimality.yaml`** — nsp14 proofreading is Shannon-optimal; nidovirus genome-size distribution should fit the Shannon capacity curve; lethal mutagenesis minimum dose derivable from the bound.
- **`unknowns-catalog/physics/u-gauge-field-epidemic-nonlocality.yaml`** — Seeded from q-bio:PE harvest; QED gauge-field formalism applied to non-local epidemic spreading (April 2026 preprints); speculation clearly labelled.
- **`data/harvest/qbio-pe-2026-05-04.jsonl`** — 25 records from q-bio:q-bio:PE (April 2026).
- **`packages/ingest/src/usdr_ingest/constants.py`** — Fixed OAI-PMH endpoint URL (`/oai` → `/oai2`).
- **`dashboard/index.html`** — Updated counts: 19 unknowns · 18 hypotheses · 12 bridges.
- **`.planning/STATE.md`** — Bridge network table updated to 12 bridges.

### Added (2026-05-04 session — RG and epidemiology bridges)
- **`cross-domain/mathematics-biology/b-renormalization-biological-scaling.yaml`** — 9th bridge: renormalization group (RG) fixed point ↔ biological allometric scaling laws. The WBE vascular branching recursion is structurally an RG equation; the correction-to-scaling exponent predicts how Kleiber's Law breaks down below 1g. Includes full translation table with 7 entries and cross-pollination opportunities.
- **`unknowns-catalog/biology/u-renormalization-allometric.yaml`** — Has the WBE vascular recursion ever been cast as a real-space RG transformation and the correction-to-scaling exponent derived? No.
- **`hypotheses/active/h-allometric-rg-fixed-point.yaml`** — Wilson-Fisher correction-to-scaling exponent from the branching-network RG predicts the observed sub-1g deviation in Savage et al. (2004); testable against ectotherm data.
- **`cross-domain/physics-epidemiology/b-percolation-epidemiology.yaml`** — 10th bridge: network percolation ↔ epidemic threshold. R_0=1 is a percolation phase transition; FSS corrections predict finite-population R_0 bias. COVID-19 nursing home datasets provide the test.
- **`unknowns-catalog/biology/u-percolation-epidemic-fss.yaml`** — Do percolation FSS corrections quantitatively improve R_0 estimates in populations of N < 10,000?
- **`hypotheses/active/h-percolation-outbreak-threshold.yaml`** — FSS correction exponent nu=1 (random-graph universality class) measurable from COVID-19 nursing home outbreak data; 30% R_0 estimation improvement predicted.
- **GitHub Issues #24-26** — contributor tasks for KZ experiment, FSS epidemiology analysis, and RG allometry calculation.
- **`dashboard/index.html`** — Updated counts: 16 unknowns · 16 hypotheses · 10 bridges.
- **`.planning/STATE.md`** — Full bridge network table updated to 10 bridges.

### Added (2026-05-04 session — cross-domain catalog expansion)
- **8th bridge** [`cross-domain/cosmology-biology/b-kibble-zurek-morphogenesis.yaml`](cross-domain/cosmology-biology/b-kibble-zurek-morphogenesis.yaml)
  — Kibble-Zurek mechanism (Big Bang defect formation) ↔ embryonic symmetry breaking (PAR polarisation in *C. elegans*);
  includes full `translation_table`, `cross_pollination_opportunities`, and `communication_gap`.
- **Unknown** [`unknowns-catalog/physics/u-kibble-zurek-embryo.yaml`](unknowns-catalog/physics/u-kibble-zurek-embryo.yaml)
  — Does PAR-domain error density scale with fertilisation quench rate per KZ power-law?
- **Hypothesis** [`hypotheses/active/h-kibble-zurek-polarity-scaling.yaml`](hypotheses/active/h-kibble-zurek-polarity-scaling.yaml)
  — CDK1 quench-rate experiment in *C. elegans* + active-KZ theory extension; closes the loop to `b-topology-morphogenesis`.
- **Hypothesis** [`hypotheses/active/h-quantum-compass-precision.yaml`](hypotheses/active/h-quantum-compass-precision.yaml)
  — Cryptochrome CRY4 operates at the quantum Fisher-information Cramér-Rao bound; proposes QFI ratio measurement
  and bio-inspired protein-scaffold quantum sensor as spinoff; fills `b-quantum-biology-navigation` hypothesis gap
  and closes GitHub Issue #18.
- **`cross-domain/cosmology-biology/README.md`** — Bridge overview with 55-orders-of-magnitude span table.
- **`cross-domain/README.md`** — Updated bridge index table; 8 bridges now listed.
- **`docs/CROSS_DOMAIN_BRIDGES.md`** — Updated bridge table with new KZ and quantum compass entries.
- **`dashboard/index.html`** — Updated counts: 14 unknowns · 14 hypotheses · 8 bridges.

### Changed
- **[`.cursor/rules/documentation-and-dashboard.mdc`](.cursor/rules/documentation-and-dashboard.mdc)** — hub CDN/offline + **HAPPY_PATH_FIRST_RECORDS** when schemas/seed examples change Stream A; sync **README** / **DEV_DASHBOARD** when hub UX changes
- **[docs/DEV_DASHBOARD.md](docs/DEV_DASHBOARD.md)** and **[dashboard/README.md](dashboard/README.md)** — hub UX (theme, nav) and CDN / offline notes
- **Contributor hub** [`dashboard/index.html`](dashboard/index.html): richer hero, sticky “glass” nav + scroll-spy, light/dark toggle, stat deck and motion (respects `prefers-reduced-motion`); [`dashboard/README.md`](dashboard/README.md) updated
- **[docs/OPERATING_RHYTHM.md](docs/OPERATING_RHYTHM.md)** — branch protection: table of status check names + ingest workflow path-filter caveat
- **[docs/OPERATING_RHYTHM.md](docs/OPERATING_RHYTHM.md)** — CI guidance: no markdown links to GitHub Pages base URL until it returns 200 (or use `ignorePatterns`)

### Fixed
- **markdown-link-check (CI):** GitHub Pages URL in README/manifest as plain text (not a link until live); `docs/index.md` uses explicit reference links to `tree/main/...` (avoids broken `../tree/...`); broaden `kr8zysho3.github.io` ignore pattern in `.markdown-link-check.json`
- **ingest pytest (CI):** `test_cli_help.py` sets `TERM=dumb` for `CliRunner` so Rich/Typer help includes option text under `TERM=linux` (GitHub Actions default)

### Added
- **`docs/examples/`** — synthetic [arxiv-oai-metadata-sample.v1.jsonl](docs/examples/arxiv-oai-metadata-sample.v1.jsonl) (envelope v1, fixture-derived); [README](docs/examples/README.md); **MkDocs** Operations nav; [`scripts/generate-ingest-example-jsonl.py`](scripts/generate-ingest-example-jsonl.py); pytest asserts sample validates against [`schemas/ingestion-envelope-1.0.0.json`](schemas/ingestion-envelope-1.0.0.json); [DATA_PLAN.md](docs/DATA_PLAN.md) stretch item filled; DOC_MAP + REPOSITORY_MANIFEST rows
- **[docs/QUALITY_BAR.md](docs/QUALITY_BAR.md)** — anti-sloppiness playbook (CI, review lanes, definition of done); linked from CONTRIBUTING, collaboration doc, onboarding, MkDocs **Community & integrity**, DOC_MAP, manifest, docs index, hub, happy path
- **[docs/HAPPY_PATH_FIRST_RECORDS.md](./docs/HAPPY_PATH_FIRST_RECORDS.md)** — Stream A: setup → unknown YAML → hypothesis YAML → PR; wired through CONTRIBUTING, onboarding, MkDocs, DOC_MAP, manifest, templates README, `docs/index`, contributor hub
- **PR template** ingest/envelope checkbox; **CONTRIBUTING** tooling section for `packages/ingest`; contributor **hub** maintainer bar links **compare** `main...feat/dev-dashboard` for integration PRs
- **[packages/ingest/README.md](packages/ingest/README.md)** — package quickstart; `pyproject` **`readme`** field for metadata; root README ingest section links here
- **[docs/UAT_INGEST.md](docs/UAT_INGEST.md)** — manual acceptance steps for `usdr-ingest` (pytest + CLI smoke + optional live OAI dry-run); linked from [DATA_PLAN.md](docs/DATA_PLAN.md), MkDocs **Operations**, hub, DOC_MAP, manifest
- **[docs/GSD_INTEGRATION.md](docs/GSD_INTEGRATION.md)** — optional GSD boundaries for maintainers; linked from [ROADMAP.md](ROADMAP.md), onboarding, doc map, MkDocs **Operations**, **docs/index**, **REPOSITORY_MANIFEST**, and contributor hub (`dashboard/index.html` Cadence + Reference)
- **`schemas/ingestion-envelope-1.0.0.json`** — JSON Schema for metadata ingest JSONL (`DATA_PLAN` v1.0.0); `packages/ingest` tests validate harvest fixtures against it (`jsonschema` dev dep)
- Cursor rule **documentation-and-dashboard** (`.cursor/rules/documentation-and-dashboard.mdc`): keep docs, CHANGELOG, `.planning/STATE.md`, and `dashboard/` contributor hub current at milestones and ongoing; verify `http://localhost:8765/dashboard/` when hub links change
- AGENTS + OPERATING_RHYTHM alignment with the same expectations
- **GitHub Pages deploy** workflow (`.github/workflows/mkdocs-gh-pages.yml`) + `site_url` in `mkdocs.yml` for `https://kr8zysho3.github.io/Universal-Science-Discovery/`
- README **Published documentation** subsection and REPOSITORY_MANIFEST entry for the live docs URL and `gh-pages` Pages source; `.gitignore` **MkDocs output** (`/site/`) so local builds are not committed
- **arXiv OAI-PMH metadata ingest** — [`packages/ingest`](packages/ingest) (`usdr-ingest`), [`requirements-ingest.txt`](requirements-ingest.txt), root [`pyproject.toml`](pyproject.toml) pytest config; [`.github/workflows/ingest-ci.yml`](.github/workflows/ingest-ci.yml)
- Cursor rule **agent-execution** (`.cursor/rules/agent-execution.mdc`) — prefer in-environment installs, tests, and git
- Phase 0 **seed content**: example unknowns + linked active hypotheses (dark matter / radio–axion-like constraints; aging intervention translatability / metabolic bottlenecks) under `unknowns-catalog/high-priority/` and `hypotheses/active/`
- **Discipline stubs** [`disciplines/physics/README.md`](disciplines/physics/README.md), [`disciplines/biology/README.md`](disciplines/biology/README.md), [`disciplines/computer-science/README.md`](disciplines/computer-science/README.md)
- **Schema validation CI** ([`.github/workflows/validate-schemas.yml`](.github/workflows/validate-schemas.yml)) and [`scripts/validate_schemas.py`](scripts/validate_schemas.py) with [`scripts/requirements-validate.txt`](scripts/requirements-validate.txt)
- **MkDocs site** for `docs/` — [`mkdocs.yml`](mkdocs.yml), [`requirements-docs.txt`](requirements-docs.txt), [`docs/index.md`](docs/index.md), CI [`.github/workflows/mkdocs-build.yml`](.github/workflows/mkdocs-build.yml) (MkDocs ignores broken `../` links to repo-root files so `build --strict` passes)
- README content-layout row for the physics seed
- Blueprint MVP slice: `schemas/` (hypothesis, unknown, dataset), `templates/`, `disciplines/`, `unknowns-catalog/`, `hypotheses/` (subfolders), `cross-domain/`, `code/` with READMEs
- README + DOC_MAP updates for content layout
- `CONTRIBUTING.md` contributor path aligned with blueprint and outreach docs
- `DOC_MAP.md` traceability for all root-level policy and communication documents
- Cross-links between `WHY_CONTRIBUTE.md` and `VISION_COMMUNICATION.md`
- [ROADMAP.md](ROADMAP.md): “Interface development” section linking phased delivery to [INTERFACE.md](INTERFACE.md)

### Changed
- N/A (initial release)

---

## [0.1.0] - 2026-05-01

### Added
- Foundational repository created
- Core root documents: README, LICENSE (MIT + CC0), CONTRIBUTING.md, CODE_OF_CONDUCT.md, LEGAL.md, GOVERNANCE.md, SECURITY.md, CHANGELOG.md
- Detailed blueprint for full implementation (see `universal-science-discovery-repo-blueprint.md`)
- Initial focus on discovery-first principles: unknowns, hypotheses, cross-domain connections
- Plans for DVC integration, knowledge graph export, and AI-assisted hypothesis generation

### Notes
This is the initial planning and documentation release. The repository is not yet public. The first public launch (v0.5.0) is targeted for mid-2026 with seeded content in at least two disciplines.

---

## [0.0.1] - 2026-04-15 (Internal)

### Added
- Project concept and initial conversations
- Vision for a Git-based, version-controlled scientific discovery engine
- Emphasis on legal compliance, community governance, and sustainable open science infrastructure

---

**Legend**
- `Added` for new features
- `Changed` for changes in existing functionality
- `Deprecated` for soon-to-be removed features
- `Removed` for now removed features
- `Fixed` for any bug fixes
- `Security` for vulnerability fixes

For older versions, see the [Git history](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/commits/main).