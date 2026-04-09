# List Linear projects

Show all projects in the connected Linear workspace.

## Steps

### 1. Fetch projects

Call `list_projects` to retrieve all active projects.

### 2. Display

Present the results as a table:

| Project | Lead | Summary |
|:--------|:-----|:--------|
| Project Name | Jane Doe | One-line summary |

- If a project has no summary, show "—"
- If a project has no lead, show "—"
- Sort by most recently updated first

### 3. Summary

End with a one-line summary: "N projects found."
