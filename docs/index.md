# Universal Science Discovery Repository

**Discovery-first** open infrastructure: explicit **unknowns**, testable **hypotheses**, cross-domain links, and reproducible workflows. Git remains the source of truth; this site is a readable view of the [`docs/`][gh-tree-docs] tree.

For the full project overview and repository layout, see the [README on GitHub](https://github.com/KR8ZYSHO3/Universal-Science-Discovery).

## Start here

- [Onboarding](ONBOARDING.md)
- **[Happy path — first unknown & hypothesis (Stream A)](HAPPY_PATH_FIRST_RECORDS.md)**
- [Vision & scope](VISION_AND_SCOPE.md) and [Methodology](METHODOLOGY.md)
- [Documentation map](DOC_MAP.md)
- [Contributing (repository root)](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/blob/main/CONTRIBUTING.md) — full contributor path
- **[Contributor hub](../dashboard/index.html)** (HTML in repo; run locally per [dashboard README](../dashboard/README.md))

## Meta

- [Developer dashboard](DEV_DASHBOARD.md) — operational checklist (source: `.planning/STATE.md`)
- [GSD integration (optional maintainers)](GSD_INTEGRATION.md) — spec-driven tooling boundaries
- [Ingest UAT (manual)](UAT_INGEST.md) — `usdr-ingest` smoke / optional live OAI

## Record examples (YAML)

High-priority unknowns and active hypotheses live under the repo root, e.g. [`unknowns-catalog/`][gh-unknowns] and [`hypotheses/active/`][gh-hypotheses]. Validate locally with `python scripts/validate_schemas.py`.

[gh-tree-docs]: https://github.com/KR8ZYSHO3/Universal-Science-Discovery/tree/main/docs
[gh-unknowns]: https://github.com/KR8ZYSHO3/Universal-Science-Discovery/tree/main/unknowns-catalog
[gh-hypotheses]: https://github.com/KR8ZYSHO3/Universal-Science-Discovery/tree/main/hypotheses/active
