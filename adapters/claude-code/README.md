# Claude Code Adapter

This repository includes native Claude Code skill and subagent files under `.claude/`. These use Claude Code's project-level discovery paths and reference the portable guidance in `core/` and `skills/`.

## Included native components

- `.claude/skills/roblox-research/SKILL.md` — research skill; source content mirrors `skills/roblox-research/SKILL.md`.
- `.claude/agents/roblox-researcher.md` — native subagent definition; preloads the research skill and links to shared Atlas policies.

The canonical skill content remains in `skills/`. Keep the adapter copy synchronized when changing it. The agent definition is a Claude Code native adaptation, not a cross-platform role file.

## Other native mechanisms

Claude Code can also use hooks, MCP servers, and plugins. Atlas does not install hooks or configure MCP. `.mcp.json` or permission configuration is deliberately omitted because no specific server or permission change is required. Do not add a third-party MCP configuration without reviewing its code, access scope, and behavior.

## Manual use

Open this repository as the Claude Code project. Review the active skills and agents with Claude Code's native commands. Do not copy files into user-wide settings; project-level files already scope behavior to this repository. Host permission settings remain controlled by Claude Code and user approvals.

See [official references](../../docs/references.md) for current docs.
