---
id: intake
name: Intake
type: intake
intent: "Frame a concrete performance gap for an affected group"
delegate_rung: 1
run: human
run_ref: ""
context_packs: []
exit_evidence:
  - "A named requester and owner, affected group, real-work observation, and one-line performance gap on the item."
verify_with: platform/checks/evidence-review.md
escalate_when: "Ownership or the affected group is unclear"
escalate_to: flow owner
budget: "30 minutes"
measures: [item-age]
inner_graph: false
---

# Intake

## Intent

Frame a concrete performance gap for an affected group.

## Run contract

Read the incoming request or speak with the requester. Capture the work being done and the consequence of the gap. Use intent-framing-chooser to sharpen a solution-first request.

Stop once the owner and observation are recorded or when the intake timebox expires.

## Exit evidence

A named requester and owner, affected group, real-work observation, and one-line performance gap on the item. Link the receipt from the item. Use the [intake check](../platform/checks/evidence-review.md) with an independent verifier.

## Delegation and escalation

The human owner runs the step and can use an agent to assist with analysis and drafting. The flow owner handles the escalation. Use the named person on the card.

## Failure mode

Taking the request for a particular tool as evidence of the performance problem.
