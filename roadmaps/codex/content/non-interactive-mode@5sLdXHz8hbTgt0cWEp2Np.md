# Non-Interactive Mode

Non-interactive mode runs Codex without the terminal UI through `codex exec`. You pass a prompt as an argument or through stdin, and Codex runs the task and prints the final message. It supports JSONL output, structured output with a JSON Schema, resuming earlier runs, and read-only defaults. In CI, set `CODEX_API_KEY` only for the command that needs it.

Visit the following resources to learn more:

- [@official@Non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode)
- [@article@Codex Exec: Run OpenAI Codex Safely from the Terminal](https://www.deployhq.com/blog/codex-exec-terminal-guide)
- [@article@Codex Exec in CI: Practical Guide to Headless OpenAI Agents](https://www.developersdigest.tech/blog/codex-exec-ci-headless-guide)