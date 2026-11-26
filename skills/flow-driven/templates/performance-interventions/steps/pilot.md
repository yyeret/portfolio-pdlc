---
id: pilot
name: Pilot in real work
type: verify
intent: "See whether the intervention works for a bounded group"
delegate_rung: 1
run: human
run_ref: ""
context_packs: []
exit_evidence:
  - "A real-work pilot readout with eligible and exposed cases, KPI and leading indicator versus baseline, adoption, exceptions, harms, and costs. Record the rollout decision or signed closeout."
verify_with: platform/checks/evidence-review.md
escalate_when: "A guardrail trips or the trial cannot yield interpretable evidence"
escalate_to: sponsor
budget: "Use the approved trial window and exposure cap"
measures: [performance-kpi, adoption, guardrail]
inner_graph: false
---

# Pilot in real work

## Intent

See whether the intervention works for a bounded group.

## Run contract

Use the approved cohort and window. Sample actual work and invite affected workers to report workarounds and friction. Show missing data and comparator limits. Prepare a scale, pivot, or stop brief.

Stop at the approved date or on a guardrail breach. Contain exposure under the rollback agreement and bring the result to the sponsor.

## Exit evidence

A real-work pilot readout with eligible and exposed cases, KPI and leading indicator versus baseline, adoption, exceptions, harms, and costs. Record the rollout decision or signed closeout. Link the receipt from the item. Use the [pilot in real work check](../platform/checks/evidence-review.md) with an independent verifier.

## Delegation and escalation

The human owner runs the step and can use an agent to assist with analysis and drafting. The sponsor handles the escalation. Use the named person on the card.

## Failure mode

Reporting enthusiastic volunteers as if they represent the rollout population.
