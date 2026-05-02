# Guiding documents → repository behaviors

This map is the Phase 0 traceability layer. When you change a guiding document, update the corresponding behaviors (rules, templates, or this map) in the same change.

| Guiding document | What it governs | Concrete behaviors |
|------------------|-----------------|----------------------|
| [VISION_AND_SCOPE.md](VISION_AND_SCOPE.md) | Mission, boundaries, what belongs in-repo | README framing; issue labels; scope checks in AGENTS and Cursor rules |
| [METHODOLOGY.md](METHODOLOGY.md) | Claims vs hypotheses, evidence bars, workflows | PR template checklist; `finding_review` and `hypothesis_thread` issue templates; prompt templates in [prompts/](prompts/) |
| [ETHICS_REPRODUCIBILITY_AND_DATA.md](ETHICS_REPRODUCIBILITY_AND_DATA.md) | Data classes, privacy, reproducibility | `.gitignore`; [data/README.md](../data/README.md); no raw restricted data in git |
| [COLLABORATION_AND_REVIEWS.md](COLLABORATION_AND_REVIEWS.md) | Contributions, review expectations | [CONTRIBUTING.md](../CONTRIBUTING.md); PR template; branch protection notes in [OPERATING_RHYTHM.md](OPERATING_RHYTHM.md) |
| [OPERATING_RHYTHM.md](OPERATING_RHYTHM.md) | Cadence, versioning, when to sync rules/CI | Doc/CI updates; release/tag policy |
| [REPOSITORY_MANIFEST.md](REPOSITORY_MANIFEST.md) | Per-path roles and governing docs | Keeping structure auditable; updates when paths change |
| [ONBOARDING.md](ONBOARDING.md) | First-hour navigation | Points to all core policies and work directories |
| [LABELS_AND_MILESTONES.md](LABELS_AND_MILESTONES.md) | GitHub triage vocabulary | Aligns with [COLLABORATION_AND_REVIEWS.md](COLLABORATION_AND_REVIEWS.md); issue templates |
| [LICENSING_NOTES.md](LICENSING_NOTES.md) | Exceptions to default MIT | Per-file or per-artifact license metadata |
| [CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md) | Community behavior | [CONTRIBUTING.md](../CONTRIBUTING.md); enforcement expectations |
| [SECURITY.md](../SECURITY.md) | Private vulnerability / sensitive data reports | Automation and secrets; not scientific debate |

## Supporting files (see manifest)

Configuration and templates (`.github/`, `.cursor/`, `.markdown-link-check.json`, root `LICENSE`, `.gitignore`) are indexed in [REPOSITORY_MANIFEST.md](REPOSITORY_MANIFEST.md) so every tracked path maps to policy.

## Gaps flagged for maintainer decision

- **License interaction:** Repository default is MIT ([LICENSE](../LICENSE)). Record per-artifact exceptions in [LICENSING_NOTES.md](LICENSING_NOTES.md) when you introduce them.
- **Human subjects / regulated research:** If work involves human subjects, HIPAA, or export-controlled data, add a mandatory compliance appendix and legal review before committing study protocols or data paths.
- **Branch protection:** GitHub branch protection is configured in repository settings, not in git. See [OPERATING_RHYTHM.md](OPERATING_RHYTHM.md).
