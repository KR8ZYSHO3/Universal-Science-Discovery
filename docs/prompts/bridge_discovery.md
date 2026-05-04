# Bridge discovery prompt

Use this prompt when reading a paper or working through a topic to systematically
check whether the phenomenon being studied already has an analogue in another field —
and whether the two communities know about each other.

---

## The prompt

```
I am reading a paper / working on [TOPIC] in the field of [FIELD A].

Help me identify whether this phenomenon, model, or result has a close analogue in
one or more other scientific fields, where the fields may be using different language,
different experimental tools, or different mathematics to study what is fundamentally
the same underlying system or process.

For each candidate analogue field [FIELD B]:

1. BRIDGE CLAIM
   State precisely what concept, model, or result in [FIELD A] maps onto what concept,
   model, or result in [FIELD B]. Be specific about the mapping — do not just say
   "both study complexity."

2. TRANSLATION TABLE
   List 3–5 pairs of terms where one field's vocabulary corresponds to the other's,
   and explain why the correspondence is non-trivial (i.e. not just a synonym, but a
   genuine structural equivalence).

3. WHAT EACH FIELD HAS THAT THE OTHER LACKS
   - What tools / data / theory does [FIELD A] have that [FIELD B] needs?
   - What tools / data / theory does [FIELD B] have that [FIELD A] needs?

4. CROSS-POLLINATION OPPORTUNITY
   Describe one specific experiment, collaboration, or computation that becomes
   possible — or much more tractable — when both fields share knowledge.

5. COMMUNICATION GAP
   Why haven't these fields already converged? Name the specific barriers:
   journal siloing, incompatible training, grant structure, data format mismatch,
   terminology, etc.

6. STATUS ASSESSMENT
   Is this connection:
   - proposed  — plausible but not yet documented in cross-disciplinary literature
   - established — recognised in at least one explicit cross-disciplinary paper
   - contested — active disagreement about whether the analogy holds
   - stale — the fields have diverged or the connection was refuted

Rate your confidence in each candidate analogue on a scale of 1–5.
```

---

## How to use this output

Once you have responses, record the highest-confidence bridges as YAML entries under
`cross-domain/`. A bridge entry requires at minimum:

| Field | Content |
|-------|---------|
| `id` | `b-<field-a>-<field-b>` or `b-<short-descriptive-name>` |
| `title` | One sentence stating the equivalence |
| `status` | `proposed / established / contested / stale` |
| `fields` | At least two disciplines |
| `bridge_claim` | The precise mapping, 2–5 sentences |

Then run `python scripts/validate_schemas.py` to confirm the file is valid.

---

## Heuristics for spotting bridge candidates

These patterns often signal an unrecognised cross-domain connection:

| Signal | Example |
|--------|---------|
| Power-law / scale-free behaviour | Zipf in language, Pareto in economics, scale-free networks in biology — often the same universality class |
| Phase transitions and critical points | Any field that describes a sharp qualitative change as a parameter crosses a threshold |
| Conservation laws | When two fields have conserved quantities with the same mathematical structure |
| Network topology | Graph-theoretic results (percolation, small-world, modularity) apply wherever entities connect |
| Optimisation under constraints | Evolution, economics, and engineering all find optima under resource constraints — the mathematics is shared |
| Self-organisation | Whenever a system develops structure without a central controller |
| Information and entropy | Shannon entropy appears in thermodynamics, biology, linguistics, and finance |
| Oscillators and synchronisation | Kuramoto model applies to neurons, fireflies, power grids, and financial markets |

---

## Example: How the existing bridges were found

> **Session:** Reading arXiv 2504.18362 on percolation in active solids.
>
> Bridge candidate: statistical physics ↔ oncology
>
> Bridge claim: The percolation threshold in a passive bond network is the same
> mathematical object as the minimum viable vascular density in a tumour under
> adaptive therapy. Active matter physics adds a new wrinkle — self-propulsion
> can drive a network *below* its threshold paradoxically.
>
> Result: `b-percolation-oncology` (existing entry) strengthened; new unknown
> `u-active-matter-percolation` opened from the physics side.

See [`cross-domain/`](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/tree/main/cross-domain)
for the full catalog of existing bridges.
