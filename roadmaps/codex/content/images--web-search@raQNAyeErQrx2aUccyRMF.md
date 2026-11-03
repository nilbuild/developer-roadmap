# Images & Web Search

Codex accepts images and can search the web. You can add screenshots, designs or diagrams by pasting into the composer, attaching them on the web, holding Shift while dragging a file into the desktop app or IDE extension, or using `--image` in the CLI. Web search uses a cached index by default in local sessions, and `web_search = "live"` or `--search` switches to live results. Treat all web results as untrusted input, because live pages can contain prompt injection.

Visit the following resources to learn more:

- [@official@Image inputs](https://learn.chatgpt.com/docs/image-inputs)
- [@official@Web search](https://learn.chatgpt.com/docs/web-search)