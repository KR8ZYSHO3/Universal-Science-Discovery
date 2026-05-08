# How Physicists Priced Options Before Traders Did

*Bridge: b-turbulence-financial-markets (physics-finance)*

---

In 1827, botanist Robert Brown observed pollen grains zigzagging randomly through water.
In 1905, Albert Einstein explained it: each grain is being buffeted by millions of
invisible water molecules, executing what we now call **Brownian motion**. In 1973,
Fischer Black and Myron Scholes published a formula for pricing stock options — and
without realizing it, they had rediscovered the same mathematics Einstein used to
describe pollen.

## What is an option?

A stock option gives you the right — but not the obligation — to buy a stock at a fixed
price (the "strike price") on a future date. If the stock price rises above the strike,
you exercise the option and pocket the difference. If it falls below, you let it expire
worthless. The question is: what should you pay for this right today?

Black and Scholes' breakthrough was to realize that you can construct a **hedging
portfolio** — a combination of the option and the underlying stock — that is momentarily
risk-free, regardless of which direction the stock moves next. A risk-free portfolio
must earn exactly the risk-free interest rate. This constraint turns into a partial
differential equation for the option price.

## The equation that changed finance

The Black-Scholes equation for the price of an option *V* as a function of stock price
*S* and time *t* is:

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS \frac{\partial V}{\partial S} - rV = 0$$

where σ is the volatility (standard deviation of log-returns) and *r* is the risk-free
interest rate. If you've seen this before in physics class, you should recognize it.
With the substitution *x* = ln(*S*), this equation becomes the **heat equation**:

$$\frac{\partial V}{\partial t} = \frac{\sigma^2}{2} \frac{\partial^2 V}{\partial x^2}$$

This is exactly the equation describing how heat spreads through a metal rod, or how
ink diffuses through water, or how a cloud of pollen particles spreads through a still
liquid. The stock option price *is* temperature. The log-price is position. Volatility
is thermal diffusivity.

## Why the analogy is exact, not approximate

The connection is not accidental. The stock price model underlying Black-Scholes assumes
that log-returns are drawn independently from a normal distribution — exactly the
statistical model for Brownian motion that Einstein derived from first principles.
Brownian motion is the unique continuous stochastic process with independent increments
and finite variance. The heat equation is its governing PDE.

This means that every intuition about heat diffusion applies directly to option pricing:

- **Heat spreads from hot to cold** → option value spreads from high-payoff to
  low-payoff regions as time passes.
- **A thin hot wire spreads heat in a Gaussian profile** → a "digital" option with
  a spike payoff at one stock price spreads into a bell curve of probability over time.
- **More thermal diffusivity = faster spreading** → higher volatility = wider range of
  possible option payoffs, making options more valuable.
- **Boundary conditions determine the solution** → the option's payoff function at
  expiration is the "initial condition" (running time backward), and no-arbitrage
  constraints are the boundary conditions.

## What traders got wrong and physicists saw clearly

Finance textbooks in the 1950s treated option pricing as a matter of taste — there was
no agreed formula, and traders relied on intuition. The key insight Black and Scholes
(and, independently, Robert Merton) brought was to reframe the question: not "what is
this option worth to me?" but "what is the cheapest portfolio that exactly replicates
the option's payoff in every possible future state?" That replication argument — borrowed
implicitly from physics' focus on deterministic constraints rather than preferences —
is what makes the Black-Scholes price unique and universally agreed.

## The limits of the analogy

The Black-Scholes formula is elegant but its assumptions fail in practice:

- Real stock returns have **fat tails** — extreme events are far more common than the
  Gaussian model predicts. (Heat diffusion has Gaussian tails; financial crises do not.)
- **Volatility is not constant** — it clusters (high volatility days cluster together),
  which heat diffusion with constant thermal diffusivity cannot capture.
- **Illiquid markets** cannot be continuously hedged, breaking the no-arbitrage argument.

The map from heat equation to option price is exact within the model, but the model
is an idealization. The important lesson is methodological: a physicist's toolkit —
stochastic processes, PDEs, boundary value problems — translated directly into a
framework for pricing financial instruments that traders had previously treated as
entirely subjective. The pollen grain and the stock certificate are, mathematically,
the same object.

---

*Further reading: Black & Scholes (1973) "The pricing of options and corporate
liabilities." Journal of Political Economy 81(3):637-654. Bachelier L (1900)
"Théorie de la spéculation" — the original connection between Brownian motion and
financial markets, predating Einstein by five years.*
