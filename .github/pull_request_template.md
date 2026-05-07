## What does this PR add or change?

<!-- Brief description of the contribution -->

## Checklist

### For new bridges
- [ ] Bridge YAML file created in correct `cross-domain/{domain-a}-{domain-b}/` directory
- [ ] Bridge ID follows convention: `b-{short-descriptive-name}`
- [ ] `bridge_claim` field is a single, precise statement of the mathematical connection
- [ ] `translation_table` has at least 3 rows mapping Domain A concepts to Domain B
- [ ] `status` is set honestly: `established` / `proposed` / `speculative`
- [ ] All citations are real (DOIs preferred, no fabricated references)
- [ ] Related unknown and hypothesis are linked
- [ ] Schema validation passes: `python scripts/validate_schemas.py`

### For new unknowns
- [ ] Unknown YAML created in correct `unknowns-catalog/{domain}/` directory
- [ ] ID follows convention: `u-{short-descriptive-name}`
- [ ] Schema validation passes

### For new hypotheses
- [ ] Hypothesis YAML created in `hypotheses/active/`
- [ ] ID follows convention: `h-{short-descriptive-name}`
- [ ] Proposed test is concrete and falsifiable
- [ ] Schema validation passes

### For all contributions
- [ ] I have not fabricated any citations
- [ ] Content is original (not copied verbatim from papers)
- [ ] Speculative content is labeled as `status: speculative` or `status: proposed`

## Related issues

Closes #
