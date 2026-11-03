# Sandbox Modes

The sandbox is an enforced boundary around the commands Codex runs. `read-only` lets Codex inspect files but not change them, `workspace-write` allows edits inside the workspace and routine local commands, and `danger-full-access` removes the limits on files and network. `workspace-write` is the default low-friction mode for local work. You can allow extra writable folders with `--add-dir`.

Visit the following resources to learn more:

- [@official@Sandboxing and approvals](https://learn.chatgpt.com/docs/sandboxing)
- [@article@A Deep Dive into Codex Windows Sandbox](https://jonny-johnson.medium.com/a-deep-dive-into-codex-windows-sandbox-a2489bf4ae91)
- [@article@Codex Sandbox, Explained](https://www.agent37.com/blog/codex-sandbox)