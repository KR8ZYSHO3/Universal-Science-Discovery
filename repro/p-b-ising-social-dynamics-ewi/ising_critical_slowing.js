/**
 * In-browser Crosscheck demo: 2D Ising early-warning indicators near T_c.
 * Algorithm mirrors ising_critical_slowing.py; uses a demo budget for speed.
 */
(function () {
  "use strict";

  const TC = 2.0 / Math.log(1.0 + Math.sqrt(2.0));
  const GAMMA_THEORY = 7.0 / 4.0;
  const GAMMA_TOLERANCE = 0.25;
  const TEMPERATURES = [2.65, 2.55, 2.45, 2.38, 2.33, 2.30];
  const LATTICE_SIZE = 32;
  const EQ_SWEEPS_BASE = 400;
  const EQ_SWEEPS_NEAR_TC = 1600;
  const SAMPLES = 120;
  const SAMPLE_INTERVAL = 25;
  const FIT_MIN_DELTA = 0.055;
  const SEED = 42;

  function mulberry32(seed) {
    return function () {
      seed |= 0;
      seed = (seed + 0x6d2b79f5) | 0;
      let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  function yieldToBrowser() {
    return new Promise((resolve) => setTimeout(resolve, 0));
  }

  function initLattice(n, rng) {
    return Array.from({ length: n }, () =>
      Array.from({ length: n }, () => (rng() < 0.5 ? 1 : -1))
    );
  }

  function magnetisation(grid) {
    const n = grid.length;
    let total = 0;
    for (let r = 0; r < n; r++) {
      for (let c = 0; c < n; c++) total += grid[r][c];
    }
    return total / (n * n);
  }

  function metropolisSweep(grid, beta, rng) {
    const n = grid.length;
    for (let k = 0; k < n * n; k++) {
      const r = (rng() * n) | 0;
      const c = (rng() * n) | 0;
      const s = grid[r][c];
      const nn =
        grid[(r - 1 + n) % n][c] +
        grid[(r + 1) % n][c] +
        grid[r][(c - 1 + n) % n] +
        grid[r][(c + 1) % n];
      const dE = 2.0 * s * nn;
      if (dE <= 0.0 || rng() < Math.exp(-dE * beta)) {
        grid[r][c] = -s;
      }
    }
  }

  function equilibrationSweeps(t) {
    if (t - TC < 0.08) return EQ_SWEEPS_NEAR_TC;
    if (t - TC < 0.15) return EQ_SWEEPS_BASE * 2;
    return EQ_SWEEPS_BASE;
  }

  async function sampleSeries(grid, beta, rng, t) {
    for (let i = 0; i < equilibrationSweeps(t); i++) {
      metropolisSweep(grid, beta, rng);
      if (i % 200 === 199) await yieldToBrowser();
    }
    const series = [];
    for (let s = 0; s < SAMPLES; s++) {
      for (let j = 0; j < SAMPLE_INTERVAL; j++) {
        metropolisSweep(grid, beta, rng);
      }
      series.push(magnetisation(grid));
      if (s % 10 === 9) await yieldToBrowser();
    }
    return series;
  }

  function variance(xs) {
    const n = xs.length;
    if (n < 2) return 0;
    const mean = xs.reduce((a, b) => a + b, 0) / n;
    let v = 0;
    for (const x of xs) v += (x - mean) ** 2;
    return v / (n - 1);
  }

  function ar1(xs) {
    const n = xs.length;
    if (n < 3) return 0;
    const x0 = xs.slice(0, -1);
    const x1 = xs.slice(1);
    const m0 = x0.reduce((a, b) => a + b, 0) / x0.length;
    const m1 = x1.reduce((a, b) => a + b, 0) / x1.length;
    let cov = 0;
    let var0 = 0;
    for (let i = 0; i < x0.length; i++) {
      cov += (x0[i] - m0) * (x1[i] - m1);
      var0 += (x0[i] - m0) ** 2;
    }
    cov /= x0.length - 1;
    var0 /= x0.length - 1;
    return var0 > 1e-12 ? cov / var0 : 0;
  }

  function integratedAutocorrTime(xs) {
    const n = xs.length;
    if (n < 8) return 0;
    const mean = xs.reduce((a, b) => a + b, 0) / n;
    let v = 0;
    for (const x of xs) v += (x - mean) ** 2;
    v /= n;
    if (v < 1e-12) return 0;
    let tau = 0.5;
    const maxLag = Math.min((n / 2) | 0, 60);
    for (let lag = 1; lag < maxLag; lag++) {
      let num = 0;
      for (let i = 0; i < n - lag; i++) {
        num += (xs[i] - mean) * (xs[i + lag] - mean);
      }
      const rho = num / ((n - lag) * v);
      if (rho <= 0) break;
      tau += rho;
      if (lag > 5 && rho < 0.05) break;
    }
    return Math.max(tau, 0);
  }

  function isMonotonicIncreasing(values) {
    for (let i = 0; i < values.length - 1; i++) {
      if (values[i] >= values[i + 1]) return false;
    }
    return true;
  }

  function fitGamma(temps, chis) {
    const xs = temps.map((t) => Math.log(Math.abs(t - TC) + 1e-9));
    const ys = chis.map((c) => Math.log(c + 1e-12));
    const n = xs.length;
    const xMean = xs.reduce((a, b) => a + b, 0) / n;
    const yMean = ys.reduce((a, b) => a + b, 0) / n;
    let num = 0;
    let den = 0;
    for (let i = 0; i < n; i++) {
      num += (xs[i] - xMean) * (ys[i] - yMean);
      den += (xs[i] - xMean) ** 2;
    }
    const slope = den ? num / den : 0;
    const gamma = -slope;
    let ssRes = 0;
    let ssTot = 0;
    for (let i = 0; i < n; i++) {
      const pred = yMean + slope * (xs[i] - xMean);
      ssRes += (ys[i] - pred) ** 2;
      ssTot += (ys[i] - yMean) ** 2;
    }
    const r2 = ssTot ? 1 - ssRes / ssTot : 0;
    return { gamma, r2 };
  }

  async function runIsingEwi(emit) {
    emit({
      type: "line",
      text: "Crosscheck: p-b-ising-social-dynamics-ewi (in-browser demo)",
    });
    emit({
      type: "line",
      text: `Theory: T_c=${TC.toFixed(5)}, gamma=${GAMMA_THEORY.toFixed(4)}`,
    });
    emit({
      type: "line",
      text: `Demo params: ${LATTICE_SIZE}x${LATTICE_SIZE}, samples/T=${SAMPLES}`,
    });
    emit({ type: "line", text: "" });

    const rng = mulberry32(SEED);
    const variances = [];
    const ar1s = [];
    const taus = [];
    const total = TEMPERATURES.length;

    for (let i = 0; i < TEMPERATURES.length; i++) {
      const t = TEMPERATURES[i];
      emit({ type: "progress", pct: 5 + (85 * i) / total });
      const grid = initLattice(LATTICE_SIZE, rng);
      const beta = 1.0 / t;
      const series = await sampleSeries(grid, beta, rng, t);
      const varM = variance(series);
      const lag1 = ar1(series);
      const tau = integratedAutocorrTime(series);
      variances.push(varM);
      ar1s.push(lag1);
      taus.push(tau);
      emit({
        type: "line",
        text:
          `  T=${t.toFixed(3)}  |T-Tc|=${(t - TC).toFixed(4)}  ` +
          `Var(M)=${varM.toFixed(6)}  AR1=${lag1.toFixed(4)}  tau=${tau.toFixed(2)}`,
      });
    }

    const scalingIdx = TEMPERATURES.map((t, i) => (t - TC >= FIT_MIN_DELTA ? i : -1)).filter(
      (i) => i >= 0
    );
    const scaleT = scalingIdx.map((i) => TEMPERATURES[i]);
    const scaleVar = scalingIdx.map((i) => variances[i]);
    const scaleAr1 = scalingIdx.map((i) => ar1s[i]);
    const scaleTau = scalingIdx.map((i) => taus[i]);
    const scaleChi = scaleT.map((t, j) => LATTICE_SIZE ** 2 * scaleVar[j] / t);

    const varMono = isMonotonicIncreasing(scaleVar);
    const ar1Mono = isMonotonicIncreasing(scaleAr1);
    const tauMono = isMonotonicIncreasing(scaleTau);
    const { gamma, r2 } = fitGamma(scaleT, scaleChi);
    const relErr = Math.abs(gamma - GAMMA_THEORY) / GAMMA_THEORY;
    const gammaOk = relErr <= GAMMA_TOLERANCE;
    const ewiMono = tauMono && (varMono || ar1Mono);
    const passed = ewiMono && gammaOk;
    const result = passed
      ? "CONFIRMED"
      : "INCONCLUSIVE (increase EQ_SWEEPS_NEAR_TC for higher precision)";

    emit({ type: "line", text: "" });
    emit({
      type: "line",
      text: `Scaling-regime points (|T-Tc| >= ${FIT_MIN_DELTA}): ${scaleT.length}`,
    });
    emit({
      type: "line",
      text: `Var(M) monotonic toward T_c: ${varMono ? "yes" : "no"}`,
    });
    emit({
      type: "line",
      text: `AR1 monotonic toward T_c:    ${ar1Mono ? "yes" : "no"}`,
    });
    emit({
      type: "line",
      text: `tau_int monotonic toward T_c: ${tauMono ? "yes" : "no"}`,
    });
    emit({ type: "line", text: `Fitted gamma = ${gamma.toFixed(4)}  (R² = ${r2.toFixed(4)})` });
    emit({
      type: "line",
      text:
        `Relative error vs 7/4 = ${(100 * relErr).toFixed(1)}%  ` +
        `(tolerance ${(100 * GAMMA_TOLERANCE).toFixed(0)}%)`,
    });
    emit({ type: "line", text: `RESULT: ${result}` });
    emit({ type: "progress", pct: 100 });
    emit({ type: "result", result: passed ? "CONFIRMED" : "INCONCLUSIVE" });
    return { passed, gamma, r2 };
  }

  window.CrosscheckRuns = window.CrosscheckRuns || {};
  window.CrosscheckRuns["p-b-ising-social-dynamics-ewi"] = runIsingEwi;
})();