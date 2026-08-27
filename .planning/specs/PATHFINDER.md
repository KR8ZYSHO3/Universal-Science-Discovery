# Pathfinder — Cross-domain graph path discovery

**ID:** DISC-01  
**Status:** Spec approved — ready to plan/execute  
**Accelerates:** `INTERFACE.md` P2.3 (pulled forward from Interface Phase 2 / 2028–2029)  
**Ship bar pillar:** Pillar 3 — Interface truly awesome (researcher “aha” moment)

---

## Problem

USDR has 1,124 bridges and a 3,861-node graph, but newcomers cannot answer:

> *“How does field A connect to field B?”*

The D3 graph is exploratory, not **goal-directed**. Pathfinder turns the catalog into an instrument: pick two domains (or two node IDs) and get the shortest credible path through the graph.

---

## User stories

1. **Researcher:** “How does statistical physics connect to conservation biology?” → 2-hop path via `b-habitat-percolation-ecology`, with `evidence_tier: proven` and Crosscheck link.
2. **Maintainer:** CLI prints paths for scripting and smoke tests.
3. **Hub visitor:** Domain dropdowns in the knowledge-graph section → path list → click hop → graph highlights + node panel opens.

---

## Scope (v1)

### In scope

- **Inputs:** two discipline labels (from bridge `fields` / unknown `disciplines`) *or* two catalog node IDs
- **Graph:** `docs/knowledge_graph.json` edges only (no orphan endpoints)
- **Algorithm:** unweighted shortest path (BFS); if multiple equal-length paths, return up to **3** diverse paths (prefer paths that include a `bridge` node)
- **Output per hop:** `id`, `type`, `title` (truncated), `evidence_tier` (bridges only)
- **CLI:** `python scripts/graph_pathfinder.py --from ecology --to epidemiology` (and `--from-id` / `--to-id`)
- **Hub (minimal):** two `<select>` domain pickers + “Find path” → render hop chips below graph filters; clicking a hop calls existing `highlightNeighborhood` + panel load

### Out of scope (v1)

- Weighted paths (citation count, curator score)
- Semantic / embedding similarity between domains
- Path export to PDF or permalink URLs (`INTERFACE.md` P1.4)
- Auto-suggest “related paths” without user picking endpoints

---

## Technical design

| Layer | Artifact |
|-------|----------|
| Core | `scripts/graph_pathfinder.py` — load graph, BFS, domain→node index |
| Data | Reuse `knowledge_graph.json`; domain list from unique `fields` on bridge nodes |
| Hub | Patch `dashboard/index.html` knowledge-graph section (markers `@pathfinder-begin` / `@pathfinder-end` optional) |
| CI | `tests/repo_smoke/test_graph_pathfinder.py` — fixed seed path between known domains (e.g. `statistical-physics` → `conservation-biology` includes `b-habitat-percolation-ecology`) |

**Domain matching:** normalize kebab-case; a node “belongs” to a domain if that string appears in `node.fields` (bridges) or `node.fields` / disciplines array (unknowns, hypotheses).

**Path quality:** if no path exists, return clear message + suggest `propose_bridges.py --top 5` output for the domain pair (optional v1.1).

---

## Acceptance criteria

1. CLI returns at least one path for `statistical-physics` → `conservation-biology` including `b-habitat-percolation-ecology`.
2. CLI exits 1 with helpful stderr when domains unknown or disconnected.
3. Hub pathfinder UI loads without console errors on GitHub Pages; found path highlights on graph.
4. Bridge hops show `evidence_tier` chip in path result row.
5. `pytest tests/repo_smoke` includes pathfinder test; `validate_schemas.py` unchanged.

---

## Verification

```bash
python scripts/graph_pathfinder.py --from statistical-physics --to conservation-biology
python scripts/graph_pathfinder.py --from-id b-habitat-percolation-ecology --to-id u-percolation-epidemic-fss
python -m pytest tests/repo_smoke/test_graph_pathfinder.py -q
```

---

## Sequencing

| Step | Deliverable |
|------|-------------|
| 1 | `graph_pathfinder.py` + smoke test |
| 2 | Hub UI wired to client-side pathfinder (inline JS or fetch + compute) |
| 3 | `docs/CROSSCHECK.md` or hub copy: one-line “find how domains connect” |

**GSD:** Plan as Phase 5 plan `05-pathfinder` or standalone quick phase after UI-01 polish.

---

## Related docs

- `INTERFACE.md` § P2.3 — Cross-domain Discovery Engine (vision source)
- `ROADMAP.md` § Track E — Discovery instruments
- `.planning/PROJECT.md` — DISC-01 active requirement
- `scripts/propose_bridges.py` — complementary (suggests *new* bridges; pathfinder uses *existing* graph)