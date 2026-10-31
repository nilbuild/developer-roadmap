# CI/CD

CI/CD integration runs Claude Code inside your pipelines to review pull requests, triage issues and turn requests into code changes. It is built on the CLI and Agent SDK, so a job runs `claude -p` with a prompt and a limited set of allowed tools. Claude follows your [CLAUDE.md](http://CLAUDE.md) rules, and its changes arrive as pull or merge requests that go through your normal approvals. Claude Code provides ready integrations for GitHub Actions and GitLab CI/CD.

Visit the following resources to learn more:

- [@official@Run Claude Code programmatically](https://code.claude.com/docs/en/headless)
- [@official@Claude Code GitHub Actions](https://code.claude.com/docs/en/github-actions)
- [@official@Claude Code GitLab CI/CD](https://code.claude.com/docs/en/gitlab-ci-cd)