# Project State

## Project Reference

See: `.planning/PROJECT.md` (updated 2026-06-23)

**Core value:** Researchers can run falsifiable Crosscheck experiments in minutes.
**Ship bar:** Single-dev robust · workflows excellent · interface awesome (see PROJECT.md § Ship Bar).
**Current focus:** Phase 2 — Epidemic FSS precision (must tie to WORK-01, not isolated tuning)

**Parked:** v1.2 Launch (marketing) — `LAUNCH_PLAYBOOK.md` — owner not interested until dev milestone ships.

## Current Position

Phase: 2 of 5 (Epidemic FSS precision)
Plan: 0 of 3 in current phase
Status: Ready to execute
Last activity: 2026-08-26 — Phase 2 planned (methodology pass: ν̄=3, S≥N^{-1/3}); executing 02-01

Progress: [████░░░░░░] 38% (3/11 plans complete)

## Performance Metrics

| Phase | Plans | Total | Status |
|-------|-------|-------|--------|
| 1 Crosscheck credibility | 3 | 3 | Complete |
| 2 Epidemic FSS | 0 | 3 | **Active** |

## Accumulated Context

### Decisions

- **Development before marketing** (2026-06-23) — outreach/DNS/arXiv deferred to v1.2
- GSD active — no ad-hoc implementation without a plan
- Python canonical; browser demo tier

### Blockers/Concerns

- Epidemic FSS: bond percolation on ER graphs, `networkx` dependency, wider ν tolerance (0.25) — needs precision sweep like habitat FSS

### Pending Todos

None in `.planning/todos/pending/`.

## Deferred Items

| Category | Item | Milestone |
|----------|------|-----------|
| Marketing | Reddit, LinkedIn, outreach copy | v1.2 Launch |
| Infrastructure | usdr.science DNS, arXiv | v1.2 Launch |
| Engineering | Epidemic FSS | Phase 2 (active) |

## Session Continuity

Last session: 2026-08-26
Stopped at: Phase 2 plans verified; executing 02-01
Resume file: None

Local note: previous checkout was stale `launch/june-2026-shipping`. June-pause catalog drafts (climate cascades + zeta) stashed as `june-2026-pause leftover launch docs and climate drafts`. Parked until after v1.1.

**Next command:** `/gsd-plan-phase 2` (in progress)