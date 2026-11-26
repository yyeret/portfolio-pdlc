---
id: discovery
name: Problem discovery
type: transform
intent: "Establish the performance gap and where it arises"
delegate_rung: 1
run: human
run_ref: ""
context_packs: []
exit_evidence:
  - "A discovery readout with affected workers, workflow and friction, KPI and leading-indicator baselines, source and window, and plausible causes. Record the sponsor’s proceed or stop decision."
verify_with: platform/checks/evidence-review.md
escalate_when: "The gap cannot be observed or baseline access is missing"
escalate_to: sponsor
budget: "One week"
measures: [performance-kpi]
inner_graph: false
---

# Problem discovery

## Intent

Establish the performance gap and where it arises.

## Run contract

Observe real work or use a representative sample of cases. Map the affected part of the process and compare it with a better-performing slice when available. Use intent-framing-chooser to express the desired behaviour, consequence, and falsifiable hypothesis.

Stop at the timebox or when the sponsor can judge the size of the gap and the riskiest assumption.

## Exit evidence

A discovery readout with affected workers, workflow and friction, KPI and leading-indicator baselines, source and window, and plausible causes. Record the sponsor’s proceed or stop decision. Link the receipt from the item. Use the [problem discovery check](../platform/checks/evidence-review.md) with an independent verifier.

## Delegation and escalation

The human owner runs the step and can use an agent to assist with analysis and drafting. The sponsor handles the escalation. Use the named person on the card.

## Failure mode

Selecting only the cases that support the preferred explanation.
