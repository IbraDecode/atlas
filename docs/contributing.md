# Contributing

Atlas repository documentation and agent instructions use clear English. Keep user-facing explanations in the user's language when appropriate.

## Conventions

- Use lowercase kebab-case for new directory and file names unless a host format requires an exact name (such as `SKILL.md`).
- Put shared rules in `core/`; add host-specific syntax only under the matching `adapters/` directory.
- Keep external-system guidance under `integrations/`; distinguish integration guidance from working implementation.
- Cite first-party sources with title, URL, and date checked. Mark uncertainty and distinguish fact from recommendation.
- Avoid credentials, unrequested dependencies, empty scaffolding, and untested compatibility claims.

## Adding components

### Skill

Add a focused folder under `skills/` with `SKILL.md`. State when to use it, procedure, output expectations, and security boundaries. When exposed natively, mirror it under `.claude/skills/` and `.opencode/skills/` using each host's documented metadata; keep instructions synchronized.

### Specialist role

Add a Markdown contract under `agents/` defining responsibility, activation conditions, inputs, outputs, boundaries, and handoff. Add host-native definitions under `.claude/agents/` or `.opencode/agents/` only with platform-specific required metadata. Do not duplicate core policy.

### Adapter

Document exact native formats and prerequisites, cite official docs, and state what is and is not tested. Never copy configuration over a user's files automatically. Add a runtime package only when it provides real value and its validation path is available.

## Validation and tests

Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v`. Add a small standard-library test for meaningful validator changes. Check `git diff --check` before proposing changes.

## Versions and releases

This repository has no formal versioning, compatibility matrix, release automation, or release guarantees yet. When releases begin, document supported host versions and migration policy before claiming compatibility. Do not create or publish releases without explicit authorization.
