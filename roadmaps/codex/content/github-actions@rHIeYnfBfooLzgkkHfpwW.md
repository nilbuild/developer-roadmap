# GitHub Actions

The `openai/codex-action@v1` action installs the Codex CLI and runs `codex exec` inside a GitHub workflow. You give it a prompt or a prompt file, a sandbox setting and your API key from a repository secret, and it returns the final message as an output. By default only users with write access can trigger it, and the docs advise sanitizing pull request text and running Codex as the last step of a job.

Visit the following resources to learn more:

- [@official@Codex GitHub Action](https://learn.chatgpt.com/docs/github-action)
- [@article@How to Set Up AI Code Review in GitHub Actions](https://www.samuelfaj.com/en/blog/how-to-set-up-ai-code-review-in-github-actions/)
- [@video@AI Fixed My Code While I Slept! (OpenAI Codex + Github Actions)](https://www.youtube.com/watch?v=y6JUy244oso)