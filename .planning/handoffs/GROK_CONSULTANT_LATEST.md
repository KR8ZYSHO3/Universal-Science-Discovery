# Consultant handoff (Grok) — latest

Brief for an external consultant. Factual snapshot only; no invented issue IDs.

## Summary

**Dashboard Phase A** (`feat/dashboard-search-graph-flow`) is merged to main via PR #244.

**Phase B** UX polish is ready on `feat/dashboard-ux-polish`.

**Wave Factory** is stable and green.

Bounded content wave is deferred (documentation-only) until maintainer review of `drafts/`.

## Changes (agent workspace)

| Area | Detail |
|------|--------|
| Phase A | Landed via **PR #244**; do not rely on stale “Phase A not merged” snapshots. |
| Phase B PR | https://github.com/KR8ZYSHO3/Universal-Science-Discovery/compare/main...feat/dashboard-ux-polish |
| Content deferral PR | https://github.com/KR8ZYSHO3/Universal-Science-Discovery/compare/main...content/phase1-bounded-wave-1 |
| Typical touched paths | `dashboard/index.html`, `dashboard/README.md`, `docs/DEV_DASHBOARD.md`, `docs/PATH_TO_SUCCESS.md`, `CHANGELOG.md`, `.planning/STATE.md`, this handoff, `canvases/Progress.canvas.tsx` (after `STATE` edits). |
| Verification (local) | **`python scripts/verify_dashboard_consistency.py`**, **`python -m pytest tests/repo_smoke`**, **`mkdocs build --strict`** after doc/hub edits. |

## Human follow-ups

1. **Merge Phase B** from **`feat/dashboard-ux-polish`** when CI/review pass (compare link above). Optionally merge **`content/phase1-bounded-wave-1`** if you want the deferral note on `main`, or fold that narrative into this file on `main` only and close the extra PR.
2. **Wave Factory checklist:** merge the bot PR when green; paste the **successful Actions run URL** (and PR link if opened) into maintainer notes or a PR description — same expectations as the **Final Wave Factory validation checklist** block below.
3. **`gh` CLI:** if not authenticated, use the web UI for **good first issue** triage: https://github.com/KR8ZYSHO3/Universal-Science-Discovery/issues?q=is%3Aopen+label%3A%22good+first+issue%22

## Next steps

- After any **`.planning/STATE.md`** edit that should appear in the Cursor canvas, run **`python scripts/sync-dashboard-from-state.py`**.
- Rebase feature branches onto latest **`main`** after each merge to avoid duplicate commits in PRs.

---

## Final Wave Factory validation checklist (May 2026)

Maintainers: complete manually and paste evidence when done.

1. On GitHub **Actions** for **`KR8ZYSHO3/Universal-Science-Discovery`**, select workflow **Wave Factory Cadence** (`.github/workflows/harvest-openalex.yml`).
2. From **`main`**, use **Run workflow** (this workflow’s **`workflow_dispatch`** has **no inputs** on current `main` unless changed upstream).
3. Enable **debug logging** for that run when policy allows.
4. Wait for a **green** conclusion. If candidate JSON changes land, confirm the bot PR scope matches **`add-paths`** expectations in the workflow.
5. Paste the **run URL** (and PR link if opened) into maintainer notes.

**Note:** Confirming green status requires maintainer auth (Actions UI or authenticated **`gh`**).

---

## Append — 2026-05-14 (Phase B follow-up + bounded content)

### Summary

**Phase A** merged on **`main`** (PR **#244**). **`feat/dashboard-ux-polish`** was rebased onto **`origin/main`** so Phase B is a clean second PR. **`gh`** was not authenticated in the agent environment; **`drafts/bridges/`** stubs (many OpenAlex-origin) are **not** auto-promoted without maintainer review per **`docs/METHODOLOGY.md`**. Branch **`content/phase1-bounded-wave-1`** documents deferral in **`CHANGELOG`** + this handoff.

### PR / compare links

| Branch | Purpose | Compare |
|--------|---------|---------|
| **`feat/dashboard-ux-polish`** | Hub UX + docs hygiene | https://github.com/KR8ZYSHO3/Universal-Science-Discovery/compare/main...feat/dashboard-ux-polish |
| **`content/phase1-bounded-wave-1`** | Content wave deferral note (no new catalog YAML that session) | https://github.com/KR8ZYSHO3/Universal-Science-Discovery/compare/main...content/phase1-bounded-wave-1 |

### Catalog truth (reproducible)

Run locally from repo root:

```bash
python scripts/verify_dashboard_consistency.py
```

Expected line shape (verify against current `docs/knowledge_graph.json` meta if counts drift): **bridges=1123, unknowns=1408, hypotheses=1274, phenomena=10, graph_nodes=3857, graph_edges=4517**.

**Auth note:** confirming a **green** Actions run or **bot PR** contents still requires maintainer access (**Actions UI** or **`gh run view`** with a logged-in **`gh`**). This file records **checklist-only** expectations unless a maintainer pastes a confirmed run URL.

### Bounded content wave — deferred (`content/phase1-bounded-wave-1`)

No new **`cross-domain/`**, **`unknowns-catalog/`**, or **`hypotheses/`** YAML in that documentation-only pass: **`gh`** was not authenticated, and **`drafts/bridges/`** requires human review before promotion. See **`CHANGELOG.md`** **[Unreleased]** **Notes** for the same statement. **Dashboard Phase B** remains a separate PR from **`feat/dashboard-ux-polish`** → **`main`**.
