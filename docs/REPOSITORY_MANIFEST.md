# Repository manifest

Exhaustive index of **tracked** paths (excluding `.git`), what each is for, and which guiding documents govern it. Use this when onboarding, auditing, or changing structure.

| Path | Kind | Purpose | Governing / related docs |
|------|------|---------|---------------------------|
| [README.md](../README.md) | Entry | Project hub, links to core docs | [VISION_AND_SCOPE.md](VISION_AND_SCOPE.md), [DOC_MAP.md](DOC_MAP.md) |
| [AGENTS.md](../AGENTS.md) | Policy | Instructions for AI assistants | All `docs/*.md` policy set; [DOC_MAP.md](DOC_MAP.md) |
| [CONTRIBUTING.md](../CONTRIBUTING.md) | Policy | Human contribution workflow | [COLLABORATION_AND_REVIEWS.md](COLLABORATION_AND_REVIEWS.md), [METHODOLOGY.md](METHODOLOGY.md) |
| [CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md) | Policy | Expected community behavior | [CONTRIBUTING.md](../CONTRIBUTING.md) |
| [SECURITY.md](../SECURITY.md) | Policy | Vulnerability reporting | Maintainer contact; ethics doc for sensitive data |
| [LICENSE](../LICENSE) | Legal | Default OSS license (MIT) | [LICENSING_NOTES.md](LICENSING_NOTES.md) |
| [.gitignore](../.gitignore) | Config | Files never committed | [ETHICS_REPRODUCIBILITY_AND_DATA.md](ETHICS_REPRODUCIBILITY_AND_DATA.md) |
| [.markdown-link-check.json](../.markdown-link-check.json) | Config | Link checker rules for CI/local | [OPERATING_RHYTHM.md](OPERATING_RHYTHM.md) |
| [mkdocs.yml](../mkdocs.yml) | Config | MkDocs Material site (sources under `docs/`) | [INTERFACE.md](../INTERFACE.md), [OPERATING_RHYTHM.md](OPERATING_RHYTHM.md), [README.md](../README.md) |
| [requirements-docs.txt](../requirements-docs.txt) | Config | MkDocs / Material dependencies | [mkdocs.yml](../mkdocs.yml) |
| [pyproject.toml](../pyproject.toml) | Config | Root pytest entry for `packages/ingest/tests` | [docs/DATA_PLAN.md](DATA_PLAN.md) |
| [requirements-ingest.txt](../requirements-ingest.txt) | Config | Deps for `usdr-ingest` CLI | [docs/DATA_PLAN.md](DATA_PLAN.md) |
| [.cursor/rules/science-discovery-core.mdc](../.cursor/rules/science-discovery-core.mdc) | Config | Cursor always-on rules | [AGENTS.md](../AGENTS.md), [DOC_MAP.md](DOC_MAP.md) |
| [.cursor/rules/agent-execution.mdc](../.cursor/rules/agent-execution.mdc) | Config | Cursor: prefer in-environment installs, tests, git | [AGENTS.md](../AGENTS.md) |
| [.cursor/rules/documentation-and-dashboard.mdc](../.cursor/rules/documentation-and-dashboard.mdc) | Config | Cursor: keep docs, CHANGELOG, STATE, `dashboard/` hub current; verify `http://localhost:8765/dashboard/` when hub changes | [AGENTS.md](../AGENTS.md), [docs/OPERATING_RHYTHM.md](OPERATING_RHYTHM.md), [docs/DEV_DASHBOARD.md](DEV_DASHBOARD.md) |
| [.github/dependabot.yml](../.github/dependabot.yml) | Config | Dependency update PRs (Actions) | [OPERATING_RHYTHM.md](OPERATING_RHYTHM.md) |
| [.github/workflows/markdown-link-check.yml](../.github/workflows/markdown-link-check.yml) | CI | Validates Markdown links | [CONTRIBUTING.md](../CONTRIBUTING.md), [OPERATING_RHYTHM.md](OPERATING_RHYTHM.md) |
| [.github/workflows/validate-schemas.yml](../.github/workflows/validate-schemas.yml) | CI | Validates hypothesis / unknown YAML against `schemas/` | [schemas/README.md](../schemas/README.md), [OPERATING_RHYTHM.md](OPERATING_RHYTHM.md) |
| [.github/workflows/mkdocs-build.yml](../.github/workflows/mkdocs-build.yml) | CI | Builds MkDocs site from `docs/` (`mkdocs build --strict`); uploads `site` artifact where configured | [INTERFACE.md](../INTERFACE.md), [OPERATING_RHYTHM.md](OPERATING_RHYTHM.md), [mkdocs.yml](../mkdocs.yml) |
| [.github/workflows/ingest-ci.yml](../.github/workflows/ingest-ci.yml) | CI | Pytest for `packages/ingest` | [docs/DATA_PLAN.md](DATA_PLAN.md), [LEGAL.md](../LEGAL.md) |
| [.github/workflows/mkdocs-gh-pages.yml](../.github/workflows/mkdocs-gh-pages.yml) | CI | On push to `main`: `mkdocs build --strict`, deploy `./site` to branch `gh-pages` (peaceiris/actions-gh-pages@v4). **Live:** `https://kr8zysho3.github.io/Universal-Science-Discovery/` after Pages source is `gh-pages` / root | [INTERFACE.md](../INTERFACE.md), [README.md](../README.md) |
| [.github/pull_request_template.md](../.github/pull_request_template.md) | Template | PR checklist | [METHODOLOGY.md](METHODOLOGY.md), [ETHICS_REPRODUCIBILITY_AND_DATA.md](ETHICS_REPRODUCIBILITY_AND_DATA.md) |
| [.github/ISSUE_TEMPLATE/config.yml](../.github/ISSUE_TEMPLATE/config.yml) | Template | Issue chooser config | — |
| [.github/ISSUE_TEMPLATE/bug_report.md](../.github/ISSUE_TEMPLATE/bug_report.md) | Template | Bugs / inaccuracies | [METHODOLOGY.md](METHODOLOGY.md) |
| [.github/ISSUE_TEMPLATE/feature_request.md](../.github/ISSUE_TEMPLATE/feature_request.md) | Template | Tooling / repo features | [VISION_AND_SCOPE.md](VISION_AND_SCOPE.md) |
| [.github/ISSUE_TEMPLATE/finding_review.md](../.github/ISSUE_TEMPLATE/finding_review.md) | Template | Finding proposals / reviews | [METHODOLOGY.md](METHODOLOGY.md) |
| [.github/ISSUE_TEMPLATE/methods_change.md](../.github/ISSUE_TEMPLATE/methods_change.md) | Template | Protocol / analysis changes | [METHODOLOGY.md](METHODOLOGY.md) |
| [.github/ISSUE_TEMPLATE/hypothesis_thread.md](../.github/ISSUE_TEMPLATE/hypothesis_thread.md) | Template | New or revised hypotheses | [VISION_AND_SCOPE.md](VISION_AND_SCOPE.md), [METHODOLOGY.md](METHODOLOGY.md) |
| [schemas/hypothesis.yaml](../schemas/hypothesis.yaml) | Schema | Hypothesis record shape | [schemas/README.md](../schemas/README.md) |
| [schemas/ingestion-envelope-1.0.0.json](../schemas/ingestion-envelope-1.0.0.json) | Schema | Metadata ingest JSONL envelope v1.0.0 | [docs/DATA_PLAN.md](DATA_PLAN.md), [packages/ingest/pyproject.toml](../packages/ingest/pyproject.toml) |
| [docs/DOC_MAP.md](DOC_MAP.md) | Policy | Doc → behavior traceability | All guiding docs |
| [docs/index.md](index.md) | Guide | MkDocs homepage for the `docs/` tree; links to repo root on GitHub | [README.md](../README.md), [INTERFACE.md](../INTERFACE.md), [mkdocs.yml](../mkdocs.yml) |
| [docs/ONBOARDING.md](ONBOARDING.md) | Guide | First-hour navigation | — |
| [docs/SOLVING_UNKNOWNS.md](SOLVING_UNKNOWNS.md) | Guide | Status ladder and evidence bar for resolving catalog unknowns | [DOC_MAP.md](DOC_MAP.md), [METHODOLOGY.md](METHODOLOGY.md); orphan checks via `scripts/build_graph.py --report-orphans` |
| [docs/BREAKTHROUGH_GAPS.md](BREAKTHROUGH_GAPS.md) | Guide | Breakthrough-gap steward checklist; ties to roadmap priorities | [breakthrough-gaps/README.md](../breakthrough-gaps/README.md), [ROADMAP.md](../ROADMAP.md) |
| [docs/HAPPY_PATH_FIRST_RECORDS.md](HAPPY_PATH_FIRST_RECORDS.md) | Guide | Stream A happy path: first unknown + hypothesis YAML → PR | [CONTRIBUTING.md](../CONTRIBUTING.md), [METHODOLOGY.md](METHODOLOGY.md), [LEGAL.md](../LEGAL.md), [schemas/unknown.yaml](../schemas/unknown.yaml), [schemas/hypothesis.yaml](../schemas/hypothesis.yaml) |
| [docs/GSD_INTEGRATION.md](GSD_INTEGRATION.md) | Guide | Optional GSD (get-shit-done / spec-driven) boundaries for maintainers | [METHODOLOGY.md](METHODOLOGY.md), [DATA_PLAN.md](DATA_PLAN.md), [LEGAL.md](../LEGAL.md), [DEV_DASHBOARD.md](DEV_DASHBOARD.md) |
| [docs/UAT_INGEST.md](UAT_INGEST.md) | Guide | Manual UAT for `usdr-ingest` CLI | [DATA_PLAN.md](DATA_PLAN.md), [LEGAL.md](../LEGAL.md), [packages/ingest/pyproject.toml](../packages/ingest/pyproject.toml) |
| [docs/examples/README.md](examples/README.md) | Guide | Checked-in synthetic ingest JSONL exemplar + regen notes | [DATA_PLAN.md](DATA_PLAN.md), [schemas/ingestion-envelope-1.0.0.json](../schemas/ingestion-envelope-1.0.0.json) |
| [docs/examples/arxiv-oai-metadata-sample.v1.jsonl](examples/arxiv-oai-metadata-sample.v1.jsonl) | Example data | Two envelope v1 rows (fixture-derived; not live OAI) | [docs/examples/README.md](examples/README.md), [LEGAL.md](../LEGAL.md) |
| [docs/REPOSITORY_MANIFEST.md](REPOSITORY_MANIFEST.md) | Index | This file | — |
| [docs/LABELS_AND_MILESTONES.md](LABELS_AND_MILESTONES.md) | Guide | GitHub labels / milestones | [COLLABORATION_AND_REVIEWS.md](COLLABORATION_AND_REVIEWS.md) |
| [docs/LICENSING_NOTES.md](LICENSING_NOTES.md) | Policy | Exceptions to default LICENSE | [LICENSE](../LICENSE) |
| [docs/VISION_AND_SCOPE.md](VISION_AND_SCOPE.md) | Policy | Mission, scope, terms | README, templates, AGENTS |
| [docs/METHODOLOGY.md](METHODOLOGY.md) | Policy | Evidence bar, workflows | Templates, prompts, PRs |
| [docs/ETHICS_REPRODUCIBILITY_AND_DATA.md](ETHICS_REPRODUCIBILITY_AND_DATA.md) | Policy | Data classes, integrity | `data/`, `.gitignore` |
| [docs/COLLABORATION_AND_REVIEWS.md](COLLABORATION_AND_REVIEWS.md) | Policy | Review norms, communication | CONTRIBUTING, labels doc |
| [docs/QUALITY_BAR.md](QUALITY_BAR.md) | Policy | Anti-sloppiness: CI + review lanes + def. of done | [METHODOLOGY.md](METHODOLOGY.md), [COLLABORATION_AND_REVIEWS.md](COLLABORATION_AND_REVIEWS.md), [HAPPY_PATH_FIRST_RECORDS.md](HAPPY_PATH_FIRST_RECORDS.md), [.github/workflows/validate-schemas.yml](../.github/workflows/validate-schemas.yml) |
| [docs/OPERATING_RHYTHM.md](OPERATING_RHYTHM.md) | Policy | Cadence, CI, tags, protection | Workflows, Dependabot |
| [docs/prompts/literature_synthesis.md](prompts/literature_synthesis.md) | Prompt | Literature discipline | [METHODOLOGY.md](METHODOLOGY.md) |
| [docs/prompts/hypothesis_comparison.md](prompts/hypothesis_comparison.md) | Prompt | Compare hypotheses | [METHODOLOGY.md](METHODOLOGY.md) |
| [docs/prompts/falsification_pass.md](prompts/falsification_pass.md) | Prompt | Red-team / falsification | [METHODOLOGY.md](METHODOLOGY.md) |
| [methods/README.md](../methods/README.md) | Guide | Protocols folder contract | [METHODOLOGY.md](METHODOLOGY.md) |
| [data/README.md](../data/README.md) | Guide | Data folder contract | [ETHICS_REPRODUCIBILITY_AND_DATA.md](ETHICS_REPRODUCIBILITY_AND_DATA.md) |
| [data/raw/.gitkeep](../data/raw/.gitkeep) | Placeholder | Preserve `raw/` in git | [data/README.md](../data/README.md) |
| [artifacts/README.md](../artifacts/README.md) | Guide | Outputs contract | [METHODOLOGY.md](METHODOLOGY.md) |
| [scripts/README.md](../scripts/README.md) | Guide | Automation contract | [METHODOLOGY.md](METHODOLOGY.md), [ETHICS_REPRODUCIBILITY_AND_DATA.md](ETHICS_REPRODUCIBILITY_AND_DATA.md) |
| [scripts/validate_schemas.py](../scripts/validate_schemas.py) | Tool | CI + local YAML validation | [schemas/README.md](../schemas/README.md) |
| [scripts/domain_matching.py](../scripts/domain_matching.py) | Library | Maps bridge/hypothesis discipline tags to `unknowns-catalog/` domains for dashboard pages | [schemas/bridge.yaml](../schemas/bridge.yaml), [dashboard/README.md](../dashboard/README.md) |
| [scripts/generate_domain_pages.py](../scripts/generate_domain_pages.py) | Tool | Writes `dashboard/domains/*.html` from catalog + bridge `fields` | [dashboard/README.md](../dashboard/README.md), `scripts/domain_matching.py` |
| [scripts/render_breakthrough_gaps_hub.py](../scripts/render_breakthrough_gaps_hub.py) | Tool | Injects Breakthrough Gaps card grid into `dashboard/index.html` from `breakthrough-gaps/bg-*.yaml` | [docs/BREAKTHROUGH_GAPS.md](BREAKTHROUGH_GAPS.md), `.github/workflows/build-graph.yml` |
| [scripts/verify_domain_pages.py](../scripts/verify_domain_pages.py) | Tool | CI regression: minimum bridge counts visible per domain | `.github/workflows/validate-schemas.yml` |
| [scripts/requirements-validate.txt](../scripts/requirements-validate.txt) | Config | Deps for `validate_schemas.py` | [scripts/README.md](../scripts/README.md) |
| [scripts/sync-dashboard-from-state.py](../scripts/sync-dashboard-from-state.py) | Tool | Rewrites Canvas snapshot from `.planning/STATE.md` | [docs/DEV_DASHBOARD.md](DEV_DASHBOARD.md) |
| [scripts/generate-ingest-example-jsonl.py](../scripts/generate-ingest-example-jsonl.py) | Tool | Regenerate `docs/examples/arxiv-oai-metadata-sample.v1.jsonl` from offline fixtures | [docs/examples/README.md](examples/README.md) |
| [packages/ingest/README.md](../packages/ingest/README.md) | Guide | `usdr-ingest` quickstart (install, CLI, tests) | [docs/DATA_PLAN.md](DATA_PLAN.md), [docs/UAT_INGEST.md](UAT_INGEST.md), [LEGAL.md](../LEGAL.md) |
| [packages/ingest/pyproject.toml](../packages/ingest/pyproject.toml) | Code | `usdr-ingest` — arXiv OAI-PMH metadata harvest (see `src/usdr_ingest/`; **no PDFs**) | [docs/DATA_PLAN.md](DATA_PLAN.md), [LEGAL.md](../LEGAL.md) |
| [disciplines/README.md](../disciplines/README.md) | Guide | Discipline tree contract | [VISION_AND_SCOPE.md](VISION_AND_SCOPE.md) |
| [disciplines/physics/README.md](../disciplines/physics/README.md) | Guide | Physics seed + catalog pointers | [METHODOLOGY.md](METHODOLOGY.md), [LEGAL.md](../LEGAL.md) |
| [disciplines/biology/README.md](../disciplines/biology/README.md) | Guide | Biology seed + catalog pointers | [METHODOLOGY.md](METHODOLOGY.md), [LEGAL.md](../LEGAL.md) |
| [disciplines/computer-science/README.md](../disciplines/computer-science/README.md) | Guide | CS / AI-for-science stub | [METHODOLOGY.md](METHODOLOGY.md), [AGENTS.md](../AGENTS.md) |
| [unknowns-catalog/high-priority/u-dark-matter-microphysics.yaml](../unknowns-catalog/high-priority/u-dark-matter-microphysics.yaml) | Content | Seed example unknown | [schemas/unknown.yaml](../schemas/unknown.yaml) |
| [unknowns-catalog/high-priority/u-aging-interventions-translatability.yaml](../unknowns-catalog/high-priority/u-aging-interventions-translatability.yaml) | Content | Seed example unknown | [schemas/unknown.yaml](../schemas/unknown.yaml) |
| [hypotheses/active/h-radio-axion-like-dm-constraints.yaml](../hypotheses/active/h-radio-axion-like-dm-constraints.yaml) | Content | Seed example hypothesis | [schemas/hypothesis.yaml](../schemas/hypothesis.yaml) |
| [hypotheses/active/h-conserved-metabolic-bottlenecks-longevity.yaml](../hypotheses/active/h-conserved-metabolic-bottlenecks-longevity.yaml) | Content | Seed example hypothesis | [schemas/hypothesis.yaml](../schemas/hypothesis.yaml) |
| [notebooks/README.md](../notebooks/README.md) | Guide | Exploratory analysis contract | [METHODOLOGY.md](METHODOLOGY.md) |
| [dashboard/index.html](../dashboard/index.html) | UI | Browser dashboard: founding-doc links + live `STATE`/`ROADMAP` via local server | [DEV_DASHBOARD.md](DEV_DASHBOARD.md), [DOC_MAP.md](DOC_MAP.md) |
| [dashboard/README.md](../dashboard/README.md) | Guide | How to run the HTML dashboard + regenerate `domains/` and breakthrough-gap cards | [DEV_DASHBOARD.md](DEV_DASHBOARD.md), [BREAKTHROUGH_GAPS.md](BREAKTHROUGH_GAPS.md) |

## Maintenance rule

When you add, rename, or remove a **policy-relevant** path, update this manifest and [DOC_MAP.md](DOC_MAP.md) in the same change.
