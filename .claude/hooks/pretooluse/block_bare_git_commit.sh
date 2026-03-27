#!/bin/bash
# PreToolUse hook: block ALL bare git commit commands.
#
# All commits must go through the /commit skill, which uses
# .claude/hooks/do_commit.sh instead of git commit directly.
# The hook only sees the top-level Bash command, so the wrapper
# script's internal git commit is invisible to it.
#
# Receives JSON on stdin with tool_input.command. Exits 0 to allow,
# exits 2 to block with a message.

COMMAND=$(jq -r '.tool_input.command // ""')

echo "$COMMAND" | grep -qE '^\s*git\s+commit\b' || exit 0

cat <<EOF
BLOCKED: bare "git commit" is not allowed.

You MUST invoke the /commit skill using the Skill tool before committing.
Do not call do_commit.sh directly — follow the four-pass workflow first.
EOF
exit 2
