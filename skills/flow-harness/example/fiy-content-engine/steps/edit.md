---
id: edit
name: Edit for truth and voice
type: verify
intent: "Make the piece true, tight, and unmistakably ours before our name goes on it"
delegate_rung: 1
run: human
run_ref: ""
context_packs: [house-voice]
inputs: [draft, research pack]
exit_evidence:
  - "Claims audit complete: every claim traced to the research pack or removed"
  - "Edit findings recorded on the item — including the ones we chose not to act on"
  - "A one-line editor's verdict: publish, rework, or drop"
verify_with: platform/checks/claims-audit.md
escalate_when: "the piece needs a claim we cannot source"
escalate_to: Dana
budget: "45 human-minutes"
measures: [rework-rate, escape-rate]
inner_graph: false
---

# Edit for truth and voice

## Intent

The last place a wrong claim is cheap. After this step, correcting it costs an audience.

## Exit evidence

- The claims audit output is attached to the item, not summarised as "checked".
- Findings we chose *not* to act on are recorded with why. Silent dismissals are how a
  rework rate hides.
- The verdict is one of three words. "Nearly there" is not a verdict.

## Run contract

- **Inputs**: draft, research pack, house-voice pack.
- **Agent's part**: run the claims audit and present the diff-ready findings.
- **Human's part**: the actual edit and the verdict.
- **Guardrails**: the agent may not resolve its own audit findings at this step.
- **Stop rule**: one pass. A second pass means the answer is `rework`.

## Delegation & escalation

- **Why rung 1**: this is the step where taste and accountability meet. The agent prepares;
  Dana decides.
- **What would promote it**: 10 items where the claims audit found everything Dana found.
  We are at 4.
- **What demotes it**: n/a — it is already the human-heaviest step in the flow.

## Failure modes

The rubber stamp. A tired editor and a fluent draft produce a `publish` verdict in four
minutes, and the board looks identical to the case where the work was done. The meta-loop
watches `edit` cycle time for exactly this: an edit that never takes 45 minutes is not an
edit.
