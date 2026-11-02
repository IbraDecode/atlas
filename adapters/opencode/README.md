# OpenCode Adapter

This guide describes OpenCode's native mechanisms independently of Claude Code. It does not claim OpenCode supports Claude Code plugins or their full feature set.

## Native mechanisms

OpenCode configuration supports JSON and JSONC. Agent definitions can be provided in `opencode.json` or Markdown files under `.opencode/agents/`. Skills use a `SKILL.md` file under `.opencode/skills/<name>/`, with required `name` and `description` frontmatter. OpenCode also documents native commands, plugins, and MCP server configuration; consult current docs before authoring those formats.

## Use Atlas guidance

Read the shared policies and select applicable Atlas skill guidance manually. The current `skills/roblox-research/SKILL.md` is reusable content, not an installed OpenCode skill; copy it to the native layout only after checking frontmatter/name requirements and destination contents. `agents/roblox-researcher.md` is a portable role description, not a native OpenCode agent file. No OpenCode configuration, plugin, installer, or permissions file is included in this phase.

## MCP and permissions

OpenCode's MCP configuration and tool permissions are host-specific. Review official documentation and the server itself before connecting. Never place secrets in committed config; use environment variables or host-supported secret handling. Do not assume a server's tools are read-only.

## Official references

See [dated source inventory](../../docs/references.md) for OpenCode config, agents, skills, commands, plugins, and MCP documentation.
