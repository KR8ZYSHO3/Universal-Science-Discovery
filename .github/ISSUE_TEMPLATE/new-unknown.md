---
name: New Unknown (research gap)
about: Propose a new open question for the unknowns catalog
labels: content:unknown, good first issue
---

## The Question

<!-- What is the precise scientific question? Be as specific as possible. -->

## Why It Matters

<!-- Why is this unknown important? What would change if we knew the answer? -->

## Domain(s)

<!-- Which field(s) does this touch? e.g. neuroscience, statistical-physics, ecology -->

## Related Bridges or Hypotheses

<!-- Any existing catalog entries this connects to? Use u-, h-, or b- IDs if known. -->

## Proposed YAML

<!-- Copy-paste and fill in the template below. See schemas/unknown.yaml for all fields. -->

```yaml
id: u-your-slug-here
title: "Your precise research question here?"
status: open
priority: medium   # low | medium | high | critical
disciplines:
  - field-one
  - field-two
summary: >
  2-3 sentence explanation of why this is a genuine open question in the field.
references:
  - doi: 10.xxxx/xxxxx
    note: Optional supporting reference
```

## Checklist

- [ ] Title is a specific, answerable research question (not a topic)
- [ ] `id` starts with `u-` and uses only lowercase letters, digits, and hyphens
- [ ] At least one discipline listed
- [ ] `python scripts/validate_schemas.py` passes locally
