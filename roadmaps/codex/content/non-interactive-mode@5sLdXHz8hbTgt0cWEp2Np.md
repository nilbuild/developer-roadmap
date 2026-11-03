# Non-Interactive Mode

Non-interactive mode runs Codex without a person in the loop, through `codex exec` in scripts and CI. You pass a prompt as an argument or through stdin, and Codex runs the task and prints the final message. It supports JSONL output, structured output with a JSON Schema, resuming earlier runs, and read-only defaults. For code that needs more control, the Codex SDK for TypeScript and Python starts and resumes Codex threads, and the app server lets you build your own client.

Visit the following resources to learn more:

- [@official@Non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode)
- [@official@Codex SDK](https://learn.chatgpt.com/docs/codex-sdk)