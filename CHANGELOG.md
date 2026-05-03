# Changelog

All notable changes to the Universal Science Discovery Repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Changed
- **[`.cursor/rules/documentation-and-dashboard.mdc`](.cursor/rules/documentation-and-dashboard.mdc)** — hub CDN/offline + **HAPPY_PATH_FIRST_RECORDS** when schemas/seed examples change Stream A; sync **README** / **DEV_DASHBOARD** when hub UX changes
- **[docs/DEV_DASHBOARD.md](docs/DEV_DASHBOARD.md)** and **[dashboard/README.md](dashboard/README.md)** — hub UX (theme, nav) and CDN / offline notes
- **Contributor hub** [`dashboard/index.html`](dashboard/index.html): richer hero, sticky “glass” nav + scroll-spy, light/dark toggle, stat deck and motion (respects `prefers-reduced-motion`); [`dashboard/README.md`](dashboard/README.md) updated
- **[docs/OPERATING_RHYTHM.md](docs/OPERATING_RHYTHM.md)** — branch protection: table of status check names + ingest workflow path-filter caveat
- **[docs/OPERATING_RHYTHM.md](docs/OPERATING_RHYTHM.md)** — CI guidance: no markdown links to GitHub Pages base URL until it returns 200 (or use `ignorePatterns`)

### Fixed
- **markdown-link-check (CI):** GitHub Pages URL in README/manifest as plain text (not a link until live); `docs/index.md` uses explicit reference links to `tree/main/...` (avoids broken `../tree/...`); broaden `kr8zysho3.github.io` ignore pattern in `.markdown-link-check.json`

### Added
- **[docs/QUALITY_BAR.md](docs/QUALITY_BAR.md)** — anti-sloppiness playbook (CI, review lanes, definition of done); linked from CONTRIBUTING, collaboration doc, onboarding, MkDocs **Community & integrity**, DOC_MAP, manifest, docs index, hub, happy path
- **[docs/HAPPY_PATH_FIRST_RECORDS.md](docs/HAPPY_PATH_FIRST_RECORDS.md)** — Stream A: setup → unknown YAML → hypothesis YAML → PR; wired through CONTRIBUTING, onboarding, MkDocs, DOC_MAP, manifest, templates README, `docs/index`, contributor hub
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