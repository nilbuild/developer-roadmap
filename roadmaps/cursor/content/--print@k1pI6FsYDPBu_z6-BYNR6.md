# --print

`--print` (or `-p`) runs the agent non-interactively and prints the response, with access to all tools. Use it in scripts and CI. File edits are only proposed unless you also pass `--force`. In scripts, `--trust` skips the workspace trust prompt and `--approve-mcps` approves MCP servers automatically, so use both only on projects you control.

Visit the following resources to learn more:

- [@official@Headless CLI](https://cursor.com/docs/cli/headless)
- [@official@CLI parameters](https://cursor.com/docs/cli/reference/parameters)