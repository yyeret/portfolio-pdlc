# <Portfolio Name> — Agent Instructions

This folder is a **portfolio workspace** run on the `portfolio-pdlc` operating system
(from the portfolio-pdlc repo — set `<PDLC_REPO>` below to wherever you cloned it).

## Session start

1. Read `PORTFOLIO.md` (charter) and skim `board.md`.
2. Load `<PDLC_REPO>/skills/portfolio-pdlc.md` and follow its operating loop.
3. Regenerate the board before acting:

```bash
python3 <PDLC_REPO>/skills/portfolio-pdlc/scripts/portfolio_board.py .
```

## House rules

- One loop cycle = one move. The leverage table in the umbrella skill picks it.
- Humans decide invest / commit / pivot / kill / reorganize. Agents prepare decision briefs
  in `reviews/` and set `next_decision` on cards — never advance a card across a decision
  boundary without a dated Decision-log entry naming a human.
- `board.md` and `flow-log.csv` are generated — never hand-edit.
- Improvement ideas are captured as cards in `improvements/`, not implemented on the spot.
- Confidence language with sponsors, never gate/compliance language.

## If the portfolio-pdlc repo is missing on this machine

The workspace remains readable and editable by hand — the contract is plain markdown.
Clone https://github.com/yyeret/portfolio-pdlc, or proceed manually and note it in
`reviews/loop-log.md`.
