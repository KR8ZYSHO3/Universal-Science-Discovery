# Cross-domain bridges

A **bridge entry** captures an explicit connection between two or more scientific
fields studying the same underlying phenomenon with different language, methods, or
tools — and with little awareness of each other.

Bridge files live under `cross-domain/` in the repository root,
validated against `schemas/bridge.yaml`.

---

## Why bridges matter

When physics, biology, chemistry, and medicine each study the same phenomenon, they often
rediscover it independently — wasting decades. Bridges make the connection explicit so that:

- Researchers can borrow tools and vocabulary from adjacent fields.
- Experiments that are impossible in one field become routine in another.
- Journal siloing stops hiding obvious collaborations.

---

## Active bridges

| ID | Fields | Unknown | Hypothesis |
|----|--------|---------|-----------|
| b-percolation-oncology | statistical-physics ↔ oncology | u-tumor-containment-percolation, u-active-matter-percolation | h-adaptive-therapy-percolation-threshold |
| b-criticality-neuroscience | condensed-matter ↔ neuroscience | u-brain-criticality-function | h-criticality-conscious-integration |
| b-glymphatic-aging | sleep-medicine ↔ neurology ↔ geroscience | u-amyloid-progression-trajectory | h-glymphatic-amyloid-clearance-rate |
| b-lichen-astrobiology | synthetic-biology ↔ astrobiology | u-synthetic-lichen-biofabrication | h-lichen-consortium-metabolic-coupling |
| b-topology-morphogenesis | mathematical-physics ↔ developmental-biology | u-topological-morphogenesis | h-topological-defect-morphogenesis |
| b-grokking-criticality | machine-learning ↔ statistical-physics | u-grokking-phase-transition | — |

---

## Schema

Each bridge requires at minimum:

| Field | Purpose |
|-------|---------|
| `id` | Stable `b-...` identifier |
| `title` | One-sentence equivalence statement |
| `status` | `proposed / established / contested / stale` |
| `fields` | At least two disciplines |
| `bridge_claim` | Precise description of the mapping |

Optional enrichment fields: `translation_table`, `cross_pollination_opportunities`,
`communication_gap`, `related_unknowns`, `related_hypotheses`, `references`.

Full schema: `schemas/bridge.yaml` in the repository root.

---

## Contributing a bridge

1. Pick two fields you suspect are studying the same thing with different vocabulary.
2. Copy the template below into `cross-domain/<field-a>-<field-b>/b-<short-name>.yaml`.
3. Run `python scripts/validate_schemas.py` — it now validates bridge entries automatically.
4. Open a PR describing the connection and at least one `cross_pollination_opportunity`.

```yaml
id: b-your-bridge-name
title: "..."
status: proposed
fields:
  - field-a
  - field-b
bridge_claim: >
  ...
```
