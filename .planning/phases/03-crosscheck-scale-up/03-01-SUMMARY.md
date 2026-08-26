---
phase: 03-crosscheck-scale-up
plan: 01
subsystem: crosscheck
tags: [generate_crosscheck, protocols-catalog, percolation, oncology, stdlib]

requires:
  - phase: 02-epidemic-fss-precision
    provides: RESULT stdout contract (exit 0 always) and epidemic NU_THEORY=3.0 freeze
provides:
  - Gitignored drafts/crosscheck/ staging for generate_crosscheck.py --write
  - Promoted p-b-percolation-oncology-gcc (status ready, pollination_index 1)
  - Thin stdlib giant_component_fraction.py printing RESULT: INCONCLUSIVE and exiting 0
affects: [03-02-parity-matrix, CROSS-06]

tech-stack:
  added: []
  patterns:
    - generate_crosscheck.py --bridge <id> --write then human copy into protocols-catalog
    - Drafts stay gitignored; validate_schemas.py is the catalog merge gate
    - New-bridge repro may print RESULT: INCONCLUSIVE with exit 0; never a 5th CI CONFIRMED grep

key-files:
  created:
    - protocols-catalog/physics-oncology/p-b-percolation-oncology-gcc.yaml
    - repro/p-b-percolation-oncology-gcc/giant_component_fraction.py
    - repro/p-b-percolation-oncology-gcc/README.md
    - repro/p-b-percolation-oncology-gcc/requirements.txt
  modified:
    - .gitignore

key-decisions:
  - "D-12: gitignore drafts/crosscheck/; do not commit generator TODO YAML"
  - "D-17: no promote CLI; human-filled catalog YAML is the path"
  - "D-13: promoted YAML status ready, never confirmed"
  - "D-04/D-14: L=32 TRIALS=8 stdlib lattice always prints RESULT: INCONCLUSIVE and returns 0"

patterns-established:
  - "Happy-path generate is --bridge <id> --write (not --all); promote is manual rename + fill TODOs"
  - "Catalog parent mirrors cross-domain parent (physics-oncology/)"
  - "Ising README honesty: Exit code 0 always; inspect stdout for CONFIRMED vs INCONCLUSIVE"

requirements-completed: [CROSS-06]

duration: 5min
completed: 2026-08-26
---

# Phase 3 Plan 01: Crosscheck generate/promote/repro Summary

**Repeatable bridge → generate_crosscheck.py --write → gitignored drafts → human-promoted `p-b-percolation-oncology-gcc` → stdlib L=32 GCC repro that prints RESULT: INCONCLUSIVE and exits 0**

## Performance

- **Duration:** 5 min
- **Started:** 2026-08-26T19:32:14Z
- **Completed:** 2026-08-26T19:37:00Z
- **Tasks:** 2
- **Files modified:** 5

## Accomplishments

- Ran `python scripts/generate_crosscheck.py --bridge b-percolation-oncology --write`; opportunity 1 landed at `drafts/crosscheck/physics-oncology/p-b-percolation-oncology-percolation-derived-metrics-giant-compon.yaml` (gitignored, untracked)
- Promoted opportunity 1 as `protocols-catalog/physics-oncology/p-b-percolation-oncology-gcc.yaml` with `status: ready`, `pollination_index: 1`, no TODO / `[DRAFT]` / `confirmed`; `validate_schemas.py` passed (5 crosscheck protocols)
- Shipped `repro/p-b-percolation-oncology-gcc/giant_component_fraction.py` (L=32, TRIALS=8, habitat `spans()` + cluster `UnionFind`); stdout `RESULT: INCONCLUSIVE`, exit 0; four CI CONFIRMED greps unchanged; epidemic `NU_THEORY = 3.0` untouched

## Task Commits

Each task was committed atomically:

1. **Task 1: Gitignore drafts, generate oncology drafts, promote opportunity 1 YAML** - `65caf76` (feat)
2. **Task 2: Add thin stdlib GCC repro that always prints INCONCLUSIVE and exits 0** - `0cf78dd` (feat)

**Plan metadata:** `docs(03-01): complete generate/promote/repro plan` (this commit)

## Files Created/Modified

- `.gitignore` - ignore `drafts/crosscheck/` after existing `drafts/wave_factory/`
- `protocols-catalog/physics-oncology/p-b-percolation-oncology-gcc.yaml` - promoted second-bridge protocol (status ready)
- `repro/p-b-percolation-oncology-gcc/giant_component_fraction.py` - thin stdlib lattice demo
- `repro/p-b-percolation-oncology-gcc/README.md` - run command + Ising-style exit-0 honesty
- `repro/p-b-percolation-oncology-gcc/requirements.txt` - comment-only, stdlib only

## Decisions Made

- Generate command is `--bridge b-percolation-oncology --write` (not `--all`); drafts stay local
- Promote is a human rewrite with id `p-b-percolation-oncology-gcc` and `pollination_index: 1`; no `scripts/promote_crosscheck.py`
- Quoted the experimental_design RESULT step so YAML does not parse `RESULT:` as a mapping (plan allowed wrapping of long strings)
- Repro is a pipeline demo, not a fifth CONFIRMED trophy; YAML status stays `ready` even after a local run

## Deviations from Plan

None - plan executed exactly as written.

Quoted one `experimental_design` string for valid YAML (allowed wrapping). No extra keys, no CI job, no JS, no generator pytest, epidemic freeze untouched.

---

**Total deviations:** 0 auto-fixed
**Impact on plan:** None

## Issues Encountered

None

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- CROSS-06 generate+promote+repro path exists for `b-percolation-oncology`
- 03-02 can document the generate command, add the parity matrix, and run `build_crosscheck.py --apply` (not done here)
- Do not add a 5th `RESULT: CONFIRMED` CI grep; do not set oncology YAML `confirmed`

## Verification snippets

Generator:

```
b-percolation-oncology  (3 opportunities)
  [1] p-b-percolation-oncology-percolation-derived-metrics-giant-compon  tier=desktop
      wrote: drafts\crosscheck\physics-oncology\p-b-percolation-oncology-percolation-derived-metrics-giant-compon.yaml
```

`validate_schemas.py`: `OK: all ... YAML files validate. (5 crosscheck protocols, ...)`

Repro stdout:

```
Crosscheck: p-b-percolation-oncology-gcc
L=32 TRIALS=8 SPAN_THRESHOLD=0.5
  p=0.40  span=0.000 (below 0.5)  giant=0.032
  p=0.50  span=0.000 (below 0.5)  giant=0.114
  p=0.59  span=0.125 (below 0.5)  giant=0.266
  p=0.70  span=1.000 (above 0.5)  giant=0.674
RESULT: INCONCLUSIVE (thin synthetic lattice; not a clinical biomarker; not an FSS precision pass)
```

Exit code 0. `git ls-files drafts/crosscheck` empty.

## Self-Check: PASSED

- FOUND: `.gitignore`, `protocols-catalog/physics-oncology/p-b-percolation-oncology-gcc.yaml`, `repro/p-b-percolation-oncology-gcc/{giant_component_fraction.py,README.md,requirements.txt}`, `03-01-SUMMARY.md`
- FOUND: commits `65caf76`, `0cf78dd`
- `git ls-files drafts/crosscheck` empty; no `scripts/promote_crosscheck.py`
- CROSS-06 marked complete in REQUIREMENTS.md

---
*Phase: 03-crosscheck-scale-up*
*Completed: 2026-08-26*
