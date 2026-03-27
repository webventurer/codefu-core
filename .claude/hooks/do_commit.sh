#!/bin/bash
# Wrapper for git commit — used exclusively by the /commit skill.
#
# The PreToolUse hook blocks all bare "git commit" commands.
# This script is the only sanctioned path to commit. Because the
# hook inspects the top-level Bash command (not subprocesses),
# calling this script bypasses the block cleanly.
#
# Usage: .claude/hooks/do_commit.sh -m "feat: Subject" -m "Body..."
# All arguments are forwarded to git commit.

git commit "$@"
