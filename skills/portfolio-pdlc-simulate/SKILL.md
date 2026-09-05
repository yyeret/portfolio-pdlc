---
name: portfolio-pdlc-simulate
description: Run a deterministic Monte Carlo simulation of flow through the portfolio PDLC — baseline from the workspace's own flow history, plus what-if scenarios (WIP limit changes, arrival-rate shaping, dependency-tax reduction from platform extraction or team reorganization). Use as the Discovery move for improvement bets before anyone changes policies or reorganizes teams, or to set Service Level Expectations. Advanced member of the portfolio-pdlc family; produces confidence-labeled forecasts, never point predictions.
metadata:
  tags: flow-agile, product-strategy
  version: 1.0.0
---

# Portfolio PDLC — Simulate

## Outcome

A side-by-side, confidence-labeled read of "the system as it is" versus one or more
proposed futures — cycle-time percentiles, annual throughput, average WIP — good enough to
decide whether an improvement bet earns a real pilot, and honest enough to refuse false
precision when the data is thin.

## When this is the right move

- An improvement card's Discovery approach names a scenario (WIP limits, intake shaping,
  dependency tax) — this is the cheap experiment before the org-level one.
- Sponsors want an SLE ("what can we promise about time-through-stage?").
- A topology bet (platform extraction, outcome team) needs its flow claim quantified
  before the option-comparison conversation.

## Workflow

1. **Establish the baseline.**

```bash
python3 <this-repo>/skills/portfolio-pdlc/scripts/portfolio_sim.py <workspace>
```

   The script estimates per-stage duration distributions from `flow-log.csv` when there are
   enough samples (≥3 per stage) and falls back to the priors in the scenario file
   otherwise — every estimate is labeled `history` or `prior` in the output. **If most
   stages run on priors, hold the priors dialogue first**: get the humans' min/mode/max
   guesses per stage into the baseline scenario rather than silently trusting defaults.
2. **Write the what-if scenario file(s)** (`reviews/scenarios/<slug>.txt`, format below) —
   one per alternative, changing as few knobs as possible so the comparison isolates the
   bet. Typical knobs per improvement type:
   - WIP-limit bet → `wip_limits`
   - Intake-shaping bet → `arrivals_per_quarter`
   - Platform-extraction / T-shaping / outcome-team bet → `dependency_tax` (the multiplier
     on execute-stage durations that coordination overhead currently costs; the bet's claim
     is the reduction)
   - Discovery-discipline bet → `discovery_skip_rate` and the rework it prevents
3. **Run the comparison** (`--scenario` may repeat):

```bash
python3 .../portfolio_sim.py <workspace> --scenario reviews/scenarios/<slug>.txt --runs 2000
```

4. **Read it like a portfolio manager, not a lab.** Compare P50/P85 cycle time and
   throughput deltas. A delta smaller than the run-to-run noise (the script prints it) is
   "the simulation can't distinguish these" — a legitimate, decision-relevant finding.
5. **Record** the table + confidence notes in the improvement card's Evidence log and the
   current review brief. State the next derisking step (usually: a bounded real-world
   pilot of the winning scenario).

## Scenario file format

Plain `key: value` lines (comments with `#`):

```
name: extract-billing-platform
arrivals_per_quarter: 6
wip_limits: plan-commit=3, execute=4
# Coordination overhead is a RATIO: history already contains today's tax, so execute
# durations scale by dependency_tax / dependency_tax_current (here 1.1/1.3 ≈ 15% faster):
dependency_tax_current: 1.3
dependency_tax: 1.1
# Load tax: items in a fuller stage slow each other (normalized so history reproduces at
# today's WIP limit). This is what makes WIP-limit bets show their real tradeoff:
multitask_alpha: 0.25
discovery_skip_rate: 0.3
rollout_skip_rate: 0.4
# per-stage priors (days) as min,mode,max — used where history is thin:
duration_explore: 10,21,45
duration_discovery: 15,30,60
duration_plan-commit: 7,20,40
duration_execute: 45,90,180
duration_rollout: 10,25,60
```

The two behavioral knobs are honest about their leverage: `multitask_alpha` decides whether
WIP limits can win at all, and the `dependency_tax` pair carries a topology bet's whole
claim — both belong in the priors dialogue, and sensitivity-checking a delta against ±alpha
is cheap insurance against motivated scenarios.

## Rules

- **Simulation is discovery, not decision.** Results feed the improvement card's evidence;
  humans still decide at plan-commit.
- **No point predictions.** Percentiles with labels, always; refuse "so it'll take 87
  days?" framing explicitly in the write-up.
- **Thin data is a finding.** "We can't simulate this credibly yet — here's the smallest
  data we'd need" is a valid and useful output.
- **Fixed seed by default** (reproducible runs); vary `--seed` only to measure noise, and
  report that noise next to any claimed delta.
- Keep scenarios honest: one bet per scenario file; kitchen-sink scenarios prove nothing.

## Quality Gates

- Every distribution in the output is labeled `history` or `prior`; prior-heavy runs
  triggered (or explicitly waived) the priors dialogue.
- Deltas are reported against measured run-to-run noise.
- Results landed in the improvement card's Evidence log with the scenario file checked in.
- The write-up names the next real-world derisking step, not just numbers.

## References

- `skills/portfolio-pdlc/scripts/portfolio_sim.py` — stdlib-only; `--help` for flags.
- `portfolio-pdlc-improve` — where the bets that call for simulation come from.
