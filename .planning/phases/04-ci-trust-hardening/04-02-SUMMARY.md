---
phase: 04-ci-trust-hardening
plan: 02
subsystem: testing
tags: [TRUST-03, repo_smoke, generate_crosscheck, GCC, INCONCLUSIVE]

requires:
  - phase: 04-ci-trust-hardening
    provides: TRUST-02 CONFIRMED-gate inventory (four static greps; GCC not grepped CONFIRMED)
provides:
  - repo_smoke generate_crosscheck.py --bridge b-percolation-oncology --dry-run (exit 0, p-b- on stdout)
  - repo_smoke live giant_component_fraction.py RESULT: INCONCLUSIVE / exit 0 / never CONFIRMED
  - Epidemic freeze NU_THEORY == 3.0 still closed by existing test_epidemic_fss_fit_confirmed_on_reference_pcs
affects: [TRUST-03, 04-ci-trust-hardening, Phase 5]

tech-stack:
  added: []
  patterns:
    - Entry-point smokes copy test_crosscheck_artifacts.py list-argv subprocess.run with stdout capture (never shell=True, never catalog _run_script)
    - generate argv is --bridge b-percolation-oncology --dry-run only; never --write or --all
    - GCC is pytest-only INCONCLUSIVE; never a fifth CONFIRMED grep

key-files:
  created:
    - tests/repo_smoke/test_crosscheck_entry_points.py
  modified:
    - CHANGELOG.md

key-decisions:
  - "TRUST-03 generate smoke is dry-run only (D-07); assert p-b- on stdout, not p-b-percolation-oncology-gcc"
  - "TRUST-03 GCC smoke runs the real stdlib script (D-08); RESULT: INCONCLUSIVE and exit 0; never CONFIRMED"
  - "Do not duplicate test_epidemic_fss_fit_confirmed_on_reference_pcs; re-run it (D-06)"
  - "Do not add GCC to crosscheck-repro.yml; keep four static CONFIRMED greps (D-03/D-09)"

patterns-established:
  - "subprocess.run([sys.executable, script, ...], cwd=REPO_ROOT, capture_output=True, text=True, check=False)"
  - "Generate dry-run must not dirty drafts/crosscheck/"
  - "INCONCLUSIVE-only repro is asserted as INCONCLUSIVE, never as CONFIRMED"

requirements-completed: [TRUST-03]

duration: 2min
completed: 2026-08-26
---

# Phase 4 Plan 02: repo_smoke expansion (TRUST-03) Summary

**Generate dry-run and live oncology GCC entry-point smokes in repo_smoke; epidemic freeze `NU_THEORY == 3.0` re-run, not duplicated**

## Performance

- **Duration:** 2 min
- **Started:** 2026-08-26T20:26:21Z
- **Completed:** 2026-08-26T20:28:30Z
- **Tasks:** 2
- **Files modified:** 2 (1 created, 1 modified; plus planning metadata)

## Accomplishments

- Added `tests/repo_smoke/test_crosscheck_entry_points.py`: `generate_crosscheck.py --bridge b-percolation-oncology --dry-run` exits 0 with `p-b-` on stdout (no `--write` / `--all`)
- Live `giant_component_fraction.py` subprocess asserts `RESULT: INCONCLUSIVE`, exit 0, and `RESULT: CONFIRMED` absent
- Re-ran existing `test_epidemic_fss_fit_confirmed_on_reference_pcs` (`NU_THEORY == 3.0`); that file was not edited
- CHANGELOG Unreleased names the entry-point smokes above the 04-01 inventory section
- Workflow YAML, generate script, GCC script, epidemic freeze, `docs/CROSSCHECK.md`, and hub HTML were not edited

## Task Commits

Each task was committed atomically:

1. **Task 1: Write generate dry-run and GCC INCONCLUSIVE entry-point smokes** - `3d5d98d` (test)
2. **Task 2: Add CHANGELOG Unreleased entry-point bullet** - `f920115` (docs)

**Plan metadata:** `docs(04-02): complete plan` (this commit)

## Files Created/Modified

- `tests/repo_smoke/test_crosscheck_entry_points.py` - TRUST-03 generate dry-run + live GCC INCONCLUSIVE smokes
- `CHANGELOG.md` - Unreleased entry-point smokes bullet (04-01 inventory left intact)

## Decisions Made

- Generate argv is `--bridge b-percolation-oncology --dry-run` only (D-07); assert `p-b-`, not the GCC protocol id
- GCC is pytest-only (D-08/D-09); list-argv subprocess of the real stdlib script; never `importlib` / `collect_pooled_sizes`
- Epidemic TRUST-03 coverage is the existing freeze test re-run, not a second freeze vector
- Four static `crosscheck-repro.yml` CONFIRMED greps stay; no GCC workflow step

## Deviations from Plan

None - plan executed exactly as written.

---

**Total deviations:** 0 auto-fixed
**Impact on plan:** None — entry-point pytest and changelog match the plan verbatim.

## Issues Encountered

- `gsd-sdk` is not on PATH and not in `node_modules`; STATE/ROADMAP/REQUIREMENTS updated by hand to match executor handlers (same as 04-01).
- PowerShell ate escaped quotes in a one-liner workflow `count`; grep was used instead (same four greps, no GCC path in the workflow).

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- TRUST-03 closed: generate dry-run and GCC INCONCLUSIVE smokes are picked up by `validate-schemas.yml` (`python -m pytest tests/repo_smoke -v`)
- Phase 4 plans 2/2 complete; ready for `/gsd-verify-work 4` then Phase 5 (HUB-01)
- Do not add a fifth CONFIRMED grep; do not retune `NU_THEORY`; do not `yaml.safe_load` the workflow

## Verification snippets

Entry-point + freeze pytest: `3 passed in 0.17s` (`test_generate_crosscheck_dry_run_oncology_prints_protocol_id`, `test_giant_component_fraction_prints_inconclusive_and_exits_0`, `test_epidemic_fss_fit_confirmed_on_reference_pcs`)

Wave command: `5 passed in 0.17s` (adds `test_crosscheck_confirmed_gates.py` 2 tests)

Workflow: exactly four `grep -q "RESULT: CONFIRMED"`; `giant_component_fraction.py` absent from `.github/workflows/crosscheck-repro.yml`

`docs/CROSSCHECK.md` unmodified by this plan.

No `shell=True` / `collect_pooled_sizes` / `spec_from_file_location` in the new test. No `--write` / `--all` in generate argv.

## Self-Check: PASSED

- FOUND: `tests/repo_smoke/test_crosscheck_entry_points.py`, `CHANGELOG.md`, `04-02-SUMMARY.md`
- FOUND: commits `3d5d98d`, `f920115`
- Re-ran entry-point + freeze pytest: 3 passed
- Re-ran wave command: 5 passed
- Re-ran plan verification: four `grep -q "RESULT: CONFIRMED"`; no `giant_component_fraction.py` in workflow; `docs/CROSSCHECK.md` unmodified
- TRUST-03 marked complete in REQUIREMENTS.md; 04-02 checked in ROADMAP.md

---
*Phase: 04-ci-trust-hardening*
*Completed: 2026-08-26*
