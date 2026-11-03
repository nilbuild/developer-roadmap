# MCP

The Model Context Protocol connects Codex to external tools and data. Each server has a `[mcp_servers.<name>]` table in `config.toml`, which the desktop app, CLI and IDE extension share. A server is either a local STDIO process or a remote streamable HTTP server with OAuth or a bearer token, and in the CLI you add one with `codex mcp add`. Per-server and per-tool approval settings control when Codex must ask before calling a tool.

Visit the following resources to learn more:

- [@official@MCP in Codex](https://learn.chatgpt.com/docs/extend/mcp)