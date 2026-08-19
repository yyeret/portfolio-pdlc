# Step Contracts — the delegate model and the run model

Two questions per step, and they are different questions:

- **Delegate model**: *who holds this step, and what stays human?*
- **Run model**: *how is it actually executed, with what context, budget, and stop rule?*

Answer both per step. Answering them per *workflow* is how organisations end up with an
"AI-assisted process" that nobody can describe.

## The delegation ladder

| Rung | Name | Who does the work | Who is accountable | The check |
|---|---|---|---|---|
| **0** | Human only | a person | that person | their judgement |
| **1** | Agent assists | a person, with agent-prepared context | that person | their judgement |
| **2** | Agent drafts, human edits | agent produces, human is editor of record | the human editor | the human's edit |
| **3** | Agent runs, human verifies exit | agent completes the step | the step owner | a human checks the exit evidence |
| **4** | Agent runs, checked automatically | agent completes the step | the step owner | an automated check; humans see exceptions |
| **5** | Closed-loop automation | deterministic code | the system owner | the check plus the metric |

Four things people get wrong about this ladder:

1. **It is per step, not per workflow.** A healthy stream runs rung 1 and rung 4 steps side
   by side. Uniform rungs mean nobody looked at the steps individually.
2. **The rung is a property of the evidence, not the model.** "The model can do this now" is
   not a promotion criterion; "the check catches what the human catches, over ten items" is.
3. **Rung 3 is the dangerous one.** The agent is doing the whole step and the only check is a
   human reading an artefact that looks finished. It is where rubber-stamping lives. Get to
   4 by building a check, or drop to 2 where the human is genuinely in the work.
4. **Down is a legitimate direction.** Write the demotion trigger at promotion time, or the
   ladder only ever ratchets upward and the first real failure gets argued rather than acted on.

### What caps the rung

```
rung_ceiling = f(reversibility, blast radius, check quality, accountability)
```

- **Reversibility**: undo in a minute → 4–5 is available. Undo requires an apology, a legal
  process, or a customer conversation → 0–2, whatever the check quality.
- **Blast radius**: one item, or every item until someone notices?
- **Check quality**: no independent check → 3 is your ceiling, and you should not be
  comfortable there.
- **Accountability**: some decisions need a person's name on them for reasons that have
  nothing to do with capability. Say so explicitly, and stop treating those steps as backlog.

### Promotion and demotion

Promotion is an improvement bet, not an edit. It needs:

- a **baseline** for the measures it claims to move;
- an **evidence bar** — typically N consecutive items at the current rung whose independent
  check agreed with the human, plus zero escapes;
- a **shadow run** where the agent does the step but the human still owns the output, so the
  comparison is real and costs nothing if it fails;
- **demotion criteria written now**, in the step file, so the argument is over before it
  starts.

Demotion is not a failure of the programme. A step that came back down and stayed down
taught you where the boundary is — and the boundary is the most valuable thing you learn.

## The run model

`run:` names the mechanism, `run_ref:` names the thing to invoke:

| `run` | `run_ref` | Use when |
|---|---|---|
| `skill` | a skill name | the harness has a packaged capability for this step |
| `prompt` | `platform/prompts/<name>.md` | the step is a bounded generative move you want versioned |
| `script` | a path | it is deterministic; prefer this whenever it is possible |
| `tool` | a tool/connector name | an external capability does the work (scheduler, CI, API) |
| `human` | empty, or a doc | a person does it — an honest and common answer at rungs 0–1 |
| `external` | a system name | another team or system owns it; you are modelling a wait |

Prefer `script` over `prompt` for anything deterministic. A regex that always finds the same
thing beats a model that usually does, costs nothing, and never has an off day.

### The rest of the run contract

- **Context packs** — what the runner may rely on knowing. Most step quality lives here.
- **Tools allowed** — the smallest set that works. A step that can write anywhere will.
- **Guardrails** — the things it must not do, stated as prohibitions, not preferences.
- **Budget** — agent time/cost *and* human time. Human minutes are the scarce resource; if
  you never write them down you will never notice them growing.
- **Stop rule** — iteration cap, budget cap, or a falsifiable condition. Mandatory for
  anything with a loop in it.
- **Artifacts written** — where output lands, so verification knows where to look.

### Escalation is a first-class exit

Every step above rung 1 needs `escalate_when` and `escalate_to`. An agent that stops and
asks has done its job correctly; treat escalations as signal, not as failure:

- Log each one on the item.
- Read them in the meta-loop. A repeated escalation is a **missing context pack**, and
  capturing it is how the platform compounds.
- Watch the rate. Rising escalations mean the work changed. Zero escalations at rung 3+ over
  many items means the agent is not noticing when it should stop, which is worse.

## Exit evidence — how to write it

The single highest-leverage sentence in a step file. Rules:

1. **Name an artefact or an observation**, not an activity. "Findings recorded, including
   none" beats "reviewed".
2. **Checkable by a stranger.** If verifying requires having done the work, it is not evidence.
3. **Include the negative case.** A check that produced no findings must still say so, or a
   check that never ran is indistinguishable from a clean one.
4. **Two or three lines.** A ten-line exit is a step wearing a costume.
5. **Evidence that gets *used* downstream stays honest.** If the next step reads it, its
   absence gets noticed. Evidence that nobody reads decays into paperwork — delete it and
   admit the exit was decorative.

Calibration: `"Draft cites at least two named sources from the research pack"` is evidence.
`"Draft is high quality"` is a wish. `"Draft reviewed by the agent"` is theatre.

## Verification

`verify_with` must not be `run_ref`. Ranked by strength:

1. **A deterministic script.** Cheap, boring, never tired.
2. **A different agent, different context, adversarial brief** ("find the claim that will
   embarrass us; if you find nothing, say what you looked at").
3. **The same agent in a fresh context** with the rules only, and no access to its own
   reasoning.
4. **The same agent in the same context** — not a weak check, not a check at all.

Give the verifier a *sceptic's brief*, not a "please check this". And require it to report
what it examined even when it finds nothing, so a lazy check is visible.
