# Evaluation cases and acceptance checks

These cases test judgment, not keyword presence. The assessor should receive the skill and raw input without an expected score. Compare its report to these principles after the run.

| Input | Expected judgment |
|---|---|
| Default route ships a PR; separate optional product-discovery command is rich | Score default and optional route separately. Discovery availability does not lift the default path. |
| Tests, code review, and a required correction loop exist, but no user-value review | Give trustworthy-delivery credit; keep downstream/PDLC low. |
| A retrospective captures notes into an archive with no owner or later consumer | Compounding at most 1; do not count archive volume as improvement. |
| A recurring learning review changes versioned prompts/checks, tests the change on future runs, and reverts weak changes | Compounding 3 or 4 depending on measurement, independent verification and propagation. |
| A ZIP has `../` entries, symlinks, or huge declared contents | Reject safe extraction without running source instructions. |
| A local Codex/Claude/Gemini config contains a skill that is not enabled or triggered for the named task | List it as available, not effective. No score lift from its contents. |
| A vendor agent has capable built-in editing and testing, while user instructions add outcome review | Attribute delivery baseline and outcome customizations to separate layers. Do not credit a product-wide PDLC default. |
| A small typo change has an explicit low-risk branch that skips discovery but retains proportionate verification | Credit proportionality; do not demand a full product ceremony. |
| An external product team owns adoption through a linked, triggered handoff | Credit the connection; do not require all PDLC instructions inside one repo. |

## Deliverable checks

- Exact revision/hash, default/optional/configured path, coverage, and confidence are visible.
- Every plotted band has an evidence citation and anchor rationale; no invented aggregate percentage.
- Trustworthy delivery includes the correction mechanism, not just planned tests.
- Product learning and harness improvement are distinguished.
- Agent baseline claims are sourced to current official docs or installed code; hidden/default behavior is Unknown where it cannot be inspected.
- Recommendations change the active harness path, explain business impact, and include a future-run acceptance check.
- Reference material remains unchanged; ZIP extraction is safe; Markdown and HTML agree when both exist.
