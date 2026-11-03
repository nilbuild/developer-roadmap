# Manage Context

The context window is the amount of information the model can consider at once, and long chats fill it. As it fills, quality can drop because old details crowd out new ones. Compaction summarizes older context so work can continue, and in the CLI `/compact` triggers it. `/status` shows token usage, `/recap` summarizes without compacting, and starting a new chat resets the context.

Visit the following resources to learn more:

- [@official@Glossary](https://learn.chatgpt.com/docs/glossary)