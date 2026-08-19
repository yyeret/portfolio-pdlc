---
title: Readouts get checked by something other than the agent that wrote them
type: improvement-step
stage: proposed
owner: Dana
opened: 2026-08-15
benefit_hypothesis: "If a readout is checked independently, hypothesis-confirm-rate becomes trustworthy enough to steer intake with"
measures: [hypothesis-confirm-rate, evidence-coverage]
baseline: "hypothesis-confirm-rate = 3 of 7 as of 2026-07-31, with no independent check on any readout"
kill_criteria: "If two rounds of checking find nothing the readout got wrong, drop the check and say the readout was fine all along"
probe: "Re-check the last four readouts blind against the raw analytics; count how many calls change"
---

# Readouts get checked by something other than the agent that wrote them

## The signal

`flow_lint.py` warns on every run: `learn` is a rung-3 step with no `verify_with` — the
runner grades its own work. And `learn` is the step that feeds the `audience-map` context
pack, so an error here propagates into every future item's intake and angle choice.

## Benefit hypothesis

If readouts are checked against the raw analytics by a fresh context that never saw the
draft, then hypothesis-confirm-rate stops being a self-report and becomes a number we could
actually steer intake with — because the failure mode here is retrofitting the hypothesis to
the result, which a second reader catches immediately.

## Options considered

| Option | What changes | Effort | Risk | Reversible? |
|---|---|---|---|---|
| do nothing | — | — | the pack that shapes every item is fed by unchecked reads | — |
| Dana reviews each readout | +15 human-min/item | s | adds human load to the step we most want to automate | yes |
| write `platform/checks/readout-check.md` | agent, fresh context, adversarial brief | s | a check that always agrees | yes |
| both, for the first five | belt and braces while calibrating | m | slowest | yes |

## Probe

Re-check the last four readouts blind — fresh context, raw analytics, the card's original
hypothesis quoted — and count how many calls change.

- **Timebox**: one week
- **Proceed if**: any call changes, or any readout is found to have paraphrased the
  hypothesis
- **Stop if**: all four hold up exactly

## Adoption

Add `verify_with: platform/checks/readout-check.md` to `steps/learn.md`, which also clears
the lint warning. The warning is deliberately left visible until then — a known gap on the
board beats a clean board that lies.

## Watch

| Date | Measure | Value | Read |
|---|---|---|---|

## Decision log

| Date | Decision | Who | Basis |
|---|---|---|---|
