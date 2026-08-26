# Project State

## Project Reference

See: `.planning/PROJECT.md` (updated 2026-06-23)

**Core value:** Researchers can run falsifiable Crosscheck experiments in minutes.
**Ship bar:** Single-dev robust · workflows excellent · interface awesome (see PROJECT.md § Ship Bar).
**Current focus:** Phase 3 — Crosscheck scale-up (03-01 / 03-02 PLAN.md written)

**Parked:** v1.2 Launch (marketing) — `LAUNCH_PLAYBOOK.md` — owner not interested until dev milestone ships.

## Current Position

Phase: 3 of 5 (Crosscheck scale-up) — planned
Plan: 0 of 2 executed (03-01, 03-02 PLAN.md ready)
Status: Ready to execute Phase 3
Last activity: 2026-08-26 — Phase 3 plans written (oncology GCC generate/promote + parity matrix)

Progress: [██████░░░░] 55% (6/11 plans complete)

## Performance Metrics

| Phase | Plans | Total | Status |
|-------|-------|-------|--------|
| 1 Crosscheck credibility | 3 | 3 | Complete |
| 2 Epidemic FSS | 3 | 3 | Complete |
| 3 Crosscheck scale-up | 0 | 2 | Planned |

## Accumulated Context

### Decisions

- **Development before marketing** (2026-06-23) — outreach/DNS/arXiv deferred to v1.2
- GSD active — no ad-hoc implementation without a plan
- Python canonical; browser demo tier
- Epidemic FSS (02-01): PC_INF=1/6, NU_THEORY=3.0, S≥N^{-1/3}, SEEDS_PER_N=20, BOND_SAMPLES_PER_MID=8, NU_TOLERANCE=0.15; CONFIRMED ν=3.1475 (4.9%); freeze mean_pcs in 02-01-SUMMARY (do not invent)
- Epidemic FSS (02-02): pytest pins freeze mean_pcs; CI greps RESULT: CONFIRMED; NU_THEORY asserted 3.0; no live MC in repo_smoke
- Epidemic FSS (02-03): YAML/README/Colab match volume nu_bar=3, S≥N^{-1/3}, p_c(inf)=1/6, SEEDS_PER_N=20, NU_TOLERANCE=0.15; status confirmed; habitat/cluster/Ising left executed

### Blockers/Concerns

- Epidemic FSS 02-01 CONFIRMED and 02-02 pinned; full-grid R²=0.32 (N=200 non-monotonic). Do not shop a prettier freeze vector.

### Pending Todos

None in `.planning/todos/pending/`.

## Deferred Items

| Category | Item | Milestone |
|----------|------|-----------|
| Marketing | Reddit, LinkedIn, outreach copy | v1.2 Launch |
| Infrastructure | usdr.science DNS, arXiv | v1.2 Launch |
| Engineering | Epidemic FSS | Phase 2 (complete 2026-08-26) |

## Session Continuity

Last session: 2026-08-26
Stopped at: Phase 3 planned and checker-passed (0 blockers); ready to execute 03-01
Resume file: None

Local note: previous checkout was stale `launch/june-2026-shipping`. June-pause catalog drafts (climate cascades + zeta) stashed as `june-2026-pause leftover launch docs and climate drafts`. Parked until after v1.1.

**Next command:** `/gsd-execute-phase 3`