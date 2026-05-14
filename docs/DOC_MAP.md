# Guiding documents → repository behaviors

This map is the project traceability layer (delivered as part of **Phase 0 — Foundation**, now complete). When you change a guiding document, update the corresponding behaviors (rules, templates, or this map) in the same change.

**Last updated:** 2026-05-14 — **DEV_DASHBOARD.md** documents implemented hub Phase A (catalog search → graph focus → GitHub blob/raw); **`dashboard/index.html`** wires D3 zoom-to-node + GitHub deep links. Earlier: **CONTRIBUTING.md** local checks; **bug / feature** issue templates; **`tests/repo_smoke`** + **`validate-schemas.yml`**; **`OPERATING_RHYTHM.md`** dual-workflow notes; breakthrough gaps hub; roadmap § audit backlog; **repo audit:** [May 2026 full audit report](../.planning/reports/USDR_FULL_AUDIT_2026-05.md).

## Policy documents

| Guiding document | What it governs | Concrete behaviors |
|------------------|-----------------|----------------------|
| [VISION_AND_SCOPE.md](VISION_AND_SCOPE.md) | Mission, boundaries, what belongs in-repo | README framing; issue labels; scope checks in AGENTS and Cursor rules |
| [METHODOLOGY.md](METHODOLOGY.md) | Claims vs hypotheses, evidence bars, workflows | PR template checklist; **`bug_report.yml`** / **`feature_request.md`** (local checks → **CONTRIBUTING.md**); `finding_review` and `hypothesis_thread` issue templates; prompt templates in [prompts/](prompts/) |
| [ETHICS_REPRODUCIBILITY_AND_DATA.md](ETHICS_REPRODUCIBILITY_AND_DATA.md) | Data classes, privacy, reproducibility | `.gitignore`; [data/README.md](../data/README.md); no raw restricted data in git |
| [SOLVING_UNKNOWNS.md](SOLVING_UNKNOWNS.md) | How an unknown moves from open → partial → resolved | Hypothesis evidence links; status updates; graph orphan checks via `build_graph.py --report-orphans` |
| [QUALITY_BAR.md](QUALITY_BAR.md) | Explicit quality / anti-sloppiness playbook | CI gates; review lanes; def. of done; links [METHODOLOGY.md](METHODOLOGY.md), [COLLABORATION_AND_REVIEWS.md](COLLABORATION_AND_REVIEWS.md), [HAPPY_PATH_FIRST_RECORDS.md](HAPPY_PATH_FIRST_RECORDS.md) |
| [COLLABORATION_AND_REVIEWS.md](COLLABORATION_AND_REVIEWS.md) | Contributions, review expectations | [CONTRIBUTING.md](../CONTRIBUTING.md) (local checks, PR branch naming, `good first issue` path); [`.github/pull_request_template.md`](../.github/pull_request_template.md); [`.github/ISSUE_TEMPLATE/bug_report.yml`](../.github/ISSUE_TEMPLATE/bug_report.yml) + [`.github/ISSUE_TEMPLATE/feature_request.md`](../.github/ISSUE_TEMPLATE/feature_request.md); branch protection notes in [OPERATING_RHYTHM.md](OPERATING_RHYTHM.md) |
| [OPERATING_RHYTHM.md](OPERATING_RHYTHM.md) | Cadence, versioning, when to sync rules/CI; milestone doc + contributor hub | Doc/CI updates; release/tag policy; CHANGELOG, `dashboard/index.html`, `http://localhost:8765/dashboard/` check per `.cursor/rules/documentation-and-dashboard.mdc` |
| [REPOSITORY_MANIFEST.md](REPOSITORY_MANIFEST.md) | Per-path roles and governing docs | Keeping structure auditable; updates when paths change |
| [ONBOARDING.md](ONBOARDING.md) | First-hour navigation | Points to all core policies and work directories |
| [HAPPY_PATH_FIRST_RECORDS.md](HAPPY_PATH_FIRST_RECORDS.md) | Stream A: first unknown + hypothesis YAML → PR | [CONTRIBUTING.md](../CONTRIBUTING.md); [schemas/README.md](../schemas/README.md); [templates/README.md](../templates/README.md); CI validates via `scripts/validate_schemas.py` |
| [LABELS_AND_MILESTONES.md](LABELS_AND_MILESTONES.md) | GitHub triage vocabulary | Aligns with [COLLABORATION_AND_REVIEWS.md](COLLABORATION_AND_REVIEWS.md); issue templates |
| [LICENSING_NOTES.md](LICENSING_NOTES.md) | Exceptions to default MIT | Per-file or per-artifact license metadata |
| [CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md) | Community behavior | [CONTRIBUTING.md](../CONTRIBUTING.md); enforcement expectations |
| [SECURITY.md](../SECURITY.md) | Private vulnerability / sensitive data reports | Automation and secrets; not scientific debate |
| [DATA_PLAN.md](DATA_PLAN.md) | Phase A external metadata pilot; envelope schema | Must stay consistent with [ARCHITECTURE.md](../ARCHITECTURE.md) ingestion section and [LEGAL.md](../LEGAL.md) before Phase B jobs land |
| [examples/README.md](examples/README.md) | Checked-in **synthetic** ingest JSONL exemplar + regen note | Traceable to [DATA_PLAN.md](DATA_PLAN.md) stretch item; rows validated in `packages/ingest/tests/test_envelope_schema.py` |
| [UAT_INGEST.md](UAT_INGEST.md) | Manual acceptance checks for `usdr-ingest` | Implements [DATA_PLAN.md](DATA_PLAN.md) QA; automated checks in `packages/ingest/tests` |
| [DEV_DASHBOARD.md](DEV_DASHBOARD.md) | Meta checklist: active branches, shipped items, blockers; **Phase A** hub flow (catalog search → D3 graph focus/highlight → GitHub blob/raw for catalog YAML) | Edits [.planning/STATE.md](../.planning/STATE.md); optional sync to Canvas via `scripts/sync-dashboard-from-state.py`; [HTML dashboard](../dashboard/index.html) + [dashboard/README.md](../dashboard/README.md) for browser use |
| [GSD_INTEGRATION.md](GSD_INTEGRATION.md) | Optional get-shit-done / spec-driven workflows in Cursor | Boundaries vs [METHODOLOGY.md](METHODOLOGY.md), [DATA_PLAN.md](DATA_PLAN.md), [LEGAL.md](../LEGAL.md); does not replace contributor onboarding |
| [PATH_TO_SUCCESS.md](PATH_TO_SUCCESS.md) | Strategic roadmap: discoverability, community growth, long-term sustainability | arXiv preprint submission; outreach; custom domain; external contributor recruitment |
| [BREAKTHROUGH_GAPS.md](BREAKTHROUGH_GAPS.md) | Stewardship + phase-plan tie-in for `breakthrough-gaps/bg-*.yaml` | `render_breakthrough_gaps_hub.py`; `generate_api.py`; `schemas/breakthrough_gap.yaml`; [ROADMAP.md](../ROADMAP.md) integrated priorities |
| [CODE_AUDIT.md](CODE_AUDIT.md) | Python script audit findings and fix history | Script quality standards; HIGH severity issues fixed; MEDIUM/LOW backlog |

## Catalog types and schemas

| Catalog | Directory | Schema | Purpose |
|---------|-----------|--------|---------|
| Bridges | `cross-domain/` | `schemas/bridge.yaml` | Mathematical/conceptual links between disciplines; must have translation table, status, and DOI references |
| Unknowns | `unknowns-catalog/` | `schemas/unknown.yaml` | Named research gaps organized by domain |
| Hypotheses | `hypotheses/` | `schemas/hypothesis.yaml` | Testable, falsifiable hypotheses linked to unknowns |
| Pioneers | `pioneers/` | `schemas/pioneer.yaml` | Profiles of researchers who seed cross-domain bridges |
| Breakthrough Gaps | `breakthrough-gaps/` | `schemas/breakthrough_gap.yaml` | High-impact cross-domain problems whose solution would reshape science |
| Pre-formal Observations | `phenomenology/` | `schemas/phenomenon.yaml` | Raw observations not yet triaged to an unknown |

## Scripts and their purposes

| Script | Purpose | CI? |
|--------|---------|-----|
| `scripts/validate_schemas.py` | Validate all catalog YAML against JSON Schema | ✅ (`validate-schemas.yml` via **`pytest tests/repo_smoke`**; also **`validate.yml`** on path-filtered PRs) |
| `scripts/build_graph.py` | Build `docs/knowledge_graph.json` | ✅ (build-graph.yml) |
| `scripts/generate_api.py` | Generate static JSON API under `api/v1/` | ✅ (build-graph.yml) |
| `scripts/update_dashboard_stats.py` | Patch stat counters, hero **catalog snapshot** spans (`snap-*`, between `DASHBOARD_CATALOG_SNAPSHOT_*` markers), social meta, API blurbs, and graph placeholders in `dashboard/index.html` (reads `docs/knowledge_graph.json` meta for nodes/edges, with array-length fallback) | ✅ (build-graph.yml) |
| `scripts/verify_dashboard_consistency.py` | Fail CI if `snap-*` / key `stat-*` / hero pill counts disagree with YAML catalog + `docs/knowledge_graph.json` | ✅ (validate-schemas.yml) |
| `scripts/generate_domain_pages.py` | Per-domain HTML pages under `dashboard/domains/` | ✅ (pages.yml) |
| `scripts/generate_explainers.py` | Bridge explainer HTML pages under `dashboard/explainers/` | ✅ (pages.yml) |
| `scripts/propose_bridges.py` | Propose novel bridge candidates | Manual |
| `scripts/find_orphan_unknowns.py` | List unknowns with no graph connections | Manual |
| `scripts/audit_quality.py` | Flag low-quality catalog entries | Manual |
| `scripts/build_citation_index.py` | Extract and rank cross-referenced papers | Manual |

## Planning / audit artifacts

| Artifact | Purpose |
|----------|---------|
| [May 2026 full audit report](../.planning/reports/USDR_FULL_AUDIT_2026-05.md) | Periodic full-repo audit (inventory, drift, prioritized backlog); drives **ROADMAP.md** § Audit backlog |

## GitHub Actions workflows

| Workflow | Trigger | What it does |
|----------|---------|--------------|
| `.github/workflows/validate.yml` | PR to `main` (catalog-related paths only) | Runs `validate_schemas.py` + **`audit_quality.py`** + uploads quality report artifact |
| `.github/workflows/validate-schemas.yml` | Push / PR to `main` | **`pytest tests/repo_smoke`** — `validate_schemas.py`, `verify_domain_pages.py`, `verify_dashboard_consistency.py`, `build_graph.py --report-orphans` |
| `.github/workflows/build-graph.yml` | Catalog YAML push to `main`, or **Actions → manual run** | Rebuilds knowledge graph, generates API, updates dashboard stats; opens or updates PR **`bot/auto-knowledge-graph-rebuild`** when artifacts drift (branch protection blocks bot push to `main`) |
| `.github/workflows/pages.yml` | Push to `main` (paths: `dashboard/**`, `docs/**`, this workflow) | Deploys site artifact to GitHub Pages; generates **`dashboard/deploy-info.json`** at deploy time so the hub can show whether the hosted build matches **`main`** |

## Supporting files (see manifest)

Configuration and templates (`.github/`, `.cursor/`, `.markdown-link-check.json`, root `LICENSE`, `.gitignore`) are indexed in [REPOSITORY_MANIFEST.md](REPOSITORY_MANIFEST.md) so every tracked path maps to policy.

## Gaps flagged for maintainer decision

- **License interaction:** Repository default is MIT ([LICENSE](../LICENSE)). Record per-artifact exceptions in [LICENSING_NOTES.md](LICENSING_NOTES.md) when you introduce them.
- **Human subjects / regulated research:** If work involves human subjects, HIPAA, or export-controlled data, add a mandatory compliance appendix and legal review before committing study protocols or data paths.
- **Branch protection:** GitHub branch protection is configured in repository settings, not in git. See [OPERATING_RHYTHM.md](OPERATING_RHYTHM.md).
