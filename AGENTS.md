# Agent instructions (Cursor and other assistants)

## Canonical policy

Before proposing **findings**, changing **methods**, or advising on **data handling**, read these in order:

1. [docs/VISION_AND_SCOPE.md](docs/VISION_AND_SCOPE.md)
2. [docs/METHODOLOGY.md](docs/METHODOLOGY.md)
3. [docs/ETHICS_REPRODUCIBILITY_AND_DATA.md](docs/ETHICS_REPRODUCIBILITY_AND_DATA.md)

For collaboration norms and review expectations: [docs/COLLABORATION_AND_REVIEWS.md](docs/COLLABORATION_AND_REVIEWS.md).  
For how docs map to repo mechanics: [docs/DOC_MAP.md](docs/DOC_MAP.md).  
For every path’s role and governing policy: [docs/REPOSITORY_MANIFEST.md](docs/REPOSITORY_MANIFEST.md).  
For human onboarding order: [docs/ONBOARDING.md](docs/ONBOARDING.md).  
For cadence and versioning: [docs/OPERATING_RHYTHM.md](docs/OPERATING_RHYTHM.md).

## Operating rules

- **Hypothesis vs finding:** Never present speculation as an established finding. Use the terminology from VISION_AND_SCOPE.
- **Citations:** Do not invent DOIs or papers. If uncertain, say so and suggest search strategies.
- **Data:** Do not instruct committing sensitive or identifiable human data to git; follow ETHICS_REPRODUCIBILITY_AND_DATA.
- **Reproducibility:** Prefer changes that reference scripts, protocols, or explicit steps—not vague “we analyzed the data.”
- **Scope:** Decline to expand the project into out-of-scope areas listed in VISION_AND_SCOPE unless the user explicitly reframes scope and documents it.

## Prompt templates

See [docs/prompts/](docs/prompts/) for literature synthesis, hypothesis comparison, and falsification passes.

## Project rules

This repository includes Cursor rules under [.cursor/rules/](.cursor/rules/) that mirror the above; keep them in sync when policy changes.
