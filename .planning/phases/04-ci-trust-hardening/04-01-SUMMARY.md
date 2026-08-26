---
phase: 04-ci-trust-hardening
plan: 01
subsystem: testing
tags: [TRUST-02, CONFIRMED-gates, repo_smoke, crosscheck-repro, inventory]

requires:
  - phase: 03-crosscheck-scale-up
    provides: Four live tee+grep CONFIRMED steps in crosscheck-repro.yml plus INCONCLUSIVE GCC repro
provides:
  - Fail-closed pytest inventory pairing CONFIRMED-capable repro/**/*.py with crosscheck-repro.yml greps
  - Negative assertion that giant_component_fraction.py is not grepped CONFIRMED
  - docs/CROSSCHECK.md CONFIRMED-only grep policy (GCC CI column **no**, no Phase 4 TRUST-02 TODO)
affects: [TRUST-02, 04-02, TRUST-03]

tech-stack:
  added: []
  patterns:
    - TRUST-02 inventory is UTF-8 text parse of crosscheck-repro.yml split on "- name:" (never yaml.safe_load)
    - Source of truth is stdout RESULT markers in repro/**/*.py, not YAML status
    - Four static tee+grep steps stay; inventory fails CI if a fifth CONFIRMED-capable script is ungated

key-files:
  created:
    - tests/repo_smoke/test_crosscheck_confirmed_gates.py
  modified:
    - docs/CROSSCHECK.md
    - CHANGELOG.md

key-decisions:
  - "TRUST-02 is a pytest text inventory, not an Actions matrix or scripts/ helper"
  - "Do not yaml.safe_load the workflow (PyYAML 1.1 on: -> True)"
  - "GCC CI cell is **no** with CONFIRMED-only policy; not a Phase 4 TRUST-02 TODO"

patterns-established:
  - "CONFIRMED-capable markers: 'CONFIRMED' if / result = \"CONFIRMED\" / RESULT: CONFIRMED"
  - "workflow.count of grep -q RESULT: CONFIRMED must equal discovered CONFIRMED-capable count"
  - "INCONCLUSIVE-only repro scripts must not share a step with a CONFIRMED grep"

requirements-completed: [TRUST-02]

duration: 6min
completed: 2026-08-26
---

# Phase 4 Plan 01: Unified CONFIRMED gates in CI Summary

**Fail-closed repo_smoke inventory maps CONFIRMED-capable `repro/**/*.py` stdout markers to the four static `crosscheck-repro.yml` greps; GCC stays INCONCLUSIVE and is not grepped CONFIRMED**

## Performance

- **Duration:** 6 min
- **Started:** 2026-08-26T16:19:39Z
- **Completed:** 2026-08-26T16:25:39Z
- **Tasks:** 3
- **Files modified:** 3 (1 created, 2 modified; plus planning metadata)

## Accomplishments

- Added `tests/repo_smoke/test_crosscheck_confirmed_gates.py`: discovers CONFIRMED-capable scripts via source markers, pairs POSIX paths with workflow steps that contain `grep -q "RESULT: CONFIRMED"`, asserts grep count equals discovered count (4 today)
- Negative test: INCONCLUSIVE-only `giant_component_fraction.py` must not share a CONFIRMED grep step
- Rewrote `docs/CROSSCHECK.md` Run-mode parity GCC CI cell from `**no** (Phase 4 TRUST-02)` to `**no**` plus a CONFIRMED-only grep policy paragraph
- CHANGELOG Unreleased names the inventory pytest and the docs policy; generate/promote Unreleased block left intact
- Workflow YAML, epidemic freeze, generate script, GCC script, and hub HTML were not edited

## Task Commits

Each task was committed atomically:

1. **Task 1: Write CONFIRMED-gate inventory pytest (TRUST-02)** - `48f4273` (test)
2. **Task 2: Rewrite CROSSCHECK.md CI column to CONFIRMED-only policy** - `553b78c` (docs)
3. **Task 3: Add CHANGELOG Unreleased inventory bullet** - `8d11bdb` (docs)

**Plan metadata:** `docs(04-01): complete plan` (this commit)

## Files Created/Modified

- `tests/repo_smoke/test_crosscheck_confirmed_gates.py` - TRUST-02 text inventory + negative GCC assertion
- `docs/CROSSCHECK.md` - CONFIRMED-only grep policy; GCC CI column stays **no**
- `CHANGELOG.md` - Unreleased inventory + policy bullet

## Decisions Made

- Inventory mechanism is pytest text parse (D-04 discretion lock): no Actions matrix, no `scripts/check_crosscheck_gates.py`, no `repro/CONFIRMED_GATES.yml`
- Do not `yaml.safe_load` `.github/workflows/crosscheck-repro.yml` (PyYAML 1.1 coerces top-level `on:` to `True`)
- GCC is pytest-only for entry-point coverage (04-02); 04-01 only asserts it is not grepped CONFIRMED
- Docs-only CROSSCHECK.md edit: hub already links `#run-mode-parity`; no `build_crosscheck.py --apply`

## Deviations from Plan

None - plan executed exactly as written.

---

**Total deviations:** 0 auto-fixed
**Impact on plan:** None — inventory pytest, docs policy, and changelog match the plan verbatim.

## Issues Encountered

- `gsd-sdk` is not on PATH and not in `node_modules`; STATE/ROADMAP/REQUIREMENTS updated by hand to match executor handlers (same as 03-02).
- PowerShell ate escaped quotes in a one-liner `workflow.count` assert; grep + pytest were used instead (same four greps, no GCC path in the workflow).

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- TRUST-02 closed: four CONFIRMED-capable seeds ↔ four live greps; a future CONFIRMED-stdout script will fail `validate-schemas.yml` until a matching grep step is added
- Ready for 04-02 (TRUST-03): generate `--bridge b-percolation-oncology --dry-run` smoke + live GCC `RESULT: INCONCLUSIVE` / exit 0; do not edit `docs/CROSSCHECK.md`; do not duplicate epidemic freeze
- Do not add a fifth CONFIRMED grep; do not retune `NU_THEORY`; do not `yaml.safe_load` the workflow

## Verification snippets

Inventory pytest: `2 passed in 0.02s` (`test_confirmed_capable_repro_scripts_are_grepped_in_crosscheck_repro_workflow`, `test_inconclusive_only_scripts_are_not_grepped_confirmed`)

Workflow: exactly four `grep -q "RESULT: CONFIRMED"`; `giant_component_fraction.py` absent from `.github/workflows/crosscheck-repro.yml`

`docs/CROSSCHECK.md`: CONFIRMED-only grep policy present; `(Phase 4 TRUST-02)` absent; four seed ids remain; GCC CI cell `**no**`

`mkdocs build --strict`: Documentation built (exit 0)

`scripts/check_crosscheck_gates.py` does not exist. No `import yaml` / `yaml.safe_load` / `shell=True` / `strategy.matrix` in inventory code.

## Self-Check: PASSED

- FOUND: `tests/repo_smoke/test_crosscheck_confirmed_gates.py`, `docs/CROSSCHECK.md`, `CHANGELOG.md`, `04-01-SUMMARY.md`
- FOUND: commits `48f4273`, `553b78c`, `8d11bdb`
- Re-ran inventory pytest: 2 passed
- Re-ran plan verification: four `grep -q "RESULT: CONFIRMED"`; no `giant_component_fraction.py` in workflow; CROSSCHECK.md has CONFIRMED-only policy and no `(Phase 4 TRUST-02)`; `mkdocs build --strict` exit 0
- TRUST-02 marked complete in REQUIREMENTS.md; 04-01 checked in ROADMAP.md

---
*Phase: 04-ci-trust-hardening*
*Completed: 2026-08-26*
