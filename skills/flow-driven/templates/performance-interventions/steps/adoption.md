---
id: adoption
name: Adoption and transfer
type: measure
intent: "Establish whether the new way of working is taking hold"
delegate_rung: 1
run: human
run_ref: ""
context_packs: []
exit_evidence:
  - "An adoption readout by cohort with eligible cases, repeat correct use, barriers, exceptions, and the result of an operator teach-back or support rehearsal."
verify_with: platform/checks/evidence-review.md
escalate_when: "Adoption data is unreliable or a guardrail trips"
escalate_to: operating owner
budget: "One design-defined observation window"
measures: [adoption, guardrail]
inner_graph: false
---

# Adoption and transfer

## Intent

Establish whether the new way of working is taking hold.

## Run contract

Observe real workflow usage across the agreed window. Sample non-use and workarounds and check correct use as well as coverage. Have the operating team demonstrate support and exception handling using the operating notes.

Move to outcome review at the window end, or sooner if a guardrail trips. Record shortfalls without silently widening rollout or resetting the denominator.

## Exit evidence

An adoption readout by cohort with eligible cases, repeat correct use, barriers, exceptions, and the result of an operator teach-back or support rehearsal. Link the receipt from the item. Use the [adoption and transfer check](../platform/checks/evidence-review.md) with an independent verifier.

## Delegation and escalation

The human owner runs the step and can use an agent to assist with analysis and drafting. The operating owner handles the escalation. Use the named person on the card.

## Failure mode

Counting training attendance, logins, or enabled seats as adoption.
