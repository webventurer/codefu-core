# Prepare Trello to Linear session

Create these documents at the start of each session.

Both are throwaway documents — start fresh each session.

---

## Inputs needed

Before starting, collect:

| Input | How to get it |
|:------|:-------------|
| Trello board | Name or ID. If a name is given, resolve the ID via `mcp__trello__list_boards` |
| Trello workspace | Organisation name in Trello (e.g. "Wordtracker"). Use `mcp__trello__set_active_workspace` if needed |
| Linear project name | The project where issues were migrated (e.g. "What's next (archive)") |
| Linear team name | The team in the Linear workspace (e.g. "Wordtracker") |
| Output directory | Where to write export files (default: `/tmp/trello-export`) |

---

## Session workflow

Each phase follows this sequence:

1. **Run** — execute the script for the current phase
2. **Verify** — check the output (counts, spot-checks)
3. **Log** — update the session log
4. **Proceed** — move to the next phase

---

## SESSION-LOG.md

Progress log in the output directory:

```markdown
# Trello to Linear migration

**Board**: [board name] ([board ID])
**Linear project**: [project name]
**Started**: [timestamp]

## Phase 1: Export
- Cards exported: [N]
- Cards with descriptions: [N]
- Cards with comments: [N]

## Phase 2: Match
- Exact matches: [N]
- Fuzzy matches: [N]
- Creates (no match): [N]

## Phase 3: Upsert
- Updated: [N]
- Created: [N]
- Skipped (already had description): [N]
- Failed: [N]
```

---

## Cleanup

After the session ends:

```bash
rm SESSION-LOG.md
```

The export files in `/tmp/trello-export/` can be kept as a backup or deleted.
