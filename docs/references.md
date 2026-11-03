# Official References

Access date for pages below: **2026-11-02**. Titles and summaries reflect pages retrieved for this foundation and adapter review. Recheck vendor docs before relying on version-sensitive behavior.

Observed development environment: Claude Code CLI **2.1.316**; OpenCode CLI unavailable. These are observations, not supported-version guarantees. Claude CLI print output did not prove project skill or agent discovery; neither host's adapter runtime discovery is claimed as tested.

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
- **Roblox Studio MCP server** — https://create.roblox.com/docs/studio/mcp — Built-in local Studio MCP server, client setup, tool categories, and security note that clients can read and change open places.

## Roblox Studio Agent Plugin

- **Plugin README** — https://github.com/Roblox/roblox-studio-agent-plugin/blob/main/README.md — Setup instructions; the repository describes itself as Roblox's official plugin.
- **Claude Code plugin manifest** — https://github.com/Roblox/roblox-studio-agent-plugin/blob/main/.claude-plugin/plugin.json — At review, reported version `0.2.2`, author `Roblox`, and OS-specific MCP launcher commands; manifest assertions are not runtime verification.
- **Install guide** — https://github.com/Roblox/roblox-studio-agent-plugin/blob/main/skills/roblox-get-started/references/install.md — Repository-described installer approval and OS-specific signature checks.
- **Connect guide** — https://github.com/Roblox/roblox-studio-agent-plugin/blob/main/skills/roblox-get-started/references/connect.md — Client configuration and Studio Quick Connect instructions; configuration may be written by Studio or a client command.
- **Getting-started skill** — https://github.com/Roblox/roblox-studio-agent-plugin/blob/main/skills/roblox-get-started/SKILL.md — Setup flow and approval instructions.
- **Security notes** — https://github.com/Roblox/roblox-studio-agent-plugin/blob/main/skills/roblox-get-started/SECURITY.md — Installer/security assertions as described by the repository; no AI-provider retention or training details.
- **Marketplace manifest** — https://github.com/Roblox/roblox-studio-agent-plugin/blob/main/.agents/plugins/marketplace.json — Marketplace metadata; does not establish a separate marketplace version.
- **Releases** — https://github.com/Roblox/roblox-studio-agent-plugin/releases — No releases listed when checked; not evidence of compatibility guarantees.

## Model Context Protocol

- **Specification (2025-11-25)** — https://modelcontextprotocol.io/specification/2025-11-25 — Protocol architecture, messages, capabilities, and security principles.

## Verification boundaries

Roblox Creator Hub documents a Studio MCP server. No Atlas installation, live Studio connection, tool invocation, or publish test was performed. The plugin and Studio server are separate components. Plugin compatibility with a particular host/version and provider-side data practices must be verified from current sources before relying on them.
