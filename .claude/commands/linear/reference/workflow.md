# Linear workflow

> **AI Assistant Note**: Reference this document when explaining what the Linear commands do or how the workflow fits together.

## Typical workflow

```
/linear:next-steps          → see what needs doing
/linear:plan-work           → create a new issue (if needed)
/linear:start PG-X          → branch, implement, PR, terminal review
  ... you review the diff in the terminal ...
  ... someone reviews on GitHub ...
/linear:fix PG-X            → address GitHub review feedback (if any)
/linear:finish PG-X         → squash merge, clean up, Done
```

## What's an "issue"?

It's the universal term for a **tracked item** — something that needs attention. The word comes from bug tracking ("there's an issue with X"), but it got stretched to cover everything: features, bugs, tasks, research, chores.

A new feature is an "issue" in Linear/GitHub/Jira. It's not that the feature *is* an issue — it's that the **tracking artifact** for the feature is called an issue. The word describes the container, not the content.

It's like how every email is called a "message" whether it's a question, an announcement, or a complaint. "Message" is the container; the content varies.

## Reviewing PRs in VS Code

To review pull requests directly in VS Code, install the [GitHub Pull Requests](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github) extension. It lets you browse, review, and comment on PRs with in-editor line comments — no need to switch to the browser.

## Commands

### `/linear:next-steps`

**Review priorities and recommend next work.** Shows current work, open PRs, recently completed issues, and backlog — then recommends 1–3 concrete next actions.

Priority ordering: build failure > PRs needing fix > in-progress work > PRs needing review > approved PRs to merge > backlog.

For each open PR, checks GitHub for `CHANGES_REQUESTED` reviews and unresolved comments. PRs needing fix are surfaced above new backlog work.

**Usage**: `/linear:next-steps`

### `/linear:plan-work`

**Plan work and create a Linear issue.** Checks for duplicates, optionally refines the description with CRAFT, drafts title and description, and waits for your approval before creating.

In `--research` mode, explores the codebase and Linear first, then adds code examples (showing how similar patterns are already implemented) and acceptance criteria (observable outcomes, not implementation steps).

Also assesses whether tests make sense for the change. If they do, the issue notes that tests should be written first — not strict TDD, but having them in place catches regressions later.

**Usage**:

- `/linear:plan-work "add dark mode toggle"` — quick mode
- `/linear:plan-work --research "add PostHog integration"` — research mode with code examples and acceptance criteria
- `/linear:plan-work --craft "add dark mode toggle"` — auto-run CRAFT prompt refinement
- `/linear:plan-work --research --craft "add PostHog integration"` — research + CRAFT combined

### `/linear:start`

**Start work on a Linear issue.** One headless flow: create or switch to the feature branch, move the issue to Doing, implement the changes, validate (build + tests), commit, push, open a PR, move to In Review, then show the full diff for terminal review.

Trusts the issue — the plan was agreed during `/plan-work`. No approval gate mid-flow.

Ends by asking: "Does this look right, or do you want changes?" If you request changes, it fixes, re-validates, and shows the updated diff. Repeat until satisfied.

**Usage**:

- `/linear:start PG-205` — explicit issue
- `/linear:start` — infers from branch

### `/linear:fix`

**Address GitHub PR review feedback.** Reads review comments from GitHub (review body, line comments, past reviews), implements all requested changes in one pass, validates, pushes, and posts a summary comment on the PR.

Reviewer feedback takes priority over the original issue — plans evolve through review.

**Usage**:

- `/linear:fix PG-205` — explicit issue
- `/linear:fix` — infers from branch

### `/linear:finish`

**Finish the issue.** Runs build + tests (stops if they fail), squash merges the PR with a clean commit message, switches to main, deletes local and remote branches, and marks the issue Done in Linear.

The squash commit message reads as if the work was done right the first time — no mention of rejections, fix cycles, or iterations.

**Usage**:

- `/linear:finish PG-205` — explicit issue
- `/linear:finish` — infers from branch
