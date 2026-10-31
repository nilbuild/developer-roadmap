# claude --teleport

`claude --teleport` pulls a cloud session into your local terminal. Claude Code checks that you are in a checkout of the same repository, fetches and checks out the session's branch, and loads the full conversation history. Without an ID it opens an interactive session picker, and `claude --teleport <session-id>` resumes a specific session. You need a [claude.ai](http://claude.ai) login, a clean git state (it offers to stash your changes) and a branch that was pushed. The terminal gets its own copy of the session, so new work there does not appear in the cloud session.

Visit the following resources to learn more:

- [@official@Move tasks between terminal and cloud](https://code.claude.com/docs/en/claude-code-on-the-web#move-tasks-between-terminal-and-cloud)
- [@official@CLI reference](https://code.claude.com/docs/en/cli-reference)