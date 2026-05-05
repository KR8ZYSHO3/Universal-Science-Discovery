# Phenomenology Catalog

Pre-formal observations. Lower bar than `unknowns-catalog/` — no citations,
no credentials, no jargon required.

## What belongs here

Any of these is a valid entry:

- A dream about a physical object or process you couldn't name
- An engineering hunch that something *should* work but nobody has tried
- An everyday observation that feels like it shouldn't be true
- A cross-domain analogy that feels too apt to be coincidence
- A question a non-expert asked that no expert has thought to ask
- A pattern you noticed in unrelated fields that seems to share structure

## What happens to entries

```
raw observation
      ↓
  p-*.yaml entry (this directory)
      ↓
  triage by domain expert (GitHub Issue, label: needs-triage)
      ↓
  one of:
    → promoted to u-*.yaml (formal unknown)    [if open question identified]
    → promoted to b-*.yaml (formal bridge)     [if cross-domain connection confirmed]
    → explained (review_notes describes known phenomenon, entry archived)
    → stale (not actionable after review)
```

## Schema

See [`../schemas/phenomenon.yaml`](../schemas/phenomenon.yaml).
Required fields: `id`, `title`, `origin`, `description`, `date_observed`.
Everything else is optional — fill in what you can.

## Submitting an entry

See [`../docs/prompts/intuition_to_unknown.md`](../docs/prompts/intuition_to_unknown.md)
for the step-by-step guide, including an AI triage prompt you can use with any
assistant to convert a raw description into a structured YAML entry.

## Current entries

| ID | Title | Origin | Status |
|----|-------|--------|--------|
| [p-nonhelical-cavity-resonator](physics/p-nonhelical-cavity-resonator.yaml) | Hollow aluminum box with non-helical lattice-wire winding | dream | triaged |

## The principle

The formal scientific literature captures discoveries *after* formalization.
This catalog captures them *before* — at the moment of intuition.

Kekulé dreamed the benzene ring. Ramanujan filled notebooks with results he
couldn't prove. The Penrose tiling was Islamic geometric art for 800 years before
it was quasicrystal physics. This is the place for observations at that stage.
