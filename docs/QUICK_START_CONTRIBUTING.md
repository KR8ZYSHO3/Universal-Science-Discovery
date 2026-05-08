# Quick Start: Your First USDR Contribution

**Goal:** Make your first contribution in under 30 minutes.

## What you need
- A GitHub account
- Basic familiarity with YAML (it's like a structured text file)
- Knowledge of at least one scientific domain

## The 3 easiest contribution types

### 1. Complete a bridge stub (15–30 min)
Bridge stubs are half-written entries that need a domain expert to fill in the translation table and references. Look for issues labeled `good first issue`.

**Example stub to complete:**
```yaml
id: b-example-bridge
title: "Domain A ↔ Domain B: The Key Connection"
domains: [domain-a, domain-b]
bridge_claim: "Both fields are governed by the same mathematical object X"
translation_table:
  - source: "concept in domain A"
    target: "concept in domain B"
    notes: "FILL IN: explain why these are the same mathematical thing"
status: proposed
confidence: 0.7
communication_gap: "FILL IN: why haven't these fields talked to each other?"
cross_pollination_opportunities:
  - "FILL IN: specific research opportunity"
references:
  - doi: "10.XXXX/XXXXX"
    note: "FILL IN: what this paper shows"
related_unknowns: []
last_reviewed: "2026-05-07"
```

### 2. Add an open unknown (10 min)
An unknown is a research gap — a question that can't currently be answered. Good unknowns are:
- **Specific** (not "what causes cancer?" but "what mechanism allows *Borrelia* to cross the blood-brain barrier without triggering acute inflammation?")
- **Currently unanswered** in the primary literature
- **Linked to at least one discipline**

**Example unknown:**
```yaml
id: u-example-unknown
title: "What determines the threshold qubit count for quantum advantage in optimization?"
description: >
  Current NISQ hardware achieves advantage on narrow tasks but the minimum
  system size for industrially relevant optimization remains unclear.
domain: quantum-physics
status: open
related_bridges: []
related_breakthrough_gaps: []
```

### 3. Write a falsifiable hypothesis (15 min)
Pick an open unknown from the repo and write a hypothesis with:
- A **specific, testable prediction**
- A **proposed experimental test**
- A **falsification criterion** (what result would prove it wrong)

**Example hypothesis:**
```yaml
id: h-example-hypothesis
title: "Elevated CSF IL-6 persists in PTLDS patients at 12 months post-treatment"
prediction: >
  Patients with PTLDS will show CSF IL-6 ≥ 10 pg/mL at 12 months post-antibiotic
  treatment, compared to < 4 pg/mL in matched controls without PTLDS history.
proposed_test: >
  Lumbar puncture cohort study: n=60 PTLDS, n=60 treated-Lyme controls,
  blinded IL-6 ELISA at 12 months.
falsification_criterion: >
  No significant difference in CSF IL-6 between groups (p > 0.05, Cohen's d < 0.3).
related_unknowns: [u-ptlds-neuroinflammation-self-sustaining]
status: proposed
confidence: 0.55
```

## Step-by-step workflow

1. **Fork** the repository on GitHub
2. **Clone** your fork locally
3. **Create a branch**: `git checkout -b my-first-bridge`
4. **Create or edit** the YAML file described in the issue
5. **Validate**: run `python scripts/validate_schemas.py` (see below)
6. **Commit and push**: `git commit -m "bridge: add ecology-economics ecosystem services"` then `git push`
7. **Open a PR** and reference the issue number (`Closes #163`)

## Validation
Before submitting your PR, run:
```bash
python scripts/validate_schemas.py
```
This catches schema errors before review. If you don't have Python set up locally, GitHub CI will run it automatically when you open a PR.

## Finding your first issue
Browse issues labeled [`good first issue`](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/labels/good%20first%20issue) — each one has a clear file path, schema link, and estimated time.

## Where to get help
- Open a [GitHub Discussion](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/discussions) if you're unsure whether something qualifies
- Tag `@KR8ZYSHO3` in your PR for faster review
- See the full contribution guide: [CONTRIBUTING.md](../CONTRIBUTING.md)
- See schema documentation: [`schemas/`](../schemas/)
