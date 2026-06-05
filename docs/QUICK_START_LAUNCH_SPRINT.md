# USDR Launch Sprint — Make Your First Contribution in 20–40 Minutes

**Welcome to the June 2026 Launch Sprint.** You're about to make a real, reviewable contribution to one of the most ambitious open science infrastructure projects in progress.

USDR (Universal Science Discovery Repository) is a version-controlled, schema-validated catalog of **what science doesn't know yet** — open unknowns, testable hypotheses, and rigorous cross-domain mathematical bridges. (See launch PR #267 for the current institutional + dashboard push: https://github.com/KR8ZYSHO3/Universal-Science-Discovery/pull/267)

Everything lives in Git. Everything is reviewed via normal pull requests. No special permissions needed to start.

---

## The 20–40 Minute Path (Choose One)

### Option 1: Quickest Win — Improve or Complete a Bridge Stub (15–30 min)
Many high-quality bridge stubs already exist as GitHub Issues labeled `good first issue`.

**Steps:**
1. Go to the [good first issues list](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/issues?q=is%3Aopen+label%3A%22good+first+issue%22).
2. Pick one that matches your expertise (many are scoped to specific domains like quantum advantage, tipping cascades, One Health, room-temperature superconductivity, PTLDS, etc.).
3. Read the issue fully — it will tell you exactly what file to create or edit and what must be included.
4. Fork the repo → create a branch like `feat/bridge-[short-name]` or `content/[domain]-unknown`.
5. Make the change following the schema in `schemas/bridge.yaml` (or unknown/hypothesis as needed).
6. Run locally:
   ```bash
   python scripts/validate_schemas.py
   ```
7. Open a Pull Request and link it to the issue.

**We will review quickly during the launch sprint.**

### Option 2: Add a New Unknown in Your Field (20–40 min)
This is the simplest high-value contribution.

**Steps:**
1. Look at existing examples in `unknowns-catalog/[your-field]/`.
2. Copy the template from `templates/unknown.yaml` (or just copy a similar file).
3. Create a new file: `unknowns-catalog/[your-field]/u-[short-descriptive-name].yaml`
4. Fill it out honestly:
   - Clear title phrased as an open question
   - Summary of why it matters
   - Disciplines array
   - At least one real reference (DOI or arXiv preferred)
   - `status: open`
5. Validate:
   ```bash
   python scripts/validate_schemas.py
   ```
6. Open a PR titled something like `content: add u-[name] unknown in [field]`.

We especially love unknowns that connect to existing bridges or breakthrough gaps.

### Option 3: Review or Improve an Existing Entry (15–25 min)
- Spot a small improvement in a bridge/unknown/hypothesis?
- Find a missing reference, unclear translation table, or better wording?
- Open an issue or go straight to a small PR.

Small, high-quality PRs are extremely welcome during launch.

---

## Before You Submit (30 seconds)

Run this locally from the repo root:

```bash
python scripts/validate_schemas.py
```

It must pass with zero errors.

---

## What Happens Next

1. Your PR will be reviewed (we're moving fast during the launch sprint).
2. If it needs small changes, we'll give clear feedback.
3. Once merged, it becomes part of the permanent, citable catalog.
4. High-quality contributions during the launch period will be highlighted in our announcement and future "contributor spotlight" posts.

---

## Need Help?

- Ask in your PR or in a comment on the issue.
- Read [CONTRIBUTING.md](../CONTRIBUTING.md) and [docs/QUICK_START_CONTRIBUTING.md](../docs/QUICK_START_CONTRIBUTING.md) for deeper details.
- The [Live Dashboard](https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/) is the best way to explore what's already there.

**Thank you.** Every single well-formed entry makes the map of the unknown frontier a little clearer.

Let's find what we don't know — together.

---

**Launch Sprint Status:** Active — First external contributions will be celebrated publicly.