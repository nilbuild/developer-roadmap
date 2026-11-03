# MCP

The Model Context Protocol connects Codex to external tools and data. Each server has a `[mcp_servers.<name>]` table in `config.toml`, and it is either a local STDIO process or a remote streamable HTTP server with OAuth or a bearer token. You add servers with `codex mcp add`. Per-server and per-tool approval settings control when Codex must ask before calling a tool.

Visit the following resources to learn more:

- [@official@MCP in Codex](https://learn.chatgpt.com/docs/extend/mcp)
- [@article@OpenAI Codex CLI with the Bright Data MCP Server](https://brightdata.com/blog/ai/codex-cli-with-web-mcp)
- [@video@OpenAI Codex Tutorial #9 - MCP Servers](https://www.youtube.com/watch?v=zfYEZ3_Nnkc)