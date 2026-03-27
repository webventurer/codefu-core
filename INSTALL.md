# Install

```bash
pnpm dlx @codefu/core
```

Or with npx:

```bash
npx @codefu/core
```

This copies skills, commands, and hooks into your project's `.claude/` directory and merges hook config into your existing `settings.json`.

## Requirements

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI
- [Linear MCP server](https://www.npmjs.com/package/@anthropic-ai/linear-mcp-server) (for /linear commands)
- [GitHub CLI](https://cli.github.com/) (`gh`) for PR operations

## Python tools

The cross-model feedback loop in `/linear:plan-work` uses a Python script to send drafts to ChatGPT via [OpenRouter](https://openrouter.ai/). Dependencies are managed inline with [uv](https://docs.astral.sh/uv/) — no venv or `pip install` needed.

```bash
brew install uv                # macOS
# or: curl -LsSf https://astral.sh/uv/install.sh | sh
```

Add your OpenRouter API key to `~/.env`:

```
OPEN_ROUTER_API_KEY=sk-or-...
```

Get your key at [openrouter.ai/keys](https://openrouter.ai/keys).

## What gets installed

```
.claude/
├── skills/commit/           ← skill + workflow + reference docs
├── commands/linear/         ← 5 commands + reference docs
├── hooks/                   ← commit wrapper + bare-commit blocker
└── docs/                    ← supporting patterns and concepts
```

The install script merges hook config into your existing `.claude/settings.json` — it won't overwrite your other settings.
