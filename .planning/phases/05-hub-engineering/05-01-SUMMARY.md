---
phase: 05-hub-engineering
plan: 01
subsystem: ui
tags: [HUB-01, recommendations, undirected_degree, contributor-hub, static-json]

requires:
  - phase: 04-ci-trust-hardening
    provides: TRUST-02/03 closed; epidemic freeze and Crosscheck CI untouched
provides:
  - docs/HUB_RECOMMENDATIONS.md ranking spec (connectivity / harvest / curator)
  - scripts/export_recommendations.py → api/v1/recommendations.json (≤25 bridges, undirected_degree)
  - dashboard/index.html #recommendations fetch table (textContent, github.com href allowlist)
  - generate_api.py endpoints.recommendations + build-graph.yml export step + test_recommendations_json
affects: [HUB-01, 05-hub-engineering, contributor-hub]

tech-stack:
  added: []
  patterns:
    - Static panel exporter: Python stdlib → committed api/v1 JSON → hub IIFE fetch
    - Degree ranking copies build_graph.top_nodes_by_degree increment; filter type==bridge; sort (-score, id); cap 25
    - Hub titles via textContent/createElement; a.href only if url.indexOf('https://github.com/') === 0

key-files:
  created:
    - docs/HUB_RECOMMENDATIONS.md
    - scripts/export_recommendations.py
    - api/v1/recommendations.json
  modified:
    - mkdocs.yml
    - scripts/generate_api.py
    - api/v1/meta.json
    - .github/workflows/build-graph.yml
    - tests/repo_smoke/test_catalog_regression.py
    - dashboard/index.html
    - docs/DEV_DASHBOARD.md
    - CHANGELOG.md
    - dashboard/README.md
    - docs/DOC_MAP.md
    - docs/REPOSITORY_MANIFEST.md
    - scripts/README.md
    - .planning/STATE.md

key-decisions:
  - "v1 ranking is unweighted undirected degree of bridges from docs/knowledge_graph.json; do not call top_nodes_by_degree(n=25)"
  - "Omit harvest_rank and curator_score keys on JSON items (specify in docs only)"
  - "Hub #recommendations immediately after #orphan-xref-panel; never innerHTML for titles"
  - "Register endpoints.recommendations in generate_api.py so the next generate_api.py run keeps meta.json"

patterns-established:
  - "Clone orphan/xref panel: exporter → committed JSON → hub table/empty/aria-live status"
  - "Honesty copy: contributor tooling, not a scientific ranking, not a CONFIRMED/INCONCLUSIVE Crosscheck outcome"
  - "mkdocs.yml must list new docs/ files or --strict fails"

requirements-completed: [HUB-01]

duration: 6min
completed: 2026-08-26
---

# Phase 5 Plan 01: Hub recommendations spec + thin JSON slice Summary

**HUB-01 ranking spec (connectivity / harvest / curator) plus committed `api/v1/recommendations.json` fetched by hub `#recommendations` as undirected-degree contributor tooling**

## Performance

- **Duration:** 6 min
- **Started:** 2026-08-26T22:22:17Z
- **Completed:** 2026-08-26T22:28:28Z
- **Tasks:** 3
- **Files modified:** 16 (3 created, 13 modified; plus this SUMMARY and ROADMAP/REQUIREMENTS metadata)

## Accomplishments

- Wrote `docs/HUB_RECOMMENDATIONS.md`: three ranking signals; prototype computes `undirected_degree` only; harvest/curator specified and omitted on items
- Exporter ranks bridges from `docs/knowledge_graph.json` (same degree increment as `top_nodes_by_degree`; filter `type=="bridge"`; sort `(-score, id)`; cap 25); committed JSON + `test_recommendations_json`
- Hub `#recommendations` table fetch uses `textContent` and github.com href allowlist; playbook/CHANGELOG/DOC_MAP/manifest/READMEs updated
- `generate_api.py` registers `endpoints.recommendations`; `build-graph.yml` runs the exporter after orphan export

## Task Commits

Each task was committed atomically:

1. **Task 1: Write HUB_RECOMMENDATIONS spec and add mkdocs nav** - `ecf214a` (docs)
2. **Task 2: Export recommendations JSON, register API endpoint, add smoke** - `b06ab41` (feat)
3. **Task 3: Wire #recommendations hub panel and playbook docs** - `0c3b474` (feat)

**Plan metadata:** `docs(05-01): complete plan` (this commit)

## Files Created/Modified

- `docs/HUB_RECOMMENDATIONS.md` — ranking spec (connectivity / harvest / curator)
- `mkdocs.yml` — Operations nav after Dev dashboard
- `scripts/export_recommendations.py` — stdlib writer for `api/v1/recommendations.json`
- `api/v1/recommendations.json` — committed prototype (≤25 bridges)
- `scripts/generate_api.py` / `api/v1/meta.json` — `endpoints.recommendations`
- `.github/workflows/build-graph.yml` — export step after orphan panel
- `tests/repo_smoke/test_catalog_regression.py` — `test_recommendations_json`
- `dashboard/index.html` — `#recommendations` CSS/HTML/IIFE/nav/API row
- `docs/DEV_DASHBOARD.md` — Phase C stub promoted; playbook + catalog-batch command
- `CHANGELOG.md`, `dashboard/README.md`, `docs/DOC_MAP.md`, `docs/REPOSITORY_MANIFEST.md`, `scripts/README.md`, `.planning/STATE.md`

## Decisions Made

None beyond the plan — followed 05-01-PLAN.md as specified (unweighted undirected degree; omit harvest/curator keys; dedicated spec file; table not cards).

## Deviations from Plan

None - plan executed exactly as written.

Allowed extras already in the plan: related-docs links on the spec page; `sync-dashboard-from-state.py` after STATE.md (cursor documentation-and-dashboard rule; canvas content unchanged vs git). Reverted unrelated `api/v1/citations.json` `generated` date churn from `generate_api.py`.

---

**Total deviations:** 0 auto-fixed
**Impact on plan:** None. Scope stayed on HUB-01 thin slice.

## Issues Encountered

None

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- Phase 5 is the last v1.1 GSD phase; HUB-01 closed. Ready for `/gsd-verify-work 5` then milestone complete.
- Harvest rank and curator score remain specified, not computed (deferred; not blockers).
- Local sanity (not a checkpoint): `python -m http.server 8765` → `http://localhost:8765/dashboard/#recommendations`.

## Known Stubs

Harvest rank and curator score are **intentionally omitted** on JSON items (`docs/HUB_RECOMMENDATIONS.md`). Not UI placeholders; v1 computes connectivity only.

## Verification (re-run at self-check)

- All task `<acceptance_criteria>`: PASS (48/48)
- `mkdocs build --strict`: PASS
- `python scripts/export_recommendations.py`: PASS (25 items; restored committed `generated_at` after re-run)
- `python -m pytest tests/repo_smoke/test_catalog_regression.py::test_recommendations_json -q`: PASS
- `python scripts/verify_dashboard_consistency.py`: PASS (bridges=1124, unknowns=1409, hypotheses=1275, phenomena=11, graph_nodes=3861, graph_edges=4522)
- `#recommendations` IIFE: `textContent` only; `indexOf('https://github.com/') === 0`; does not fetch `graph.json`
- No `repro/**`, epidemic, or `crosscheck-repro.yml` diffs; `build_crosscheck.py --apply` was not run

## Self-Check: PASSED

- FOUND: `docs/HUB_RECOMMENDATIONS.md`
- FOUND: `scripts/export_recommendations.py`
- FOUND: `api/v1/recommendations.json`
- FOUND: commit `ecf214a`
- FOUND: commit `b06ab41`
- FOUND: commit `0c3b474`

---
*Phase: 05-hub-engineering*
*Completed: 2026-08-26*
