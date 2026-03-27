# PR vs direct commit

> **AI Assistant Note**: Reference this document when deciding whether a change needs a branch + PR or can go straight to main.

## Decision table

| | Direct commit to main | Branch + PR |
|:--|:--|:--|
| **What changed** | Docs wording, typos, config tweaks | Code, behaviour, structure |
| **Risk** | Cannot break anything | Could break build/tests/behaviour |
| **Review needed** | No — the intent is obvious from the diff | Yes — someone should sanity-check |
| **Reversibility** | Trivial `git revert` | Same, but you want the PR record |

## The rule

If a change touches **only documentation or configuration** and the intent is **obvious from the diff**, commit directly to main. If a change touches **code or structure** — or the diff needs explanation — use a branch and PR.

## Grey area

Structural docs changes (splitting a file, reorganising sections, renaming headings) benefit from a PR even though they are docs-only. The PR gives the reviewer a chance to check that nothing was lost. Once merged, follow-up wording fixes within those same files go direct.

## Examples

| Change | Route | Why |
|:-------|:------|:----|
| Fix a typo in README | Direct | Obvious, zero risk |
| Rewrite a section to reflect current reality | Direct | Docs wording, no structural change |
| Split README into README + INSTALL.md | PR | Structural — reviewer should check nothing was lost |
| Add a new component | PR | Code change |
| Update `site.json` font preset | Direct | Config tweak, obvious intent |
| Add a new convention doc + update config JSON | PR | Structural — multiple files, registry update |
