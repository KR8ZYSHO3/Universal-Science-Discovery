# Breakthrough gaps — stewardship & roadmap priority

**Purpose:** `breakthrough-gaps/bg-*.yaml` entries name **world-scale outcomes** that are plausible but blocked by specific cross-domain gaps. They complement bridges (`cross-domain/b-*.yaml`) by answering “what macro breakthrough does this catalog infrastructure ultimately serve?”

This doc ties the breakthrough-gap program to **Phase-plan priorities** alongside discovery/adoption and hub fidelity ([ROADMAP.md](../ROADMAP.md) § Integrated development priorities).

---

## Where entries live

- **YAML:** [`breakthrough-gaps/`](../breakthrough-gaps/) — one file per gap, validated by [`schemas/breakthrough_gap.yaml`](../schemas/breakthrough_gap.yaml).
- **Contributor hub:** “Breakthrough Gaps” cards are **generated** from YAML via [`scripts/render_breakthrough_gaps_hub.py`](../scripts/render_breakthrough_gaps_hub.py) (markers in `dashboard/index.html`). Do not hand-edit card grids.
- **API:** [`api/v1/breakthrough_gaps.json`](../api/v1/breakthrough_gaps.json) — summaries emitted by [`scripts/generate_api.py`](../scripts/generate_api.py).

---

## Stewardship checklist (each entry)

1. **`breakthrough_description`** — Concrete “what changes in the world” + honest uncertainty (no fake citations; use `references` for real sources).
2. **`current_trl`** — Defensible Technology Readiness Level (1–9); revisit when major demos or reversals happen.
3. **`blocking_gaps`** — At least one barrier with **`gap_type`** from the schema enum (`materials`, `economic`, `engineering`, `biological`, `mathematical`, `social`, `regulatory`, `scientific`, `algorithmic`, `control`).
4. **`required_bridges`** — List **`b-*` IDs** that would materially unblock the breakthrough. Prefer existing bridges; if an ID is missing, open an issue or add the bridge in the same effort as updating the gap.
5. **`references`** — Minimum one verifiable pointer (DOI, arXiv, or stable URL per repo policy).

---

## When to regenerate hub / API

On PRs that add or edit **`breakthrough-gaps/*.yaml`**, CI validates schemas. After merge, **`build-graph.yml`** also runs when those paths change and executes **`render_breakthrough_gaps_hub.py --apply`** plus **`generate_api.py`**, keeping `dashboard/index.html` and `api/v1/` aligned.

For local work: `python scripts/render_breakthrough_gaps_hub.py --apply` then `python scripts/generate_api.py`.

---

## Related docs

- Folder README: [`breakthrough-gaps/README.md`](../breakthrough-gaps/README.md)
- Cross-domain bridge methodology: [`docs/CROSS_DOMAIN_BRIDGES.md`](CROSS_DOMAIN_BRIDGES.md)
- Operating rhythm (docs + hub updates): [`docs/OPERATING_RHYTHM.md`](OPERATING_RHYTHM.md)
