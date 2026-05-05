# How USDR Generates Bridge Hypotheses

## Overview

The USDR co-pilot uses a two-stage approach to propose novel cross-domain bridges:

1. **Stage 1 – Gap Detection** (`propose_bridges.py`): scores all domain pairs by open-question density and existing bridge coverage, returning the highest-novelty candidates.
2. **Stage 2 – Pattern Matching** (`generate_hypothesis.py`): applies a library of mathematical pattern templates to the top candidates and drafts complete bridge YAML files for expert review.

---

## Stage 1: Gap Detection (`propose_bridges.py`)

Scores domain pairs by:

- **Unknown density**: how many open questions exist in each domain  
- **Bridge coverage**: how many existing bridges already connect this pair  
- **Novelty score**: total unknown density minus a bridge-coverage penalty  

Top pairs are written to `docs/bridge_proposals.json` with sample unknowns from each domain.

---

## Stage 2: Pattern Matching (`generate_hypothesis.py`)

For each high-scoring pair, the script analyses the domain keywords and unknown titles to detect which mathematical pattern is most likely to apply:

| Pattern | Keywords | When to apply |
|---------|----------|---------------|
| **Phase transition** | critical point, threshold, tipping, percolation, attractor | Both domains exhibit threshold / bifurcation behaviour |
| **Information theory** | entropy, capacity, coding, uncertainty, biomarker, language | Both domains involve signal/noise, capacity limits, or encoding |
| **Network / graph theory** | connectivity, hub, topology, path, connectome, microbiome | Both domains have exploitable network structure |
| **Scaling laws** | power law, allometric, fractal, Zipf, gradient | Both domains show scale-invariant or allometric behaviour |
| **Optimization** | minimum, variational, cost function, equilibrium, policy | Both domains can be framed as minimising a cost functional |

Detection is keyword-scoring: each pattern accumulates one point per keyword that appears in the combined text of both domain slugs and their sample unknown titles. The highest-scoring pattern wins.

---

## Running the Generator

```bash
# Generate drafts for the top 10 co-pilot proposals
python scripts/generate_hypothesis.py --from-proposals --top 10 --output drafts/bridges/

# Generate a single draft for a specific domain pair
python scripts/generate_hypothesis.py --domain1 neuroscience --domain2 medicine --output drafts/bridges/
```

Requirements: `pyyaml` (already in `.venv-ingest`).

---

## Output Format

Each generated file in `drafts/bridges/` is a valid YAML bridge that mirrors the production schema in `cross-domain/`. Fields are pre-populated from the chosen pattern template:

| Field | Content |
|-------|---------|
| `id` | `b-<domain1>-<domain2>` |
| `title` | Includes `[AI DRAFT — REQUIRES EXPERT REVIEW]` marker |
| `bridge_claim` | Template claim prefixed with `[AI-GENERATED DRAFT]` |
| `translation_table` | Three template translation entries with domain labels |
| `evidence` | Placeholder `[TO VERIFY]` / `[TO ADD]` items |
| `open_unknowns` | Top 2 unknowns from each domain |
| `cross_pollination_opportunities` | Three template suggestions |
| `references` | Two `TODO` reference slots |
| `last_reviewed` | Generation date |

---

## Human Review Required

All AI-generated drafts are **starting points, not conclusions**. Before a draft can be promoted to `cross-domain/`, a domain expert must:

1. **Verify the analogy** — confirm the mathematical structure genuinely applies, not just metaphorically.
2. **Replace `[TO VERIFY]` evidence** — add real literature citations with DOIs or arXiv IDs.
3. **Write a specific bridge claim** — replace the template text with a precise, falsifiable statement.
4. **Sharpen the translation table** — ensure every entry is mathematically precise (not just descriptive).
5. **Remove the `[AI DRAFT]` prefix** from the title.

---

## Submitting a Reviewed Draft

Once an expert has reviewed and refined a draft:

1. Move the file from `drafts/bridges/` to the appropriate `cross-domain/<domain1>-<domain2>/` directory.
2. Remove the `[AI DRAFT — REQUIRES EXPERT REVIEW]` marker from the title.
3. Add a `status: proposed` field (or `established` if the bridge is already in the literature).
4. Open a PR following the process in `CONTRIBUTING.md`.

---

## Design Rationale

This generator does **not** call an external LLM API. Every output is derived deterministically from:

- The keyword-scoring pattern library embedded in `MATH_PATTERNS` (in `generate_hypothesis.py`)
- The domain slugs and unknown titles from `docs/bridge_proposals.json`

This makes every draft fully reproducible, auditable, and free of hallucinated citations. The cost is that all specificity must come from the expert reviewer — the generator provides structure and prompts, not substance.
