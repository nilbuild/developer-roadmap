# Manage Context

The context window is the amount of information the model can consider at once. Long sessions fill it, and quality can drop as old details crowd out new ones. Compaction summarizes older context so work can continue, and `/compact` triggers it. `/status` shows token usage, `/recap` summarizes without compacting, and `/new` starts clean.

Visit the following resources to learn more:

- [@official@Prompting](https://learn.chatgpt.com/docs/prompting#context)
- [@official@Managing the context window](https://developers.openai.com/api/docs/guides/conversation-state?api-mode=responses#managing-the-context-window)
- [@article@Codex Context Window: Limits, Compaction, and AGENTS.md](https://iceberglakehouse.com/posts/2026-03-context-openai-codex/)