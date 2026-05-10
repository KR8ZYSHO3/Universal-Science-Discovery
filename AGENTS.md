# Agent instructions (Cursor and other assistants)

## Canonical policy

Before proposing **findings**, changing **methods**, or advising on **data handling**, read these in order:

1. [docs/VISION_AND_SCOPE.md](docs/VISION_AND_SCOPE.md)
2. [docs/METHODOLOGY.md](docs/METHODOLOGY.md)
3. [docs/ETHICS_REPRODUCIBILITY_AND_DATA.md](docs/ETHICS_REPRODUCIBILITY_AND_DATA.md)

For collaboration norms and review expectations: [docs/COLLABORATION_AND_REVIEWS.md](docs/COLLABORATION_AND_REVIEWS.md).  
For how docs map to repo mechanics: [docs/DOC_MAP.md](docs/DOC_MAP.md).  
For every path’s role and governing policy: [docs/REPOSITORY_MANIFEST.md](docs/REPOSITORY_MANIFEST.md).  
For human onboarding order: [docs/ONBOARDING.md](docs/ONBOARDING.md).  
For cadence and versioning: [docs/OPERATING_RHYTHM.md](docs/OPERATING_RHYTHM.md).

## Operating rules

- **Hypothesis vs finding:** Never present speculation as an established finding. Use the terminology from VISION_AND_SCOPE.
- **Citations:** Do not invent DOIs or papers. If uncertain, say so and suggest search strategies.
- **Data:** Do not instruct committing sensitive or identifiable human data to git; follow ETHICS_REPRODUCIBILITY_AND_DATA.
- **Reproducibility:** Prefer changes that reference scripts, protocols, or explicit steps—not vague “we analyzed the data.”
- **Scope:** Decline to expand the project into out-of-scope areas listed in VISION_AND_SCOPE unless the user explicitly reframes scope and documents it.

## Prompt templates

See [docs/prompts/](docs/prompts/) for literature synthesis, hypothesis comparison, and falsification passes.

## Documentation and contributor hub

- **Hub upkeep playbook:** **[docs/DEV_DASHBOARD.md](docs/DEV_DASHBOARD.md)** — what to run when catalog YAML, breakthrough gaps, STATE, or `dashboard/index.html` changes; includes **`scripts/verify_dashboard_consistency.py`** (also CI).
- Treat **documentation as part of the deliverable**: when you finish a milestone or merge-worthy feature, update **`README.md`**, **`CHANGELOG.md` (Unreleased)**, relevant **`docs/*.md`**, **`docs/DOC_MAP.md`** / **`docs/REPOSITORY_MANIFEST.md`** when paths or traceability change, and **`.planning/STATE.md`** for maintainer status.
- Keep **`dashboard/index.html`** aligned with onboarding and links; after hub-affecting edits, verify locally by opening [`dashboard/index.html`](dashboard/index.html) via `python -m http.server 8765` from the repo root (URL `http://localhost:8765/dashboard/`).
- When **`cross-domain/`**, **`unknowns-catalog/`**, or **`hypotheses/`** change in a merge-worthy batch, regenerate **`dashboard/domains/`** with **`python scripts/generate_domain_pages.py`** (and rely on **`python scripts/verify_domain_pages.py`** in CI). Matching rules: **`scripts/domain_matching.py`**.
- When **`breakthrough-gaps/`** YAML changes, run **`python scripts/render_breakthrough_gaps_hub.py --apply`** and **`python scripts/generate_api.py`** so the hub grid and **`api/v1/breakthrough_gaps.json`** stay aligned — see **`docs/BREAKTHROUGH_GAPS.md`**.
- If **`canvases/Progress.canvas.tsx`** exists, run **`python scripts/sync-dashboard-from-state.py`** after **`STATE.md`** changes.
- If **`docs/`** or **`mkdocs.yml`** changes, run **`mkdocs build --strict`**.

See `.cursor/rules/documentation-and-dashboard.mdc` (always apply).

## Project rules

This repository includes Cursor rules under [.cursor/rules/](.cursor/rules/) that mirror the above; keep them in sync when policy changes.
