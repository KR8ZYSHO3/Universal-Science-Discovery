# Cross-domain bridges: physics ↔ complexity science

## Active bridges

### b-self-organized-criticality — SOC ↔ brains, earthquakes, forest fires, extinctions

Per Bak had a simple question in 1987: what does a pile of sand do?

He and colleagues built a cellular automaton — the "sandpile model" — where grains
are added one at a time and topple when a threshold is exceeded.  The surprising
result: without any parameter tuning, the pile drives itself to a critical state
where avalanche sizes follow a power law with exponent **-3/2**.

This is **self-organized criticality (SOC)**: the system finds the critical point
on its own.  And then the same exponent started showing up everywhere:

| System | Observable | Exponent | Source |
|--------|-----------|---------|--------|
| Sandpile (BTW model) | Avalanche size | **-3/2** | Bak et al. 1987 |
| Cortical neurons | Neural avalanche size | **-3/2** | Beggs & Plenz 2003 |
| Earthquakes | Energy release | -1 to -1.5 | Gutenberg-Richter |
| Forest fires | Burned area | -1.2 to -1.4 | Malamud et al. 1998 |
| Extinction events | Species lost | -2 | Sole & Manrubia 1996 |
| Solar flares | Energy | -1.8 | Lu & Hamilton 1991 |

The neural result is the most striking: the brain's cortex, recorded in vitro and
in vivo, produces cascades of neural activity whose size distribution follows the
**same power law** as a sandpile.  This isn't a metaphor — the statistics are
indistinguishable.

**Why the brain might want to be critical:** at the critical point, dynamic range
(the ability to respond to inputs spanning many orders of magnitude) is maximised,
and information transmission between regions peaks.  Deviation from criticality —
subcritical silence or supercritical seizure — degrades both.

## Related bridges

- `b-criticality-neuroscience` — brain criticality more broadly
- `b-tipping-points-phase-transitions` — climate tipping as SOC-adjacent
- `b-turbulence-financial-markets` — financial crashes may have SOC statistics
- `b-percolation-epidemiology` — epidemic threshold as a different kind of criticality
