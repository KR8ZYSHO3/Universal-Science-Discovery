# USDR workspace state

Authoritative checklist for humans and agents. The Cursor Canvas [`canvases/Progress.canvas.tsx`](../canvases/Progress.canvas.tsx) mirrors this file via embedded constants — run [`scripts/sync-dashboard-from-state.py`](../scripts/sync-dashboard-from-state.py) after edits, or paste updates manually.

## Last updated

- 2026-05-03 — **Stream A** happy path doc ([docs/HAPPY_PATH_FIRST_RECORDS.md](docs/HAPPY_PATH_FIRST_RECORDS.md)) wired through CONTRIBUTING, hub, MkDocs, DOC_MAP, manifest, onboarding.
- 2026-05-03 — Cursor rule **documentation-and-dashboard**: hub CDN/privacy + UX sync with README/DEV_DASHBOARD.
- 2026-05-03 — **DEV_DASHBOARD** + hub README: document theme/CDN behavior and privacy/offline notes.
- 2026-05-03 — **Contributor hub** visual refresh (hero, theme toggle, scroll-spy nav, fonts).
- 2026-05-03 — **OPERATING_RHYTHM:** branch-protection status check names + ingest path-filter note.
- 2026-05-03 — **markdown-link-check CI:** gh.io URL as plain text; **OPERATING_RHYTHM** records “no Page hyperlink until 200”.
- 2026-05-03 — PR template ingest checkbox; CONTRIBUTING ingest section; hub **compare to main** link for integration work.
- 2026-05-03 — **`packages/ingest/README.md`** + `readme` in `pyproject.toml`; root README points at package readme for ingest.
- 2026-05-03 — **UAT_INGEST.md** for `usdr-ingest`; hub + MkDocs + DATA_PLAN links.
- 2026-05-03 — Contributor **hub** links **docs/GSD_INTEGRATION.md**; manifest row added. **docs/index** Meta link.
- 2026-05-03 — Added **docs/GSD_INTEGRATION.md** (optional GSD maintainer boundaries); MkDocs nav + DOC_MAP + onboarding cross-links.
- 2026-05-03 — Checked in **ingestion envelope** JSON Schema + ingest tests that validate harvest output against it.

## Current focus

- Docs + **dashboard** discipline: milestones and ongoing work update `README`, `CHANGELOG` (Unreleased), `docs/` as needed, `dashboard/index.html`, and spot-check **`http://localhost:8765/dashboard/`** (see `.cursor/rules/documentation-and-dashboard.mdc`).
- **Happy path (Stream A):** [docs/HAPPY_PATH_FIRST_RECORDS.md](../docs/HAPPY_PATH_FIRST_RECORDS.md) — first unknown + hypothesis → PR; keep in sync with schemas/templates and seed YAML examples.
- **usdr-ingest** (`packages/ingest`): arXiv OAI-PMH metadata only — extend CLI/manifest as needed per [DATA_PLAN.md](../docs/DATA_PLAN.md).
- Keeping [mkdocs.yml](../mkdocs.yml) + GitHub Pages (`site_url` / `edit_uri`) consistent with the default branch and fork workflow.
- Phase A plan artifacts under `.planning/` and cross-links to methodology docs (no new scientific claims in meta files).

## Active git branches / PRs

- `main` — default; policy and docs source of truth.
- `feat/dev-dashboard` — [compare to `main`](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/compare/main...feat/dev-dashboard) — contributor HTML hub, doc rules, **usdr-ingest**, mkdocs/Pages CI.
- `feat/mkdocs-gh-pages` — [compare to `main`](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/compare/main...feat/mkdocs-gh-pages) — site publishing and nav (when active).
- Open PRs: use GitHub **Pull requests** tab; add compare links here when reviewing.

## Shipped recently

- **Contributor hub** visual refresh: hero, theme toggle, scroll-spy nav, card motion (`dashboard/index.html`).
- Contributor **HTML hub** (`dashboard/index.html`) and README onboarding path.
- Cursor **documentation-and-dashboard** rule (milestones + ongoing docs + `http://localhost:8765/dashboard/` verification).
- MkDocs Material site with doc map, methodology, and ethics pages.
- **JSON Schema** for ingest: `schemas/ingestion-envelope-1.0.0.json` + pytest validation of harvest JSONL rows.
- Repository manifest and Phase A data plan documentation.

## Blocked / needs human

- None — replace this bullet when something requires credentials, legal review, or maintainer decision outside the repo.

## Next actions (max 5)

- Open **one integration PR** from `feat/dev-dashboard` → `main` (hub + docs rules + ingest + mkdocs/Pages) when ready.
- Confirm GitHub Pages branch/env matches `site_url` in `mkdocs.yml`.
- Follow **[UAT_INGEST.md](../docs/UAT_INGEST.md)** when exercising `usdr-ingest` manually (pytest is still the merge gate).
- Keep [LEGAL.md](../LEGAL.md) and science-integrity docs in mind before any new data paths or claims.
- Apply **documentation-and-dashboard** rule on each merge: update CHANGELOG Unreleased, sync Canvas from `STATE.md` when using `canvases/Progress.canvas.tsx`, re-check contributor hub if links changed.
