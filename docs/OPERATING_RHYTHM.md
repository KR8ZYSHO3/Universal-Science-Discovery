# Operating rhythm

## When guiding documents change

1. Update [DOC_MAP.md](DOC_MAP.md) if behaviors shift.
2. Sync [AGENTS.md](../AGENTS.md) and [.cursor/rules/](../.cursor/rules/) if agent-facing expectations changed.
3. Sync issue/PR templates under [.github/](../.github/) if workflow fields need to match.
4. Merge governance and tooling updates in **one PR** when possible so history stays coherent.

## CI and merges

- Pull requests should pass [Markdown link check](../.github/workflows/markdown-link-check.yml) before merge to `main`.
- Expand CI (lint, tests) when code under [scripts/](../scripts/) grows.

## Versioning and tags

- Use **date-based tags** (`YYYY.MM.DD` or `vYYYY.MM.summary`) for snapshots of methodology or milestone reports when you need a citeable point in time.
- Use **semantic versioning** (`v1.2.0`) only if the repo ships a reusable software artifact with API stability expectations.

## Releases

- For major methodological or dataset snapshots described to external readers, attach release notes listing what changed and known limitations.

## Branch protection (GitHub settings)

Recommended for `main` once collaborators join:

- Require pull request before merge.
- Require status checks to pass (at minimum: `markdown-link-check`).
- Optionally require an approving review.

These options are configured under **Settings → Branches → Branch protection rules** in the GitHub UI; they are not stored in this repository.

## Cadence

- **Weekly (lightweight):** triage issues, label stalled threads, skim open PRs.
- **Monthly:** review whether `docs/` still matches practice; prune obsolete prompts or scripts.
- **Per publication or external share:** tag a snapshot and archive relevant artifacts with provenance.
