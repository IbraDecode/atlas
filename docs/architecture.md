# Architecture

Atlas uses one portable guidance core with native adapters around it. The design avoids pretending that agent platforms share configuration formats or permission semantics.

## Components

- `core/`: shared engineering and security principles; no host-specific syntax.
- `skills/`: reusable procedures that a compatible host can load or an agent can be given directly.
- `agents/`: specialist role contracts (purpose, activation, inputs, outputs, boundaries); host adapters translate these only when needed.
- `integrations/`: guidance for external systems and research practices; not implementations of those systems.
- `adapters/`: per-host loading formats, instructions, and compatibility notes.
- `.claude/` and `.opencode/`: host-discoverable skills and specialist agent definitions for repository-local use.
- `scripts/`, `tests/`: small deterministic project validation and its tests.
- `docs/`: project architecture, standards, sources, and roadmap.

## Portable core and adapters

Core policy should exist once. An adapter may reference it, but must not silently fork or weaken it. Native config, metadata, commands, hooks, and agent/skill file formats belong in their adapter. Validate each host's behavior against its official docs and, before claiming runtime support, test it on that host.

## Current limits

Only research skill and researcher role content are included. They are not a full roster of specialist agents. The adapters are documentation, not packaged plugin/config artifacts. Roblox Studio MCP support is not implemented, and no specific server has been endorsed. There is no release or compatibility guarantee yet.
