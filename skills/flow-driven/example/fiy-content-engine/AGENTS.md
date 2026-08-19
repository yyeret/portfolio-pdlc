# FIY Content Engine — Agent Instructions

This folder is a **flow workspace** run on the `flow-driven` operating system. `<REPO>`
below is wherever you cloned https://github.com/yyeret/portfolio-pdlc.

## Session start

1. Read `workflow.md` and skim `board.md`.
2. Validate, project, then pick the move:

```bash
python3 <REPO>/skills/flow-driven/scripts/flow_lint.py .  --today 2026-08-19
python3 <REPO>/skills/flow-driven/scripts/flow_board.py . --today 2026-08-19
python3 <REPO>/skills/flow-driven/scripts/flow_next.py .  --today 2026-08-19
```

3. Load `<REPO>/skills/flow-driven.md` and run one cycle.

## House rules

- One cycle = one move.
- A step is finished when its exit evidence exists, not when a run completes.
- `publish` is a human decision. Prepare the package, set `next_decision`, stop.
- No claim without a source. Ever. If the draft needs one, take the rework edge.
- `board.md`, `flow-log.csv`, and `exports/` are generated — never hand-edit.
- Workflow changes are bets in `improvements/`, not edits in passing.
- Every question you had to ask a human is a missing context pack.

## Practice instance

This is example data with deliberately seeded smells. See `README.md` before you "fix"
anything.
