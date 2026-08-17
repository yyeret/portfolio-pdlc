#!/usr/bin/env python3
"""Deterministic Monte Carlo flow simulation for a portfolio-pdlc workspace.

Simulates initiatives flowing through the workspace's stages (WIP limits as capacity
constraints), estimating per-stage duration distributions from flow-log.csv where history
allows (>=3 samples, labeled `history`) and from triangular priors otherwise (labeled
`prior`). Compares a baseline against what-if scenario files. Stdlib only.

Usage:
  python3 portfolio_sim.py <workspace> [--scenario file]... [--runs N] [--horizon DAYS] [--seed N]

Output: a markdown comparison table on stdout, with confidence labels and run-to-run noise.
"""

import csv
import random
import re
import sys
from datetime import datetime
from pathlib import Path

DEFAULT_PRIORS = {
    "explore": (10, 21, 45),
    "discovery": (15, 30, 60),
    "plan-commit": (7, 20, 40),
    "execute": (45, 90, 180),
    "rollout": (10, 25, 60),
}
DEFAULTS = {
    "name": "baseline",
    "arrivals_per_quarter": 6.0,
    # dependency_tax semantics are RELATIVE: sampled/prior durations are assumed to already
    # contain the current system's coordination overhead (dependency_tax_current). A what-if
    # scales execute durations by dependency_tax / dependency_tax_current.
    "dependency_tax": 1.0,
    "dependency_tax_current": 1.0,
    # multitask_alpha models the load tax: items in a fuller stage run slower. Durations are
    # normalized so a stage running at the CURRENT WIP limit reproduces its history.
    "multitask_alpha": 0.25,
    "discovery_skip_rate": 0.3,
    "rollout_skip_rate": 0.4,
}


def parse_board_config_stages(ws):
    pdlc = ws / "pdlc.md"
    stages, wip_limits = ["explore", "discovery", "plan-commit", "execute", "rollout"], {}
    if pdlc.exists():
        m = re.search(r"<!--\s*board-config\s*(.*?)-->", pdlc.read_text(encoding="utf-8"), re.DOTALL)
        if m:
            for line in m.group(1).splitlines():
                key, _, val = line.strip().partition(":")
                key, val = key.strip(), val.strip()
                if key == "stages":
                    stages = [s.strip() for s in val.split(",") if s.strip() and s.strip() != "bau"]
                elif key == "wip_limits":
                    for pair in val.split(","):
                        if "=" in pair:
                            k, _, v = pair.partition("=")
                            try:
                                wip_limits[k.strip()] = int(v.strip())
                            except ValueError:
                                pass
    return stages, wip_limits


def load_history(ws, stages):
    """Per-stage duration samples from consecutive flow-log transitions."""
    log = ws / "flow-log.csv"
    samples = {s: [] for s in stages}
    if not log.exists():
        return samples
    entries = {}
    with log.open(newline="", encoding="utf-8") as fh:
        for row in csv.reader(fh):
            if len(row) >= 4 and row[0] != "date":
                try:
                    d = datetime.strptime(row[0].strip(), "%Y-%m-%d").date()
                except ValueError:
                    continue
                entries.setdefault(row[1], []).append((d, row[3]))
    for seq in entries.values():
        seq.sort()
        for (d1, s1), (d2, _s2) in zip(seq, seq[1:]):
            if s1 in samples and (d2 - d1).days > 0:
                samples[s1].append((d2 - d1).days)
    return samples


def load_scenario(path):
    sc = dict(DEFAULTS)
    sc["wip_limits"], sc["priors"] = {}, {}
    if path is None:
        return sc
    for raw in Path(path).read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line or ":" not in line:
            continue
        key, _, val = line.partition(":")
        key, val = key.strip(), val.strip()
        if key == "name":
            sc["name"] = val
        elif key in ("arrivals_per_quarter", "dependency_tax", "dependency_tax_current",
                     "multitask_alpha", "discovery_skip_rate", "rollout_skip_rate"):
            try:
                sc[key] = float(val)
            except ValueError:
                pass
        elif key == "wip_limits":
            for pair in val.split(","):
                if "=" in pair:
                    k, _, v = pair.partition("=")
                    try:
                        sc["wip_limits"][k.strip()] = int(v.strip())
                    except ValueError:
                        pass
        elif key.startswith("duration_"):
            stage = key[len("duration_"):]
            parts = [p.strip() for p in val.split(",")]
            if len(parts) == 3:
                try:
                    sc["priors"][stage] = tuple(float(p) for p in parts)
                except ValueError:
                    pass
    return sc


def build_samplers(stages, history, scenario, rng):
    """Return {stage: (label, sampler)} — bootstrap history when rich, else triangular prior."""
    samplers = {}
    for stage in stages:
        hist = history.get(stage, [])
        if len(hist) >= 3:
            samplers[stage] = ("history", lambda h=tuple(hist): rng.choice(h))
        else:
            prior = scenario["priors"].get(stage) or DEFAULT_PRIORS.get(stage) or (10, 20, 40)
            lo, mode, hi = prior
            samplers[stage] = ("prior", lambda a=lo, b=hi, c=mode: rng.triangular(a, b, c))
    return samplers


def run_once(stages, wip_limits, baseline_wip, scenario, samplers, horizon, rng):
    """FIFO chain of capacity-constrained stages. Returns completed items' cycle times."""
    import heapq
    interval = 91.25 / max(scenario["arrivals_per_quarter"], 0.01)
    arrivals, t = [], 0.0
    while t < horizon:
        arrivals.append(t)
        t += interval * rng.uniform(0.5, 1.5)
    slots = {}
    for stage in stages:
        limit = wip_limits.get(stage)
        slots[stage] = [0.0] * limit if limit else None
    tax_ratio = scenario["dependency_tax"] / max(scenario["dependency_tax_current"], 0.01)
    alpha = scenario["multitask_alpha"]
    cycle_times = []
    for arrive in arrivals:
        ready = arrive
        for stage in stages:
            if stage == "discovery" and rng.random() < scenario["discovery_skip_rate"]:
                continue
            if stage == "rollout" and rng.random() < scenario["rollout_skip_rate"]:
                continue
            duration = max(1.0, float(samplers[stage][1]()))
            if stage == "execute":
                duration *= tax_ratio
            if slots[stage] is not None:
                free_at = heapq.heappop(slots[stage])
                start = max(ready, free_at)
                # Load tax: concurrent items slow each other down. Normalized to the
                # CURRENT system's limit so history-derived durations reproduce themselves
                # when the stage runs full under today's WIP policy.
                busy_others = sum(1 for f in slots[stage] if f > start)
                ref_busy = max((baseline_wip.get(stage) or (busy_others + 1)) - 1, 0)
                duration *= (1 + alpha * busy_others) / (1 + alpha * ref_busy)
                done = start + duration
                heapq.heappush(slots[stage], done)
            else:
                done = ready + duration
            ready = done
        if ready <= horizon:
            cycle_times.append(ready - arrive)
    return cycle_times


def percentile(sorted_vals, p):
    if not sorted_vals:
        return None
    idx = min(len(sorted_vals) - 1, max(0, int(round(p * (len(sorted_vals) - 1)))))
    return sorted_vals[idx]


def simulate(stages, scenario, baseline_wip, history, runs, horizon, seed):
    rng = random.Random(seed)
    samplers = build_samplers(stages, history, scenario, rng)
    wip = dict(scenario["wip_limits"]) if scenario["wip_limits"] else {}
    all_ct, per_run_p50, completions = [], [], []
    for _ in range(runs):
        ct = run_once(stages, wip, baseline_wip, scenario, samplers, horizon, rng)
        if ct:
            all_ct.extend(ct)
            per_run_p50.append(sorted(ct)[len(ct) // 2])
            completions.append(len(ct))
    all_ct.sort()
    years = horizon / 365.0
    p50 = percentile(all_ct, 0.50)
    p85 = percentile(all_ct, 0.85)
    thr = (sum(completions) / len(completions) / years) if completions else 0.0
    half = len(per_run_p50) // 2
    noise = 0.0
    if half >= 5:
        a = sorted(per_run_p50[:half])[half // 2]
        b = sorted(per_run_p50[half:])[(len(per_run_p50) - half) // 2]
        noise = abs(a - b)
    avg_wip = thr * (p50 or 0) / 365.0  # Little's law estimate
    labels = {s: samplers[s][0] for s in stages}
    return {"name": scenario["name"], "p50": p50, "p85": p85, "throughput": thr,
            "avg_wip": avg_wip, "noise": noise, "labels": labels}


def main(argv):
    args, scenarios, runs, horizon, seed = [], [], 1000, 730, 7
    it = iter(argv[1:])
    for a in it:
        if a == "--scenario":
            scenarios.append(next(it, None))
        elif a == "--runs":
            runs = int(next(it, "1000"))
        elif a == "--horizon":
            horizon = int(next(it, "730"))
        elif a == "--seed":
            seed = int(next(it, "7"))
        elif a in ("-h", "--help"):
            print(__doc__)
            return 0
        else:
            args.append(a)
    if not args:
        print(__doc__)
        return 2
    ws = Path(args[0]).resolve()
    stages, base_wip = parse_board_config_stages(ws)
    history = load_history(ws, stages)
    baseline = load_scenario(None)
    baseline["wip_limits"] = dict(base_wip)
    runs_list = [baseline] + [load_scenario(p) for p in scenarios if p]
    for sc in runs_list[1:]:
        if not sc["wip_limits"]:
            sc["wip_limits"] = dict(base_wip)
    results = [simulate(stages, sc, base_wip, history, runs, horizon, seed) for sc in runs_list]

    print(f"# Flow simulation — {ws.name} ({runs} runs, {horizon}d horizon, seed {seed})\n")
    hist_note = ", ".join(f"{s}:{results[0]['labels'][s]}({len(history.get(s, []))})" for s in stages)
    print(f"Duration sources per stage — {hist_note}")
    print("(`prior`-labeled stages run on assumptions: hold the priors dialogue before "
          "trusting deltas.)\n")
    print("| Scenario | Cycle time P50 (d) | P85 (d) | Throughput /yr | Avg WIP (Little) |")
    print("|---|---|---|---|---|")
    for r in results:
        print(f"| {r['name']} | {r['p50']:.0f} | {r['p85']:.0f} | "
              f"{r['throughput']:.1f} | {r['avg_wip']:.1f} |")
    print(f"\nRun-to-run noise on P50 ≈ ±{results[0]['noise']:.0f}d — deltas inside that "
          "band are indistinguishable, and that is a finding, not a failure.")
    print("Simulation is discovery evidence for an improvement bet, never the decision.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
