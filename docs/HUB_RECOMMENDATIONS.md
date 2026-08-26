# Hub recommendations — contributor tooling (not a scientific ranking)

**Purpose:** Suggest high-leverage **existing** bridges to inspect or extend.
This list is **contributor tooling**, not a scientific ranking of unknowns,
and not a CONFIRMED or INCONCLUSIVE Crosscheck outcome.

The contributor hub section is `dashboard/index.html` `#recommendations`.
The committed prototype is `api/v1/recommendations.json`.

## Signals

### Connectivity (computed in this prototype)

Undirected degree in the **filtered** knowledge graph (`docs/knowledge_graph.json`).
Each edge increments both endpoints by 1 (same increment as
`build_graph.top_nodes_by_degree`). Isolates score 0 and drop out of the
top-25 list. Multi-relation pairs count separately because `seen_edges`
keys on `(source, target, relation)`.

JSON `ranking` value: `undirected_degree`. Item `score` is that integer degree.
Higher degree means more catalog links — leverage for a contributor looking
where to connect next — not scientific importance.

### Harvest (specified, not computed)

A later join from Wave Factory / harvester ranking (`citation_score`,
`recency_score`, `novelty_score` in `scripts/harvesters/wave_factory.py`).
Prototype items **omit** `harvest_rank` (do not send null or a fake number).

### Curator score (specified, not computed)

Optional maintainer overlay (YAML field or committed sidecar). No such field
exists today. Prototype items **omit** `curator_score`.

## What the prototype computes

Connectivity only. `ranking` is `undirected_degree`. Cap **≤ 25** items,
all `kind: "bridge"` with ids starting `b-`.

## Regenerate

From the repo root:

```bash
python scripts/export_recommendations.py
```

CI: `.github/workflows/build-graph.yml` runs that command immediately after
`python scripts/export_orphan_xref_panel.py`. `add-paths: api/**` already
covers the JSON. Do not compute degree in the browser. Do not call an LLM.

## Non-goals

Personalization, logged-in recommendations, browser graph math on
`graph.json`, ML / embeddings, hub visual redesign, and feeding
`RESULT: CONFIRMED` (or INCONCLUSIVE) into `score`.

## Related docs

- [DEV_DASHBOARD.md](DEV_DASHBOARD.md) — hub playbook
- [dashboard/README.md](../dashboard/README.md) — hub honesty line
- [BREAKTHROUGH_GAPS.md](BREAKTHROUGH_GAPS.md) — analog stewardship spec
- [WAVE_FACTORY.md](WAVE_FACTORY.md) — harvest-rank future slot
