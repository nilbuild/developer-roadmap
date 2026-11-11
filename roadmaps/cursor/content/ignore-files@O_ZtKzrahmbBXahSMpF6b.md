# Ignore Files

A `.cursorignore` file in the project root lists files and folders that Cursor should keep out of AI context. Cursor already skips `.env` files, `.git/` and lock files, and it respects `.gitignore`. Ignored files are blocked from the agent, but terminal commands and MCP tools run outside these controls and may still read them.

Visit the following resources to learn more:

- [@official@Ignore files](https://cursor.com/help/customization/ignore-files)