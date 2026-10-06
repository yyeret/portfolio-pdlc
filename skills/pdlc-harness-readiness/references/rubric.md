# White-box harness rubric

Score a **named workflow configuration**, not a brand. Bands are ordinal evidence anchors, not equal intervals or a validated maturity scale. A higher band requires all essential connections in that band; an optional command cannot lift a default-path score. Record confidence and the source boundary separately.

## Evidence weight

1. **Required and consumed:** normal path or explicit risk branch requires the behavior, produces evidence, and routes it to a named next step or human. Strongest documented support.
2. **Configured and reachable:** installed rule/skill/hook is enabled and has a trigger, but the handoff or response is incomplete.
3. **Available:** command, template, example, or vendor feature exists but is optional or not shown active.
4. **Aspirational:** prose says to learn, validate, or improve without an evidence/owner/response contract.
5. **Unknown:** source, configuration, runtime activation, or linked process cannot be inspected. Do not score it as absent.

Actual output/run traces can corroborate or contradict the documented path, but this white-box assessment does not require a live run. An agent's base instructions are not automatically visible; official product documentation supports only the behavior it actually documents.

## Five axes · 0–4

| Band | Upstream discovery | Trustworthy SDLC delivery | Downstream validation | PDLC integration | Compounding / ON the loop |
|---|---|---|---|---|---|
| **0** | No product problem or intended beneficiary in scope | No linked execution or verification contract | Path explicitly stops at engineering completion with no product handoff | No product intent in the inspected path | No learning or harness-improvement mechanism in scope |
| **1** | Problem/why and requirements framing | Requirements/tasks and basic checks | Rollout, operations, or validation mentioned; no owned real-use review | Product intent is framed, but delivery is the completion boundary | Retrospective, notes, or knowledge capture exists without an evidenced consumer |
| **2** | Repeatable option/outcome exploration; investment evidence incomplete | Requirements, implementation, acceptance checks, and change handling linked | Concrete product-signal collection or reporting process; decision response incomplete | Discovery or product evidence is substantial, but lifecycle links remain incomplete | Repeatable learning capture feeds a discoverable knowledge source or improvement queue, but adoption/benefit is unverified |
| **3** | Structured discovery can change go/no-go or learning-versus-delivery choice | Risk-appropriate automated checks plus independent review/verification; findings lead to correction before completion | Adoption owner plus triggered outcome decision and routed follow-through | Required intent → signal → adoption owner → human decision → next action chain | Owned, versioned harness changes are selected from evidence, checked on later runs, and can be reversed |
| **4** | Discovery, thresholds, and owned investment decisions form a linked contract | Explicit corrective convergence loop compares result with spec and evidence until residual risk is accepted; checks remain reproducible | Recurring outcome decisions steer later investment and ongoing operation | The complete product contract recurs across discovery, delivery, use, and portfolio/stream decisions | Recurring meta-loop measures harness impact, prioritizes improvement bets, independently verifies changes, and propagates or kills them across relevant agents/workflows |

**Trustworthy output check:** identify what would catch a plausible wrong-but-confident implementation. Give credit for acceptance examples, tests at the lowest useful layer, independent review, runtime/UX evidence where needed, failure handling, and a correction loop. More tests or more reviewers alone do not earn a higher band; ask whether findings can block completion and whether the evidence is reproducible. Security checks are relevant when risk warrants them, not a universal checklist.

**Discovery/validation check:** product metrics are decision evidence only when a beneficiary/cohort, observation window, baseline or probe, interpretation rule, and accountable response are tied to the outcome. Technical checks are valid guardrails and can be product signals for an internal developer-facing outcome. Do not demand post-launch results from an early-stage workflow; require a later owner and trigger if it claims end-to-end coverage.

**Compounding check:** distinguish improving the *product* from improving the *harness*. Updating a feature spec, archiving a change, or writing an engineering retrospective is not by itself a harness change. Look for a decision about workflow rules, templates, checks, or skills, a versioned change, measured effect on future runs, and a kill/revert path. An external organizational improvement system counts when the handoff and consumer are explicit.

**Conditional improvement lane example:** a repo may have a well-designed improvement queue with baselines, human adoption decisions, versioned changes, watch periods, and kill criteria, while ordinary feature runs never route findings into it. Score the active feature path at most **2** for a reachable capture/queue; describe the improvement lane as a separately selected route. Band 3 needs a named trigger and owner that move relevant delivery or outcome findings into that lane, plus later-run verification and reversal. Do not grant band 3 merely because the lane exists.

## Verdict and priority

Do not average the axes. State the actual boundary: engineering-complete, PDLC-aware with broken links, or PDLC-ready for the stated scope. PDLC-ready requires Upstream, Downstream, and PDLC integration at least 3, plus trustworthy delivery at least 2; compounding is a separate judgment and must not silently change the PDLC verdict. A strong ON-the-loop score cannot compensate for an absent product loop, nor can a strong product loop prove the harness improves itself.

Prioritize by plausible lost value or loss of trust, recurrence across the default path, and ease of proving the repair. Label impact as plausible unless measured. Name the evidence that could overturn each finding.
