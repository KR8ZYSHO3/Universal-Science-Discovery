# GSD integration (optional maintainer tooling)

[GSD / get-shit-done](https://github.com/gsd-build/get-shit-done) is an optional **spec-driven workflow** for Cursor and similar environments: discuss → plan → execute phases with tracked artifacts (often under `.planning/`). USDR does **not** require GSD for contributors; this page is for maintainers who already use GSD and want alignment with repository policy.

**Maintainer status (2026-06-23):** GSD is **active** for **v1.1 Core Development** (Crosscheck + trust surfaces). Marketing/outreach is deferred to **v1.2 Launch**. See `.planning/PROJECT.md`, `.planning/ROADMAP.md`, `.planning/STATE.md`. Repo-root `ROADMAP.md` remains the long-range vision; `.planning/ROADMAP.md` is the execution phase list.

## Boundaries

- **Science and claims** still follow [METHODOLOGY.md](METHODOLOGY.md), [ETHICS_REPRODUCIBILITY_AND_DATA.md](ETHICS_REPRODUCIBILITY_AND_DATA.md), and [LEGAL.md](../LEGAL.md). GSD plans are **process metadata**, not evidence for hypotheses.
- **Data and ingest** must match [DATA_PLAN.md](DATA_PLAN.md) and `schemas/`; do not bypass governance because a phase plan says so.
- **Canonical repo state** for humans and agents remains [.planning/STATE.md](../.planning/STATE.md) (see [DEV_DASHBOARD.md](DEV_DASHBOARD.md)). If you use GSD phases, reflect outcomes there or in the HTML contributor hub when milestones land.

## How it fits USDR

| Need | Where to look |
|------|----------------|
| Day-to-day checklist / branches | [DEV_DASHBOARD.md](DEV_DASHBOARD.md), `STATE.md` |
| Cadence, versioning, CI expectations | [OPERATING_RHYTHM.md](OPERATING_RHYTHM.md) |
| Doc ↔ behavior traceability | [DOC_MAP.md](DOC_MAP.md) |
| Installing GSD skills / CLI | Upstream [get-shit-done](https://github.com/gsd-build/get-shit-done) docs |

## Forks and minimal checkouts

Forks may omit `.planning/` history or GSD config; that is fine. Optional GSD artifacts must never be required to **read** policy, **contribute** unknowns/hypotheses, or **run** documented tools (e.g. `packages/ingest`, MkDocs).
