---
title: <outcome-flavoured name for this item>
kind: item               # item | rollup | spike
step: <step-id>
step_entered: <YYYY-MM-DD>
owner: <accountable human — whatever the delegate rung>
holder: human            # human | agent | pair | blocked | waiting-decision
class: standard          # standard | expedite | fixed-date | derisk-first
outcome_hypothesis: "<what we believe finishing this changes, and for whom>"
evidence_exits_met: []
parent: ""               # slug of the rollup this belongs to, if any
children: []             # rollup only
blocked_by: ""
next_decision: ""        # "YYYY-MM-DD — the question? (who decides)"
---

# <Title>

## Context

<What this is, why it exists, who asked. Link the source. Two paragraphs at most — the
item is a steering instrument, not a document.>

## Outcome hypothesis

<If we finish this, we expect <observable change> for <someone>, visible as <indicator>.
An item whose hypothesis is "the work will be done" is an activity, and activities do not
justify a slot in a value stream.>

## Riskiest assumptions

| Assumption | Evidence or opinion? | How we would find out cheaply |
|---|---|---|
| <the one that would hurt most if wrong> | opinion | <the probe> |

## Exit evidence log

Dated receipts, one entry per step exit. This is what `evidence_exits_met` points at.

| Date | Step | Evidence | Verified by |
|---|---|---|---|
| <YYYY-MM-DD> | <step-id> | <what exists now, where> | <script/agent/human> |

## Decision log

Dated entries naming humans. Required to enter a decision point.

| Date | Decision | Who | Basis |
|---|---|---|---|

## Escalations

| Date | Step | What the agent could not settle | Outcome |
|---|---|---|---|

## Notes

<Branch conditions taken and why, surprises, links to artifacts.>
