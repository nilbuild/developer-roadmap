# Hooks

Hooks are scripts that observe, control or extend the agent loop. You define them in `.cursor/hooks.json` for events such as `preToolUse`, `beforeShellExecution`, `afterFileEdit` and `stop`. A hook receives JSON on stdin and returns JSON on stdout, and exit code 2 blocks the action. Teams use them for formatting, audit logs and custom approval rules.

Visit the following resources to learn more:

- [@official@Hooks](https://cursor.com/docs/hooks)
- [@article@Deep Dive into the new Cursor Hooks](https://blog.gitbutler.com/cursor-hooks-deep-dive)