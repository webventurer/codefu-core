#!/bin/bash
# UserPromptSubmit hook: inject design decision principles.
#
# Outputs the design principles on every user message so they
# stay active even in long conversations where doc context may
# get compressed.

cat "$CLAUDE_PROJECT_DIR/.claude/docs/principles/design-decisions.md"
exit 0
