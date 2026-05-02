# Changelog

All notable changes to the Universal Science Discovery Repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
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