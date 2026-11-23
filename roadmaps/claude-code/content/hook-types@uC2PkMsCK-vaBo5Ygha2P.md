# Hook Types

Claude Code supports five hook handler types. Command hooks run a shell script and use exit codes to allow or block an action. HTTP hooks send the event as JSON to a URL, and MCP tool hooks call a tool on a connected MCP server. Prompt hooks ask a Claude model for a single yes/no judgement, while agent hooks start a subagent that can read files and search code before deciding. Command, HTTP and MCP tool hooks also accept "onFailure": "block", which stops the action if the hook itself fails instead of letting it continue.

Visit the following resources to learn more:

- [@official@Hook Types](https://code.claude.com/docs/en/hooks)
- [@official@Prompt-based hooks](https://code.claude.com/docs/en/hooks-guide#prompt-based-hooks)
- [@official@Agent-based hooks](https://code.claude.com/docs/en/hooks-guide#agent-based-hooks)
- [@official@Automate workflows with hooks](https://code.claude.com/docs/en/hooks-guide)