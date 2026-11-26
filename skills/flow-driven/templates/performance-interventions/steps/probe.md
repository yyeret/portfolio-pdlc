---
id: probe
name: Test the riskiest assumption
type: verify
intent: "Buy down consequential uncertainty before exposure"
delegate_rung: 1
run: human
run_ref: ""
context_packs: []
exit_evidence:
  - "A probe result with its predeclared pass criterion, observations and misses, remaining unknowns, and the signed go, pivot, or stop decision."
verify_with: platform/checks/evidence-review.md
escalate_when: "The criterion fails, results are ambiguous, or the cap is reached"
escalate_to: sponsor
budget: "One week or two iterations"
measures: [guardrail]
inner_graph: false
---

# Test the riskiest assumption

## Intent

Buy down consequential uncertainty before exposure.

## Run contract

Pick a cheap prototype, rehearsal, historical replay, or simulation. Test the assumption named in the design and repeat at most once within the same cap if the first method failed to yield interpretable evidence.

Stop after two attempts, at the evidence threshold, or at the agreed cost cap, whichever comes first. Keep exposure within the design.

## Exit evidence

A probe result with its predeclared pass criterion, observations and misses, remaining unknowns, and the signed go, pivot, or stop decision. Link the receipt from the item. Use the [test the riskiest assumption check](../platform/checks/evidence-review.md) with an independent verifier.

## Delegation and escalation

The human owner runs the step and can use an agent to assist with analysis and drafting. The sponsor handles the escalation. Use the named person on the card.

## Failure mode

Treating a favourable rehearsal as proof that people will adopt the change.
