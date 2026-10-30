# Hooks

Hooks run your own scripts at points in Codex's lifecycle. Events include `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PermissionRequest`, `PostToolUse`, `SubagentStart`, `SubagentStop` and `Stop`. A hook receives JSON on stdin and can add context, allow or deny an action, or block a result. They are defined in `hooks.json` or in `config.toml`, and you must review and trust a hook with `/hooks` before it runs.

Visit the following resources to learn more:

- [@official@Hooks](https://learn.chatgpt.com/docs/hooks)