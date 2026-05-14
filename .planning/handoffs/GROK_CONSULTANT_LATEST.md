# Consultant handoff (Grok) — latest

Brief for an external consultant. Factual snapshot only; no invented issue IDs.

## Summary

**Dashboard Phase A** (`feat/dashboard-search-graph-flow`, tip `34973ac`) is **not merged to `origin/main`** (still at `bce6bac`). A maintainer can merge the same commits via **GitHub PR** because **`main` is protected** (direct push rejected: GH013). **Phase B** contributor-hub UX polish is prepared on **`feat/dashboard-ux-polish`** (loading/status for catalog search, `prefers-reduced-motion` for the particle canvas and spinners, responsive graph height, theme-aware graph overlays). **Docs:** `docs/PATH_TO_SUCCESS.md` adds a **Content wave kickoff** checklist (bounded waves, Wave Factory traceability).

## Changes (agent workspace)

| Area | Detail |
|------|--------|
| Phase A merge | Local fast-forward `main` → `34973ac`; **`git push origin main`** → **rejected** (PR required). |
| PR link (Phase A) | https://github.com/KR8ZYSHO3/Universal-Science-Discovery/compare/main...feat/dashboard-search-graph-flow |
| Phase B branch | `feat/dashboard-ux-polish` from updated local `main` — **`dashboard/index.html`**, **`dashboard/README.md`**, **`docs/PATH_TO_SUCCESS.md`**, **`CHANGELOG.md`**, **`.planning/STATE.md`**, this handoff. |
| Verification (local on Phase B tree) | Run **`python scripts/verify_dashboard_consistency.py`**, **`python -m pytest tests/repo_smoke`**, **`mkdocs build --strict`** after doc edits. |

## Human follow-ups

1. **Merge Phase A** via the compare/PR link above (or open PR from `feat/dashboard-search-graph-flow` → `main`). Do not expect agents to push `main` directly.
2. **Wave Factory checklist:** merge the bot PR when green; paste the **successful Actions run URL** (and PR link if opened) into maintainer notes or a PR description — same expectations as the **Final Wave Factory validation checklist** block below.
3. **`gh` CLI:** not authenticated in this environment; for **good first issue** triage use the web UI: https://github.com/KR8ZYSHO3/Universal-Science-Discovery/issues?q=is%3Aopen+label%3A%22good+first+issue%22

## Next steps

- Merge Phase A PR, then rebase or merge **`feat/dashboard-ux-polish`** onto updated **`main`** and open a second PR for Phase B.
- After any **`STATE.md`** edit that should appear in the Cursor canvas, run **`python scripts/sync-dashboard-from-state.py`**.

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

**Phase A** is merged on **`origin/main`** (**`e01d55a`**, PR #244). **`feat/dashboard-ux-polish`** was **rebased onto `origin/main`** (duplicate Phase A commits dropped as already-upstream); it carries incremental Phase B polish plus README / playbook / STATE updates.

**Bounded content wave:** **`gh` is not authenticated** in the agent environment; **`drafts/bridges/`** holds **18** OpenAlex stubs — **not auto-promoted** without maintainer review. Companion branch **`content/phase1-bounded-wave-1`** (separate PR from `main`) documents **deferral** only (`CHANGELOG` + this append). When **`gh auth login`** is available, triage **good first issue**: https://github.com/KR8ZYSHO3/Universal-Science-Discovery/issues?q=is%3Aopen+label%3A%22good+first+issue%22

### PR / compare links

| Branch | Purpose | Compare |
|--------|---------|---------|
| **`feat/dashboard-ux-polish`** | Hub UX + docs hygiene | `https://github.com/KR8ZYSHO3/Universal-Science-Discovery/compare/main...feat/dashboard-ux-polish` |
| **`content/phase1-bounded-wave-1`** | Content wave deferral note (no new catalog YAML this session) | `https://github.com/KR8ZYSHO3/Universal-Science-Discovery/compare/main...content/phase1-bounded-wave-1` |

### Catalog truth (reproducible)

`python scripts/verify_dashboard_consistency.py` → **bridges=1123, unknowns=1408, hypotheses=1274, phenomena=10, graph_nodes=3857, graph_edges=4517** (matches `docs/knowledge_graph.json` meta).
