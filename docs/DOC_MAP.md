# Guiding documents → repository behaviors

This map is the Phase 0 traceability layer. When you change a guiding document, update the corresponding behaviors (rules, templates, or this map) in the same change.

| Guiding document | What it governs | Concrete behaviors |
|------------------|-----------------|----------------------|
| [VISION_AND_SCOPE.md](VISION_AND_SCOPE.md) | Mission, boundaries, what belongs in-repo | README framing; issue labels; scope checks in AGENTS and Cursor rules |
| [METHODOLOGY.md](METHODOLOGY.md) | Claims vs hypotheses, evidence bars, workflows | PR template checklist; `finding_review` issue template; prompt templates in [prompts/](prompts/) |
| [ETHICS_REPRODUCIBILITY_AND_DATA.md](ETHICS_REPRODUCIBILITY_AND_DATA.md) | Data classes, privacy, reproducibility | `.gitignore`; [data/README.md](../data/README.md); no raw restricted data in git |
| [COLLABORATION_AND_REVIEWS.md](COLLABORATION_AND_REVIEWS.md) | Contributions, review expectations | [CONTRIBUTING.md](../CONTRIBUTING.md); PR template; branch protection notes in [OPERATING_RHYTHM.md](OPERATING_RHYTHM.md) |
| [OPERATING_RHYTHM.md](OPERATING_RHYTHM.md) | Cadence, versioning, when to sync rules/CI | Doc/CI updates; release/tag policy |

## Gaps flagged for maintainer decision

- **License interaction:** Repository default is MIT ([LICENSE](../LICENSE)). If specific outputs (e.g. preprints) need CC BY, state that per artifact in metadata or a dedicated `docs/LICENSING_NOTES.md` when you introduce those artifacts.
- **Human subjects / regulated research:** If work involves human subjects, HIPAA, or export-controlled data, add a mandatory compliance appendix and legal review before committing study protocols or data paths.
- **Branch protection:** GitHub branch protection is configured in repository settings, not in git. See [OPERATING_RHYTHM.md](OPERATING_RHYTHM.md).
