# Onboarding

Path through the repository in **~30 minutes** for a new collaborator or maintainer.

## 1. Orientation (5 min)

Read [VISION_AND_SCOPE.md](VISION_AND_SCOPE.md) and [METHODOLOGY.md](METHODOLOGY.md). You should be able to answer:

- What is in scope for this repository?
- What is the difference between a hypothesis, a finding, and speculation?

## 2. Integrity and data (5 min)

Read [ETHICS_REPRODUCIBILITY_AND_DATA.md](ETHICS_REPRODUCIBILITY_AND_DATA.md). Confirm you understand:

- Which data classes may be committed
- Why `data/raw/` is gitignored

## 3. How we work together (5 min)

Read [COLLABORATION_AND_REVIEWS.md](COLLABORATION_AND_REVIEWS.md) and [CONTRIBUTING.md](../CONTRIBUTING.md). Skim [LABELS_AND_MILESTONES.md](LABELS_AND_MILESTONES.md) for triage vocabulary.

## 4. Traceability (5 min)

Open [DOC_MAP.md](DOC_MAP.md) and scan [REPOSITORY_MANIFEST.md](REPOSITORY_MANIFEST.md). These explain **which file enforces which policy**.

## 5. Tooling (5 min)

- **CI:** [.github/workflows/markdown-link-check.yml](../.github/workflows/markdown-link-check.yml) — link validation on PRs to `main`.
- **Dependabot:** [.github/dependabot.yml](../.github/dependabot.yml) — keeps GitHub Actions references current.
- **Agents:** If you use Cursor or other assistants, read [AGENTS.md](../AGENTS.md) and [.cursor/rules/science-discovery-core.mdc](../.cursor/rules/science-discovery-core.mdc).
- **Spec-driven milestones (optional):** [GSD_INTEGRATION.md](GSD_INTEGRATION.md) — [GSD / get-shit-done](https://github.com/gsd-build/get-shit-done) for phased plan → execute → verify loops that respect USDR policy.

## 6. Cadence (5 min)

Read [OPERATING_RHYTHM.md](OPERATING_RHYTHM.md) for weekly/monthly habits, tags, and branch protection expectations.

## Optional: prompts

Try [prompts/literature_synthesis.md](prompts/literature_synthesis.md) or [prompts/falsification_pass.md](prompts/falsification_pass.md) with your assistant when reviewing literature or a draft claim.

## Where to put work

| You are adding… | Put it in… |
|-----------------|------------|
| Protocol / preregistration / design | [`methods/`](../methods/) |
| Allowed small data / manifests | [`data/`](../data/) |
| Exploratory notebooks | [`notebooks/`](../notebooks/) |
| Reproducible scripts | [`scripts/`](../scripts/) |
| Committed figure/table exports | [`artifacts/`](../artifacts/) |
