/**
 * In-browser Crosscheck for 2D site percolation finite-size scaling.
 *
 * Same estimator, lattices, sample count, and 15% gate as
 * simulate_percolation_fss.py. The RESULT line is the weighted fit.
 * It is not preset.
 *
 * Estimator id: mean-first-either-wrap
 * p_c(L) = mean occupation fraction at first wrapping in either direction.
 */
(function () {
  "use strict";

  const PC_INF = 0.59274621;
  const NU_THEORY = 4 / 3;
  const NU_TOLERANCE = 0.15;
  const R2_MIN = 0.85;
  const FIT_SIZES = [32, 64, 128, 256];
  const N_SAMPLES = 400;
  const SEED = 42;
  const ESTIMATOR_ID = "mean-first-either-wrap";
  const ESTIMATOR_SENTENCE =
    "2D site percolation, periodic 4-neighbor square lattice, Newman–Ziff; p_c(L) is the mean occupation fraction at first wrapping in either direction.";

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

  function shuffle(arr, rng) {
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(rng() * (i + 1));
      const tmp = arr[i];
      arr[i] = arr[j];
      arr[j] = tmp;
    }
  }

  function firstWrapEither(L, rng) {
    const n = L * L;
    const parent = new Int32Array(n);
    const dx = new Int32Array(n);
    const dy = new Int32Array(n);
    const rank = new Int32Array(n);
    const occupied = new Uint8Array(n);
    for (let i = 0; i < n; i++) parent[i] = i;

    function find(x) {
      if (parent[x] !== x) {
        const orig = parent[x];
        const root = find(orig);
        dx[x] += dx[orig];
        dy[x] += dy[orig];
        parent[x] = root;
        return root;
      }
      return x;
    }

    const order = new Int32Array(n);
    for (let i = 0; i < n; i++) order[i] = i;
    shuffle(order, rng);

    let wrapH = false;
    let wrapV = false;
    for (let k = 0; k < n; k++) {
      const s = order[k];
      occupied[s] = 1;
      const r = (s / L) | 0;
      const c = s - r * L;
      const bonds = [
        [(r - 1 + L) % L, c, -1, 0],
        [(r + 1) % L, c, 1, 0],
        [r, (c - 1 + L) % L, 0, -1],
        [r, (c + 1) % L, 0, 1],
      ];
      for (const [nr, nc, by, bx] of bonds) {
        const t = nr * L + nc;
        if (!occupied[t]) continue;
        const rs = find(s);
        const rt = find(t);
        if (rs === rt) {
          const wx = dx[s] + bx - dx[t];
          const wy = dy[s] + by - dy[t];
          if (wx !== 0) wrapH = true;
          if (wy !== 0) wrapV = true;
        } else if (rank[rs] < rank[rt]) {
          parent[rs] = rt;
          dx[rs] = dx[t] - bx - dx[s];
          dy[rs] = dy[t] - by - dy[s];
        } else {
          parent[rt] = rs;
          dx[rt] = dx[s] + bx - dx[t];
          dy[rt] = dy[s] + by - dy[t];
          if (rank[rs] === rank[rt]) rank[rs] += 1;
        }
      }
      if (wrapH || wrapV) return (k + 1) / n;
    }
    return 1.0;
  }

  function meanSe(ps) {
    const m = ps.length;
    const mean = ps.reduce((a, b) => a + b, 0) / m;
    let varSum = 0;
    for (const p of ps) varSum += (p - mean) ** 2;
    const sigma = Math.sqrt(varSum / (m - 1));
    return { mean, se: sigma / Math.sqrt(m), sigma };
  }

  function wlsThroughOrigin(x, y, se) {
    const w = se.map((s) => (s > 0 ? 1 / (s * s) : 0));
    let den = 0;
    let num = 0;
    for (let i = 0; i < x.length; i++) {
      den += w[i] * x[i] * x[i];
      num += w[i] * x[i] * y[i];
    }
    if (den <= 0) return { c: 0, seC: Infinity, chi2: Infinity, r2: 0 };
    const c = num / den;
    const seC = Math.sqrt(1 / den);
    let chi2 = 0;
    let ssRes = 0;
    let ySum = 0;
    for (const yi of y) ySum += yi;
    const yMean = ySum / y.length;
    let ssTot = 0;
    for (let i = 0; i < x.length; i++) {
      const ri = y[i] - c * x[i];
      chi2 += w[i] * ri * ri;
      ssRes += ri * ri;
      const d = y[i] - yMean;
      ssTot += d * d;
    }
    return { c, seC, chi2, r2: ssTot ? 1 - ssRes / ssTot : 0 };
  }

  function seNuFromChi2(chi2Of, nuHat, chi2Min) {
    const target = chi2Min + 1;
    let left = chi2Of[0][0];
    let right = chi2Of[chi2Of.length - 1][0];
    let prevNu = chi2Of[0][0];
    let prevChi = chi2Of[0][1];
    let foundLeft = false;
    let foundRight = false;
    for (let i = 1; i < chi2Of.length; i++) {
      const nu = chi2Of[i][0];
      const chi2 = chi2Of[i][1];
      if (!foundLeft && prevNu <= nuHat && prevChi >= target && target > chi2) {
        const denom = prevChi - chi2;
        const frac = denom ? (prevChi - target) / denom : 0;
        left = prevNu + frac * (nu - prevNu);
        foundLeft = true;
      }
      if (!foundRight && prevNu >= nuHat && prevChi < target && target <= chi2) {
        const denom = chi2 - prevChi;
        const frac = denom ? (target - prevChi) / denom : 0;
        right = prevNu + frac * (nu - prevNu);
        foundRight = true;
      }
      prevNu = nu;
      prevChi = chi2;
    }
    return Math.max(nuHat - left, right - nuHat);
  }

  function fitA(sizes, pcs, ses) {
    const y = pcs.map((pc) => pc - PC_INF);
    const chi2Of = [];
    let best = null;
    for (let i = 0; i <= (2.5 - 0.5) / 0.002; i++) {
      const nu = 0.5 + i * 0.002;
      const x = sizes.map((L) => L ** (-1 / nu));
      const fit = wlsThroughOrigin(x, y, ses);
      chi2Of.push([nu, fit.chi2]);
      if (!best || fit.chi2 < best.chi2) {
        best = { chi2: fit.chi2, nu, c: fit.c, seC: fit.seC, r2: fit.r2 };
      }
    }
    const seNu = seNuFromChi2(chi2Of, best.nu, best.chi2);
    return {
      nu: best.nu,
      seNu,
      c: best.c,
      seC: best.seC,
      chi2: best.chi2,
      r2: best.r2,
      relErr: Math.abs(best.nu - NU_THEORY) / NU_THEORY,
    };
  }

  function sameSignDeltas(pcs) {
    const deltas = pcs.map((pc) => pc - PC_INF);
    if (deltas.some((d) => d === 0)) return false;
    const signs = deltas.map((d) => d > 0);
    return signs.every(Boolean) || signs.every((s) => !s);
  }

  function approachesPc(sizes, pcs, ses) {
    const absD = pcs.map((pc) => Math.abs(pc - PC_INF));
    for (let i = 0; i < sizes.length - 1; i++) {
      const slack = 2 * (ses[i] + ses[i + 1]);
      if (absD[i + 1] > absD[i] + slack) return false;
    }
    return true;
  }

  function classify(fit, pcs, ses) {
    const powered = fit.seNu <= NU_TOLERANCE * NU_THEORY;
    const r2Ok = fit.r2 >= R2_MIN;
    const slopeSig = Math.abs(fit.c) > 2 * fit.seC;
    const within = fit.relErr <= NU_TOLERANCE;
    const signOk = sameSignDeltas(pcs);
    const mono = pcs.length === FIT_SIZES.length ? approachesPc(FIT_SIZES, pcs, ses) : signOk;
    if (!signOk || !powered || !slopeSig || !r2Ok) return "INCONCLUSIVE";
    if (within && mono) return "CONFIRMED";
    if (!within && Math.abs(fit.nu - NU_THEORY) > 2 * fit.seNu) return "FALSIFIED";
    return "INCONCLUSIVE";
  }

  async function runPercolationFss(emit) {
    emit({
      type: "line",
      text: "Crosscheck: p-b-habitat-percolation-ecology-fss",
    });
    emit({ type: "line", text: ESTIMATOR_SENTENCE });
    emit({
      type: "line",
      text: `Estimator id: ${ESTIMATOR_ID} (do not switch to horizontal-only wrap without refitting c)`,
    });
    emit({
      type: "line",
      text: `Theory: p_c(inf)=${PC_INF}, nu=${NU_THEORY.toFixed(4)}. Gate: 15% on nu, R² ≥ ${R2_MIN}.`,
    });
    emit({
      type: "line",
      text: `Params: L in [${FIT_SIZES.join(", ")}], samples/L=${N_SAMPLES}, seed=${SEED}. Result is the fit, not a preset.`,
    });
    emit({ type: "line", text: "" });

    const rng = mulberry32(SEED);
    const rows = [];
    const total = FIT_SIZES.length * N_SAMPLES;
    let done = 0;
    for (let i = 0; i < FIT_SIZES.length; i++) {
      const L = FIT_SIZES[i];
      const ps = [];
      for (let t = 0; t < N_SAMPLES; t++) {
        ps.push(firstWrapEither(L, rng));
        done += 1;
        if (t % 2 === 1) {
          emit({ type: "progress", pct: Math.round((100 * done) / total) });
          await yieldToBrowser();
        }
      }
      const { mean, se, sigma } = meanSe(ps);
      const delta = mean - PC_INF;
      const sign = delta >= 0 ? "+" : "";
      emit({
        type: "line",
        text:
          `  L=${String(L).padStart(4)}  p_c_hat=${mean.toFixed(5)} ± ${se.toFixed(5)}  ` +
          `delta=${sign}${delta.toFixed(5)}  sigma=${sigma.toFixed(5)}`,
      });
      rows.push({ L, mean, se, sigma });
    }

    const pcs = rows.map((row) => row.mean);
    const ses = rows.map((row) => row.se);
    const fit = fitA(FIT_SIZES, pcs, ses);
    const result = classify(fit, pcs, ses);

    emit({ type: "line", text: "" });
    emit({
      type: "line",
      text:
        `Fit A  nu = ${fit.nu.toFixed(4)} ± ${fit.seNu.toFixed(4)}   ` +
        `c = ${fit.c >= 0 ? "+" : ""}${fit.c.toFixed(4)} ± ${fit.seC.toFixed(4)}`,
    });
    emit({
      type: "line",
      text:
        `  R² = ${fit.r2.toFixed(4)}   rel err vs 4/3 = ${(100 * fit.relErr).toFixed(1)}%  (tolerance 15%)`,
    });
    if (result === "INCONCLUSIVE") {
      emit({
        type: "line",
        text: "INCONCLUSIVE means this run is underpowered or the fit is unstable. It is not a claim that percolation has the wrong exponent.",
      });
    } else if (result === "FALSIFIED") {
      emit({
        type: "line",
        text: "FALSIFIED means this run's fit disagrees with nu=4/3 past the gate. That is a protocol failure, not a disproof of percolation.",
      });
    } else {
      emit({
        type: "line",
        text: "CONFIRMED means this run's weighted fit recovered nu within 15% of 4/3, with a tight enough error bar.",
      });
    }
    emit({ type: "line", text: `RESULT: ${result}` });
    emit({ type: "progress", pct: 100 });
    emit({ type: "result", result });
    return { passed: result === "CONFIRMED", result, fit, rows };
  }

  const root = typeof window !== "undefined" ? window : globalThis;
  root.CrosscheckRuns = root.CrosscheckRuns || {};
  root.CrosscheckRuns["p-b-habitat-percolation-ecology-fss"] = runPercolationFss;
})();
