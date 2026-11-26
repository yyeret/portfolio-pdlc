# Performance intervention PDLC template

Use this workspace to take a business or organizational performance intervention from a reported gap through a real-work trial, adoption, and a decision on the measured outcome.

- [Definition of workflow](workflow.md) gives states, outcomes, skills, and the decision policy.
- [Item template](item-template.md) is the copyable card. The [fictional intake item](items/reduce-incomplete-handoffs/item.md) is ready for practice.
- [Measures](measures.md) and the [independent evidence check](platform/checks/evidence-review.md) describe what to inspect.

## Run a first cycle

Run from the repository root with Python 3. On Windows, use `py -3` if that is how Python is installed.

```sh
python3 skills/flow-driven/scripts/flow_lint.py skills/flow-driven/templates/performance-interventions --strict
python3 skills/flow-driven/scripts/flow_board.py skills/flow-driven/templates/performance-interventions
python3 skills/flow-driven/scripts/flow_next.py skills/flow-driven/templates/performance-interventions
```

The fresh template selects the sample item at intake. Open `steps/intake.md`, the evidence review recipe, and the repository's `flow-driven-run` skill. Run one move. The board and CSV are generated and can be regenerated after each move.

For real work, copy this directory into your workspace. Remove the fictional card from the copy and start with one real gap by copying `item-template.md` to `items/<stable-slug>/item.md`. Set the title, owner, actual entry date, and initial hypothesis. Name the flow owner and verify decision roles with the team. Point the same three Python commands at your copy and run them before each cycle.

The scripts check workspace structure and select a move. The runner still verifies evidence, checks capacity and branch conditions, and obtains sign-off for the specific transition. WIP limits and timeboxes are defaults to test with the team. Apply the [waiting-item policy](workflow.md#operating-policy) when a selected item cannot move yet.
