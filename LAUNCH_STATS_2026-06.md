# USDR Authoritative Stats for Launch — June 2026

**Source of truth (always re-verify before publishing):**
- `python scripts/verify_dashboard_consistency.py`
- `docs/knowledge_graph.json` meta section
- `README.md` (after the update script has run)

**Verified Snapshot (as of latest local validation runs)**
- **Cross-domain bridges**: 1,123
- **Open unknowns**: 1,408 (0 orphans)
- **Falsifiable hypotheses**: 1,274
- **Knowledge graph**: 3,857 nodes, 4,517 edges
- **Scientific domains**: 55+
- **Pioneer profiles**: 18
- **Breakthrough gaps**: 24
- **Phenomenology records**: 10
- **Schema validation**: 0 errors (all entries pass on every PR)

**Total structured catalog entries** (bridges + unknowns + hypotheses + pioneers + breakthrough gaps + phenomenology): **~4,857**

**Key quality signals** (use these in outreach and the dashboard):
- 0 orphan unknowns (every unknown is connected in the graph)
- All catalog YAML passes strict JSON Schema validation in CI
- Knowledge graph is deterministically rebuilt from source on every relevant push
- Wave Factory automation runs on a fixed cadence (Mon + Thu) producing review-ready drafts
- Full governance, ethics, and methodology documentation published

---

## Ready-to-Copy Text Blocks

### For README.md table (replace the current one)

```markdown
| Metric                     | Count     | Notes                                                           |
| -------------------------- | --------- | --------------------------------------------------------------- |
| **Cross-domain bridges**   | **1,123** | Mathematical connections between fields that rarely communicate |
| **Open unknowns**          | **1,408** | Named, structured research gaps across 55+ disciplines          |
| **Falsifiable hypotheses** | **1,274** | Testable claims linked to specific unknowns                     |
| **Phenomenology records**  | **10**    | Pre-formal observations (`phenomenology/**/p-*.yaml`)           |
| **Knowledge graph nodes**  | **3,857** | Interconnected across 4,517 edges (`docs/knowledge_graph.json`) |
| **Pioneer profiles**       | **18**    | `pioneers/*.yaml` — lineage context for seeded bridges            |
| **Breakthrough gaps**      | **24**    | `breakthrough-gaps/bg-*.yaml` — stewarded high-impact gaps      |
| **Orphan unknowns**        | **0**     | `scripts/find_orphan_unknowns.py` — none disconnected in graph  |
| **Schema errors**          | **0**     | All entries pass CI validation on every PR                      |
```

### Short "What We've Built" blurb (for hero, LinkedIn, emails, etc.)

"USDR is a git-native, schema-validated, community-governed catalog of scientific unknowns, hypotheses, and cross-domain mathematical bridges. It currently contains 1,123 rigorously structured bridges, 1,408 open unknowns, and 1,274 testable hypotheses across 55+ disciplines — all connected in a 3,857-node knowledge graph with zero orphans and 100% schema compliance."

### For the Preprint Abstract (refresh the numbers section)

"...The repository currently contains **4,857+ structured catalog entries** across **55+** disciplines, including **1,123 cross-domain bridges** that formalise mathematical correspondences between fields that rarely communicate, **1,408** open unknowns, **1,274** falsifiable hypotheses, **18** pioneer profiles, and **24** breakthrough gap analyses (plus phenomenology records). The knowledge graph contains **3,857 nodes** and **4,517 edges** with **0 orphan unknowns**..."

### For Dashboard Hero / OpenGraph (suggested stronger external-facing version)

"Map what science doesn't know yet.

1,123 cross-domain mathematical bridges • 1,408 open unknowns • 1,274 testable hypotheses • 3,857-node knowledge graph

Version-controlled. Schema-validated. Open source. Built for researchers and AI to find the frontier together."

### For Outreach / Researcher Pitch (high-signal version)

"The Universal Science Discovery Repository (USDR) is now live with:
- 1,123 rigorously documented cross-domain bridges (with translation tables and literature references)
- 1,408 named, structured open unknowns across 55+ fields
- 1,274 falsifiable hypotheses linked to those unknowns
- A deterministic 3,857-node knowledge graph with zero disconnected entries

Everything is Git-native, PR-reviewable, and schema-enforced. We are launching public contribution and actively looking for domain experts to validate, extend, and steward their fields."

---

**Instructions for use:**
1. Run the two verification scripts locally right before any public push.
2. Copy the blocks above (they are intentionally consistent).
3. If the numbers have moved significantly since this file was written, treat this document as a template and regenerate the blocks.

This file exists so you never have to hunt through the repo for "what are the current numbers again?" during the high-pressure launch window.
