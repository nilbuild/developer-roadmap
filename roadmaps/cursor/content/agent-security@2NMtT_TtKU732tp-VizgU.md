# Agent Security

Agents can act in unexpected ways because of prompt injection or model mistakes, so Cursor puts guardrails around what they can do. Sensitive actions need your approval by default, including terminal commands, MCP connections and each MCP tool call unless you allowlist it. Reading files and searching code need no approval, while edits to config files do, and other edits are saved right away, so keep your work in version control. Network access from the agent's tools is limited by default to GitHub, direct link retrieval and web search providers.

Visit the following resources to learn more:

- [@official@Agent security](https://cursor.com/docs/agent/security)
- [@official@Run modes](https://cursor.com/docs/agent/security/run-modes)
- [@official@Security and privacy](https://cursor.com/help/security-and-privacy/privacy)