# Roblox Studio Integration

Atlas documents how coding agents may be connected to Roblox Studio; it does not implement Studio integration or bundle an MCP server.

## Verified scope

Roblox Creator Hub documents Studio, script editing, testing modes, collaboration, and Luau. The official Studio and Luau pages checked for this foundation do not specify a Roblox-owned Studio MCP server or its configuration. This does not prove no official integration exists elsewhere or later; current status remains unverified.

MCP is a protocol, not an implementation. Third-party Roblox Studio MCP projects may differ in ownership, capabilities, transport, permissions, and maintenance. Do not label one official without a Roblox source confirming it.

## Before connecting any MCP server

1. Identify its maintainer and repository or distribution source.
2. Inspect implementation, dependencies, releases, and issue history.
3. Review tools, file/data access, network behavior, and any ability to edit or publish.
4. Check the target host's current MCP configuration and permission behavior.
5. Start with the minimum access needed; request explicit approval for edits, publishing, or external effects.
6. Never place credentials in this repository. Prefer host-managed environment variables or secret handling.
7. Test in a disposable/local experience before using a live project; do not claim a test passed unless run.

No MCP endpoint, executable, or server configuration is prescribed here because no specific compatible implementation has been verified.
