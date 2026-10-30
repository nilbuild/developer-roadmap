# exec

`codex exec` runs Codex non-interactively, so you can use it in scripts and CI. Progress goes to stderr and the final message goes to stdout, which makes it easy to pipe. Useful flags include `--json` for JSONL events, `--output-schema` for structured results and `-o` to save the last message to a file. Runs are read-only by default unless you pick another sandbox.

Visit the following resources to learn more:

- [@official@Non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode)