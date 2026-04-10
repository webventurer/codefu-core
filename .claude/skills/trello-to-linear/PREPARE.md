# Prepare Trello to Linear session

Create these documents at the start of each session.

Both are throwaway documents — start fresh each session.

---

## Inputs needed

<mark>**Ask each question below one at a time using `AskUserQuestion`. Do not proceed until all answers are collected.**</mark>

### Step 1: Ask for Trello workspace

Ask: *"Which Trello workspace are you migrating from?"*

List available workspaces via `mcp__trello__list_boards` and extract unique organisation names. Set the active workspace with `mcp__trello__set_active_workspace`.

### Step 2: Ask for Trello board

Ask: *"Which Trello board do you want to migrate?"*

List boards in the selected workspace via `mcp__trello__list_boards` and present board names as options. Record the board ID.

### Step 3: Ask for Linear workspace

Ask: *"Which Linear workspace are you migrating TO?"*

Offer the available Linear MCP servers as options (e.g. `linear-personal`, `linear-wordtracker`).

### Step 4: Ask for Linear project

Use the target MCP server to call `list_projects` and present the project names as options.

Ask: *"Which Linear project should receive the migrated cards? (Select 'Other' to create a new one)"*

Record the project name and its team.

### Step 5: Confirm

Display a summary table and ask for confirmation before proceeding:

| | Source | Value |
|:--|:-------|:------|
| **Trello workspace** | *answer 1* | |
| **Trello board** | *answer 2* | |
| **Linear workspace** | *answer 3* | |
| **Linear team** | *from step 4* | |
| **Linear project** | *answer 4* | |

Ask: *"Does this look correct?"*

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
