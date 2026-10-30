# GitHub Actions

The `openai/codex-action@v1` action installs the Codex CLI and runs `codex exec` inside a GitHub workflow. You give it a prompt or a prompt file, a sandbox setting and your API key from a repository secret, and it returns the final message as an output. By default only users with write access can trigger it, and the docs advise sanitizing pull request text and running Codex as the last step of a job.

Visit the following resources to learn more:

- [@official@Codex GitHub Action](https://learn.chatgpt.com/docs/github-action)