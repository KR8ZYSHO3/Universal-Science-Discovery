---
phase: 3
slug: crosscheck-scale-up
status: approved
nyquist_compliant: true
wave_0_complete: true
created: 2026-08-26
---

# Phase 3 — Validation Strategy

Existing pytest + `validate_schemas.py` + `build_crosscheck.py --check` cover Wave 0.

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | pytest + schema validator |
| **Quick run command** | `python scripts/validate_schemas.py` |
| **Full suite command** | `python -m pytest tests/repo_smoke -q` ; `python scripts/build_crosscheck.py --check` |
| **Estimated runtime** | seconds (no live NetworkX sweep) |

## Sampling Rate

- After every task: that task's `<automated>` command
- After each wave: `python scripts/validate_schemas.py`
- Before verify-work: repo_smoke + `--check`

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Automated Command | File Exists |
|---------|------|------|-------------|-------------------|-------------|
| 03-01-01 | 01 | 1 | CROSS-06 | `validate_schemas.py` + assert generator draft path exists + catalog YAML `status: ready` | ✅ |
| 03-01-02 | 01 | 1 | CROSS-06 | run `giant_component_fraction.py`; assert `RESULT: INCONCLUSIVE` and exit 0; four CI greps; `NU_THEORY = 3.0` | ✅ |
| 03-02-01 | 02 | 2 | CROSS-07 | `docs/CROSSCHECK.md` asserts generate command + four seed ids + GCC id | ✅ |
| 03-02-02 | 02 | 2 | CROSS-07 | `build_crosscheck.py --check`; `validate_schemas.py`; `mkdocs build --strict`; hub/index honesty | ✅ |

## Wave 0 Requirements

Existing infrastructure covers all phase requirements.

## Manual-Only Verifications

None required.

## Validation Sign-Off

- [x] All tasks have `<automated>` verify
- [x] Sampling continuity
- [x] Wave 0 present
- [x] No watch-mode
- [x] `nyquist_compliant: true`

**Approval:** 2026-08-26 (post checker; 0 blockers)
