# Roblox Studio Integration

Atlas documents supported connection concepts and safety boundaries; it does not implement an MCP server, install a client plugin, or configure host permissions.

## Official Studio MCP

Roblox Creator Hub documents an MCP server built into Roblox Studio. The server runs locally and communicates with compatible AI clients over stdio, connecting clients to the currently open Studio session. Studio exposes controls to enable the server and client setup paths such as Quick connect or manual configuration. Exact support and config differ by client; follow current first-party instructions for the chosen client and Studio version.

The official documentation lists tools across these categories:

- Script read, search, and multi-edit.
- Data-model search and inspection.
- Luau execution.
- Asset search, generation, insertion, upload, and storage.
- Play controls, Studio state, console output, and screenshots.
- Simulated keyboard, mouse, and character input.
- Documentation/skill retrieval and Studio session listing.

This tool surface can read and change content in an open place. In particular, Luau execution, multi-edit, asset upload/insertion, play controls, and simulated input can have consequential effects. Connect only clients you trust; review tool calls, protect valuable places with backups, and first test in a disposable experience. Atlas does not configure access restrictions or guarantee a read-only mode.

## Roblox Studio Agent Plugin

Roblox hosts [`roblox-studio-agent-plugin`](https://github.com/Roblox/roblox-studio-agent-plugin) in its GitHub organization. Its README describes it as Roblox's official plugin for AI assistants and gives setup instructions for supported clients. Attribute that official-status statement to the repository; do not treat GitHub organization ownership alone as proof of every security, compatibility, or maintenance claim.

The plugin is a client-side setup/instruction package for Studio's built-in MCP server; it is distinct from the Studio MCP server itself. The repository security note describes user-approved installer actions and signature verification for Roblox-hosted downloads. The reviewed note does not establish AI-provider data handling, retention, or training behavior. The releases page currently lists no releases, so no release-based compatibility guarantee is available from that page.

No plugin installation, server connection, or Studio session was performed for Atlas. This repository does not require or bundle the plugin.

## Review before connection

1. Verify current official Studio setup and the target client's native MCP configuration.
2. Confirm server command/transport and inspect every tool exposed to the agent.
3. Treat all project edits, code execution, asset operations, uploads, and simulated inputs as potentially consequential; require user approval where appropriate.
4. Use minimum necessary access, protect or back up the place, and test in a disposable/local experience first.
5. Keep credentials out of repository files and logs. Do not claim private-data guarantees unless the relevant client/provider documents them.
6. Re-check compatibility, security notes, and release status before updates; they can change independently of Atlas.

## Scope and claims

The MCP server is a Roblox Studio feature documented by Roblox. Atlas provides guidance only. No live Studio connection, tool invocation, plugin installation, or publishing test has been performed.
