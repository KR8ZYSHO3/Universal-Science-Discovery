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
| [.cursor/rules/science-discovery-core.mdc](../.cursor/rules/science-discovery-core.mdc) | Config | Cursor always-on rules | [AGENTS.md](../AGENTS.md), [DOC_MAP.md](DOC_MAP.md) |
| [.github/dependabot.yml](../.github/dependabot.yml) | Config | Dependency update PRs (Actions) | [OPERATING_RHYTHM.md](OPERATING_RHYTHM.md) |
| [.github/workflows/markdown-link-check.yml](../.github/workflows/markdown-link-check.yml) | CI | Validates Markdown links | [CONTRIBUTING.md](../CONTRIBUTING.md), [OPERATING_RHYTHM.md](OPERATING_RHYTHM.md) |
| [.github/pull_request_template.md](../.github/pull_request_template.md) | Template | PR checklist | [METHODOLOGY.md](METHODOLOGY.md), [ETHICS_REPRODUCIBILITY_AND_DATA.md](ETHICS_REPRODUCIBILITY_AND_DATA.md) |
| [.github/ISSUE_TEMPLATE/config.yml](../.github/ISSUE_TEMPLATE/config.yml) | Template | Issue chooser config | — |
| [.github/ISSUE_TEMPLATE/bug_report.md](../.github/ISSUE_TEMPLATE/bug_report.md) | Template | Bugs / inaccuracies | [METHODOLOGY.md](METHODOLOGY.md) |
| [.github/ISSUE_TEMPLATE/feature_request.md](../.github/ISSUE_TEMPLATE/feature_request.md) | Template | Tooling / repo features | [VISION_AND_SCOPE.md](VISION_AND_SCOPE.md) |
| [.github/ISSUE_TEMPLATE/finding_review.md](../.github/ISSUE_TEMPLATE/finding_review.md) | Template | Finding proposals / reviews | [METHODOLOGY.md](METHODOLOGY.md) |
| [.github/ISSUE_TEMPLATE/methods_change.md](../.github/ISSUE_TEMPLATE/methods_change.md) | Template | Protocol / analysis changes | [METHODOLOGY.md](METHODOLOGY.md) |
| [.github/ISSUE_TEMPLATE/hypothesis_thread.md](../.github/ISSUE_TEMPLATE/hypothesis_thread.md) | Template | New or revised hypotheses | [VISION_AND_SCOPE.md](VISION_AND_SCOPE.md), [METHODOLOGY.md](METHODOLOGY.md) |
| [docs/DOC_MAP.md](DOC_MAP.md) | Policy | Doc → behavior traceability | All guiding docs |
| [docs/ONBOARDING.md](ONBOARDING.md) | Guide | First-hour navigation | — |
| [docs/REPOSITORY_MANIFEST.md](REPOSITORY_MANIFEST.md) | Index | This file | — |
| [docs/LABELS_AND_MILESTONES.md](LABELS_AND_MILESTONES.md) | Guide | GitHub labels / milestones | [COLLABORATION_AND_REVIEWS.md](COLLABORATION_AND_REVIEWS.md) |
| [docs/LICENSING_NOTES.md](LICENSING_NOTES.md) | Policy | Exceptions to default LICENSE | [LICENSE](../LICENSE) |
| [docs/VISION_AND_SCOPE.md](VISION_AND_SCOPE.md) | Policy | Mission, scope, terms | README, templates, AGENTS |
| [docs/METHODOLOGY.md](METHODOLOGY.md) | Policy | Evidence bar, workflows | Templates, prompts, PRs |
| [docs/ETHICS_REPRODUCIBILITY_AND_DATA.md](ETHICS_REPRODUCIBILITY_AND_DATA.md) | Policy | Data classes, integrity | `data/`, `.gitignore` |
| [docs/COLLABORATION_AND_REVIEWS.md](COLLABORATION_AND_REVIEWS.md) | Policy | Review norms, communication | CONTRIBUTING, labels doc |
| [docs/OPERATING_RHYTHM.md](OPERATING_RHYTHM.md) | Policy | Cadence, CI, tags, protection | Workflows, Dependabot |
| [docs/prompts/literature_synthesis.md](prompts/literature_synthesis.md) | Prompt | Literature discipline | [METHODOLOGY.md](METHODOLOGY.md) |
| [docs/prompts/hypothesis_comparison.md](prompts/hypothesis_comparison.md) | Prompt | Compare hypotheses | [METHODOLOGY.md](METHODOLOGY.md) |
| [docs/prompts/falsification_pass.md](prompts/falsification_pass.md) | Prompt | Red-team / falsification | [METHODOLOGY.md](METHODOLOGY.md) |
| [methods/README.md](../methods/README.md) | Guide | Protocols folder contract | [METHODOLOGY.md](METHODOLOGY.md) |
| [data/README.md](../data/README.md) | Guide | Data folder contract | [ETHICS_REPRODUCIBILITY_AND_DATA.md](ETHICS_REPRODUCIBILITY_AND_DATA.md) |
| [data/raw/.gitkeep](../data/raw/.gitkeep) | Placeholder | Preserve `raw/` in git | [data/README.md](../data/README.md) |
| [artifacts/README.md](../artifacts/README.md) | Guide | Outputs contract | [METHODOLOGY.md](METHODOLOGY.md) |
| [scripts/README.md](../scripts/README.md) | Guide | Automation contract | [METHODOLOGY.md](METHODOLOGY.md), [ETHICS_REPRODUCIBILITY_AND_DATA.md](ETHICS_REPRODUCIBILITY_AND_DATA.md) |
| [notebooks/README.md](../notebooks/README.md) | Guide | Exploratory analysis contract | [METHODOLOGY.md](METHODOLOGY.md) |

## Maintenance rule

When you add, rename, or remove a **policy-relevant** path, update this manifest and [DOC_MAP.md](DOC_MAP.md) in the same change.
