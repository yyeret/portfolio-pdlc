---
name: portfolio-pdlc
description: Run a portfolio-level, product-oriented PDLC (Explore → Discovery → Plan/Commit → Execute → Rollout → BAU, with humans keeping the investment decisions) as a compounding loop over a plain-file workspace. Use when standing up, operating, or resuming a portfolio of initiatives/epics — seeing where everything is, advancing initiatives with evidence, improving artifact quality and outcome orientation, and continuously improving the process and portfolio construction themselves. Entry point and operating loop for the portfolio-pdlc-* skill family; for one-off diagnostics of a single initiative use sniff-test instead.
metadata:
  tags: flow-agile, product-strategy, sdd-process
  version: 1.0.0
---

# Portfolio PDLC — Operating System

## Outcome

A portfolio of significant investments (initiatives, epics, strategic bets) runs as a
product-oriented lifecycle on plain files: every item's real stage is visible and
evidence-verified, work advances toward decisions instead of drifting, cards steer on
outcome hypotheses and leading indicators instead of reported progress, and the operating
system improves itself — process and portfolio construction both — through its own
spec-driven improvement lane. Agents do the clerical and analytical work; humans keep the
decisions that are actually theirs (invest, commit, pivot, kill, reorganize).

## Outcome Indicators

- Every Tier-1 card carries an outcome-oriented title, an outcome hypothesis, and at least
  one leading indicator with a target.
- Stage labels survive evidence checks (stale-status findings trend to zero).
- Each operating-loop cycle ends with exactly one move executed, a regenerated board, and at
  most one captured learning.
- The improvement lane always holds live bets with benefit hypotheses and kill criteria —
  and big bets go through Discovery (probe or simulation) before anyone reorganizes anything.

## The Mental Model

Three ideas, borrowed deliberately:

1. **From enterprise portfolio practice**: a lifecycle is a *common language, not gates*. Confidence grows through
   Explore → Discovery *(optional)* → Plan/Commit → Execute/Build → Rollout *(optional)* → BAU.
   The question is never "did the ceremony run" but "has confidence grown enough for this
   stage, backed by evidence rather than opinion."
2. **From compound engineering**: state is *derived from evidence, not declared in documents*.
   The board is a deterministic projection of initiative frontmatter; stage labels get
   verified against reality; every unit of work should make the next unit easier, so each
   cycle may capture one durable learning or improvement bet.
3. **From the Portfolio Agility Trailmap**: the operating model is itself a product. It gets
   an improvement backlog, benefit hypotheses, leading indicators, discovery (including
   simulation), and honest kill criteria — walked through the very same lifecycle it manages.

## The Workspace

Any folder becomes a portfolio when it follows the contract in
`skills/portfolio-pdlc/references/workspace-contract.md`:

```
PORTFOLIO.md   charter (anchor, not plan)     initiatives/<slug>/initiative.md   one card per bet
pdlc.md        definition of workflow         improvements/<slug>/improvement.md the walk-the-talk lane
topology.md    teams, platforms, dependencies reviews/                           briefs + decision records
board.md       GENERATED — never hand-edit    learnings/                         one learning per file
flow-log.csv   GENERATED transition history
```

Regenerate the board any time with:

```bash
python3 <this-repo>/skills/portfolio-pdlc/scripts/portfolio_board.py <portfolio-workspace>
```

No workspace yet? Load `portfolio-pdlc-wire` first.

## The Operating Loop (one cycle)

Run this whenever you're asked to "work the portfolio", on a cadence, or inside a `/goal`
loop. One cycle is deliberately small; the power is in repetition.

1. **Refresh the board.** Run `portfolio_board.py`. GATE: never pick a move from a stale
   board — if the script fails or flags contract violations, fixing those IS this cycle's move.
2. **Sense.** Read `board.md` (flags, ages, WIP vs limits, risk balance, orientation counts).
   On a review cadence — or when flags look systemic — run `portfolio-pdlc-assess` for the
   full evidence-verified read instead.
3. **Pick ONE move** from the leverage table below. One cycle, one move. Resist fan-out.
4. **Execute the move** by loading the matching skill (routing table below).
5. **Record.** Update the card frontmatter you touched, re-run the board script (it appends
   stage transitions to `flow-log.csv`), and capture **at most one** learning in `learnings/`
   if this cycle genuinely taught something durable.
6. **Hand off.** Append one line (date, move, what changed, next decision pending) to
   `reviews/loop-log.md`. If ending the session, update the thread ledger per the
   cross-machine session contract.

### Leverage table — how to pick the one move

Work top-down; first matching row wins. Ties inside a row: oldest Tier-1 item first.

| # | Signal on the board | The move | Skill |
|---|---|---|---|
| 1 | A prepared human decision is past its `next_decision` date | Surface it: refresh the decision brief, notify, stop piling work behind it | `portfolio-pdlc-advance` (decision-brief mode) |
| 2 | Contract violations: missing frontmatter, unlogged transitions, board won't build | Restore board integrity | `portfolio-pdlc-assess` (sweep mode) |
| 3 | Committed money at risk: Execute/Rollout item with open riskiest assumptions, `orientation: activity`, or no leading indicators | Derisk the committed bet | `portfolio-pdlc-compound` |
| 4 | An item is aging past its stage threshold or sitting at a decision point | Drive it to the decision | `portfolio-pdlc-advance` |
| 5 | A Discovery timebox has lapsed without a proceed/stop recommendation | Force the learning to a recommendation | `portfolio-pdlc-advance` |
| 6 | Any Tier-1 card flagged for outcome orientation or thin evidence | Strengthen the card | `portfolio-pdlc-compound` |
| 7 | An improvement bet's next step is Discovery | Run the probe or simulation | `portfolio-pdlc-simulate` / `portfolio-pdlc-advance` |
| 8 | Board is clean and flowing | Probe the system itself; capture new improvement bets | `portfolio-pdlc-improve` |

Rationale for the ordering: waiting decisions starve everything downstream; a broken board
lies to every later cycle; committed money outranks uncommitted ideas; finishing outranks
starting (right-to-left); and only a healthy board earns the luxury of self-improvement.

## The Human Decision Boundary

Agents **prepare** decisions; they never make them. The decisions that stay human: invest in
discovery, commit to build (the point of last return), pivot, kill/freeze, change WIP limits,
reorganize teams, extract platforms, change the workflow definition. The agent's deliverable
at each of these points is a decision brief in `reviews/`: what we can rely on, what's still
open, evidence vs. opinion, options with tradeoffs, a recommendation — and the card's
`next_decision` field set. Speak in confidence and "what you can count on," not gates.

## Walk the Talk — the Improvement Lane

Improvement ideas (process or topology) are **captured, not implemented**. They become cards
in `improvements/` with a benefit hypothesis, leading indicators, and success/kill criteria,
and they advance through the same stages as everything else: Explore (framing) → Discovery
(a probe, a pilot on one initiative, or a `portfolio-pdlc-simulate` what-if) → Plan/Commit
(the humans agree to change the operating model) → Execute (roll the change into `pdlc.md` /
`topology.md` / templates) → BAU (watch the leading indicators; keep or revert). Use the
`sdd-specify` / `sdd-plan` skills for bets big enough to deserve full spec ceremony.

## Routing

| Situation | Load |
|---|---|
| No portfolio workspace exists yet / onboarding an org's material | `portfolio-pdlc-wire` |
| "Where is everything? What's really going on?" / review prep / systemic doubt | `portfolio-pdlc-assess` |
| Move one initiative forward; prep an investment/commit decision | `portfolio-pdlc-advance` |
| A card is weak: activity-framed, unevidenced, no indicators, unclear risks | `portfolio-pdlc-compound` |
| "How do we make the PDLC/portfolio itself better?" | `portfolio-pdlc-improve` |
| What-if on WIP limits, topology change, arrival rate; derisk a big improvement bet | `portfolio-pdlc-simulate` |
| Deep single-initiative diagnostic | `sniff-test` (in this repo) |
| Board-level pattern read | `sniff-test-portfolio` (in this repo) |
| Build/strengthen a canvas | `lean-product-canvas-coach` (in this repo) |

**Self-contained by design:** everything the loop needs ships in this repo — the
diagnostic skills above plus inline rubrics (stage expectations, input→impact ladder,
derisking matrix) inside each member skill. If you run a larger skill library (OKR
rewriting, flow-metrics coaching, spec-writing skills), the member skills name the seams
where those compose in; without them, proceed on the inline rubrics.

## Cross-Harness Rules

- Everything is plain markdown + `python3` stdlib scripts; nothing here assumes a specific
  agent harness. Use your file tools; spawn subagents only if your harness supports them —
  the loop is designed to run fine single-threaded.
- Headless / loop mode (`mode:loop`): no blocking questions; when a cycle hits a human
  decision, write the decision brief, set `next_decision`, log it, and end the cycle
  reporting `DECISION-PENDING <slug>`. Otherwise end cycles reporting `CYCLE-COMPLETE <move> <slug>`.
- Never auto-advance a card past Plan/Commit or into/out of Execute without a recorded human
  decision (a dated entry in the card's Decision Log naming who decided).

## Quality Gates

- The board was regenerated before and after the cycle's move.
- Exactly one move was executed; anything else discovered went to `improvements/` or the
  loop log, not into scope.
- Any stage transition has a matching human decision recorded where the boundary requires one.
- At most one learning captured, and only if it changes how the next cycle behaves.
- Sponsor-facing output uses confidence language, not gate/compliance language.

## References

- `skills/portfolio-pdlc/references/workspace-contract.md` — file layout, frontmatter schema, generated-file rules.
- `skills/portfolio-pdlc/references/probe-library.md` — the minibook-derived probe families used by `portfolio-pdlc-improve`.
- `skills/portfolio-pdlc/templates/` — charter, pdlc, initiative, improvement, review, workspace AGENTS.md.
- `skills/portfolio-pdlc/example/fiy-portfolio/` — FlowImpact Yoga demo instance (safe to practice on).
