# Chris Beams commit style

Chris Beams is a software engineer who wrote one of the most widely cited articles on how to write good Git commit messages. His influential post ["How to Write a Git Commit Message"](https://chris.beams.io/posts/git-commit/) established what has become the de facto style guide for many development teams.

---

## The 7 rules of great commit messages

1. **Separate subject from body with a blank line**
2. **Limit the subject line to 50 characters**
3. **Capitalize the subject line**
4. **Do not end the subject line with a period**
5. **Use the imperative mood in the subject line**
6. **Wrap the body at 72 characters**
7. **Use the body to explain what and why vs. how**

---

## Example git commit message

```text
Summarize changes in around 50 characters or less

More detailed explanatory text, if necessary. Wrap it to about 72
characters or so. In some contexts, the first line is treated as the
subject of the commit and the rest of the text as the body. The
blank line separating the summary from the body is critical (unless
you omit the body entirely); various tools like log, shortlog
and rebase can get confused if you run the two together.

Explain the problem that this commit is solving. Focus on why you
are making this change as opposed to how (the code explains that).
Are there side effects or other unintuitive consequences of this
change? Here's the place to explain them.

Further paragraphs come after blank lines.

 - Bullet points are okay, too

 - Typically a hyphen or asterisk is used for the bullet, preceded
   by a single space, with blank lines in between, but conventions
   vary here

If you use an issue tracker, put references to them at the bottom,
like this:

Resolves: #123
See also: #456, #789
```

---

## Why the Chris Beams style works

Written during his time in software engineering and leadership roles, Beams' guidelines address the practical realities of collaborative development:

- **Tool compatibility** — the character limits work perfectly with git's built-in formatting
- **Human readability** — natural English structure that reads like proper sentences
- **Scalability** — works for small personal projects and large enterprise codebases
- **Timeless principles** — focus on clear communication rather than specific tooling

---

## Adoption and influence

The Chris Beams style has become the standard because it:

- Balances structure with flexibility
- Prioritizes human understanding over automation
- Has stood the test of time across different development eras
- Provides clear, actionable rules that teams can adopt immediately
