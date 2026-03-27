# Project documentation paths

Standard locations for project documentation in consuming repos. Check for these paths — only use what exists.

## Always check

| Doc | Path |
|:----|:-----|
| Project instructions | `CLAUDE.md` |
| Project overview | `README.md` |
| Build targets | `Makefile` |

## Standalone docs

| Doc | Path |
|:----|:-----|
| Tech stack | `stack.md` |
| Technical specification | `tech-spec.md` |

## Documentation directories

| Directory | Contains |
|:----------|:---------|
| `docs/architecture/` | Architecture decisions, system design |
| `docs/engineering/` | Coding standards, development guides |
| `docs/features/` | Feature specifications and requirements |
| `docs/process/` | Workflows, team processes |

## May also be available

| Roadmap | `roadmap.md` |
| Principles | `principles.md` |

## Discovery

These standalone docs may also live in non-standard locations (e.g. `docs/stack.md`, `config/stack.md`). If not found at root, run a quick glob for `**/stack.md`, `**/stack-review.md`, `**/roadmap.md`, `**/principles.md` to catch them wherever they are.
