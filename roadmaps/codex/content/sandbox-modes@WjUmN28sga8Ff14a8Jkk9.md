# Sandbox Modes

The sandbox is an enforced boundary around the commands Codex runs, and it works the same way in the desktop app, the CLI and the IDE extension. `read-only` lets Codex inspect files but not change them, `workspace-write` allows edits inside the workspace and routine local commands, and `danger-full-access` removes the limits on files and network. `workspace-write` is the default low-friction mode for local work, and you can allow extra writable folders with `--add-dir` or `sandbox_workspace_write.writable_roots`.

Visit the following resources to learn more:

- [@official@Sandboxing and approvals](https://learn.chatgpt.com/docs/sandboxing)