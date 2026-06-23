# 01-02 Summary: Core Crosscheck pipeline robustness

**Completed:** 2026-06-22 (PRs #299, #300, #301)

## One-liner

`build_crosscheck.py` orchestrates artifact regen; CI `--check` drift gate; stale dashboard graph removed.

## Shipped

- `scripts/build_crosscheck.py` (`--apply` / `--check`)
- `tests/repo_smoke/test_crosscheck_artifacts.py`
- `tests/repo_smoke/test_crosscheck_repro_regression.py` (initial)
- `build-graph.yml` runs crosscheck regen on catalog changes
- Deleted stale `dashboard/knowledge_graph.json`

## Verification

- `pytest tests/repo_smoke` — 8 tests (pre cluster regression)
- `verify_dashboard_consistency.py` fails if stale graph reappears