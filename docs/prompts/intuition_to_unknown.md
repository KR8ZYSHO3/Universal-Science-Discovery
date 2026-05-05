# Prompt: Intuition → Phenomenology entry → Unknown

Use this template to convert any pre-formal observation — dream, hunch, engineering
anomaly, everyday pattern, or cross-domain feeling — into a structured
`phenomenology/` entry that can be triaged and eventually promoted to a formal `u-`
unknown or `b-` bridge.

**No physics background required. No citations required. No jargon required.**

---

## Step 1 — Describe it concretely

Answer these questions as specifically as you can. Vague is OK; concrete details
are better.

```
1. What did you observe / imagine / dream?
   (Describe it like you're telling a friend who wasn't there.)

2. If it has a shape or geometry, describe it spatially.
   (Top/bottom, inside/outside, left/right, how big, what material.)

3. What was surprising or anomalous about it?
   (Why did it catch your attention? What "rule" did it seem to break?)

4. What does it remind you of, even if the analogy seems absurd?
   ("This felt like X" — complete this sentence.)

5. What field do you *think* this belongs to?
   (Physics, biology, mathematics, engineering, economics, something else?)

6. What would have to be true for this to be real / important?
```

---

## Step 2 — Feed to AI for triage

Give your answers from Step 1 to an AI assistant (Claude, Grok, GPT, etc.)
with this system prompt:

```
You are helping triage a pre-formal scientific observation for the Universal
Science Discovery Repository. The observer may have no scientific background.

Your job:
1. Identify which scientific fields the observation most likely belongs to.
2. Find any existing named phenomena, devices, or mathematical structures
   that match the description (even partially).
3. Identify what is genuinely novel or unexplained, if anything.
4. Draft a phenomenology entry in this YAML format:

id: p-[short-slug]
title: "[one-line description]"
origin: [dream|intuition|engineering-observation|everyday-observation|analogy|other]
date_observed: "[YYYY-MM-DD]"
status: raw
description: >
  [plain-language description]
sketch_description: >
  [geometry/spatial details if any]
why_anomalous: >
  [what makes this surprising]
analogies:
  - "[analogy 1]"
candidate_fields:
  - [field 1]
  - [field 2]
review_notes: >
  [What real device/phenomenon/equation this most closely matches.
   What the open question is, if anything.]

5. If the observation maps to a known device or phenomenon, explain it clearly
   in plain language so the observer understands what they intuited.
6. If there is a genuinely open question embedded in the observation, suggest
   a draft u- unknown title.
```

---

## Step 3 — Submit to the repo

1. Save the YAML output to `phenomenology/[field]/p-[your-slug].yaml`
2. Open a GitHub Issue with label `content:phenomenon`
3. Tag it `needs-triage` — someone with domain expertise will review it

**That's it.** Your observation is now in the discovery pipeline.

---

## Examples of valid phenomenology entries

- "I dreamed of a wire wound non-helically inside an aluminum box — what is that?"
- "Every time I boil water in a specific pot, bubbles form in the same spots — why?"  
- "Airport security lines feel like they follow a mathematical pattern — is there one?"
- "My code gets slower in a specific non-obvious way that reminds me of traffic jams"
- "The way starling murmurations change direction looks identical to how opinions flip"
- "I noticed that every language I've studied has a word for 'the feeling after rain'"

All of these are valid entries. Some will map to known physics. Some will map to
existing bridges. Some will be genuinely new.

---

## Why this matters

The formal scientific literature captures discoveries *after* they've been
formalized. This catalog captures them *before* — at the moment of intuition,
when they're still just a feeling that something is connected, or a dream about
a machine you've never seen.

Alan Turing described his morphogenesis insight in a letter before writing the
mathematics. Ramanujan filled notebooks with results he couldn't prove.
Both were doing science. Neither would have passed peer review that day.

This is the place for that kind of observation.
