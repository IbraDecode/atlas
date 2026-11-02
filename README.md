# Atlas for Roblox

Atlas is a modular development toolkit that gives existing coding agents reusable Roblox engineering guidance, research practices, and specialist workflows.

Atlas is **not** an AI application, chatbot, SaaS product, Roblox experience, or Roblox Studio replacement. It does not call an AI API, publish experiences, or implement an MCP server.

## What exists now

- Shared engineering and security guidance in `core/`.
- One reusable Roblox research skill in `skills/roblox-research/`.
- One specialist definition in `agents/`.
- Separate Claude Code and OpenCode native skill/agent files in `.claude/` and `.opencode/`, with adapter guidance in `adapters/`.
- Roblox Studio's documented local MCP server and safety guidance in `integrations/roblox-studio/`; no server or client plugin is installed or bundled.
- A standard-library validator for required files, adapter metadata, skill-copy parity, and local Markdown links.

These are initial foundations, not a complete toolkit. No native plugin package, installer, Roblox Studio MCP connection, Roblox Studio Agent Plugin installation, or additional specialist agents are included yet.

## Architecture

`core/` holds agent-neutral principles. `skills/` contains reusable procedures, and `agents/` describes task-focused roles. `integrations/` documents external systems and research practice. `adapters/` documents how each coding agent loads or uses Atlas content through its own native mechanisms; platform configurations are not interchangeable. See [architecture](docs/architecture.md).

## Setup and use

No installer exists. The repository-local `.claude/` and `.opencode/` skill/agent files are intended for their respective hosts when opened at this repository. Review behavior before use; no user-wide settings or permissions are changed. See [Claude Code](adapters/claude-code/README.md) and [OpenCode](adapters/opencode/README.md).

## Security

Follow [Atlas security policy](core/security-policy.md). Review external MCP servers before connecting them. Atlas documents safeguards; it does not enforce host permission controls. Never commit credentials or authorize publishing or destructive actions without explicit approval.

## Validate

Running Atlas validation requires Python 3.10+; no third-party packages. This is the project's current tooling minimum, not a guarantee that older versions work.

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

The validator checks required files, required native adapter frontmatter keys, parity of mirrored skill instructions, and relative Markdown links. It does not fully parse YAML, fetch URLs, prove host runtime discovery, or test a Roblox Studio connection.

## Contributing

Read [contribution guidance](docs/contributing.md). Use English for repository documentation and agent instructions. Run validation and tests before submitting changes. Python 3.10+ is the current minimum for validation tooling; supported Claude Code and OpenCode versions remain unverified, with no release or compatibility guarantees yet.

## Next priorities

See [roadmap](docs/roadmap.md) for staged work and deferred features.
