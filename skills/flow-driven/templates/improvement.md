---
title: <the change to the workflow, stated as an outcome>
type: improvement-step        # improvement-step | improvement-flow | improvement-platform | improvement-delegation
stage: proposed               # proposed | probing | adopted | watching | rejected | reverted
owner: <human who carries it>
opened: <YYYY-MM-DD>
benefit_hypothesis: "<if we change X, we expect measure Y to move by Z, because ...>"
measures: []                  # ids from measures.md — the ones this bet claims to move
baseline: "<measure id> = <value> as of <YYYY-MM-DD>"
kill_criteria: "<what we would see that means we revert — written before we start>"
probe: "<the cheapest way to find out: a one-item pilot, a shadow run, a data probe>"
---

# <Title>

## The signal

<What fired this: which probe, which measure, which recurring learning. Cite the data —
board line, flow-log row, learning file. An improvement with no signal is a preference.>

## Benefit hypothesis

<If we <change>, then <measure> moves <direction> by <amount>, because <mechanism>.
The mechanism matters: it is what makes the bet falsifiable rather than hopeful.>

## Options considered

| Option | What changes | Effort | Risk | Reversible? |
|---|---|---|---|---|
| do nothing | — | — | <what continues to cost us> | — |
| <option A> | <the change> | <s/m/l> | <what could go wrong> | <yes/no> |

Keeping "do nothing" as a real row is not a formality — most workflow changes lose to it.

## Probe (this bet's discovery)

<The cheapest thing that would move our confidence: shadow-run the new step contract on
the next three items; drop the rung on one step for a week; replay last month's flow-log
under the proposed WIP limit. Timebox it and name the exit.>

- **Timebox**: <dates>
- **What would make us proceed**: <observable>
- **What would make us stop**: <observable — the kill criteria above, in context>

## Adoption

<What actually changes when this is adopted: which file, which step contract, which limit.
Adoption requires a dated human decision and a line in workflow.md's Change log.>

## Watch

| Date | Measure | Value | Read |
|---|---|---|---|

<After adoption, watch the measures for at least <n> items. A change nobody watched is a
change nobody can revert with confidence.>

## Decision log

| Date | Decision | Who | Basis |
|---|---|---|---|
