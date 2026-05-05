# Cross-domain bridges: physics ↔ information theory

## Active bridges

### b-landauer-information-thermodynamics — Landauer's principle ↔ thermodynamic cost of computation

In 1867, James Clerk Maxwell proposed a thought experiment: a tiny demon
controls a trapdoor between two gas chambers and sorts fast molecules to one
side, apparently reducing entropy without doing work — violating the second law.

The paradox went unresolved for **94 years**.

In 1961, Rolf Landauer at IBM wrote a two-page paper with a startling answer:
the demon must *store* information about each molecule it sorts.  When the
demon's memory fills up and must be erased to make room for the next measurement,
that erasure is irreversible and costs exactly:

> **k_B · T · ln(2)  per bit erased  ≈ 3 × 10⁻²¹ J at room temperature**

This is the **Landauer limit** — the absolute minimum energy any computation
must dissipate per bit of information destroyed.  It connects Shannon's abstract
information entropy directly to Boltzmann's physical thermodynamic entropy.

**Experimental verification (2012):** Berut et al. trapped a colloidal particle
in a laser double-well potential (a physical 1-bit memory), erased the bit by
tilting the potential, and measured the heat dissipated.  Result: within 1% of
the Landauer limit.

**Why this matters for technology:** A modern CPU erases ~10¹⁸ bits per second.
The minimum power it could ever dissipate is ~3 nW.  Actual dissipation is ~100 W
— 10 orders of magnitude above the limit.  Neuromorphic computing and optical
computing are closing that gap.

**Why this matters for biology:** A synapse fires by erasing the state of ion
channels (a bit erasure).  The per-synapse energy budget (measured by Attwell &
Laughlin 2001) places the brain within ~10² of the Landauer limit per synaptic
event — closer to the physical bound than any silicon processor.

---

## Related bridges

- `b-error-threshold-information` — Shannon capacity of the mutation channel
- `b-fisher-information-evolution` — Fisher information as a thermodynamic resource
