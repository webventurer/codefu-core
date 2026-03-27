# codefu-core

Claude Code skills for **atomic commits** and **Linear workflow**.

## Install

```bash
pnpm dlx @codefu/core
```

Or with npx:

```bash
npx @codefu/core
```

This copies skills, commands, and hooks into your project's `.claude/` directory and merges hook config into your existing `settings.json`.

## What you get

### /commit — atomic git commits

A four-pass methodology that separates content decisions from formatting standards:

1. **Pre-flight** — fix formatting, identify atomic changes
2. **Content** — stage selectively, verify one logical change
3. **Standards** — verify message format against checklists
4. **Post-commit** — verify atomicity after committing

### /linear — Linear workflow

Five commands that cover the full development cycle:

| Command | What it does |
|:--------|:-------------|
| `/linear:start` | Branch, implement, PR — full cycle from a Linear issue |
| `/linear:plan-work` | Research a problem and create a Linear issue |
| `/linear:fix` | Address PR review feedback |
| `/linear:finish` | Merge approved PR and close the issue |
| `/linear:next-steps` | Review priorities and recommend next work |

## Requirements

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI
- [Linear MCP server](https://www.npmjs.com/package/@anthropic-ai/linear-mcp-server) (for /linear commands)
- [GitHub CLI](https://cli.github.com/) (`gh`) for PR operations

## What gets installed

```
.claude/
├── skills/commit/           ← skill + workflow + reference docs
├── commands/linear/         ← 5 commands + reference docs
├── hooks/                   ← commit wrapper + bare-commit blocker
└── docs/                    ← supporting patterns and concepts
```

The install script merges hook config into your existing `.claude/settings.json` — it won't overwrite your other settings.

## License

MIT
