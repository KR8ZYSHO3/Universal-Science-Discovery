# Cross-domain bridges: mathematics ↔ biology

## Active bridges

### b-turing-reaction-diffusion — Turing instability ↔ biological pattern formation

Alan Turing's 1952 paper "The Chemical Basis of Morphogenesis" is one of the
most extraordinary predictions in all of science.  Writing before DNA was
understood, Turing showed that two diffusing chemicals — one a self-activator,
one an inhibitor of the activator — could spontaneously generate stripes, spots,
and labyrinthine patterns from a uniform starting state, *if* the inhibitor
diffuses faster than the activator.

The key mathematical condition is a ratio:

> **d = D_inhibitor / D_activator > d_critical**

When this ratio is met, the homogeneous steady state becomes unstable to
periodic perturbations at a characteristic wavelength:

> **Λ\* = 2π · √(D_activator / reaction_rate)**

This wavelength sets the *spacing* of whatever pattern forms — digit spacing,
stripe period, hair follicle density, intestinal villus pitch.

**The stunning confirmation (2012):** Müller et al. measured the diffusivities
of Nodal (the activator in zebrafish embryo patterning) and Lefty (its inhibitor)
using fluorescence correlation spectroscopy and found d = 20, well above d_c ~ 4.
The *predicted* stripe wavelength from those measurements alone was 0.48 mm.
The *observed* zebrafish stripe period is 0.5 mm.  No fitting.

### b-renormalization-biological-scaling — RG theory ↔ allometric scaling laws

See [`../mathematics-biology/b-renormalization-biological-scaling.yaml`](b-renormalization-biological-scaling.yaml)

---

## Why this bridge matters

Turing's result is not a metaphor or an analogy — it is an exact mathematical
equivalence.  If you can measure the two diffusivities and the reaction rates
in a developing embryo, you can predict the pattern spacing to within 15%
without any free parameters.

The fields were slow to connect:
- Turing published in 1952
- Gierer & Meinhardt formalized the activator-inhibitor framework in 1972
- Kondo & Asai made the first quantitative fish skin fit in 1995 — 43 years later
- The first *measurement* of the diffusivities confirming the Turing criteria came in 2012

This 60-year lag is exactly the kind of missed connection this repository exists to close.

## Open unknowns seeded by this bridge

- `u-turing-digit-wavelength-scaling` — does digit number scale with embryo width as Λ\*/limb_width?
- `u-turing-nodal-lefty-quantitative` — what constrains the reaction rates γ independently of Λ\*?
