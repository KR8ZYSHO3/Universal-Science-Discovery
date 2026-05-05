# Statistics ↔ Evolutionary Biology (Fisher Information)

## The bridge in one sentence

R.A. Fisher invented both statistical Fisher information (1925) and the fundamental
theorem of natural selection (1930) — they are the same mathematical object, giving
evolutionary biology the full toolkit of statistical estimation theory and connecting
natural selection to natural gradient ascent in machine learning.

## The identity

Fisher's fundamental theorem:
```
dW̄/dt = V_A    (rate of mean fitness increase = additive genetic variance)
```

Fisher information interpretation:
```
V_A = I_pop    (additive genetic variance = population Fisher information about fitness gradient)
```

Therefore: **evolution proceeds at the speed allowed by the population's Fisher information.**

## The three-way connection

```
Statistics          Evolution               Machine Learning
─────────────────────────────────────────────────────────────
Fisher info I(θ)  = Additive variance V_A = Hessian of objective
Cramér-Rao bound  = Selection speed limit  = Convergence lower bound
Natural gradient  = Natural selection      = Natural Policy Gradient / TRPO
Score function    = Selection gradient     = Policy gradient estimator
```

## Connection to quantum sensing

The `h-quantum-compass-precision` hypothesis already in this repository proposes
that cryptochrome CRY4 operates at the *quantum* Fisher-information Cramér-Rao bound.
The Fisher bridge connects classical evolution, quantum sensing, and machine learning
into a single information-geometric framework.

## Bridge entries

- [`b-fisher-information-evolution`](b-fisher-information-evolution.yaml)

## Unknowns seeded here

- [`u-fisher-natural-gradient-evolution`](../../unknowns-catalog/biology/u-fisher-natural-gradient-evolution.yaml)

## Hypotheses to test

- [`h-fisher-speed-limit-selection`](../../hypotheses/active/h-fisher-speed-limit-selection.yaml)

## Next contributor action

1. Download the Illinois long-term maize oil selection dataset (>100 generations, public)
2. Compute G-matrix at each 10-generation interval
3. Fit Fisher speed limit: compare R/(V_A * beta) across generations
4. Test whether response direction matches natural gradient vs ordinary gradient
5. Open a PR against `h-fisher-speed-limit-selection.yaml`
