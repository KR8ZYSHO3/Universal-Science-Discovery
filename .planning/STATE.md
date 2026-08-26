# Project State

## Project Reference

See: `.planning/PROJECT.md` (updated 2026-06-23)

**Core value:** Researchers can run falsifiable Crosscheck experiments in minutes.
**Ship bar:** Single-dev robust · workflows excellent · interface awesome (see PROJECT.md § Ship Bar).
**Current focus:** Phase 4 complete (CI & trust hardening) — TRUST-02/03 closed; next Phase 5 hub engineering

**Parked:** v1.2 Launch (marketing) — `LAUNCH_PLAYBOOK.md` — owner not interested until dev milestone ships.

## Current Position

Phase: 4 of 5 (CI & trust hardening) — complete
Plan: 2 of 2 executed
Status: Phase complete — orchestrator-verified (pytest 14/14)
Last activity: 2026-08-26 — Phase 4 verified (inventory + entry-point smokes)

Progress: [█████████░] 91% (10/11 plans complete; Phase 5 remaining)

## Performance Metrics

| Phase | Plans | Total | Status |
|-------|-------|-------|--------|
| 1 Crosscheck credibility | 3 | 3 | Complete |
| 2 Epidemic FSS | 3 | 3 | Complete |
| 3 Crosscheck scale-up | 2 | 2 | Complete |
| 4 CI & trust hardening | 2 | 2 | Complete |

## Accumulated Context

### Decisions

- **Development before marketing** (2026-06-23) — outreach/DNS/arXiv deferred to v1.2
- GSD active — no ad-hoc implementation without a plan
- Python canonical; browser demo tier
- Epidemic FSS (02-01): PC_INF=1/6, NU_THEORY=3.0, S≥N^{-1/3}, SEEDS_PER_N=20, BOND_SAMPLES_PER_MID=8, NU_TOLERANCE=0.15; CONFIRMED ν=3.1475 (4.9%); freeze mean_pcs in 02-01-SUMMARY (do not invent)
- Epidemic FSS (02-02): pytest pins freeze mean_pcs; CI greps RESULT: CONFIRMED; NU_THEORY asserted 3.0; no live MC in repo_smoke
- Epidemic FSS (02-03): YAML/README/Colab match volume nu_bar=3, S≥N^{-1/3}, p_c(inf)=1/6, SEEDS_PER_N=20, NU_TOLERANCE=0.15; status confirmed; habitat/cluster/Ising left executed
- Crosscheck scale-up (03-01): generate path is `python scripts/generate_crosscheck.py --bridge b-percolation-oncology --write`; drafts/crosscheck/ gitignored; promote is human copy (no CLI); `p-b-percolation-oncology-gcc` status ready, pollination_index 1, never confirmed
- Oncology GCC repro: L=32 TRIALS=8 stdlib lattice; always RESULT: INCONCLUSIVE and exit 0; no 5th CI CONFIRMED grep; epidemic NU_THEORY=3.0 untouched
- Crosscheck scale-up (03-02): Run-mode parity section in `docs/CROSSCHECK.md` (Python canonical; browser/Colab demo tier); generate command and `drafts/crosscheck/physics-oncology/` documented; CROSS-06/07 closed pending verify-work
- CI & trust hardening (planned 2026-08-26): TRUST-02 = pytest text inventory of CONFIRMED-capable `repro/**/*.py` vs four static `crosscheck-repro.yml` greps (not YAML `status`; never `yaml.safe_load`); GCC pytest-only INCONCLUSIVE; TRUST-03 = generate `--bridge b-percolation-oncology --dry-run` + live GCC smoke; epidemic freeze `NU_THEORY = 3.0` untouched; sequential 04-01 then 04-02
- CI & trust hardening (04-01): TRUST-02 closed — `test_crosscheck_confirmed_gates.py` pairs four CONFIRMED-capable seeds with four static greps; GCC not grepped CONFIRMED; `docs/CROSSCHECK.md` CONFIRMED-only policy; workflow YAML untouched
- CI & trust hardening (04-02): TRUST-03 closed — `test_crosscheck_entry_points.py` generate `--bridge b-percolation-oncology --dry-run` (exit 0, `p-b-`) plus live GCC `RESULT: INCONCLUSIVE` / exit 0; epidemic freeze re-run not duplicated; no fifth CONFIRMED grep

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
Stopped at: Phase 4 executed and orchestrator-verified (pytest 14/14, four CONFIRMED greps, NU_THEORY=3.0)
Resume file: None
Duration (04-01): 6 min · Duration (04-02): 2 min

Local note: previous checkout was stale `launch/june-2026-shipping`. June-pause catalog drafts (climate cascades + zeta) stashed as `june-2026-pause leftover launch docs and climate drafts`. Parked until after v1.1.

**Next command:** `/gsd-plan-phase 5`