# Check — publish pre-flight

**Verifies**: the exit of `publish`. Deterministic where possible; boring on purpose.

## Checklist

- [ ] Every link resolves (200, not a redirect chain to the homepage)
- [ ] Every statistic carries its denominator
- [ ] Product claims present in `product-truths.md` and unexpired
- [ ] No customer named without a recorded permission
- [ ] No unreleased feature referenced
- [ ] Disclosure line present where we cite our own data
- [ ] Metadata: title, description, canonical, author, publication date
- [ ] Renders on a phone — the primary reader is on one

## Output

The completed checklist attached to the item, with the URL, date, and channel. Attach it
before the human signs the Decision log, not after: the decision should be made with the
pre-flight in hand.
