# Claude Code Adapter

This guide describes Claude Code's documented native loading formats. It does not claim that the repository is already a packaged or installed Claude Code plugin.

## Native mechanisms

Claude Code supports standalone skills, subagents, hooks, and MCP configuration; plugins can package components as one installable unit. A plugin manifest lives at `.claude-plugin/plugin.json`. Plugin components include skills, agents, hooks, and MCP servers. Plugin mechanisms are Claude Code-specific; do not assume OpenCode loads them.

## Use Atlas guidance

For manual use, point Claude Code to the relevant Atlas files in the task or copy a skill into a location documented by Claude Code. Review destinations before copying; do not overwrite existing settings, hooks, or permissions. This repository currently has no Claude Code plugin manifest or automated installer.

Current guidance files:

- Shared policy: `core/engineering-standards.md`, `core/security-policy.md`.
- Skill: `skills/roblox-research/SKILL.md`.
- Specialist role description: `agents/roblox-researcher.md`.

## Permissions and MCP

Claude Code permission controls are host features. Atlas does not enable, weaken, or validate those controls. Inspect the official permissions and MCP documentation before changing settings or connecting a server. Treat MCP tools as capable of accessing data or taking actions, and review each server before use.

## Official references

See [dated source inventory](../../docs/references.md) for plugin, skills, subagent, hooks, and MCP documentation.
