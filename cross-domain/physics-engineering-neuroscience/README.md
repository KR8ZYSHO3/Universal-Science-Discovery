# Physics ↔ Engineering ↔ Neuroscience (Kuramoto Synchronization)

## The bridge in one sentence

The Kuramoto model of coupled phase oscillators governs neural gamma oscillations,
cardiac pacemaker synchrony, power-grid frequency stability, and laser array
coherence — four separate fields sharing identical governing equations that have
almost never exchanged analytical results.

## The four fields, one equation

```
d(theta_i)/dt = omega_i + (K/N) * sum_j sin(theta_j - theta_i)
```

| Field | theta_i | K | Order parameter r |
|-------|---------|---|-------------------|
| Neuroscience | interneuron phase | GABAergic synapse conductance | LFP gamma power |
| Cardiology | pacemaker cell phase | gap junction conductance | Atrial synchrony index |
| Power engineering | generator rotor angle | transmission line susceptance | Grid frequency coherence |
| Laser physics | cavity phase | injection coupling | Array coherence |

## Why this matters for patients

Atrial fibrillation (AF) affects 60 million people. AF onset is a Kuramoto
desynchronization transition — coupling K drops below K_c due to fibrosis and gap
junction remodelling. The spectral gap of the sinoatrial coupling network determines
K_c. This formula was derived by power engineers for grid stability. It has never
been applied to cardiac tissue.

## Bridge entries

- [`b-kuramoto-synchronization`](b-kuramoto-synchronization.yaml)

## Hypotheses to test

- [`h-kuramoto-af-spectral-gap`](../../hypotheses/active/h-kuramoto-af-spectral-gap.yaml)
- [`h-cardiac-arrhythmia-phase-transition`](../../hypotheses/active/h-cardiac-arrhythmia-phase-transition.yaml) *(seeded earlier, directly connected)*

## Related bridges

- [`b-criticality-neuroscience`](../physics-neuroscience/b-criticality-neuroscience.yaml) — Kuramoto is the mechanism behind neural phase transitions

## Next contributor action

1. Obtain a human sinoatrial node gap junction immunofluorescence dataset (Dobrzynski 2013 is public)
2. Construct the coupling Laplacian and compute spectral gap lambda_2
3. Predict K_c from the power-engineering formula K_c = 1/lambda_2
4. Compare to observed AF inducibility threshold from electrophysiology
5. Open a PR against `h-kuramoto-af-spectral-gap.yaml`
