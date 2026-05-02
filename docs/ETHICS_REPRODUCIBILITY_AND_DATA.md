# Ethics, reproducibility, and data

## Data classes

| Class | May be committed | Requirements |
|-------|------------------|--------------|
| Public, non-sensitive summaries | Yes | Provenance and license noted |
| Derived aggregates (k-anonymous, no re-identification risk) | Yes if policy allows | Document transformation pipeline |
| Identifiable or sensitive human data | **No** in raw form | Store in approved systems only; link with access procedure |
| Third-party restricted data | **No** without license text | Reference terms of use; do not commit proprietary dumps |

## Reproducibility

- Pin software versions when analysis is code-backed (requirements files, lockfiles, or environment notes in the relevant folder).
- Record random seeds where stochastic processes matter.
- For long pipelines, a short `RUNBOOK` in [scripts/](../scripts/) or [methods/](../methods/) beats tribal knowledge.

## Human subjects

If any work involves human participants: obtain appropriate approvals, use consent-aligned sharing, and never commit identifiers or protected health information.

## Integrity

- Do not fabricate data or citations.
- Correct errors transparently (follow-up issues or PRs).
