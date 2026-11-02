# Engineering Standards

Atlas guidance is portable by default. Keep host-specific syntax and behavior in `adapters/`; do not assume one agent's feature exists in another.

## Roblox and Luau work

- Verify engine APIs, behavior, and platform constraints against current Roblox Creator Hub documentation.
- Prefer Luau and Roblox-native patterns. State assumptions about replication, authority, lifecycle, and data persistence.
- Separate client presentation/input from server-authoritative state changes. Treat client input and remote-event payloads as untrusted.
- Keep changes scoped; explain trade-offs that affect performance, reliability, or player experience.
- Do not invent APIs or claim code was executed in Studio when it was not.

## Sources and claims

- Prefer first-party documentation for platform behavior; cite title and URL for nontrivial or time-sensitive claims.
- Distinguish verified facts, recommendations, and unknowns.
- When sources conflict or are unavailable, report that limitation instead of silently guessing.

## Changes and checks

- Inspect existing files and local changes before editing; preserve user work.
- Validate inputs at trust boundaries and handle failures that could lose data.
- Run relevant checks and report actual results. Do not state that code or integration was tested when it was only reviewed.
- Avoid unnecessary dependencies, abstraction, and generated scaffolding.
