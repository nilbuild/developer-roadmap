# Custom Agents

Custom agents are subagents you define yourself in a standalone TOML file. Put them in `~/.codex/agents/` for personal use or `.codex/agents/` for a project. Each file needs a `name`, a `description` and `developer_instructions`, and it can set a model and reasoning effort. A custom agent with the same name as a built-in one takes precedence. Custom agents inherit the parent's sandbox and approval settings and cannot override them.

Visit the following resources to learn more:

- [@official@Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)