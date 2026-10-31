# claude --bare -p

`--bare` is a minimal startup mode for scripted calls with `-p`. It skips auto-discovery of hooks, skills, custom commands, subagents, installed plugins, MCP servers, auto memory and [CLAUDE.md](http://CLAUDE.md), so a run starts faster and behaves the same on every machine. You pass any context you need with flags such as `--settings`, `--mcp-config` or `--append-system-prompt`. Bare mode never reads OAuth credentials, so it needs an `ANTHROPIC_API_KEY` or a provider credential. The docs recommend it for CI and scripts, and say it will become the default for `-p` in a future release.

Visit the following resources to learn more:

- [@official@Run Claude Code programmatically](https://code.claude.com/docs/en/headless)