# Consultant handoff (Grok) — latest

Brief for an external consultant. Factual snapshot only; no invented issue IDs.

## Summary

Recent maintainer-facing work spans documentation priority material, CI harvest workflow hardening, and supporting automation hygiene (graph bot PR path, markdown link checks for DOI/arXiv, citation index generator, and optional split PRs for `OPERATING_RHYTHM` / changelog when scope warrants).

## Changes

### Branch `docs/maintainer-priority-prompt-2026-05`

- Added or updated **`docs/MAINTAINER_PRIORITY_PROMPT.md`**, **`docs/DOC_MAP.md`**, **`docs/REPOSITORY_MANIFEST.md`**, **`CHANGELOG.md`**, and MkDocs navigation for discoverability.
- Open a PR from this branch (maintainer merges manually):  
  `https://github.com/KR8ZYSHO3/Universal-Science-Discovery/pull/new/docs/maintainer-priority-prompt-2026-05`

### Branch `fix/harvest-openalex-git-128` (commit `12889d8`)

- **`.github/workflows/harvest-openalex.yml`**: `ubuntu-24.04`; `actions/checkout` with `fetch-depth: 0` and token as needed for history/PR flows; `actions/setup-python@v6`; `peter-evans/create-pull-request@v7` with explicit bot identity; `workflow_dispatch` debug input mapped to **`ACTIONS_STEP_DEBUG`** for troubleshooting.
- **`CHANGELOG.md`**: **Unreleased** bullet documenting the workflow updates.
- Open a PR from this branch:  
  `https://github.com/KR8ZYSHO3/Universal-Science-Discovery/pull/new/fix/harvest-openalex-git-128`

### Cursor / agent habit (this repo)

- **`.cursor/rules/documentation-and-dashboard.mdc`**: after substantive merge-worthy work, agents should post a short Markdown handoff in chat (Summary / Changes / Human follow-ups / Next steps) and may mirror it here (**`GROK_CONSULTANT_LATEST.md`**).
- **`AGENTS.md`**: one-line pointer under the documentation section.

## Human follow-ups

- **GitHub → Settings → Actions → General**: workflows that open or update PRs need appropriate permissions (read/write for `contents` where applicable, and **allow GitHub Actions to create and approve pull requests** where the bot already does so for graph-related automation). Re-check when adding or tightening org/repo policy; same settings family applies to harvest PR automation.

## Next steps

- Review and merge the two PRs above in the order that matches maintainer risk tolerance (docs branch is low risk; harvest workflow should be validated on a fork or with `workflow_dispatch` before relying on scheduled runs).
- After merges, confirm scheduled **`harvest-openalex`** behavior and that PR creation succeeds under current Actions permissions.
- If `OPERATING_RHYTHM` / changelog edits grow large relative to other work, keep using split PRs to keep review focused.

---

## Snapshot — Wave Factory / validation (2026-05-13, `main`)

- **Local tests:** `python -m pytest tests/repo_smoke` → **4 passed** (same bundle as **`validate-schemas.yml`**).
- **`.github/workflows/harvest-openalex.yml` (Wave Factory Cadence):**
  - **`workflow_dispatch`** has **no `inputs`** block. For verbose runner logs use GitHub’s **Re-run jobs** UI and enable **“Enable debug logging”** when the repository/org allows it, or set repository/environment secrets **`ACTIONS_RUNNER_DEBUG`** / **`ACTIONS_STEP_DEBUG`** to `true` for a targeted rerun (see GitHub Actions documentation for debug logging).
  - **Create Pull Request** step: **`add-paths`** lists **three** tracked JSON files (`drafts/openalex_candidates.json`, `drafts/pubmed_candidates.json`, `drafts/semantic_scholar_candidates.json`) only. **`drafts/wave_factory/`** stays **gitignored** (see `.gitignore`), so it is intentionally **not** in `add-paths` (see **CHANGELOG** Unreleased Wave Factory CPR note). **`skip-commit`** / **`skip-checks`** are **not** passed to `peter-evans/create-pull-request@v7`; the commit message includes **`[skip ci]`** to limit redundant CI on the bot branch.
  - **Change detection** step uses **`git ls-files --modified --others --exclude-standard`** piped to **`grep -E`** for the JSON paths and (in the pattern) `drafts/wave_factory/` — note ignored paths will not appear in `ls-files` unless force-added.
- **Handoff hygiene:** Older bullets in **“Branch `fix/harvest-openalex-git-128`”** above may describe **`workflow_dispatch` debug `inputs`** that are **not** present on current `main`; treat this snapshot as the corrected description until that branch is merged or the file is rewritten.
