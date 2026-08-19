# Workflow Archetypes — starting points, not templates

Flow-driven is workflow-agnostic. These archetypes exist so you do not start from a blank
graph — take one, argue with it, and make it yours within a week. Each gives the steps, the
exits worth enforcing, sensible starting rungs, the measures that matter, and the way that
particular archetype usually goes wrong.

Set `kind:` in the flow-config to the archetype you started from. It is a hint for future
readers, not a constraint.

---

## `development` — product / spec-driven delivery

**Steps**: `intake → shape → derisk (optional) → commit → build → verify → release → learn`

| Aspect | Starting point |
|---|---|
| Evidence exits | `shape` (a problem framed with a testable hypothesis), `derisk` (the riskiest assumption tested), `verify` (tests + review findings recorded) |
| Decision points | `commit` — the point of last return, and `release` where blast radius is high |
| Starting rungs | shape 2 · derisk 2 · build 3 · verify 4 (tests are the archetypal independent check) · release 1 |
| Inner graphs | `build` (plan → implement → self-review → test → fix, capped) · `verify` (static → tests → adversarial read) |
| Measures | cycle time by step, rework out of `verify`, escape rate to production, first-pass yield |
| Fails by | committing before derisking; a `verify` step that only re-runs what the builder already ran |

This is where spec-driven toolchains (spec-kit, Kiro) slot in — see `ingest-recipes.md`.
Their phases usually map to `shape`/`commit`, and their artefacts make excellent exit
evidence.

---

## `operational` — a request stream with someone waiting

**Steps**: `receive → classify → gather → resolve → verify → close → learn`

| Aspect | Starting point |
|---|---|
| Evidence exits | `classify` (category + class of service, with the reason), `verify` (the resolution was checked against the request) |
| Decision points | usually only exceptions — an escalation path rather than a gate |
| Starting rungs | classify 3–4 · gather 3 (context assembly is the sweet spot) · resolve 2–3 · verify 4 · close 5 |
| Inner graphs | `resolve` (retrieve → propose → check policy → draft response) |
| Measures | time to first response, time in queue vs touch time, reopen rate, escalation rate, cost per request |
| Fails by | optimising average handling time while reopen rate climbs; classifying into buckets nobody routes on |

Operational streams are where classes of service earn their keep: expedite, standard, and
fixed-date behave genuinely differently and should have different pull policies.

---

## `content` — research-backed publishing

**Steps**: `intake → research → angle-test (optional) → draft → edit → publish → amplify (optional) → learn`

| Aspect | Starting point |
|---|---|
| Evidence exits | `research` (sources with a primary), `angle-test` (a dated probe with a recorded response), `edit` (claims audited), `publish` (URL, date, decision) |
| Decision points | `publish` — your name goes on it |
| Starting rungs | intake 2 · research 3 · angle-test 1 · draft 2 · edit 1 · publish 1 · amplify 4 · learn 3 |
| Inner graphs | `draft` (outline → expand → self-critique → revise → citation-check, capped at 2) |
| Measures | rework out of `edit`, evidence coverage, hypothesis-confirm rate, human minutes per piece |
| Fails by | fluent drafts with untraceable claims; publishing volume becoming the goal; probing to confirm rather than to find out |

Worked instance: `../example/fiy-content-engine/`.

---

## `ai-use-case` — taking an AI capability from idea to production

**Steps**: `intake → feasibility → eval-design → prototype → pilot → harden → deploy → monitor`

| Aspect | Starting point |
|---|---|
| Evidence exits | `feasibility` (a documented failure mode inventory), `eval-design` (a dataset and a threshold agreed *before* building), `pilot` (results against the eval, with the misses) |
| Decision points | `pilot` (do we take this to real users) and `deploy` |
| Starting rungs | feasibility 2 · eval-design 2 · prototype 3 · pilot 1 · harden 3 · deploy 1 · monitor 4 |
| Inner graphs | `prototype` (baseline → iterate → eval → error-analyse, capped) |
| Measures | eval pass rate by slice, cost per successful task, human override rate, time from intake to a real user |
| Fails by | building before the eval exists — after which every result is a vibe; demos that never enter `pilot`; monitoring that watches uptime rather than answer quality |

The eval **is** the evidence exit. An AI use-case stream without one is a demo pipeline, and
flow-driven will make that embarrassingly visible, which is the point.

---

## `research` / analysis

**Steps**: `question → scope → gather → analyse → challenge → synthesise → decide`

| Aspect | Starting point |
|---|---|
| Evidence exits | `gather` (sources with provenance), `challenge` (the adversarial read, findings recorded) |
| Decision points | `decide` — the whole stream exists to serve it |
| Starting rungs | gather 3–4 · analyse 2 · challenge 3 (a different agent, adversarial brief) · synthesise 2 · decide 0 |
| Measures | time to decision, share of findings that survived the challenge step, decision reversal rate |
| Fails by | synthesising before challenging; a `challenge` step run by whoever did the analysis |

`challenge` is the step everyone skips and the only reason to trust the output.

---

## Choosing and mixing

- **Start from the archetype whose *failure mode* you recognise**, not the one whose steps
  look familiar. The failure mode is the thing you are buying protection from.
- **Mixing is normal.** A content engine with an `ai-use-case` sub-flow for its research
  tooling is two streams, not one hybrid — give each its own workspace and let items
  reference each other.
- **Delete a step in the first month.** Every archetype here has one step your stream does
  not need. Finding it is a good early meta-loop result.
- **The default is a straight line.** Add a branch when the work actually branches, and a
  back-edge when rework is real. A graph that flatters is worse than a chain that is honest.
