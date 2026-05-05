# Information Theory ↔ Molecular Evolution

## The bridge in one sentence

Eigen's error threshold (the mutation rate above which genetic information is lost)
and Shannon's channel capacity theorem (the noise level above which transmitted
information is lost) are the same mathematical result — Claude Shannon and Charles
Darwin have been studying the same problem for 70 years without knowing it.

## Shannon meets Darwin

| Shannon (1948) | Eigen (1971) |
|----------------|--------------|
| Binary symmetric channel noise p | Per-base mutation rate mu |
| Channel capacity C = 1 - H(p) | Error threshold mu_c = sigma/L |
| Information rate exceeds capacity → erasure | Mutation rate exceeds threshold → error catastrophe |
| Error-correcting code | DNA repair, proofreading exonuclease |
| Block length N | Genome length L |
| Capacity-approaching code (polar code, LDPC) | Near-threshold genome (RNA virus) |

The formal equivalence was established in 1979 (Eigen & Schuster) and 1997
(Domingo & Holland). Despite this, virology journals don't use information-theoretic
notation and coding theorists are unaware that RNA viruses have been solving
near-capacity replication problems for billions of years.

## The coronavirus case study

SARS-CoV-2 has the largest known RNA genome (~30 kb). It achieves this by encoding
the nsp14 proofreading exonuclease, which reduces its mutation rate ~15x. This is a
direct Shannon capacity expansion: higher channel fidelity → larger information
content → larger genome. The quantitative trade-off is predicted by the Shannon
bound. The prediction has never been tested across nidovirus genome sizes.

## Bridge entries

- [`b-error-threshold-information`](b-error-threshold-information.yaml)

## Unknowns seeded here

- [`u-error-threshold-genome-size`](../../unknowns-catalog/biology/u-error-threshold-genome-size.yaml)

## Hypotheses to test

- [`h-viral-proofreading-shannon-optimality`](../../hypotheses/active/h-viral-proofreading-shannon-optimality.yaml)

## Next contributor action

1. Compile mutation rates and genome sizes for all sequenced nidoviruses (public data)
2. Fit the Shannon bound C = 1 - H(mu) to the (mu, L) distribution
3. Test whether nsp14+ species cluster at higher L*mu than nsp14- species
4. Open a PR against `h-viral-proofreading-shannon-optimality.yaml`
