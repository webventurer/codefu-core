# Can't we just use Lovable?

It's the first question anyone sensible asks. Lovable gets you from an idea to a running, authed, deployed web app in an afternoon — no terminal, no git, no Linear board. Stride takes longer on day one and asks you to care about atomic commits. Why wouldn't you pick Lovable?

The honest answer: **for a lot of projects, you should.** Lovable and Stride are not competitors sitting in the same square on the grid — they are two stages of the same journey. Lovable owns zero-to-one for people who don't already code. Stride takes over when the codebase grows up.

<mark>Outgrowing Lovable is a success marker, not a failure. The platform is designed to get you to a working product fast. Needing more means it worked.</mark>

## What Lovable is genuinely good at

Give it credit — the magic moment is real.

| What | Why it works |
|:-----|:-------------|
| **Prompt → running app in minutes** | A non-coder can have a deployed, authed, DB-backed web app before lunch. This is not marketing. |
| **Supabase wired in from a prompt** | Auth, schema, row-level security scaffolded without a single config file opened. |
| **Exported code is cleaner than expected** | When you connect GitHub, you get readable React components, not no-code spaghetti. |
| **Visual Edits** | Click on the rendered UI, edit it, the code updates. Figma-for-code that actually works. |
| **Non-technical reach** | Founders, designers, PMs, marketers, ops — roughly 63% of active users are not developers by trade. |

If you are a non-technical founder who needs a demo by Friday, Lovable is the right tool. Don't let anyone talk you out of it.

## Where Lovable stops scaling

The friction shows up the same way every time, regardless of who the user is.

| Signal | What it looks like |
|:-------|:-------------------|
| **The looping problem** | The agent tries to fix a bug, fails, reintroduces an old error, confidently announces it's fixed, burns credits on the loop. |
| **Broken working code** | More than half of generations either break something that was working or claim a fix without making one. |
| **Code quality doesn't scale** | Data structures are inflexible. Small feature tweaks mean rewriting large chunks. The generated code isn't built to be changed. |
| **Opaque failures** | When something goes wrong, error messages are vague. You can't always see *why*. |
| **Team collaboration is weak** | Multiple people cannot work on the same codebase at the same time in Lovable. |
| **Debugging eats the day** | When more than a third of the time is spent re-prompting rather than building, the tool is no longer paying for itself. |
| **Credit trap** | Loop bugs cost credits. Spend becomes unpredictable. |
| **Stack lock-in** | React + Vite + Tailwind + Supabase is the product. Need Next.js, a Python backend, or a different auth provider? You're exporting. |

None of these are bugs in Lovable. They are the predictable ceiling of any tool that optimises for zero-to-one speed over long-term changeability.

## The graduation moment

You will know you've hit it. It tends to look like one of these:

- The same bug re-appears for the third time after an "it's fixed" message
- You open the exported GitHub repo and realise the Lovable chat is no longer the fastest way to change it
- A second person needs to work on the code and there's nowhere for them to stand
- You're asking questions the agent can't answer — *why is this function here? what does this call?*
- You need a stack Lovable doesn't ship — a real backend, a different database, a specific auth system
- The credit bill is bigger than the value of the changes being made

At that moment, the question stops being *"can't we just use Lovable?"* and starts being *"how do we keep going without throwing this away?"*

## What Stride gives you on the other side

Stride is designed for exactly that moment. Not a replacement product — a continuation.

| What | What it does | The parallel in Lovable |
|:-----|:-------------|:-----------------------|
| **[app-starter](https://github.com/webventurer/app-starter)** | React + TypeScript + Vite + Hono + Neon + Clerk + Drizzle + shadcn/ui + Biome. Sensible defaults, every layer independently replaceable. | The same "don't make me pick a stack" energy — but yours, locally, with the seams visible. |
| **`/craft`** | Structured prompts (Context, Role, Action, Format, Target) that sharpen the ask *before* the agent starts. | Replaces the "just type what you want" chat box with a frame that the agent can actually execute against. |
| **`/linear`** | Kanban board + atomic issues synced with Claude Code. Every piece of work has a card, every card has a state. | Replaces "chat history with the agent" with a real board anyone on the team can read. |
| **`/commit`** | Four-pass atomic commits — one idea per commit, independently revertible, with a reason attached. | Replaces the monolithic Lovable → GitHub sync with a git history you can `bisect`, `blame`, and `revert` without fear. |

<mark>The starter-app borrows Lovable's lesson — sensible defaults, wired together, don't make the user choose. Then Stride adds the things that only matter once the codebase is real: atomicity, traceability, team-readable structure.</mark>

## Side by side

| Dimension | Lovable | Stride |
|:----------|:--------|:-------|
| **Optimises for** | First hour | Next six months |
| **Runs** | Browser, hosted | Locally, your machine, your infra |
| **Stack** | Fixed (React + Vite + Tailwind + Supabase) | Opinionated defaults, every layer swappable |
| **Best for** | Greenfield, solo, non-technical | Existing codebases, teams, engineers |
| **History model** | Chat messages + sync to `main` | Atomic commits, branches, PRs |
| **Collaboration** | Single-user at a time | Multi-person, Linear-tracked |
| **Agent steering** | Free-text prompts | CRAFT prompts + Linear issues |
| **Deploy** | Lovable hosting or export to Vercel | Your infra, your rules |
| **Cost shape** | Credits per message | Claude Code subscription + your cloud |
| **Ceiling** | Hits it when codebase needs real structure | Compounds as models improve |

## The migration path

If you are reading this with a Lovable project that has hit its ceiling, the path is short:

1. **Export to GitHub** — Lovable supports this directly. Your code comes out as a real React + Vite + Tailwind + Supabase repo.
2. **Point Claude Code at it** — open the repo locally, install Stride with `npx github:webventurer/stride`.
3. **Wire up Linear** — `/linear:check` confirms MCP, `/linear:plan-work` starts putting existing features onto a board.
4. **Commit discipline from here forward** — `/commit` on every change. The past is what it is; the future is atomic.

You keep the code Lovable generated. You inherit a better loop for changing it.

## So — can't we just use Lovable?

Yes, until you can't. Then Stride.

| Stage | Tool | Why |
|:------|:-----|:----|
| **Day 1** | Lovable | Fastest path from idea to running app. Nothing beats it. |
| **Day 30, still exploring** | Lovable | Keep going. You're not stuck, you're iterating. |
| **Day 30, shipping to real users** | Stride | The codebase is now a thing you need to change safely, not a prompt you're still tuning. |
| **Day 90** | Stride | Atomic history, Linear-tracked work, team collaboration. Lovable's graduation speech is behind you. |

Lovable gets you to the starting line of being a real product. Stride runs the race.

## Further reading

- [Agentic engineering](/reference/agentic-engineering) — the philosophy Stride imposes on the agent
- [Kanban process](/reference/kanban) — how Stride uses Linear to keep work atomic
- [Chris Beams commit style](/reference/commit-style) — the seven rules behind `/commit`
