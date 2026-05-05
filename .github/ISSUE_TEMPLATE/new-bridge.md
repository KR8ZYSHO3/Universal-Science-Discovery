---
name: New Cross-Domain Bridge
about: Propose a mathematical or conceptual connection between two or more fields
labels: content:bridge
---

## The Two (or More) Domains

Source field(s): 
Target field(s): 

## The Bridge Claim

<!-- What mathematical structure, model, or framework connects these fields?
     What concept in field A maps to what concept in field B, and why is this non-trivial? -->

## Why Non-Obvious

<!-- Why would experts in each field not naturally see this connection?
     Journal siloing? Terminology gap? Funding structures? -->

## Evidence

<!-- What supports this bridge? Links to papers, preprints, or existing cross-disciplinary work. -->

## Related Unknowns or Hypotheses

<!-- Which u-* or h-* catalog entries does this bridge illuminate? -->

## Proposed YAML

<!-- Fill in the template below. See schemas/bridge.yaml for all fields. -->

```yaml
id: b-field-a-field-b
title: "One-sentence statement of the cross-domain connection."
status: proposed   # proposed | established | contested | stale
fields:
  - field-a
  - field-b
bridge_claim: >
  Precise description of what concept in field A maps onto what concept in field B,
  and why the mapping is mathematically or structurally non-trivial.
communication_gap: >
  Why have these fields not already converged on this connection?
references:
  - doi: 10.xxxx/xxxxx
    note: Paper establishing or supporting the connection
```

## Checklist

- [ ] At least two distinct scientific fields listed in `fields`
- [ ] `bridge_claim` explains the mapping concretely (not just "these fields are similar")
- [ ] `id` starts with `b-` and uses only lowercase letters, digits, and hyphens
- [ ] `python scripts/validate_schemas.py` passes locally
