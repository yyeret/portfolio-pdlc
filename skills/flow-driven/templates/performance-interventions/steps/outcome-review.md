---
id: outcome-review
name: Outcome review and disposition
type: measure
intent: "Decide what to sustain, test further, change, or end"
delegate_rung: 1
run: human
run_ref: ""
context_packs: []
exit_evidence:
  - "An independently checked KPI, adoption, guardrail, and cost readout versus agreed bars, with limitations and a dated sponsor decision. Sustaining includes accepted handover and monitoring. Pivot or stop includes signed closeout."
verify_with: platform/checks/evidence-review.md
escalate_when: "Outcome, adoption, safety, or ownership remains unresolved"
escalate_to: sponsor
budget: "One review, with at most one sponsor-approved extension"
measures: [performance-kpi, adoption, guardrail, operating-cost]
inner_graph: false
---

# Outcome review and disposition

## Intent

Decide what to sustain, test further, change, or end.

## Run contract

Compare results for the agreed cohort and window, and note confounders or unpaid costs. Use the flow-driven-run decision brief. For sustain, record the operating owner, runbook, support responsibilities, follow-up date, and the trigger for corrective action.

Finish with a signed disposition or remain here for one bounded extension specifying evidence, owner, and due date.

## Exit evidence

An independently checked KPI, adoption, guardrail, and cost readout versus agreed bars, with limitations and a dated sponsor decision. Sustaining includes accepted handover and monitoring. Pivot or stop includes signed closeout. Link the receipt from the item. Use the [outcome review and disposition check](../platform/checks/evidence-review.md) with an independent verifier.

## Delegation and escalation

The human owner runs the step and can use an agent to assist with analysis and drafting. The sponsor handles the escalation. Use the named person on the card.

## Failure mode

Claiming success from adoption alone, or handing off to an owner who cannot operate the change.
