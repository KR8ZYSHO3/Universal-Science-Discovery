# USDR workspace state

Authoritative checklist for humans and agents. The Cursor Canvas [`canvases/Progress.canvas.tsx`](../canvases/Progress.canvas.tsx) mirrors this file via embedded constants — run [`scripts/sync-dashboard-from-state.py`](../scripts/sync-dashboard-from-state.py) after edits, or paste updates manually.

## Last updated

- 2026-05-03 — Documentation + contributor-hub rule (`.cursor/rules/documentation-and-dashboard.mdc`); AGENTS / OPERATING_RHYTHM aligned.

## Current focus

- Docs + **dashboard** discipline: milestones and ongoing work update `README`, `CHANGELOG` (Unreleased), `docs/` as needed, `dashboard/index.html`, and spot-check **`http://localhost:8765/dashboard/`** (see `.cursor/rules/documentation-and-dashboard.mdc`).
- Phase B ingestion package (`packages/ingest` when present): CLI ergonomics, manifest validation, and docs alignment with [DATA_PLAN.md](../docs/DATA_PLAN.md).
- Keeping [mkdocs.yml](../mkdocs.yml) + GitHub Pages (`site_url` / `edit_uri`) consistent with the default branch and fork workflow.
- Phase A plan artifacts under `.planning/` and cross-links to methodology docs (no new scientific claims in meta files).

## Active git branches / PRs

- `main` — default; policy and docs source of truth.
- `feat/phase-b-ingest` — [compare to `main`](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/compare/main...feat/phase-b-ingest) — ingest CLI and tests.
- `feat/mkdocs-gh-pages` — [compare to `main`](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/compare/main...feat/mkdocs-gh-pages) — site publishing and nav (when active).
- Open PRs: use GitHub **Pull requests** tab; add compare links here when reviewing.

## Shipped recently

- Contributor **HTML hub** (`dashboard/index.html`) and README onboarding path.
- Cursor **documentation-and-dashboard** rule (milestones + ongoing docs + `http://localhost:8765/dashboard/` verification).
- MkDocs Material site with doc map, methodology, and ethics pages.
- Repository manifest and Phase A data plan documentation.

## Blocked / needs human

- None — replace this bullet when something requires credentials, legal review, or maintainer decision outside the repo.

## Next actions (max 5)

- Land Phase B ingest MVP with tests and `mkdocs build --strict` clean.
- Confirm GitHub Pages branch/env matches `site_url` in `mkdocs.yml`.
- Add or refresh UAT notes for ingest when the CLI surface stabilizes.
- Keep [LEGAL.md](../LEGAL.md) and science-integrity docs in mind before any new data paths or claims.
- Apply **documentation-and-dashboard** rule on each merge: update CHANGELOG Unreleased, sync Canvas from `STATE.md` when using `canvases/Progress.canvas.tsx`, re-check contributor hub if links changed.
