# OpenCode Adapter

This repository includes native OpenCode skill and subagent files under `.opencode/`. These formats are separate from Claude Code agent definitions.

## Included native components

- `.opencode/skills/roblox-research/SKILL.md` — native discoverable skill, with required OpenCode `name` and `description` frontmatter.
- `.opencode/agents/roblox-researcher.md` — native subagent definition, using OpenCode `description` and `mode` frontmatter.

Canonical portable skill instructions remain in `skills/roblox-research/SKILL.md`; keep the native copy synchronized. Shared policies are referenced in `core/` rather than copied into the adapter files.

## Verification status

The files follow documented OpenCode project paths and frontmatter requirements. OpenCode CLI was not installed in the development environment, so runtime discovery and compatibility remain unverified.

## Other native mechanisms

OpenCode supports project config, commands, plugins, and MCP servers. Atlas does not configure these because no external server or behavior is needed now. Review permissions and tool access before adding configuration. Do not commit secrets.

See [official references](../../docs/references.md) for current docs.
