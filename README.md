# Universal Science Discovery

A structured workspace for **hypothesis-driven science**: methods, evidence, and reproducible artifacts live together with explicit separation between hypotheses, findings, and speculation.

## Start here

| Document | Purpose |
|----------|---------|
| [docs/VISION_AND_SCOPE.md](docs/VISION_AND_SCOPE.md) | Mission, in/out of scope, terminology |
| [docs/METHODOLOGY.md](docs/METHODOLOGY.md) | Evidence bar, claims discipline, outputs |
| [docs/ETHICS_REPRODUCIBILITY_AND_DATA.md](docs/ETHICS_REPRODUCIBILITY_AND_DATA.md) | Data classes, reproducibility, integrity |
| [docs/COLLABORATION_AND_REVIEWS.md](docs/COLLABORATION_AND_REVIEWS.md) | Reviews, labels, communication |
| [docs/DOC_MAP.md](docs/DOC_MAP.md) | **Guiding doc → concrete behaviors** (traceability) |
| [docs/OPERATING_RHYTHM.md](docs/OPERATING_RHYTHM.md) | Cadence, versioning, branch protection, CI |
| [docs/ONBOARDING.md](docs/ONBOARDING.md) | First-time contributor path (~30 min) |
| [docs/REPOSITORY_MANIFEST.md](docs/REPOSITORY_MANIFEST.md) | Every path: purpose and governing doc |
| [docs/LABELS_AND_MILESTONES.md](docs/LABELS_AND_MILESTONES.md) | Issue labels and optional milestones |
| [docs/LICENSING_NOTES.md](docs/LICENSING_NOTES.md) | License exceptions and per-artifact notes |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | Community expectations |
| [SECURITY.md](SECURITY.md) | Reporting security issues and secrets |

## Repository layout

| Path | Role |
|------|------|
| [docs/](docs/) | Guiding documents, doc map, operating rhythm, [prompts/](docs/prompts/) |
| [methods/](methods/) | Protocols and study designs |
| [data/](data/) | Allowed non-sensitive data; `raw/` is gitignored |
| [artifacts/](artifacts/) | Committed generated outputs with provenance |
| [scripts/](scripts/) | Reproducible automation |
| [notebooks/](notebooks/) | Exploratory analysis (reproducibility expectations in folder README) |
| [AGENTS.md](AGENTS.md) | Agent instructions (Cursor and other assistants) |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Pull requests should pass Markdown link check on `main`.

## License

This repository is licensed under the [MIT License](LICENSE) unless noted otherwise in specific files or future `docs/LICENSING_NOTES.md`.

## Citation

If you reference a snapshot of this repository, cite the URL and the **commit hash** or **release tag** you used.
