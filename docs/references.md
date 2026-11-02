# Official References

Access date for pages below: **2026-11-02**. Titles and behavior summaries reflect pages retrieved for this foundation. Recheck current vendor documentation before relying on version-sensitive behavior.

## Claude Code

- **Plugins overview** — https://code.claude.com/docs/en/plugins — Plugins package skills, agents, hooks, MCP servers, and other components; standalone mechanisms also exist.
- **Plugin components** — https://code.claude.com/docs/en/plugins/components — Component locations and supported types.
- **Skills** — https://code.claude.com/docs/en/skills — Native skill format and loading.
- **Subagents** — https://code.claude.com/docs/en/sub-agents — Native subagent definitions and delegation.
- **Hooks guide** — https://code.claude.com/docs/en/hooks-guide — Lifecycle hook configuration and behavior.
- **MCP** — https://code.claude.com/docs/en/mcp — MCP server connections and host behavior; project configuration uses `.mcp.json` with an `mcpServers` object.

Claude Code project skills use `.claude/skills/<name>/SKILL.md`; skill frontmatter is optional, with `description` recommended. Project subagents use `.claude/agents/<name>.md` with `name` and `description` required; agents may preload skills through `skills` frontmatter.

## OpenCode

- **Config** — https://opencode.ai/docs/config/ — JSON/JSONC configuration and config precedence.
- **Agents** — https://opencode.ai/docs/agents/ — Agent definitions in config or Markdown.
- **Claude Code subagents** — https://code.claude.com/docs/en/sub-agents — Project subagent definition format and skill preloading.
- **Agent Skills** — https://opencode.ai/docs/skills/ — Skill layout, frontmatter, and paths.
- **Commands** — https://opencode.ai/docs/commands/ — Native commands.
- **Plugins** — https://opencode.ai/docs/plugins/ — Native plugin mechanisms.
- **MCP servers** — https://opencode.ai/docs/mcp-servers/ — Local and remote MCP configuration.

OpenCode project skills are discovered in `.opencode/skills/<name>/SKILL.md`; frontmatter requires `name` and `description`, and `name` must match the folder. Project agent files use `.opencode/agents/<name>.md` with `description` frontmatter; `mode` selects agent mode.

## Roblox and Luau

- **Roblox Studio** — https://create.roblox.com/docs/studio — Official Studio overview.
- **Get Studio** — https://create.roblox.com/docs/studio/setup — Studio setup.
- **Script editor** — https://create.roblox.com/docs/studio/script-editor — Editor features.
- **Studio testing modes** — https://create.roblox.com/docs/studio/testing-modes — Testing in Studio.
- **Luau** — https://create.roblox.com/docs/luau — Official Luau overview.

The Creator Hub Studio page retrieved here does not specify an official Roblox Studio MCP. This is a limitation of the checked page, not proof that no official MCP exists.

## Model Context Protocol

- **Specification (2025-11-25)** — https://modelcontextprotocol.io/specification/2025-11-25 — Protocol architecture, messages, capabilities, and security principles.

## Verification boundaries

No specific Roblox Studio MCP implementation, Roblox-owned MCP endpoint, or live Studio connection was verified. Atlas does not claim one exists or is supported. Host configuration details are documented separately and must be checked against the linked vendor docs before use.
