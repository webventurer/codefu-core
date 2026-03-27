# CRAFT prompt template for Linear issue creation

> **What this is**: A CRAFT prompt template used by `plan-work.md` step 3 to turn a vague user description into a precise problem statement before research and drafting.
>
> **Why it exists**: Users often describe work loosely — "add error handling" or "fix the dashboard". Running this through CRAFT produces a structured brief (problem, outcome, acceptance criteria, scope) that gives the research step (4) precise targets and the drafting step (5) concrete material to work with.
>
> **Where it comes from**: The [CRAFT framework](../../../skills/craft/SKILL.md) (Context, Role, Action, Format, Target audience) — a meta-prompting technique for generating structured, high-quality LLM outputs.

---

Replace `[user's description]` with what the user provided:

```text
CONTEXT:
We are creating a Linear issue for a software project. The user
has described the work as: "[user's description]". This prompt
will be used to guide codebase research and issue drafting — it
needs to surface the right problem, the right scope, and the
right success criteria so the resulting issue is immediately
actionable by a developer.

ROLE:
You are a senior product engineer with 20+ years of experience
breaking down ambiguous feature requests into precise, atomic
engineering tasks. You excel at identifying the core problem
behind a request, separating must-haves from nice-to-haves,
and writing issue descriptions that a developer can start
working on without asking clarifying questions.

ACTION:
1. Restate the user's description as a clear problem statement
   — what is broken, missing, or suboptimal?
2. Identify the single most important outcome (one deliverable,
   not a bundle of changes)
3. List 2–3 acceptance criteria that define "done"
4. Flag any ambiguities or assumptions that need confirming
5. Suggest a scope boundary — what is explicitly out of scope
   for this issue?

FORMAT:
Return a structured brief matching the Linear issue template:

### Problem
What problem exists (1–2 sentences)

### Goal
Desired outcome (1 sentence)

### Scope
- Bullet list of what's included

### Out of scope
(Only if genuinely useful — omit if nothing meaningful)

### Success metric
(Only if measurable — omit if not applicable)

### Assumptions to confirm
- Bullet list of ambiguities that need resolving

TARGET AUDIENCE:
A developer who will implement this issue. They need clarity,
not context they already have from the codebase. Prefer
concrete over abstract — "the API returns 500 when X is null"
beats "improve error handling".
```
