# Project State

## Project Reference

See: `.planning/PROJECT.md` (updated 2026-08-26 — v1.3 opened)

**Core value:** Researchers can run falsifiable Crosscheck experiments in minutes.
**Ship bar:** Single-dev robust · workflows excellent · interface awesome (see PROJECT.md § Ship Bar).
**Current focus:** v1.3 University-ready robustness (phases 6–9). Product path: repo-root `ROADMAP.md`.

**Parked:** v1.2 Launch (marketing, DNS, arXiv submit) — `LAUNCH_PLAYBOOK.md`

## Current Position

Phase: 6 of 9 (Crosscheck closed loop) — not started
Plan: —
Status: Ready to plan
Last activity: 2026-08-27 — utilization flow is visual: docs/USE.md + SVG figures + hub door cards (FLOW-01)

Progress: v1.3 [░░░░░░░░░░] 0% (0/4 plans)

## Performance Metrics

| Milestone | Phases | Plans | Status |
|-----------|--------|-------|--------|
| v1.0 Foundation | repo Phase 0 | — | Complete |
| v1.1 Core Development | 1–5 | 11 | Shipped 2026-08-26 (#308) |
| v1.3 University-ready | 6–9 | 4 (planned) | Planning |

## Accumulated Context

### Decisions

- GSD progress lives **in this USDR repo** (`.planning/STATE.md`, `ROADMAP.md`, `REQUIREMENTS.md`, `phases/`). Not a separate GSD repository.
- **Root `ROADMAP.md` is the only product path.** PATH_TO_SUCCESS, INTERFACE, LAUNCH_* are appendices or parked.
- Development before marketing — v1.2 still parked after v1.1 close; v1.3 is engineering
- Epidemic FSS: `NU_THEORY = 3.0`, freeze mean_pcs, do not shop R²
- CONFIRMED CI gates use stdout tokens, not YAML `status`
- Hub recommendations: undirected degree; not a scientific ranking
- GitHub `main` PR-only; squash PR at big milestones

### Blockers/Concerns

- Epidemic freeze R²=0.32 (N=200 non-monotonic). Do not retune.
- No `v1.1-MILESTONE-AUDIT.md` at close; 11/11 requirements used as coverage.
- Crosscheck loop still does not feed stdout RESULT back into catalog YAML (WORK-01).

### Pending Todos

None in `.planning/todos/pending/`.

## Deferred Items

| Category | Item | Milestone |
|----------|------|-----------|
| Marketing | Reddit, LinkedIn, outreach copy | v1.2 Launch (parked) |
| Infrastructure | usdr.science DNS, arXiv submit | v1.2 Launch (parked) |
| Engineering | Epidemic freeze R² | Do not retune |
| Process | `/gsd-audit-milestone` skipped at v1.1 close | Optional later |
| Hub | Harvest-rank / curator-score implementation | After HUB-01 spec |

## Session Continuity

Last session: 2026-08-26
Stopped at: Product-path consolidation + v1.3 GSD artifacts written; engineering **not** executed
Resume file: None

**Next command:** `/gsd-plan-phase 6` (or `/gsd-discuss-phase 6`) to plan WORK-01. Do not start v1.2 Launch unless you reopen marketing. Do not push until the next milestone PR.
