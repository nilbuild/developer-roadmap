# GitHub Actions

You can run Cursor CLI inside a GitHub Actions workflow to review code, fix lint errors or update docs automatically. The workflow installs the CLI, adds it to the path and runs `agent -p` with `CURSOR_API_KEY` stored as a repository secret. Restricted autonomy, where CI handles commits and pushes, is recommended for production.

Visit the following resources to learn more:

- [@official@GitHub Actions](https://cursor.com/docs/cli/github-actions)