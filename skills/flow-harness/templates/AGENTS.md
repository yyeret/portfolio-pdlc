# <Stream Name> — Agent Instructions

This folder is a **flow workspace** run on the `flow-harness` operating system (from the
portfolio-pdlc repo — set `<REPO>` below to wherever you cloned it).

## Session start

1. Read `workflow.md` (the definition of workflow) and skim `board.md`.
2. Validate, project, then pick the move:

```bash
python3 <REPO>/skills/flow-harness/scripts/flow_lint.py .     # contract violations first
python3 <REPO>/skills/flow-harness/scripts/flow_board.py .    # regenerate the projection
python3 <REPO>/skills/flow-harness/scripts/flow_next.py .     # the run card for one move
```

3. Load `<REPO>/skills/flow-harness.md` and run the cycle it describes.

## House rules

- One cycle = one move. The run card names it; everything else waits.
- A step is finished when its **exit evidence exists**, not when a run completes.
- Humans decide at decision points. Agents prepare the brief and set `next_decision`.
- `board.md`, `flow-log.csv`, and `exports/` are generated — never hand-edit.
- Workflow changes are bets: capture them in `improvements/`, never edit `workflow.md` or a
  step contract in passing. Adopted changes get a dated line in the Change log.
- Every question an agent had to ask a human is a missing context pack. Capture it in
  `platform/context/` so the next run does not need to ask.

## If the repo is missing on this machine

The workspace stays readable and editable by hand — it is plain markdown. Clone
https://github.com/yyeret/portfolio-pdlc, or proceed manually and note it in
`reviews/loop-log.md`.
