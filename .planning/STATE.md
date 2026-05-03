# USDR workspace state

Authoritative checklist for humans and agents. The Cursor Canvas [`canvases/Progress.canvas.tsx`](../canvases/Progress.canvas.tsx) mirrors this file via embedded constants — run [`scripts/sync-dashboard-from-state.py`](../scripts/sync-dashboard-from-state.py) after edits, or paste updates manually.

## Last updated

- 2026-05-03 — Dev dashboard scaffolding (`feat/dev-dashboard`); MkDocs strict build gate.

## Current focus

- Phase B ingestion package (`packages/ingest`): CLI ergonomics, manifest validation, and docs alignment with [DATA_PLAN.md](../docs/DATA_PLAN.md).
- Keeping [mkdocs.yml](../mkdocs.yml) + GitHub Pages (`site_url` / `edit_uri`) consistent with the default branch and fork workflow.
- Phase A plan artifacts under `.planning/` and cross-links to methodology docs (no new scientific claims in meta files).

## Active git branches / PRs

- `main` — default; policy and docs source of truth.
- `feat/phase-b-ingest` — [compare to `main`](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/compare/main...feat/phase-b-ingest) — ingest CLI and tests.
- `feat/mkdocs-gh-pages` — [compare to `main`](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/compare/main...feat/mkdocs-gh-pages) — site publishing and nav (when active).
- Open PRs: use GitHub **Pull requests** tab; add compare links here when reviewing.

## Shipped recently

- Agent execution rule (`.cursor/rules/agent-execution.mdc`) — run installs, tests, and git in-environment.
- MkDocs Material site with doc map, methodology, and ethics pages.
- Repository manifest and Phase A data plan documentation.

## Blocked / needs human

- None — replace this bullet when something requires credentials, legal review, or maintainer decision outside the repo.

## Next actions (max 5)

- Land Phase B ingest MVP with tests and `mkdocs build --strict` clean.
- Confirm GitHub Pages branch/env matches `site_url` in `mkdocs.yml`.
- Add or refresh UAT notes for ingest when the CLI surface stabilizes.
- Keep [LEGAL.md](../LEGAL.md) and science-integrity docs in mind before any new data paths or claims.
- After merging this dashboard PR, run the sync script once so canvas constants match this file.
