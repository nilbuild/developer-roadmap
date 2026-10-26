# Permission Modes

Permission modes control how much Claude Code can do without asking you first. Manual (default) only runs reads without approval, acceptEdits also allows file edits and common filesystem commands, and plan restricts Claude to research and planning. auto lets a separate classifier model review each action and block risky ones, and it is the built-in starting mode in interactive sessions on recent versions. dontAsk denies anything that would prompt, and bypassPermissions runs everything and should only be used in isolated containers or VMs.

Visit the following resources to learn more:

- [@official@Permission modes](https://code.claude.com/docs/en/permissions#permission-modes)
- [@article@A complete guide to Claude Code permissions](https://www.eesel.ai/blog/claude-code-permissions)
- [@article@3 Things You Must Know About /permissions in Claude Code](https://wmedia.es/en/tips/claude-code-permissions-3-key-concepts)
- [@article@Claude Code on Loop: The Ultimate YOLO Mode](https://mfyz.com/claude-code-on-loop-autonomous-ai-coding/)
- [@video@Claude Code Tutorial #4 - Tools & Permissions](https://www.youtube.com/watch?v=TU0ZcDFq0e0)