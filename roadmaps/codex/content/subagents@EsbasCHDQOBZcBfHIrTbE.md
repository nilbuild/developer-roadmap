# Subagents

Subagents are specialized agents that Codex spawns to work in parallel and report back. They keep noisy output such as logs and exploration notes out of the main thread. Built-in agents are `default`, `worker` and `explorer`, and you can ask Codex directly to spawn them. They suit read-heavy work like exploration and triage, and they use more tokens than a single agent. Write-heavy parallel work can cause edit conflicts.

Visit the following resources to learn more:

- [@official@Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)