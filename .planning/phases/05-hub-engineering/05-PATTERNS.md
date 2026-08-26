# Phase 5: Hub engineering - Pattern Map

**Mapped:** 2026-08-26
**Files analyzed:** 16 (3 create, 13 modify)
**Analogs found:** 16 / 16

Phase 5 is **copy-the-orphan-panel**, not a recommender system. Clone the shipped pipeline: Python exporter → committed static JSON under `api/v1/` → hub IIFE `fetch` → table / empty / `aria-live` status, with honesty copy that this is contributor tooling. Rank **bridges** by **unweighted undirected degree** (copy the four-line loop from `top_nodes_by_degree`; filter `type == "bridge"`). Harvest/curator are spec-only future slots.

Primary assignment (one plan **05-01**):

- `docs/HUB_RECOMMENDATIONS.md` (new spec) + `scripts/export_recommendations.py` → `api/v1/recommendations.json`
- `dashboard/index.html` `#recommendations` immediately after `#orphan-xref-panel`
- `scripts/generate_api.py` `endpoints["recommendations"]` (does **not** write the panel JSON)
- `.github/workflows/build-graph.yml` one `run:` after orphan export
- `tests/repo_smoke/test_catalog_regression.py::test_recommendations_json`
- `mkdocs.yml` nav + playbook/docs/CHANGELOG

---

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|-------------------|------|-----------|----------------|---------------|
| `docs/HUB_RECOMMENDATIONS.md` | config | file-I/O | `docs/BREAKTHROUGH_GAPS.md` (purpose / regenerate / related) + `docs/DEV_DASHBOARD.md` Phase C stub (lines 19–29) | role-match |
| `scripts/export_recommendations.py` | utility | transform + file-I/O | `scripts/export_orphan_xref_panel.py` (header, GitHub URLs, cap, `generated_at`, JSON write) + `scripts/build_graph.py` `top_nodes_by_degree` (degree loop) | exact |
| `api/v1/recommendations.json` | model | file-I/O | `api/v1/orphan_xref_panel.json` (`generated_at`, `source`, `items[]`, `meta`) | exact |
| `dashboard/index.html` | component | request-response | Same file: `#orphan-xref-panel` HTML (1975–2022), CSS (913–975), IIFE (4862–4966), sticky nav (1666), `#developer-api` (2547–2550) | exact |
| `scripts/generate_api.py` | utility | transform | Same file: docstring bullet + `endpoints["orphan_xref_panel"]` (does **not** copy the panel file) | exact |
| `api/v1/meta.json` | model | file-I/O | Same file `endpoints` map — **writer is `generate_api.py`**, not a hand edit | exact |
| `.github/workflows/build-graph.yml` | config | batch | Same file: `Export orphan xref panel JSON` step + PR body bullet + `add-paths: api/**` | exact |
| `tests/repo_smoke/test_catalog_regression.py` | test | file-I/O | Same file `test_orphan_xref_panel_json` (shape, cap, ids; no subprocess exporter) | exact |
| `mkdocs.yml` | config | file-I/O | Same file `nav` → Operations → `Dev dashboard: DEV_DASHBOARD.md` (line 56); `validation.nav.omitted_files: warn` + `strict: true` | exact |
| `docs/DEV_DASHBOARD.md` | config | file-I/O | Same file Phase C stub + playbook table row + catalog-batch command for orphan export | exact |
| `CHANGELOG.md` | config | file-I/O | Same file `## [Unreleased]` “Added — Dashboard orphan / xref hygiene panel (2026-05-15)” | exact |
| `dashboard/README.md` | config | file-I/O | Same file xref honesty line (line 11) | exact |
| `docs/DOC_MAP.md` | config | file-I/O | Same file Scripts table row for `export_orphan_xref_panel.py` | exact |
| `docs/REPOSITORY_MANIFEST.md` | config | file-I/O | Same file scripts row for `export_orphan_xref_panel.py` | exact |
| `scripts/README.md` | config | file-I/O | Same file orphan-export bullet (line 9) | exact |
| `.planning/STATE.md` | config | file-I/O | Same file Current focus / last activity (after merge-worthy work) | role-match |

**Do not create/modify (keep as analog / freeze):**

| File | Why it is off-limits |
|------|----------------------|
| `scripts/build_graph.py` | Degree loop analog only. Do **not** call `top_nodes_by_degree(..., n=25)` as a black box (ranks all node types). |
| `docs/knowledge_graph.json` | Degree **input**. Do not rebuild in this phase; exporter json-loads the committed file. |
| `api/v1/graph.json` | Do not fetch from the recommendations IIFE (D-03). |
| `api/v1/bridge_proposals.json` / `scripts/propose_bridges.py` | Different product (missing-ID proposals vs existing high-degree bridges). |
| `scripts/harvesters/wave_factory.py` | Harvest **future slot** language only (`RankedCandidate`). Do not compute harvest in v1. |
| `dashboard/index.html` `#crosscheck`, D3 graph, hero pills, `id="snap-` / `id="stat-` | D-05 / D-11. Consistency script only checks those counts. |
| `scripts/build_crosscheck.py` | Do **not** `--apply`. Crosscheck markers must not change. |
| `repro/**`, epidemic freeze, `crosscheck-repro.yml` | D-10. Phase 4 closed TRUST-02/03. |
| NetworkX / new pip extra / React / design-system CSS file | Not in smoke CI; analog is stdlib + existing tokens. |

---

## Pattern Assignments

### `docs/HUB_RECOMMENDATIONS.md` (config, file-I/O) — CREATE

**Analog (structure):** `docs/BREAKTHROUGH_GAPS.md` lines 1–39 — purpose, where artifacts live, regenerate command, related docs.

**Analog (honesty + Phase C language):** `docs/DEV_DASHBOARD.md` lines 19–29.

**Structure to copy:**

```markdown
# Hub recommendations — contributor tooling (not a scientific ranking)

**Purpose:** Suggest high-leverage **existing** bridges to inspect or extend.
This list is **contributor tooling**, not a scientific ranking of unknowns,
and not a CONFIRMED or INCONCLUSIVE Crosscheck outcome.

## Signals

### Connectivity (v1, computed)
Undirected degree in the filtered knowledge graph (`docs/knowledge_graph.json`).
Each edge increments both endpoints by 1. Isolates score 0 and drop out of top-25.
`ranking` JSON value: `undirected_degree`.

### Harvest (future, not computed)
Later join from Wave Factory (`citation_score`, `recency_score`, `novelty_score`
in `scripts/harvesters/wave_factory.py`). v1 items **omit** the field.

### Curator score (future, not computed)
Optional maintainer overlay. No such field exists today. v1 **omits** it.

## Prototype
- JSON: `api/v1/recommendations.json` (cap 25)
- Exporter: `python scripts/export_recommendations.py`
- Hub: `dashboard/index.html` `#recommendations`
- CI: `build-graph.yml` immediately after `export_orphan_xref_panel.py`

## Non-goals
Personalization, browser graph math, ML, feeding `RESULT: CONFIRMED` into scores.
```

**MkDocs:** new `docs/` file **must** be in `mkdocs.yml` `nav` (`omitted_files: warn` + `strict: true`). Place under Operations next to Dev dashboard:

```yaml
      - Dev dashboard: DEV_DASHBOARD.md
      - Hub recommendations: HUB_RECOMMENDATIONS.md
```

**Link from:** `docs/DEV_DASHBOARD.md` when promoting the Phase C stub.

---

### `scripts/export_recommendations.py` (utility, transform + file-I/O) — CREATE

**Analog (script skeleton):** `scripts/export_orphan_xref_panel.py` (entire file, 202 lines).

**Analog (degree increment):** `scripts/build_graph.py` `top_nodes_by_degree` lines 184–200.

**Analog (YAML path for bridges):** `scripts/generate_api.py` lines 60–61 `(ROOT / "cross-domain").rglob("b-*.yaml")` — **not** `_unknown_yaml_path` (that walks `unknowns-catalog`).

**Do not** `import build_graph` unless you need `bg.ROOT`. Prefer stdlib-only: json-load `docs/knowledge_graph.json`. PyYAML is not required for this exporter. Do **not** import NetworkX. Do **not** call `build_graph()` live (slower; can drift from the committed file). Do **not** call `top_nodes_by_degree(nodes, edges, n=25)` — that helper is type-agnostic and can drop bridges from a mixed top-25.

**Imports / paths pattern** (orphan exporter lines 1–32, adapted — drop `import build_graph`):

```python
#!/usr/bin/env python3
"""Export a small JSON panel for the contributor hub: high-degree bridges.

Ranks existing bridge nodes by undirected degree in ``docs/knowledge_graph.json``
(same increment as ``build_graph.top_nodes_by_degree``; bridges only).
Does **not** walk the graph in the browser — output is static
``api/v1/recommendations.json`` for the hub to fetch.

Usage (from repo root)::

    python scripts/export_recommendations.py

See ``docs/HUB_RECOMMENDATIONS.md`` and ``docs/DEV_DASHBOARD.md``.
"""
from __future__ import annotations

import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API_OUT = ROOT / "api" / "v1" / "recommendations.json"
KG_PATH = ROOT / "docs" / "knowledge_graph.json"

GITHUB_OWNER = "KR8ZYSHO3"
GITHUB_REPO = "Universal-Science-Discovery"
GITHUB_BRANCH = "main"

MAX_ITEMS = 25
```

**GitHub URL helpers** (orphan exporter lines 39–45) — copy verbatim:

```python
def _github_blob(rel_path: str) -> str:
    return f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/blob/{GITHUB_BRANCH}/{rel_path}"


def _github_filename_search(node_id: str) -> str:
    q = f"filename:{node_id}.yaml"
    return f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/search?q={q}&type=code"
```

**Bridge YAML path** (orphan `_unknown_yaml_path` lines 83–87, retarget `cross-domain`):

```python
def _bridge_yaml_path(node_id: str) -> str | None:
    matches = list((ROOT / "cross-domain").rglob(f"{node_id}.yaml"))
    if not matches:
        return None
    return matches[0].relative_to(ROOT).as_posix()
```

**Degree loop** (`scripts/build_graph.py` lines 189–192) plus orphan’s defensive source/target decode (lines 99–106). Committed graph edges use **string** `source`/`target`; no `weight` key.

```python
degree: dict[str, int] = defaultdict(int)
for edge in edges:
    s, t = edge.get("source"), edge.get("target")
    sid = s if isinstance(s, str) else (s or {}).get("id", "")
    tid = t if isinstance(t, str) else (t or {}).get("id", "")
    if sid:
        degree[sid] += 1
    if tid:
        degree[tid] += 1

bridges = [
    n for n in nodes
    if n.get("type") == "bridge" and str(n.get("id", "")).startswith("b-")
]
ranked = sorted(bridges, key=lambda n: (-degree.get(n["id"], 0), n["id"]))[:MAX_ITEMS]
```

**Payload header** (orphan `main()` lines 182–198) plus D-04 keys `ranking` and `disclaimer`. **Omit** `harvest_rank` / `curator_score` on items (D-02 allows null/omit; omit keeps the contract smaller).

```python
def main() -> int:
    generated = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    items = build_items()  # len <= 25
    payload = {
        "generated_at": generated,
        "source": (
            "scripts/export_recommendations.py "
            "(undirected degree from docs/knowledge_graph.json; "
            "same increment as build_graph.top_nodes_by_degree; bridges only)"
        ),
        "ranking": "undirected_degree",
        "disclaimer": (
            "Contributor tooling, not a scientific ranking and not a "
            "CONFIRMED or INCONCLUSIVE Crosscheck outcome. "
            "score is undirected catalog-graph degree (connectivity only). "
            "Harvest rank and curator score are specified for a later phase and are not computed here."
        ),
        "items": items,
        "meta": {
            "item_cap": MAX_ITEMS,
            "ranking_computed": "undirected_degree",
            "ranking_future_slots": ["harvest", "curator_score"],
        },
    }
    API_OUT.parent.mkdir(parents=True, exist_ok=True)
    API_OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {API_OUT.relative_to(ROOT)} ({len(items)} items)")
    return 0
```

**Per-item shape:**

```python
{
    "id": node["id"],                          # b-…
    "title": (node.get("title") or "").strip(),  # full title; do not truncate
    "score": int(degree.get(node["id"], 0)),
    "kind": "bridge",
    "github_blob_url": _github_blob(ypath) if ypath else None,
    "github_search_url": _github_filename_search(node["id"]),
}
```

If no YAML file, blob `None`, search URL still set (orphan orphan-unknown items do the same).

**Error handling:** If `docs/knowledge_graph.json` is missing, orphan’s `collect_orphan_unknowns` returns `[]`. For recommendations, fail loudly in `main()` (print + non-zero) — empty top-25 would hide a missing graph. Empty `items` after a successful load is valid (all isolates) and the hub empty-state already covers it.

---

### `api/v1/recommendations.json` (model, file-I/O) — CREATE (exporter output)

**Analog:** `api/v1/orphan_xref_panel.json` lines 1–4 (`generated_at`, `source`, `items`).

**Writer:** `scripts/export_recommendations.py` only. `generate_api.py` must **not** copy/write this file (it lists `orphan_xref_panel` in `endpoints` but never writes that file — lines 5–16, 142–151, 154–187).

**Contract extras vs analog:** `ranking` (string `"undirected_degree"`), `disclaimer` (honesty paragraph). Item keys: `id`, `title`, `score` (int), `kind: "bridge"`, GitHub URLs. Cap ≤ 25.

Do **not** pin specific ids or scores in tests (graph will move). Empirical sanity for implementers only (2026-06-21 export): `b-boltzmann-shannon-entropy` degree 12, `b-self-organized-criticality` 11, `b-criticality-neuroscience` 8.

---

### `dashboard/index.html` (component, request-response) — MODIFY

**Analog:** same file. Clone four slices. Do **not** redesign nav, hero, Crosscheck grid, or graph. Dark theme only (`<html … data-theme="dark">` line 2). Copy tokens `--surface`, `--border`, `--muted`, `--accent`, `--teal`, `--mono`.

**Placement:** new `<section id="recommendations">` **immediately after** `#orphan-xref-panel` (ends line 2022), **before** `#discovery-engines` (line 2024).

#### 1) CSS — copy orphan block as `.rec-*` (lines 913–975)

Prefer a copied `.rec-*` block (not shared `.orphan-xref-*` classes) so a later hygiene restyle does not hit recommendations. Same tokens, same reduced-motion spinner rule.

```css
    /* ── RECOMMENDATIONS PANEL (contributor tooling, not a ranking) ─ */
    .rec-panel { max-width: min(1100px, 94vw); margin: 0 auto; }
    .rec-foot {
      font-size: .78rem;
      color: var(--muted);
      margin-top: .75rem;
      font-family: var(--mono);
    }
    .rec-table-wrap {
      overflow-x: auto;
      border: 1px solid var(--border);
      border-radius: var(--r);
      background: var(--surface);
      margin-top: 1rem;
    }
    .rec-table { width: 100%; border-collapse: collapse; font-size: .84rem; }
    .rec-table th, .rec-table td {
      padding: .55rem .65rem;
      border-bottom: 1px solid var(--border);
      text-align: left;
      vertical-align: top;
    }
    .rec-table th {
      font-size: .72rem;
      text-transform: uppercase;
      letter-spacing: .06em;
      color: var(--muted);
      font-weight: 600;
      white-space: nowrap;
    }
    .rec-table tr:last-child td { border-bottom: none; }
    .rec-score { font-family: var(--mono); color: var(--teal); white-space: nowrap; }
    .rec-actions { white-space: nowrap; }
    .rec-actions a { margin-right: .5rem; }
    .rec-status { min-height: 1.25rem; font-size: .82rem; color: var(--muted); margin-top: .5rem; }
```

Spinner: copy `.orphan-xref-status[aria-busy="true"] .orphan-xref-spinner` as `.rec-status[aria-busy="true"] .rec-spinner` including the `prefers-reduced-motion` override (lines 962–975).

#### 2) HTML section — clone `#orphan-xref-panel` (lines 1975–2022)

Honesty copy must include **not a scientific ranking** and **not a CONFIRMED/INCONCLUSIVE outcome**. Do not mix Crosscheck RESULT tokens into this section.

```html
    <section id="recommendations" class="aos">
      <div class="rec-panel">
        <span class="section-tag">Contributor tooling</span>
        <h2 class="section-title">High-connectivity bridges</h2>
        <p class="section-desc">
          Read-only list of existing bridges ranked by undirected catalog-graph degree
          (not a scientific ranking and not a CONFIRMED or INCONCLUSIVE Crosscheck outcome).
          Higher degree means more catalog links — leverage for a contributor looking where to connect next.
          Harvest rank and curator score are specified for a later phase and are not computed here.
          See <a href="https://github.com/KR8ZYSHO3/Universal-Science-Discovery/blob/main/docs/HUB_RECOMMENDATIONS.md" …>docs/HUB_RECOMMENDATIONS.md</a>.
        </p>
        <p id="recommendations-status" class="rec-status" role="status" aria-live="polite" aria-busy="true">
          <span class="rec-spinner" aria-hidden="true"></span>Loading recommendations…
        </p>
        <div id="recommendations-empty" …>No rows in this export (or JSON not found).</div>
        <div id="recommendations-table-wrap" class="rec-table-wrap" style="display:none;">
          <table class="rec-table" aria-label="High-connectivity bridges">
            <thead>
              <tr>
                <th scope="col">Score</th>
                <th scope="col">Bridge</th>
                <th scope="col">Links</th>
              </tr>
            </thead>
            <tbody id="recommendations-tbody"></tbody>
          </table>
        </div>
        <p id="recommendations-foot" class="rec-foot" style="display:none;"></p>
      </div>
    </section>
```

Columns: **Score · Bridge (title + `b-` id) · Links**. Table, not cards (orphan uses `<table class="orphan-xref-table">`).

#### 3) Fetch IIFE — clone lines 4862–4966

Replace IDs `orphan-xref-*` → `recommendations-*`. Fetch **only** `recommendations.json` (never `graph.json`). Safe sink: `createElement` + `textContent`. **Never** `innerHTML` for `item.title`.

**Security overlay (orphan analog does not check URL prefix; RESEARCH requires it):** set `a.href` only when the URL starts with `https://github.com/`. Keep `target="_blank"` + `rel="noopener"`.

```javascript
  <script>
  /* Recommendations panel — static JSON (no graph walk in browser) */
  (function () {
    var statusEl = document.getElementById('recommendations-status');
    var emptyEl = document.getElementById('recommendations-empty');
    var wrapEl = document.getElementById('recommendations-table-wrap');
    var tbody = document.getElementById('recommendations-tbody');
    var footEl = document.getElementById('recommendations-foot');
    if (!statusEl || !tbody) return;

    function apiBase() {
      var loc = window.location.href;
      if (loc.indexOf('github.io') !== -1) return 'https://kr8zysho3.github.io/Universal-Science-Discovery/';
      if (loc.indexOf('/dashboard/') !== -1) return loc.replace(/dashboard\/.*$/, '');
      return '../';
    }
    var paths = [
      apiBase() + 'api/v1/recommendations.json',
      '../api/v1/recommendations.json'
    ];

    function done(msg, busy) {
      statusEl.textContent = msg || '';
      statusEl.setAttribute('aria-busy', busy ? 'true' : 'false');
    }

    function tryFetch(i) {
      if (i >= paths.length) {
        done('Could not load recommendations JSON (offline or missing file).', false);
        if (emptyEl) emptyEl.style.display = 'block';
        return;
      }
      fetch(paths[i])
        .then(function (r) { return r.ok ? r.json() : Promise.reject(new Error(String(r.status))); })
        .then(function (data) {
          var items = (data && Array.isArray(data.items)) ? data.items : [];
          /* render rows with textContent; github href iff starts with https://github.com/ */
        })
        .catch(function () { tryFetch(i + 1); });
    }
    tryFetch(0);
  })();
  </script>
```

Row cells (copy sink from lines 4915–4954):

```javascript
tdScore.textContent = String(item.score);
tdTitle.textContent = item.title || item.id || '';
code.textContent = item.id;
aSearch.href = item.github_search_url;  // only if indexOf('https://github.com/') === 0
aSearch.textContent = 'View on GitHub';
aSearch.target = '_blank';
aSearch.rel = 'noopener';
```

Footer: `Generated:` + `ranking=undirected_degree` + cap (from `data.ranking` / `data.meta.item_cap`). Skip non-object items.

#### 4) Sticky nav — analog completeness, not a redesign

Orphan has a nav link at line 1666. Add **one** `<a>` immediately after Xref hygiene. Do **not** restyle or reorder other links. Skip first-contrib checklist (`#start`) changes.

```html
      <a href="#orphan-xref-panel" title="Broken cross-reference targets you can fix in a pull request">Xref hygiene</a>
      <a href="#recommendations" title="Existing bridges ranked by catalog-graph degree — contributor tooling, not a scientific ranking">Recommendations</a>
      <a href="#discovery-engines">Engines</a>
```

Planner may drop the `<a>` if they read D-05 strictly; section id remains `#recommendations`.

#### 5) `#developer-api` — clone orphan row (lines 2547–2550)

```html
        <a href="../api/v1/recommendations.json" class="api-endpoint" target="_blank" rel="noopener">
          <code>GET /api/v1/recommendations.json</code>
          <span>Capped list of existing bridges ranked by undirected graph degree (contributor tooling; regenerate via export script)</span>
          <span class="api-endpoint-badge">~8 KB</span>
        </a>
```

Place after the orphan_xref_panel row. Badge size is approximate; do not invent precision.

**Do not touch:** `id="snap-`, `id="stat-`, hero pills, Crosscheck marker blocks, D3 graph IIFE.

**After HTML/stats edits:** `python scripts/verify_dashboard_consistency.py` (D-11). It only checks count alignment — still run it; do not treat a pass as proof the new IIFE works. Manual: `python -m http.server 8765` → `http://localhost:8765/dashboard/#recommendations`.

---

### `scripts/generate_api.py` (utility, transform) — MODIFY

**Analog:** same file. Panel JSON is **not** written here.

**Pitfall:** `endpoints` is a hardcoded dict (lines 142–151). Next graph-bot run **drops** unknown keys. `pages.yml` only patches `pages_deploy` onto existing `meta.json`.

**Required edits (same change):**

1. Docstring bullet after the orphan line (line 14):

```python
  api/v1/recommendations.json — hub panel: high-degree bridges (see export_recommendations.py)
```

2. `endpoints` dict (after `orphan_xref_panel`):

```python
            "orphan_xref_panel": "api/v1/orphan_xref_panel.json",
            "recommendations": "api/v1/recommendations.json",
```

Do **not** add a `shutil.copy2` for `recommendations.json` (orphan is not copied either). `write_json(API_DIR / "meta.json", meta)` remains the only `meta.json` `endpoints` writer.

---

### `api/v1/meta.json` (model, file-I/O) — MODIFY via generate_api.py

**Analog:** same file `endpoints` (lines 15–24). After `python scripts/generate_api.py`, expect:

```json
    "orphan_xref_panel": "api/v1/orphan_xref_panel.json",
    "recommendations": "api/v1/recommendations.json"
```

Do not hand-edit `meta.json` as the source of truth — regenerate so the bot loop cannot regress the key.

---

### `.github/workflows/build-graph.yml` (config, batch) — MODIFY

**Analog:** same file, step immediately after orphan export (lines 45–46).

```yaml
      - name: Export orphan xref panel JSON
        run: python scripts/export_orphan_xref_panel.py

      - name: Export recommendations JSON
        run: python scripts/export_recommendations.py
```

Also add a PR-body bullet next to the orphan line (line 91):

```yaml
            - `api/v1/orphan_xref_panel.json` (xref hygiene hub panel)
            - `api/v1/recommendations.json` (hub recommendations panel)
```

**Do not** add the script to `on.push.paths` (orphan exporter is not listed there either). `add-paths: api/**` (line 108) already covers the JSON. Do not bump `actions/checkout@v7` / `setup-python@v6` / Python 3.11.

---

### `tests/repo_smoke/test_catalog_regression.py` (test, file-I/O) — MODIFY

**Analog:** `test_orphan_xref_panel_json` lines 47–58. Add a sibling function. Do **not** subprocess-run the exporter (orphan test does not). Do **not** pin ids/scores. Do **not** import NetworkX. Do **not** add a JSON Schema file (orphan has none; smoke is the contract).

```python
def test_recommendations_json() -> None:
    """Committed hub recommendations JSON parses and matches the export contract."""
    path = REPO_ROOT / "api" / "v1" / "recommendations.json"
    assert path.is_file(), "api/v1/recommendations.json missing — run scripts/export_recommendations.py"
    data = json.loads(path.read_text(encoding="utf-8"))
    for key in ("generated_at", "source", "ranking", "disclaimer", "items"):
        assert key in data
    assert data["ranking"] == "undirected_degree"
    assert isinstance(data["items"], list)
    assert len(data["items"]) <= 25
    for item in data["items"]:
        assert str(item.get("id", "")).startswith("b-")
        assert item.get("kind") == "bridge"
        assert isinstance(item.get("score"), int)
        assert item.get("github_search_url") or item.get("github_blob_url")
```

Optionally (RESEARCH validation map):

```python
    meta = json.loads((REPO_ROOT / "api" / "v1" / "meta.json").read_text(encoding="utf-8"))
    assert meta.get("endpoints", {}).get("recommendations") == "api/v1/recommendations.json"
```

Update the module docstring (lines 1–5) to mention the new shape check.

**Quick command:** `python -m pytest tests/repo_smoke/test_catalog_regression.py::test_recommendations_json -q`

`.github/workflows/validate-schemas.yml` already runs `python -m pytest tests/repo_smoke` with no path filter — no workflow edit.

---

### `mkdocs.yml` (config, file-I/O) — MODIFY

**Analog:** `nav` Operations block line 56; CHANGELOG Unreleased already records adding omitted files so `--strict` passes.

```yaml
  - Operations:
      - Operating rhythm: OPERATING_RHYTHM.md
      …
      - Dev dashboard: DEV_DASHBOARD.md
      - Hub recommendations: HUB_RECOMMENDATIONS.md
      - Optional GSD tooling: GSD_INTEGRATION.md
```

Gate: `mkdocs build --strict`. Warning treated as error via `validation.nav.omitted_files: warn` (lines 120–128) + `strict: true`.

---

### `docs/DEV_DASHBOARD.md` (config, file-I/O) — MODIFY

**Analog:** same file.

1. **Promote Phase C stub** (lines 19–29): “Smart recommendations” moves from planned table to a **Shipped (thin slice)** paragraph like orphan/xref. Leave harvest/curator as future slots. Link `docs/HUB_RECOMMENDATIONS.md`.

2. **Playbook table** (after orphan row, line 47):

```markdown
| `api/v1/recommendations.json` (hub recommendations panel) | `python scripts/export_recommendations.py` (runs in **`build-graph.yml`** after orphan export) |
```

3. **Catalog-batch command order** (after line 61):

```bash
python scripts/export_orphan_xref_panel.py
python scripts/export_recommendations.py
python scripts/generate_api.py
```

---

### `CHANGELOG.md` (config, file-I/O) — MODIFY

**Analog:** `## [Unreleased]` “Added — Dashboard orphan / xref hygiene panel (2026-05-15)” lines 46–51.

Prepend under Unreleased (do not collide with Crosscheck bullets already there):

```markdown
### Added — Hub recommendations thin slice (HUB-01)
- **`docs/HUB_RECOMMENDATIONS.md`:** ranking spec (connectivity / harvest / curator); v1 computes undirected degree only. Contributor tooling, not a scientific ranking.
- **`scripts/export_recommendations.py`:** writes **`api/v1/recommendations.json`** (≤25 bridges by undirected degree).
- **`dashboard/index.html`:** `#recommendations` table fetch (clone of xref hygiene panel).
- **`build-graph.yml`:** export step after orphan panel.
- **`api/v1/meta.json`:** `endpoints.recommendations`; **`scripts/generate_api.py`** keeps the key.
- **Docs:** **`docs/DEV_DASHBOARD.md`**, **`docs/DOC_MAP.md`**, **`docs/REPOSITORY_MANIFEST.md`**, **`scripts/README.md`**, **`dashboard/README.md`**, **`mkdocs.yml`** nav.
```

---

### `dashboard/README.md` (config, file-I/O) — MODIFY

**Analog:** honesty line 11. Add a sibling bullet:

```markdown
- **Recommendations panel:** static **`api/v1/recommendations.json`** (regenerate with **`python scripts/export_recommendations.py`**) lists ≤25 existing bridges by undirected graph degree — contributor tooling, not a scientific ranking and not a Crosscheck outcome.
```

---

### `docs/DOC_MAP.md` / `docs/REPOSITORY_MANIFEST.md` / `scripts/README.md` (config, file-I/O) — MODIFY

**Analog rows to clone:**

`docs/DOC_MAP.md` Scripts table line 51:

```markdown
| `scripts/export_recommendations.py` | Writes **`api/v1/recommendations.json`** for the hub recommendations panel (undirected degree, bridges only) | ✅ (build-graph.yml, after orphan export) |
```

Bump DOC_MAP “Last updated” (line 5).

`docs/REPOSITORY_MANIFEST.md` line 73 sibling:

```markdown
| [scripts/export_recommendations.py](../scripts/export_recommendations.py) | Tool | Writes `api/v1/recommendations.json` for the hub recommendations panel | [docs/HUB_RECOMMENDATIONS.md](HUB_RECOMMENDATIONS.md), `.github/workflows/build-graph.yml` |
```

Also add a policy-doc row for `docs/HUB_RECOMMENDATIONS.md` if the Policy documents table is the home for specs (BREAKTHROUGH_GAPS.md pattern in DOC_MAP line 31).

`scripts/README.md` line 9 sibling:

```markdown
- **Recommendations hub export:** `python scripts/export_recommendations.py` — writes **`api/v1/recommendations.json`** for the contributor hub panel (runs in **`build-graph.yml`** after the orphan export).
```

---

### `.planning/STATE.md` (config, file-I/O) — MODIFY after merge-worthy work

**Analog:** same file Current focus / last activity (lines 9–18). Update when 05-01 lands — not a blocker for the code slice. Do **not** treat GSD artifacts as scientific evidence.

---

## Shared Patterns

### Static panel exporter (Python → committed JSON)

**Source:** `scripts/export_orphan_xref_panel.py`
**Apply to:** `scripts/export_recommendations.py`

- Shebang + module docstring with `Usage (from repo root)::`
- `ROOT` via `Path(__file__).resolve().parents[1]`
- GitHub URL constants `KR8ZYSHO3` / `Universal-Science-Discovery` / `main`
- Cap constant; `generated_at` ISO-8601 Z with microseconds stripped
- `json.dumps(..., indent=2, ensure_ascii=False) + "\n"`
- Print `Wrote {rel} ({n} items)`; `raise SystemExit(main())`

### Degree = unweighted undirected increment

**Source:** `scripts/build_graph.py` lines 184–200
**Apply to:** exporter ranking only (copy the loop; filter `type == "bridge"`)

```python
degree[edge["source"]] += 1
degree[edge["target"]] += 1
```

Edges have keys `{relation, source, target}` only. Sort `(-degree, id)`, cap 25.

### Hub fetch IIFE (Pages vs local vs `../`)

**Source:** `dashboard/index.html` lines 4872–4964
**Apply to:** `#recommendations` script

- `apiBase()` github.io / `/dashboard/` / `../`
- Two-path fallback; `r.ok ? r.json() : reject`; `.catch` next path
- `role="status"` / `aria-live="polite"` / `aria-busy`
- Empty + table wrap `display` toggle
- `textContent` for all catalog-derived strings

### meta.json endpoints are generated, panel JSON is not

**Source:** `scripts/generate_api.py` lines 5–16, 142–151, 154–187
**Apply to:** `recommendations` key

Register in docstring **and** `endpoints` dict. Do not teach `generate_api.py` to write the panel file.

### Honesty copy (contributor tooling ≠ finding)

**Source:** `dashboard/index.html` line 1981; `dashboard/README.md` line 11
**Apply to:** spec, JSON `disclaimer`, hub `#recommendations` `section-desc`, README

Phrase: “not a scientific ranking”. Never display `RESULT:` in this section. Never feed Crosscheck outcomes into `score`.

### Docs-with-the-change

**Source:** `.cursor/rules/documentation-and-dashboard.mdc`
**Apply to:** CHANGELOG Unreleased, DEV_DASHBOARD playbook, DOC_MAP, REPOSITORY_MANIFEST, scripts/README, dashboard/README, mkdocs nav, STATE after merge-worthy work.

Root `README.md` does **not** currently mention the xref panel — skip unless a hub-panel list is added there later.

### After-hub-edit gates

**Source:** `docs/DEV_DASHBOARD.md` § 3; CONTRIBUTING.md

```bash
python -m pytest tests/repo_smoke -v
python scripts/verify_dashboard_consistency.py
mkdocs build --strict   # if docs/ or mkdocs.yml changed
python -m http.server 8765  # then open /dashboard/#recommendations
```

Do **not** run `build_crosscheck.py --apply`.

---

## No Analog Found

None. Every file has an in-tree analog. Harvest/curator **implementation** is deferred; the spec points at `scripts/harvesters/wave_factory.py` `RankedCandidate` (`citation_score`, `recency_score`, `novelty_score`) as future-slot language only.

| File | Role | Data Flow | Reason |
|------|------|-----------|--------|
| — | — | — | — |

**Security overlay (not present on analog, required by RESEARCH):** orphan IIFE assigns `a.href = item.github_search_url` without a scheme check. Recommendations IIFE must require `url.indexOf('https://github.com/') === 0` before setting `href`. Do not add DOMPurify.

---

## Metadata

**Analog search scope:** `scripts/export_orphan_xref_panel.py`, `scripts/build_graph.py`, `scripts/generate_api.py`, `dashboard/index.html` (`#orphan-xref-panel`, CSS, IIFE, sticky nav, `#developer-api`), `api/v1/orphan_xref_panel.json`, `api/v1/meta.json`, `tests/repo_smoke/test_catalog_regression.py`, `.github/workflows/build-graph.yml`, `docs/DEV_DASHBOARD.md`, `docs/BREAKTHROUGH_GAPS.md`, `docs/DOC_MAP.md`, `docs/REPOSITORY_MANIFEST.md`, `docs/HUB`-adjacent nav in `mkdocs.yml`, `CHANGELOG.md`, `dashboard/README.md`, `scripts/README.md`, `.planning/STATE.md`, `scripts/harvesters/wave_factory.py` (future-slot citation only)

**Files scanned:** 20+ (analogs + freeze list)
**Pattern extraction date:** 2026-08-26
**Confidence:** HIGH — in-repo analog, zero new libraries

---

*Phase: 05-hub-engineering*
*Pattern mapping complete: 2026-08-26*
*Ready for planning: yes*
