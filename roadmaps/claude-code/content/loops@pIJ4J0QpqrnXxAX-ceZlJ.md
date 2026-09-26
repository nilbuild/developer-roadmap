# Loops

`/loop` is a Claude Code command that reruns a prompt on a repeating interval within an open session, useful for polling a deployment or babysitting a pull request. Giving it an interval and a prompt runs on a fixed schedule, giving just a prompt lets Claude pick the interval dynamically each iteration, and giving neither runs a built-in maintenance prompt that checks unfinished work and pending PR comments. Loops are session-scoped and expire after seven days, and can be stopped early by pressing Es

Visit the following resources to learn more:

- [@article@Run a prompt repeatedly with /loop](https://code.claude.com/docs/en/scheduled-tasks#run-a-prompt-repeatedly-with-/loop)
- [@article@What Is the Claude Code /loop Command?](https://www.mindstudio.ai/blog/what-is-claude-code-loop-command-recurring-tasks)
- [@video@Stop Prompting Claude. Start Loop Engineering.](https://www.youtube.com/watch?v=YAS4ojuhbW4)
- [@video@Claude Code Loops in 7 Minutes](https://www.youtube.com/watch?v=pWZh37iRnDA)