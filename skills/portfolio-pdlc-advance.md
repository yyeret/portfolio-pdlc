---
name: portfolio-pdlc-advance
description: Advance ONE initiative (or improvement bet) through the portfolio PDLC — do the stage-appropriate work that grows confidence, and prepare (never make) the human decision at the next boundary. Use when an item is aging, a discovery timebox lapsed without a recommendation, a decision is due or overdue, or a card is ready to move stage. The loop-1 skill of the portfolio-pdlc family.
metadata:
  tags: flow-agile, product-strategy
  version: 1.0.0
---

# Portfolio PDLC — Advance

## Outcome

One card measurably closer to its next confidence milestone: the stage's missing work
produced, the pending decision packaged for humans, or — when a decision is recorded — the
stage transitioned and logged. Advance means *growing confidence toward a decision*, not
pushing cards rightward.

## Pick-one rule

Work exactly one card per invocation (the loop's leverage table usually picked it; if
called ad-hoc, take the named card). Everything else you notice goes to the loop log or
`improvements/`, not into scope.

## Stage-appropriate moves

| Card sits in | Advance means | Compose |
|---|---|---|
| explore | Frame the problem for real: draft/complete the lightweight canvas; identify the riskiest DVF assumptions; recommend investigate-further / park | `lean-product-canvas-coach` |
| discovery | Drive the timebox to a verdict: run/summarize the experiments against the riskiest assumptions, tag results evidence/opinion, produce a proceed / de-risk-further / stop recommendation | `sniff-test` (readiness check) |
| plan-commit | Build the commit package: Outcome-Oriented Roadmap with an explicit confidence range, resourcing picture, what's still unproven at commit | |
| execute | Keep confidence honest: read leading indicators, check slices are validating the hypothesis, surface drift (scope creep on an "experiment", indicators flat) as a steer-or-escalate note | |
| rollout | Turn "shipped" into "realized": adoption/hypercare status, instrument the outcome measures, draft the Value Realization read | |
| bau | Run the measure-and-learn questions (hypothesis achieved? metrics teach what? diminishing returns? still a constraint?) and recommend keep / enhance / close — plus the baseline-vs-actual watermelon check on exit | |

Improvement cards advance the same way; their discovery is a probe, a one-review pilot, or
a `portfolio-pdlc-simulate` scenario.

## Decision boundaries — prepare, don't cross

Entering `plan-commit` or `execute` (and any invest / pivot / kill / freeze call) is human
territory:

1. Write the **decision brief** to `reviews/YYYY-MM-DD-<slug>-decision.md`:
   *what you can rely on* (evidence-backed), *what's still open* (opinion-tagged), options
   framed as **double down / de-risk further / kill-pause** (or invest/skip-discovery at
   the earlier boundary), a recommendation with reasoning, and what would make us say no.
2. Set the card's `next_decision` (date — decision — owner) and stop there.
3. Only when a dated human decision exists in the card's Decision log: update `stage` +
   `stage_entered`, re-run the board script (it logs the transition), and confirm the
   flow-log row appeared.

Overdue-decision cycles (leverage row 1) refresh the brief, restate the cost of waiting
(items queued behind it, aging), and surface it — they never pile more work behind the
stuck decision.

## Rules

- Confidence forward, not cards rightward: a proceed/stop recommendation or an honest
  "stay and de-risk" is a successful advance.
- Respect optionality: discovery and rollout are skippable **by decision** — prepare the
  skip decision when risk is genuinely low; flag habitual skipping.
- Evidence vs opinion tagging in everything you produce; unevidenced confidence stays a
  question mark in the brief.
- Timeboxes are real: a lapsed discovery gets a verdict from what was learned, not an
  extension by default.
- Update the card's Evidence log with what this advance produced.

## Quality Gates

- Exactly one card touched; its frontmatter, Evidence log, and (if transitioned) flow log
  all agree.
- Any boundary transition has a dated, named Decision-log entry — or didn't happen.
- The decision brief (when one was due) states evidence, open risks, options, a
  recommendation, and "what would make us say no."
- Board regenerated after the move.

## References

- Stage expectations inline above; depth: `skills/sniff-test/references/` (this repo).
- Umbrella: `portfolio-pdlc` (leverage table, loop mechanics).
