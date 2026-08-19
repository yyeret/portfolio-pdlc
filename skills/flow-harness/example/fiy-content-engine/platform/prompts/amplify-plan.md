# Run ref — amplify plan

**Step**: `amplify` · **rung 4** (runs unattended, audited automatically)

Turn the published piece into a scheduled distribution plan.

**Produce** `items/<slug>/amplify-plan.md`:

| Date | Channel | Format | Variant text | Claim source in the piece |
|---|---|---|---|---|

**Rules**:

- Six touches over three weeks, formats per `platform/context/audience-map.md`.
- **Every variant maps to a claim in the published piece.** The mapping column is not
  bookkeeping — it is the thing the audit checks.
- No statistic in a hook that is not in the piece. No @-mention of a customer.
- Schedule through the connector queue only.

**Exit**: run `platform/checks/amplify-audit.md`. Clean audit → schedule and record.
Any drift finding → do not schedule; escalate to Dana with the finding.
