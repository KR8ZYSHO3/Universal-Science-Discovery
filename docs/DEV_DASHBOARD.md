# Developer dashboard (USDR meta)

Human- and agent-editable checklist for **repository operations** — not scientific output. Canonical narrative status lives in [.planning/STATE.md](../.planning/STATE.md) at the repo root.

## HTML dashboard (browser)

For a **single web page** for **contributors**: ordered “start here” path, links to policies and to **`unknowns-catalog/`** / **`hypotheses/`**, plus maintainer **live** `STATE` + `ROADMAP` when served locally — use [`dashboard/index.html`](../dashboard/index.html). The page includes optional **light/dark** theme, sticky section nav with scroll highlight, and loads **Google Fonts** / **`marked`** / **lunr** / **d3** from CDNs when online — see [`dashboard/README.md`](../dashboard/README.md). From the repo root run `python -m http.server 8765`, then open [`dashboard/index.html`](../dashboard/index.html) (URL `http://localhost:8765/dashboard/`).

The Cursor Canvas at [`canvases/Progress.canvas.tsx`](../canvases/Progress.canvas.tsx) is optional; the HTML hub is the main browser entry for people exploring the repo. **Agents:** `.cursor/rules/documentation-and-dashboard.mdc` (always on) requires keeping docs, CHANGELOG, STATE, and this hub aligned — especially at milestones — and spot-checking the hub after hub-affecting edits.

### Planned UX — catalog search → graph highlight → GitHub (Phase A)

**Not implemented yet.** Target flow: from **catalog search** in the hub, jump to a **knowledge-graph** view that highlights the selected record, with a clear **“open on GitHub”** path to the source YAML. Track and break down work on a dedicated **`feat/dashboard-search-graph-flow`** branch or issue when you split implementation from docs-only PRs; keep CDN-heavy hub changes behind the usual local `http://localhost:8765/dashboard/` smoke check.

---

## Contributor hub maintenance playbook (methodical)

Use this so **`dashboard/index.html`**, generated HTML, API JSON, and **README headline metrics** do not drift from the YAML catalog.

### 1) What changed? → What to refresh

| You edited… | Refresh / run… |
|-------------|----------------|
| `unknowns-catalog/`, `hypotheses/`, `cross-domain/`, `phenomenology/` | `python scripts/validate_schemas.py` → rebuild graph (below) → `python scripts/update_dashboard_stats.py --apply` → update **README** table + **CHANGELOG** if counts changed materially |
| Any catalog YAML (above) | `python -X utf8 scripts/build_graph.py` (or rely on **`build-graph.yml`** on `main`) so `docs/knowledge_graph.json` matches git |
| `breakthrough-gaps/bg-*.yaml` | `python scripts/render_breakthrough_gaps_hub.py --apply` and `python scripts/generate_api.py` (also triggered from **`build-graph.yml`** when those paths change) |
| `unknowns-catalog/` or bridge `fields` without folder moves | `python scripts/generate_domain_pages.py` then `python scripts/verify_domain_pages.py` |
| `.planning/STATE.md` | `python scripts/sync-dashboard-from-state.py` (updates Canvas snapshot constants) |
| `dashboard/index.html` hero pills / snapshot only (no YAML change) | Run **`python scripts/verify_dashboard_consistency.py`** before merge — it fails if numbers disagree with disk |
| `docs/preprint/usdr_preprint.md` | `python scripts/render_preprint_html.py --apply` |
| `docs/` or `mkdocs.yml` | `mkdocs build --strict` |
| Milestone ring / `MS` JavaScript array in the hub | Align manually with **`ROADMAP.md`** Phase 1 — not auto-generated today |

**GitHub Actions:** On `main`, **`build-graph.yml`** rebuilds the graph, regenerates **`api/v1/`**, runs **`update_dashboard_stats.py --apply`**, domain/breakthrough renderers as configured, and opens the PR path for catalog batches. **`pages.yml`** publishes the hub and writes **`dashboard/deploy-info.json`** for freshness. PRs still need locally consistent HTML if you touch **`dashboard/index.html`** without waiting for that bot loop.

### 2) Standard “catalog batch” command order (local)

Run from the repo root when you are not relying solely on CI:

```bash
python scripts/validate_schemas.py
python -X utf8 scripts/build_graph.py
python scripts/generate_api.py
python scripts/update_dashboard_stats.py --apply
python scripts/render_breakthrough_gaps_hub.py --apply
python scripts/generate_domain_pages.py
python scripts/verify_domain_pages.py
python scripts/verify_dashboard_consistency.py
```

Then update **README** metrics table if totals moved, **CHANGELOG** (Unreleased), and **`.planning/STATE.md`** when maintainers need the story.

### 3) Before merge checklist (human or agent)

- [ ] `python scripts/verify_dashboard_consistency.py` passes (CI runs this in **`validate-schemas.yml`**).
- [ ] Served hub sanity check: `python -m http.server 8765` → open **`/dashboard/`**, confirm sections load and links you touched work.
- [ ] If `docs/` changed: `mkdocs build --strict`.

### 4) Automation reference

| Script | Role |
|--------|------|
| [`scripts/update_dashboard_stats.py`](../scripts/update_dashboard_stats.py) | Single source of truth for **pill**, **snap-***, **stat-***, OG/Twitter, API blurbs tied to catalog + graph |
| [`scripts/verify_dashboard_consistency.py`](../scripts/verify_dashboard_consistency.py) | Guardrail: YAML/graph vs dashboard numbers |
| [`scripts/sync-dashboard-from-state.py`](../scripts/sync-dashboard-from-state.py) | STATE → Canvas embed |

See also [DOC_MAP.md](DOC_MAP.md) § Scripts and [scripts/README.md](../scripts/README.md).

---

## Editing workflow (STATE + Canvas)

1. **Update state** — Open `.planning/STATE.md` and adjust the stable sections (`Last updated`, `Current focus`, branches/PR bullets with compare URLs, shipped items, blockers, next actions).

2. **Refresh the Cursor Canvas** — Constants in [`canvases/Progress.canvas.tsx`](../canvases/Progress.canvas.tsx) are a snapshot mirror of STATE (Canvas cannot read disk). After editing STATE, regenerate that block:

   ```bash
   python scripts/sync-dashboard-from-state.py
   ```

3. **Open the Canvas in Cursor** — Open `canvases/Progress.canvas.tsx` in the editor and use Cursor’s Canvas affordance (“Open Canvas” / canvas panel beside the chat) so the dashboard renders live. If the Canvas entry point is unavailable, editing STATE plus the snippet in the canvas source still keeps the checklist useful.

## Complementary tooling

The GSD **`/gsd-progress`** command (via your Cursor GSD workspace setup) complements this file set: `/gsd-progress` answers situational workflow status; `.planning/STATE.md` is the narrative checklist you trim next to MkDocs policy docs.

Integrity and licensing expectations for substantive work remain in [LEGAL.md](../LEGAL.md), the [documentation map](DOC_MAP.md), and Cursor rules — this dashboard stays **meta** (branches, docs, ingestion milestones).
