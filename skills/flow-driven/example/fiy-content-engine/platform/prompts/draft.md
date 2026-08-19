# Run ref — draft

**Step**: `draft` · **rung 2** (agent drafts, Dana edits) · runs the inner graph in `steps/draft.md`

Write `items/<slug>/draft.md` from the research pack and the angle evidence.

**Inner loop** — follow it, do not improvise around it:

1. **outline** — the spine: the move the reader should make, and the three things that have
   to be true for them to make it.
2. **expand** — write it. Mark every claim inline as `[S3]` pointing at the source table.
3. **self-critique** — read as the most sceptical studio owner in the community. Where does
   this overstate? What would they reply?
4. **revise** — fix findings. Maximum two passes through 3–4, then out.
5. **citation-check** — every `[Sn]` resolves to a row in the source table; every source row
   that is not used gets dropped.

**Hard rules**:

- No claim that is not in the research pack. If the draft needs one, **stop and send the
  item back to `research`** across the rework edge. This is the correct move and costs
  nothing; inventing the claim costs an audience.
- Follow `platform/context/house-voice.md`. Run `platform/checks/house-voice.md` before
  exiting and either fix or explicitly waive each finding with a reason.

**Exit**: draft, house-voice findings with dispositions, and a non-empty "open questions for
the editor" list. Set `holder: human`.
