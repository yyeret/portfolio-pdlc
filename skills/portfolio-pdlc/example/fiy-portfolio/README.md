# FlowImpact Yoga (FIY) — Example Portfolio

A safe practice instance of the portfolio-pdlc workspace contract, populated with the
fictional scale-up from the Portfolio Agility Trailmap minibook (Mary, co-founder; Jim,
CPO; ~200-person product & tech org serving yoga/pilates studios).

**Deliberately seeded smells** — the loops should find these, so don't "fix" the seed data
casually:

| Card | Seeded smell |
|---|---|
| `pilates-vertical-expansion` | Aging in execute past threshold; orientation still `mixed` |
| `sso-enterprise-readiness` | Activity-framed, high-risk, committed with no discovery record, same-day rubber-stamp commit, no leading indicators |
| `churn-save-desk-reduction` | Discovery timebox lapsed; invest decision overdue since 2026-08-10 |
| `mobile-app-rewrite` | An "experiment" that ballooned into a full build; activity-oriented; no outcome hypothesis; skipped discovery at high risk |
| `gym-partnerships-integration` | Thin explore card; altitude conversation zone (score 5) |
| `soc2-type2-attestation` | Tier-2 awareness-lane example |
| `billing-platform-extraction` | The topology bet: three cards name `payments-billing` as a dependency |
| flow-log | Mixed history: enough samples for explore/execute (`history` label), thin for discovery/rollout (`prior` label) |

Historical slugs in `flow-log.csv` (`studio-scheduling-revamp`, `instructor-payroll-automation`,
`pricing-page-experiment`) have no card folders — they finished before this board was wired
and exist to make throughput/cycle-time metrics computable.

## Exercises

1. `python3 ../../scripts/portfolio_board.py .` — regenerate the board; read the flags.
2. Run one operating-loop cycle per the umbrella skill — the leverage table should route
   you to the overdue decision on `churn-save-desk-reduction` first.
3. Run `portfolio-pdlc-assess` in full mode; check it catches the rubber-stamp commit.
4. Run `portfolio-pdlc-improve focus:topology`; it should fire the dependency-concentration
   probe on `payments-billing`.
5. Discovery for `limit-execute-wip`: `python3 ../../scripts/portfolio_sim.py . --scenario reviews/scenarios/limit-execute-wip.txt`

Dates in this instance assume "today" ≈ 2026-08-17; pass `--today 2026-08-17` to the board
script for reproducible flags.
