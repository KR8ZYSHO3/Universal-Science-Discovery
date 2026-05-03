# USDR workspace state

Authoritative checklist for humans and agents. The Cursor Canvas [`canvases/Progress.canvas.tsx`](../canvases/Progress.canvas.tsx) mirrors this file via embedded constants — run [`scripts/sync-dashboard-from-state.py`](../scripts/sync-dashboard-from-state.py) after edits, or paste updates manually.

## Last updated

- 2026-05-03 — Checked in **ingestion envelope** JSON Schema + ingest tests that validate harvest output against it.

## Current focus

- Docs + **dashboard** discipline: milestones and ongoing work update `README`, `CHANGELOG` (Unreleased), `docs/` as needed, `dashboard/index.html`, and spot-check **`http://localhost:8765/dashboard/`** (see `.cursor/rules/documentation-and-dashboard.mdc`).
- **usdr-ingest** (`packages/ingest`): arXiv OAI-PMH metadata only — extend CLI/manifest as needed per [DATA_PLAN.md](../docs/DATA_PLAN.md).
- Keeping [mkdocs.yml](../mkdocs.yml) + GitHub Pages (`site_url` / `edit_uri`) consistent with the default branch and fork workflow.
- Phase A plan artifacts under `.planning/` and cross-links to methodology docs (no new scientific claims in meta files).

## Active git branches / PRs

- `main` — default; policy and docs source of truth.
- `feat/dev-dashboard` — [compare to `main`](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/compare/main...feat/dev-dashboard) — contributor HTML hub, doc rules, **usdr-ingest**, mkdocs/Pages CI.
- `feat/mkdocs-gh-pages` — [compare to `main`](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/compare/main...feat/mkdocs-gh-pages) — site publishing and nav (when active).
- Open PRs: use GitHub **Pull requests** tab; add compare links here when reviewing.

## Shipped recently

- Contributor **HTML hub** (`dashboard/index.html`) and README onboarding path.
- Cursor **documentation-and-dashboard** rule (milestones + ongoing docs + `http://localhost:8765/dashboard/` verification).
- MkDocs Material site with doc map, methodology, and ethics pages.
- **JSON Schema** for ingest: `schemas/ingestion-envelope-1.0.0.json` + pytest validation of harvest JSONL rows.
- Repository manifest and Phase A data plan documentation.

- None — replace this bullet when something requires credentials, legal review, or maintainer decision outside the repo.

## Next actions (max 5)

- Open **one integration PR** from `feat/dev-dashboard` → `main` (hub + docs rules + ingest + mkdocs/Pages) when ready.
- Confirm GitHub Pages branch/env matches `site_url` in `mkdocs.yml`.
- Add or refresh UAT notes for ingest when the CLI surface stabilizes.
- Keep [LEGAL.md](../LEGAL.md) and science-integrity docs in mind before any new data paths or claims.
- Apply **documentation-and-dashboard** rule on each merge: update CHANGELOG Unreleased, sync Canvas from `STATE.md` when using `canvases/Progress.canvas.tsx`, re-check contributor hub if links changed.
