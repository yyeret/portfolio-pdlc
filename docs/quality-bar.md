# Quality Bar — what a change to this repo has to clear

Every pull request opened from an agent session in this repo is reviewed against this bar
by an **independent reviewer** — a fresh context that did not write the change — before it
merges. A clean verdict merges automatically; anything else goes back to a human.

In this repo's own vocabulary: merging is a step whose delegate rung is 4 — the agent runs
it, this bar is the independent check that makes that safe, and §4 is the `escalate_when`.
The verifier is never the doer.

## 1. The reviewer's stance

You are not helping the author. Your job is to find the thing that will embarrass this repo
in public — a script that does not run, a claim the diff does not support, a convention
quietly broken. Read the diff yourself; do not take the PR body's word for anything.

**Report what you examined, even when you find nothing.** A review with no output is
indistinguishable from a review that never happened.

Verdict: **PASS** · **PASS-WITH-NOTES** (merge, notes recorded for later) · **BLOCK** (do
not merge; say exactly what is wrong and what would fix it).

## 2. Mechanical checks — every one must pass

Run them; do not reason about whether they would pass.

```bash
python3 -m py_compile skills/*/scripts/*.py

python3 skills/flow-driven/scripts/flow_lint.py  skills/flow-driven/example/fiy-content-engine --today 2026-08-19
python3 skills/flow-driven/scripts/flow_board.py skills/flow-driven/example/fiy-content-engine --today 2026-08-19
python3 skills/flow-driven/scripts/flow_next.py  skills/flow-driven/example/fiy-content-engine --today 2026-08-19
python3 skills/portfolio-pdlc/scripts/portfolio_board.py skills/portfolio-pdlc/example/fiy-portfolio --today 2026-08-17
```

| # | Check | Passes when |
|---|---|---|
| M1 | Scripts compile | `py_compile` clean on every script |
| M2 | Flow example lints | `CLEAN`, **0 violations**; warnings only the ones its README documents as seeded |
| M3 | Board regenerates | exits 0, and `git diff --stat` on the example shows no unexplained churn |
| M4 | Orchestrator runs | prints a run card and exits 0/3/4, never a traceback |
| M5 | Portfolio example still works | exits 0 and `board.md` regenerates |
| M6 | Skill frontmatter | every `skills/*.md` has `name` (matching its filename), `description`, `metadata.version` |
| M7 | No dangling references | every `skills/…` or `docs/…` path named in changed files exists |
| M8 | Stdlib only | no third-party imports, no network calls in any script |
| M9 | No junk committed | no `__pycache__/`, `exports/`, `.pyc`, scratch files, or editor droppings |

## 3. Convention checks — cite the line or stay silent

| # | Check | The convention |
|---|---|---|
| C1 | Layout | skills at `skills/<name>.md`, companions under `skills/<name>/` |
| C2 | Language | confidence and "what you can rely on" — never gates, compliance, or consultant filler |
| C3 | Generated files | `board.md`, `flow-log.csv`, `exports/` are regenerated, never hand-edited |
| C4 | Bets, not edits | workflow/process changes ride the improvement lane; they are not slipped into a definition in passing |
| C5 | Spec in step | `docs/specs/flow-driven.md` matches what `skills/flow-driven*` actually does; **R-ids are stable and never renumbered** |
| C6 | Evidence language | exit evidence is written as artefacts and observations, never activities |
| C7 | No session leakage | no model identifiers, session URLs, or harness-specific assumptions in committed **files** (commit trailers are out of scope) |
| C8 | No secrets | no tokens, keys, internal hostnames, or private personal data |

## 4. Escalation — do NOT auto-merge, hand back to the human

Any one of these turns a PASS into a hand-back, however good the change is:

1. Any mechanical check fails, or a convention finding the reviewer rates as blocking.
2. **Public framing**: README top matter, LICENSE, the name of a skill family, or how the
   work is positioned to readers.
3. **Deletions or renames** of existing material beyond what the stated scope requires.
4. The change is **larger than the request that prompted it** — scope crept.
5. The PR body itself flags an open question, a judgement call, or a trade-off it resolved
   unilaterally.
6. Anything irreversible or outward-facing that a revert would not actually undo.

Condition 1 is the review loop's own material: a failed check or a blocking convention
finding routes to a fix round (§6) and reaches a human only by surviving the loop's bound.
Conditions 2–6 are about what the change *is* rather than a defect in it — no fix round
resolves them, so they leave for a human the moment they trip.

## 5. Change integrity

- The commit messages and PR body describe what the diff **does**, not what was intended.
- Every verification claim in the PR body is reproducible by running the command it quotes.
- Existing behaviour is unchanged unless the PR says otherwise and shows why that is safe.

## 6. The review loop

Review is a loop, not a single pass: **review → fix the blocking findings → re-review →
merge when clean.** It is bounded, because an unbounded critique-revise loop converges on
plausibility rather than truth — the same rule this repo applies to every inner graph.

```
round 1..3:
    verdict = independent review (fresh context, given the diff + every prior round's findings)
    any of §4.2–§4.6 tripped       -> hand to a human immediately, whatever the round
    PASS / PASS-WITH-NOTES         -> merge, record the rounds, done
    BLOCK on round 3               -> hand to a human with what is still open
    BLOCK otherwise                -> fix ONLY the blocking findings, push, next round
```

**At most three reviews — two fix rounds.** If it is not clean by then, the problem is not
one more fix.

Rules that keep the loop honest:

1. **Every round gets a fresh context.** Not the same reviewer continued — a reviewer that
   already published a verdict defends it. Hand the new one the diff, the previous rounds'
   findings, and the fix commits; it re-reads the diff itself and checks both that the old
   findings are genuinely fixed and that the fixes broke nothing.
2. **Only BLOCK-level findings get fixed in the loop.** Notes are recorded in the PR body
   and left. Chasing notes is how a review loop turns into infinite polish.
3. **Convergence guard.** If a round raises a *new* blocking finding that is not a
   consequence of the previous round's fix — something an earlier round could have caught
   and did not — the reviews have stopped converging. Stop the loop, hand back with
   everything still open, and do not spend the remaining round.
4. **Escalation short-circuits.** §4.2–§4.6 are not fixable by another round — they are
   about what the change *is*, not a defect in it. Exit to a human the moment one trips.
   §4.1 is the exception: a failed check or a blocking convention finding is precisely what
   this loop exists to fix, so it routes to a fix round and reaches a human only by
   surviving the bound.
5. **The loop leaves a trace.** Each round is recorded in the PR body: round number,
   verdict, blocking findings, what changed in response. A reader should be able to tell a
   loop that converged from one that gave up.

## 7. Merging

On PASS or PASS-WITH-NOTES: merge with **rebase** — this repo's history is linear and each
commit carries its own reasoning. Report the merge, the rounds it took, and any notes.

On hand-back: leave the PR open, say what is open in one paragraph, and name what would
resolve it.
