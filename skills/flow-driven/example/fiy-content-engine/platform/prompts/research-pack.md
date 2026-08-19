# Run ref — research pack

**Step**: `research` · **rung 3** (agent runs, verified at exit)

Build the evidence base for this item. Output `items/<slug>/research-pack.md`.

**Structure**:

```
## Claims we intend to make
| # | Claim | Source | Primary? | Date | Confidence |

## Sources read
| Source | What it actually says | What it does not say |

## Opinions (labelled, unsourced, kept honest)
## Open questions for the editor
```

**Rules**:

- At least three sources, at least one primary (customer call, ticket thread, product data).
- Never cite a source you have not read in full. Never cite our own published content as
  evidence for a claim it also only asserted.
- Only claims present in `platform/context/product-truths.md` may be made about our product.
- Anything you believe but cannot source goes under **Opinions**, labelled. This is the
  most valuable section in the pack; do not shrink it to look thorough.

**Stop rule**: three sources including a primary, or 90 minutes. Then escalate with what
you have, including what you looked for and could not find.

**Exit**: run `platform/checks/evidence-check.md`, record its findings on the item, and add
`research` to `evidence_exits_met`.
