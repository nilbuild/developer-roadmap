# Modes

Modes set the level of autonomy Claude Code has in a session. Manual mode asks before edits and shell commands, Accept Edits mode approves file changes and common filesystem commands automatically, and Plan mode keeps Claude read-only while it outlines a strategy. Auto mode has a classifier model check actions in the background instead of prompting you, dontAsk denies every call that would prompt, and Bypass Permissions removes all checks. You switch between modes during a session with the mode shortcut, or you start in one with the --permission-mode flag.

Visit the following resources to learn more:

- [@official@Configure permissions](https://code.claude.com/docs/en/permissions)
- [@article@A complete guide to Claude Code permissions](https://www.eesel.ai/blog/claude-code-permissions)
- [@video@Claude Code Tutorial #4 - Tools & Permissions](https://www.youtube.com/watch?v=TU0ZcDFq0e0)