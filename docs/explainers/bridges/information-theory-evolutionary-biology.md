# Natural Selection Is a Bayesian Algorithm

*Bridge: b-fisher-information-evolution (statistics-evolution)*

---

In 1763, Reverend Thomas Bayes described a method for updating beliefs in light of
evidence: start with a prior probability, multiply by the likelihood of observing
your data given each hypothesis, normalize, and get a posterior probability that
is more concentrated on the right answer. In 1859, Charles Darwin described a
process of updating populations in light of differential reproduction: start with
a distribution of heritable variation, apply selection pressure, normalize (the
survivors reproduce), and get a next generation more concentrated on well-adapted
forms. These are, it turns out, the same algorithm.

## How Bayesian inference works

Bayes' theorem says: **posterior ∝ prior × likelihood**.

More precisely: *P*(hypothesis | data) = *P*(data | hypothesis) × *P*(hypothesis) / *P*(data).

Start with your best guess about which hypothesis is true (the prior). Observe data.
Update by weighting each hypothesis by how well it explains the data (the likelihood).
Renormalize. Repeat each time you get new data. Over many rounds of observation,
your beliefs converge toward the truth — the prior gradually washes out and the
posterior is dominated by accumulated evidence.

## How natural selection works

Consider a population with two alleles at a gene: A (frequency *p*) and B (frequency
1-*p*). Allele A gives its carriers fitness *w_A* (expected offspring); allele B gives
fitness *w_B*. After one generation of selection, the frequency of A becomes:

*p'* = *p* × *w_A* / (*p* × *w_A* + (1-*p*) × *w_B*)

Now look at this formula. If you identify:
- *p* with the prior probability of hypothesis A
- *w_A* with the likelihood of observing the environment given allele A
- the denominator with the normalizing constant *P*(data)

...then *p'* is exactly the **Bayesian posterior** for allele A after one round of updating.

Natural selection is Bayesian updating in disguise. The "data" is the environment.
The "hypothesis" is the allele. The "likelihood" is fitness. Selection updates
population frequencies exactly as Bayes' theorem updates beliefs.

## What this connection actually means

This is not just a formal trick. The analogy generates genuine insight in both
directions:

**From Bayesian theory to evolution:**

- **Rates of adaptation** correspond to how much information about the environment
  is contained in the selection differential. Fisher's fundamental theorem of natural
  selection — "the rate of increase in fitness equals the additive genetic variance"
  — is the evolutionary analog of the information-theoretic result that Bayesian
  updating is fastest when the prior is most diffuse (maximum entropy).

- **Bet-hedging** in biology (some organisms randomize their offspring's phenotypes)
  is the evolutionary equivalent of keeping a diffuse prior when the environment
  is uncertain — a rational Bayesian strategy for maximizing long-run fitness under
  temporal variation.

- **Sexual recombination** shuffles alleles between individuals, generating novel
  combinations that selection hasn't yet seen. In Bayesian terms, this is
  **exploration** — sampling from a wider distribution to find higher-likelihood
  hypotheses, rather than exploiting the current best estimate.

**From evolution to Bayesian theory:**

- **Overfitting** in machine learning corresponds to a population perfectly adapted
  to one environment that then goes extinct when the environment changes. Evolutionary
  robustness — staying slightly sub-optimal across many environments — is the
  biological version of regularization.

- **Genetic drift** (random fluctuation in allele frequencies in small populations)
  is the evolutionary analog of **sampling noise** in Bayesian inference from few
  data points. Small populations drift away from the fitness peak just as Bayesian
  inference with few observations retains high posterior uncertainty.

## Where the analogy breaks down

Natural selection is not *exactly* Bayesian inference, and the differences are instructive:

- Bayesian inference can combine information across independent datasets perfectly.
  Natural selection cannot: information is destroyed at every death event (phenotypes
  that die don't pass on what they learned). Lamarckian evolution would be Bayesian;
  Darwinian evolution is only Bayesian at the population-frequency level.

- Mutation introduces **model jumps** — new hypotheses (alleles, genes, whole genome
  duplications) that were not in the original prior. Bayesian inference within a
  fixed hypothesis space cannot do this; only transdimensional methods (reversible-jump
  MCMC) come close. Evolution's ability to generate genuinely novel variation has no
  clean Bayesian analog.

- Epistasis — gene interactions where the effect of allele A depends on what allele
  is present at gene B — breaks the independence assumptions that make Bayesian
  computation tractable. Evolution navigates a fitness landscape with high-dimensional
  dependencies that no Bayesian algorithm scales to efficiently.

## The deeper implication

The correspondence between Bayesian inference and natural selection suggests that
**any adaptive process operating on heritable variation under selection pressure will
inevitably implement something like Bayesian updating**. This is not a coincidence —
it is a consequence of the mathematics of probability: there is only one way to
update a probability distribution on observations that satisfies coherence conditions
(Dutch book arguments), and it is Bayes' theorem.

Brains learn by approximately Bayesian inference. Immune systems adapt by clonal
selection (literally evolutionary dynamics applied to antibody populations). Cultural
evolution spreads memes by differential replication. In each case, the algorithm
that emerges from the selection pressure is recognizably Bayesian — not because
evolution or learning theory "knows" about Bayes, but because Bayesian updating
is the uniquely rational response to new evidence, and any adaptive system that
fails to be approximately Bayesian will be outcompeted by one that is.

---

*Further reading: Harper M (2009) "The replicator equation as an inference dynamic."
arXiv:0911.1763. Frank SA (2012) "Natural selection. V. How to read the fundamental
equations of evolutionary change in terms of information theory." J Evol Biol 25:2377-2396.*
