# Hooks

Hooks run your own scripts at points in Codex's lifecycle. Events include `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PermissionRequest`, `PostToolUse`, `SubagentStart`, `SubagentStop` and `Stop`. A hook receives JSON on stdin and can add context, allow or deny an action, or block a result. They are defined in `hooks.json` or in `config.toml`, and you must review and trust a hook with `/hooks` before it runs.

Visit the following resources to learn more:

- [@official@Hooks](https://learn.chatgpt.com/docs/hooks)
- [@article@Hooks vs. Skills in Codex Plugins](https://www.mindstudio.ai/blog/hooks-vs-skills-codex-plugins-deterministic-checks-never-left-to-model)
- [@article@Hooks in Codex: What They Are and How to Use](https://www.c-sharpcorner.com/article/hooks-in-codex-what-they-are-and-how-to-use?srsltid=AYCX9vJDbSkDLtY5NRYe4o1zUgQFeccfhPigZvRSYmAAt7yMbLw8KsG6)
- [@article@Codex Hooks Reference: PreToolUse, PostToolUse, Examples](https://agenticcontrolplane.com/blog/codex-cli-hooks-reference)