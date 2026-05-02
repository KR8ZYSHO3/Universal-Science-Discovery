# Notebooks

Exploratory analysis and narrative investigations belong here when they support **active threads** documented in issues or `methods/`.

## Expectations

- Prefer **small** outputs or references to `artifacts/` for large exports, per [docs/METHODOLOGY.md](../docs/METHODOLOGY.md).
- **Checkpoint hygiene:** the repo root [`.gitignore`](../.gitignore) ignores `.ipynb_checkpoints/` project-wide.
- Before promoting notebook conclusions to **findings**, run a [falsification pass](../docs/prompts/falsification_pass.md) and capture reproducible steps in [scripts/](../scripts/) where possible.

## Naming

Use descriptive prefixes and dates, for example `2026-05-initial-signal-foo.ipynb`, consistent with naming guidance in [methods/README.md](../methods/README.md).
