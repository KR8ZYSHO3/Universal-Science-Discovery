## Summary

Add a new **hypothesis** entry (YAML or Markdown front matter + body) validated against [schemas/hypothesis.yaml](../schemas/hypothesis.yaml).

## Links

- Unknown(s) addressed: 
- Related issue(s): 

## Record

Paste YAML (or link path under `hypotheses/active/`).

```yaml
id: h-<slug>
title: ""
status: draft
created: YYYY-MM-DD
author: "@handle"
unknowns_addressed: []
evidence_links: []
proposed_tests: []
related_disciplines: []
```

## Checklist

- [ ] `id` is unique; follows `h-...` convention
- [ ] Evidence entries are **metadata / DOI / open URLs** only ([LEGAL.md](../LEGAL.md))
- [ ] Unknown links reference existing `u-...` ids where possible
- [ ] Status is honest (`draft` until reviewed)

## AI / assisted drafting note

If AI drafted text, cite and verify every DOI or URL against the primary source.
