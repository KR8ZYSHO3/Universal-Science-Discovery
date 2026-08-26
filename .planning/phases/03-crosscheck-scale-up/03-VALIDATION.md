---
phase: 3
slug: crosscheck-scale-up
status: draft
nyquist_compliant: true
wave_0_complete: true
created: 2026-08-26
---

# Phase 3 — Validation Strategy

Existing pytest + `validate_schemas.py` + `build_crosscheck.py --check` cover Wave 0. No new test framework.

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

Filled after plans land. Expected coverage:

| Requirement | Automated |
|-------------|-----------|
| CROSS-06 generate | `generate_crosscheck.py --bridge b-percolation-oncology --dry-run` prints a protocol id |
| CROSS-06 promote | catalog YAML exists, `status: ready`, `validate_schemas.py` |
| CROSS-06 repro | script prints `RESULT:` and process returncode 0 |
| CROSS-07 | `docs/CROSSCHECK.md` contains all four seed protocol ids in a table |
| D-07 | epidemic `NU_THEORY = 3.0` unchanged |
| D-03 | `crosscheck-repro.yml` still has exactly four CONFIRMED grep jobs |

## Wave 0 Requirements

Existing infrastructure covers all phase requirements.

## Manual-Only Verifications

None required. Hosted Pages/Colab are optional after merge.

## Validation Sign-Off

- [ ] All tasks have `<automated>` verify
- [x] Wave 0 present
- [x] No watch-mode
- [ ] `nyquist_compliant: true` after plans land

**Approval:** pending
