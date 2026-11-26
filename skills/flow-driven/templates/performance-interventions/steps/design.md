---
id: design
name: Intervention and evidence design
type: transform
intent: "Choose what to change and how to tell if it works"
delegate_rung: 1
run: human
run_ref: ""
context_packs: []
exit_evidence:
  - "A design brief with options, mechanism, desirability, feasibility, viability, total cost, risks and owner. Predeclare cohort, baseline, comparator where practical, KPI, leading indicator, adoption bar, guardrails, evidence window, and pilot decision criteria before exposure."
verify_with: platform/checks/evidence-review.md
escalate_when: "No safe exposure boundary or credible way to measure the effect"
escalate_to: sponsor
budget: "One week"
measures: [guardrail]
inner_graph: false
---

# Intervention and evidence design

## Intent

Choose what to change and how to tell if it works.

## Run contract

Compare the smallest plausible process, practice, or tool changes and the cost of the current way of working. Include recurring time, support, maintenance, and debt. Specify rollback. If AI is involved, agree representative evaluation slices and failure/override thresholds up front.

Stop with a bounded probe or trial proposal, or a signed stop or pivot. The sponsor records why a direct pilot can skip the probe.

## Exit evidence

A design brief with options, mechanism, desirability, feasibility, viability, total cost, risks and owner. Predeclare cohort, baseline, comparator where practical, KPI, leading indicator, adoption bar, guardrails, evidence window, and pilot decision criteria before exposure. Link the receipt from the item. Use the [intervention and evidence design check](../platform/checks/evidence-review.md) with an independent verifier.

## Delegation and escalation

The human owner runs the step and can use an agent to assist with analysis and drafting. The sponsor handles the escalation. Use the named person on the card.

## Failure mode

Moving the threshold after seeing the results or calling a cost shift a gain.
