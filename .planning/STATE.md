# Project State

## Project Reference

See: `.planning/PROJECT.md` (updated 2026-06-23)

**Core value:** Researchers can run falsifiable Crosscheck experiments in minutes.
**Ship bar:** Single-dev robust · workflows excellent · interface awesome (see PROJECT.md § Ship Bar).
**Current focus:** Phase 2 — Epidemic FSS precision (02-02 regression+CI done; 02-03 Colab/notebook next)

**Parked:** v1.2 Launch (marketing) — `LAUNCH_PLAYBOOK.md` — owner not interested until dev milestone ships.

## Current Position

Phase: 2 of 5 (Epidemic FSS precision)
Plan: 2 of 3 in current phase (02-02 complete)
Status: Ready to execute 02-03
Last activity: 2026-08-26 — 02-02 freeze pytest + CI RESULT: CONFIRMED grep

Progress: [█████░░░░░] 45% (5/11 plans complete)

## Performance Metrics

| Phase | Plans | Total | Status |
|-------|-------|-------|--------|
| 1 Crosscheck credibility | 3 | 3 | Complete |
| 2 Epidemic FSS | 2 | 3 | **Active** |

## Accumulated Context

### Decisions

- **Development before marketing** (2026-06-23) — outreach/DNS/arXiv deferred to v1.2
- GSD active — no ad-hoc implementation without a plan
- Python canonical; browser demo tier
- Epidemic FSS (02-01): PC_INF=1/6, NU_THEORY=3.0, S≥N^{-1/3}, SEEDS_PER_N=20, BOND_SAMPLES_PER_MID=8, NU_TOLERANCE=0.15; CONFIRMED ν=3.1475 (4.9%); freeze mean_pcs in 02-01-SUMMARY (do not invent)
- Epidemic FSS (02-02): pytest pins freeze mean_pcs; CI greps RESULT: CONFIRMED; NU_THEORY asserted 3.0; no live MC in repo_smoke

### Blockers/Concerns

- Epidemic FSS 02-01 CONFIRMED and 02-02 pinned; full-grid R²=0.32 (N=200 non-monotonic). Do not shop a prettier freeze vector.

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
Stopped at: Completed 02-02-PLAN.md
Resume file: None

Local note: previous checkout was stale `launch/june-2026-shipping`. June-pause catalog drafts (climate cascades + zeta) stashed as `june-2026-pause leftover launch docs and climate drafts`. Parked until after v1.1.

**Next command:** `/gsd-execute-phase 2` (continue 02-03)