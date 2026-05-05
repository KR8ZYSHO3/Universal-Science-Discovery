# Drafts Directory

Files in this directory are **AI-generated stubs awaiting human expert review**.

## What's here

| Subdirectory | Contents |
|---|---|
| `bridges/` | Draft bridge YAML stubs produced by `scripts/propose_bridges.py --draft-yaml` |

## Bridge drafts (`bridges/`)

Each file is a candidate cross-domain bridge identified by the USDR co-pilot based on
domain connectivity gaps in the knowledge graph. The co-pilot scores domain pairs by
their combined open-unknown density and penalises pairs that already share a formal
bridge.

**These files are NOT peer-reviewed.** They are starting points — pre-filled templates
designed to lower the barrier to contribution, not finished scientific claims.

### Before submitting a draft as a PR

1. **Verify the bridge claim** — does a real mathematical or conceptual correspondence
   exist between the two domains? Replace `"TODO: state the mathematical/conceptual
   bridge"` with a precise, citable statement.
2. **Fill the translation table** — map at least one source concept to a target concept
   via a named mathematical object (e.g. a group, a differential equation, a generating
   function).
3. **Add evidence** — cite at least one primary source (DOI preferred). Do not invent
   citations; if unsure, say so and leave a search suggestion.
4. **Review open unknowns** — confirm the listed unknowns are genuine open problems in
   each domain. Add or replace entries as needed.
5. **Update `last_reviewed`** — set this to today's date after your review.

### How to contribute

```bash
# Fork, branch, edit a draft, then open a PR
git checkout -b bridge/<your-bridge-slug>
# edit drafts/bridges/b-<slug>.yaml
git add drafts/bridges/b-<slug>.yaml
git commit -m "bridge: <domain1> ↔ <domain2> — <one-line claim>"
# open PR against main
```

See [CONTRIBUTING.md](../CONTRIBUTING.md) (if present) and the
[GitHub Issues](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/issues) for
discussion.

---

*Auto-generated stubs are produced by `python scripts/propose_bridges.py --draft-yaml`.
Re-run after knowledge graph updates to surface new candidates.*
