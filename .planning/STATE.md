# Project State

## Project Reference

See: `.planning/PROJECT.md` (updated 2026-08-26 after v1.1)

**Core value:** Researchers can run falsifiable Crosscheck experiments in minutes.
**Ship bar:** Single-dev robust · workflows excellent · interface awesome (see PROJECT.md § Ship Bar).
**Current focus:** v1.1 Core Development **shipped**. No active GSD milestone. v1.2 Launch parked.

**Parked:** v1.2 Launch (marketing) — `LAUNCH_PLAYBOOK.md`

## Current Position

Phase: — (v1.1 complete; next milestone not opened)
Plan: —
Status: Milestone v1.1 archived
Last activity: 2026-08-26 — `/gsd-complete-milestone` v1.1

Progress: v1.1 [██████████] 100% (11/11 plans)

## Performance Metrics

| Milestone | Phases | Plans | Status |
|-----------|--------|-------|--------|
| v1.0 Foundation | repo Phase 0 | — | Complete |
| v1.1 Core Development | 1–5 | 11 | Shipped 2026-08-26 (#308) |

## Accumulated Context

### Decisions

- GSD progress lives **in this USDR repo** (`.planning/STATE.md`, `ROADMAP.md`, `REQUIREMENTS.md`, `phases/`). Not a separate GSD repository.
- Development before marketing — v1.2 still parked after v1.1 close
- Epidemic FSS: `NU_THEORY = 3.0`, freeze mean_pcs, do not shop R²
- CONFIRMED CI gates use stdout tokens, not YAML `status`
- Hub recommendations: undirected degree; not a scientific ranking
- GitHub `main` PR-only; squash PR at big milestones

### Blockers/Concerns

- Epidemic freeze R²=0.32 (N=200 non-monotonic). Do not retune.
- No `v1.1-MILESTONE-AUDIT.md` at close; 11/11 requirements used as coverage.

### Pending Todos

None in `.planning/todos/pending/`.

## Deferred Items

Items acknowledged at milestone close 2026-08-26:

| Category | Item | Milestone |
|----------|------|-----------|
| Marketing | Reddit, LinkedIn, outreach copy | v1.2 Launch (parked) |
| Infrastructure | usdr.science DNS, arXiv | v1.2 Launch (parked) |
| Ship Bar | ROBUST-01, WORK-01, WORK-02, UI-01 | Unscheduled |
| Engineering | Epidemic freeze R² | Do not retune |
| Process | `/gsd-audit-milestone` skipped at v1.1 close | Optional later |
| Hub | Harvest-rank / curator-score implementation | After HUB-01 spec |

## Session Continuity

Last session: 2026-08-26
Stopped at: v1.1 archived; local `main` = `origin/main` (`cda2526`) plus pending archive commit
Resume file: None

**Next command:** `/gsd-new-milestone` when you want more GSD phases — or keep working ad-hoc against the Ship Bar. Do not start v1.2 Launch unless you reopen marketing.
