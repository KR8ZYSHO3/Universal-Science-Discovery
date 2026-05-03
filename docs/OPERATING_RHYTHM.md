# Operating rhythm

## When guiding documents change

1. Update [DOC_MAP.md](DOC_MAP.md) if behaviors shift.
2. Sync [AGENTS.md](../AGENTS.md) and [.cursor/rules/](../.cursor/rules/) if agent-facing expectations changed.
3. Sync issue/PR templates under [.github/](../.github/) if workflow fields need to match.
4. Merge governance and tooling updates in **one PR** when possible so history stays coherent.
5. **Milestones and features:** update [CHANGELOG.md](../CHANGELOG.md) (Unreleased), [README.md](../README.md) or deeper docs as needed, [.planning/STATE.md](../.planning/STATE.md), and [dashboard/index.html](../dashboard/index.html) so [http://localhost:8765/dashboard/](http://localhost:8765/dashboard/) stays accurate; run `mkdocs build --strict` when `docs/` or `mkdocs.yml` changed. Cursor rule: `.cursor/rules/documentation-and-dashboard.mdc`.

## CI and merges

- Pull requests should pass [Markdown link check](../.github/workflows/markdown-link-check.yml) before merge to `main`.
- **GitHub Pages:** Until the published site at `https://kr8zysho3.github.io/Universal-Science-Discovery/` returns HTTP **200**, do not use that URL as a markdown **hyperlink** in tracked docs (the checker treats 404 as failure). Use backticks, or add/adjust an entry in [.markdown-link-check.json](../.markdown-link-check.json) `ignorePatterns` if you intentionally link before go-live.
- [Dependabot](../.github/dependabot.yml) opens weekly PRs to update GitHub Actions; review and merge to reduce supply-chain drift.
- Expand CI (lint, tests) when code under [scripts/](../scripts/) grows.

## Versioning and tags

- Use **date-based tags** (`YYYY.MM.DD` or `vYYYY.MM.summary`) for snapshots of methodology or milestone reports when you need a citeable point in time.
- Use **semantic versioning** (`v1.2.0`) only if the repo ships a reusable software artifact with API stability expectations.

## Releases

- For major methodological or dataset snapshots described to external readers, attach release notes listing what changed and known limitations.

## Branch protection (GitHub settings)

Recommended for `main` once collaborators join:

- Require pull request before merge.
- Require status checks to pass — see **Status check names** below (pick what matches how strictly you want to gate merges).
- Optionally require an approving review.

These options are configured under **Settings → Branches → Branch protection rules** in the GitHub UI; they are not stored in this repository.

### Status check names (as GitHub lists them)

Use **Actions → … → workflow run** to copy exact names into branch protection. Typical identifiers:

| Workflow file | Often appears as |
|---------------|------------------|
| [markdown-link-check.yml](../.github/workflows/markdown-link-check.yml) | `markdown-link-check` (job: `markdown-link-check`) |
| [mkdocs-build.yml](../.github/workflows/mkdocs-build.yml) | `mkdocs-build / mkdocs` |
| [validate-schemas.yml](../.github/workflows/validate-schemas.yml) | `validate-schemas / validate-schemas` |
| [ingest-ci.yml](../.github/workflows/ingest-ci.yml) | `ingest tests / pytest-ingest` |

**Ingest caveat:** [ingest-ci.yml](../.github/workflows/ingest-ci.yml) runs only when PRs touch ingest-related paths (`packages/ingest/`, `requirements-ingest.txt`, envelope schema, etc.). If you mark **`ingest tests / pytest-ingest`** as **required**, GitHub may block merges on docs-only PRs where that workflow did not run. Options: omit it from required checks, use a ruleset that allows skipped optional checks, or touch an ingest path when you need the check to appear.

## Cadence

- **Weekly (lightweight):** triage issues, label stalled threads, skim open PRs.
- **Monthly:** review whether `docs/` still matches practice; prune obsolete prompts or scripts.
- **Per publication or external share:** tag a snapshot and archive relevant artifacts with provenance.
