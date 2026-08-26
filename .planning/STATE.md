# Project State

## Project Reference

See: `.planning/PROJECT.md` (updated 2026-06-23)

**Core value:** Researchers can run falsifiable Crosscheck experiments in minutes.
**Ship bar:** Single-dev robust · workflows excellent · interface awesome (see PROJECT.md § Ship Bar).
**Current focus:** Phase 2 — Epidemic FSS precision (must tie to WORK-01, not isolated tuning)

**Parked:** v1.2 Launch (marketing) — `LAUNCH_PLAYBOOK.md` — owner not interested until dev milestone ships.

## Current Position

Phase: 2 of 5 (Epidemic FSS precision)
Plan: 1 of 3 in current phase (02-01 complete)
Status: Ready to execute 02-02
Last activity: 2026-08-26 — 02-01 CONFIRMED (ν̄=3.1475, SEEDS=20, BOND_SAMPLES=8); freeze in 02-01-SUMMARY

Progress: [████░░░░░░] 36% (4/11 plans complete)

## Performance Metrics

| Phase | Plans | Total | Status |
|-------|-------|-------|--------|
| 1 Crosscheck credibility | 3 | 3 | Complete |
| 2 Epidemic FSS | 1 | 3 | **Active** |

## Accumulated Context

### Decisions

- **Development before marketing** (2026-06-23) — outreach/DNS/arXiv deferred to v1.2
- GSD active — no ad-hoc implementation without a plan
- Python canonical; browser demo tier
- Epidemic FSS (02-01): PC_INF=1/6, NU_THEORY=3.0, S≥N^{-1/3}, SEEDS_PER_N=20, BOND_SAMPLES_PER_MID=8, NU_TOLERANCE=0.15; CONFIRMED ν=3.1475 (4.9%); freeze mean_pcs in 02-01-SUMMARY (do not invent)

### Blockers/Concerns

- Epidemic FSS 02-01 CONFIRMED; 02-02 must pin SUMMARY mean_pcs (no live MC). Full-grid R²=0.32; N≥500 window did not pass.

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
Stopped at: Completed 02-01-PLAN.md (RESULT: CONFIRMED)
Resume file: None

Local note: previous checkout was stale `launch/june-2026-shipping`. June-pause catalog drafts (climate cascades + zeta) stashed as `june-2026-pause leftover launch docs and climate drafts`. Parked until after v1.1.

**Next command:** `/gsd-execute-phase 2` (continue 02-02)