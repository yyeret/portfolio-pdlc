---
id: rollout
name: Release and support
type: transform
intent: "Make the change usable and supportable in the approved scope"
delegate_rung: 1
run: human
run_ref: ""
context_packs: []
exit_evidence:
  - "A release or abort record with actual coverage, enablement, monitoring, support path, rollback readiness, and owned residual risks or debt."
verify_with: platform/checks/evidence-review.md
escalate_when: "Support or rollback is unavailable, or a guardrail trips"
escalate_to: operating owner
budget: "One approved rollout wave at a time"
measures: [adoption, guardrail]
inner_graph: false
---

# Release and support

## Intent

Make the change usable and supportable in the approved scope.

## Run contract

Confirm the signed scope, enable the next cohort, and check a real case end to end. Provide instructions or coaching where people do the work. Record actual coverage and check whether support can diagnose and handle a failure.

End each wave with a readiness check. Keep the card here until the approved scope is live, or contain the rollout and escalate when a guardrail trips.

## Exit evidence

A release or abort record with actual coverage, enablement, monitoring, support path, rollback readiness, and owned residual risks or debt. Link the receipt from the item. Use the [release and support check](../platform/checks/evidence-review.md) with an independent verifier.

## Delegation and escalation

The human owner runs the step and can use an agent to assist with analysis and drafting. The operating owner handles the escalation. Use the named person on the card.

## Failure mode

Counting a launch announcement or installed software as change in how work gets done.
