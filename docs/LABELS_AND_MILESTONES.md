# Labels and milestones

GitHub does not load label definitions from the repository automatically. Use this list when configuring labels under **Issues → Labels** (and optionally align **Projects / Milestones**).

## Recommended labels

| Label | Color suggestion | Meaning |
|-------|------------------|---------|
| `hypothesis` | #7057ff | Open scientific hypothesis or thread |
| `finding` | #0e8a16 | Proposed or accepted finding under review |
| `methods` | #1d76db | Protocols, analysis plans, reproducibility |
| `docs` | #0075ca | Documentation and governance only |
| `tooling` | #d876e3 | CI, bots, templates, automation |
| `enhancement` | #a2eeef | Feature / improvement (non-science) |
| `bug` | #d73a4a | Incorrect or broken content/tooling |
| `needs-evidence` | #fbca04 | More data or analysis required |
| `blocked` | #b60205 | Waiting on external dependency |
| `good first issue` | #7057ff | Friendly for newcomers |

Names match [COLLABORATION_AND_REVIEWS.md](COLLABORATION_AND_REVIEWS.md). Adjust the palette to taste; keep names stable so templates stay meaningful.

## Optional milestones

| Milestone | Use |
|-----------|-----|
| `Backlog` | Triaged but not scheduled |
| `Active inquiry` | Hypotheses with ongoing work |
| `Evidence review` | Findings awaiting critique |
| `Release candidate` | Snapshot tag / external share imminent |

## Issue template ↔ label hints

- **Finding review** template suggests `finding`.
- **Methods change** suggests `methods`.
- **Hypothesis thread** suggests `hypothesis`.
- **Bug report** suggests `bug`.
- **Feature request** suggests `enhancement`.

After creating labels once, you can set default labels per template in the template YAML if you switch templates to the form format later.
