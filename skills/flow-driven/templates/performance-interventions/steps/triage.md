---
id: triage
name: Reality check
type: transform
intent: "Decide whether the gap merits discovery here"
delegate_rung: 1
run: human
run_ref: ""
context_packs: []
exit_evidence:
  - "A triage note naming remit, duplicate and existing-capability checks, plausible sponsor, and a dated discover or close decision."
verify_with: platform/checks/evidence-review.md
escalate_when: "Remit, sponsorship, or priority is disputed"
escalate_to: flow owner
budget: "30 minutes"
measures: [item-age]
inner_graph: false
---

# Reality check

## Intent

Decide whether the gap merits discovery here.

## Run contract

Check the local intake and relevant capabilities with the process owner. Consider impact, urgency, capacity, and whether onboarding to an existing practice would address the gap. Use sniff-test if a developed initiative already exists.

Timebox to one pass. Send a redirect with the alternative owner or capability if the flow owner closes it.

## Exit evidence

A triage note naming remit, duplicate and existing-capability checks, plausible sponsor, and a dated discover or close decision. Link the receipt from the item. Use the [reality check check](../platform/checks/evidence-review.md) with an independent verifier.

## Delegation and escalation

The human owner runs the step and can use an agent to assist with analysis and drafting. The flow owner handles the escalation. Use the named person on the card.

## Failure mode

Filling discovery WIP with work whose sponsor or operating remit is unknown.
