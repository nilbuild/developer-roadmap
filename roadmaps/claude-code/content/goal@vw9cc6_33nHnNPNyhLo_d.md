# /goal

`/goal` sets a completion condition, and Claude keeps working turn after turn until the condition is met, without you prompting each step. After every turn a small model reads the conversation and decides whether the goal is met, not yet met or impossible. Run `/goal` with no argument to see the status, and `/goal clear` to remove an active goal. Write the condition as something Claude's own output can prove, like "`npm test` exits 0", and add a turn limit if you want to bound the run.

Visit the following resources to learn more:

- [@official@Keep Claude working toward a goal](https://code.claude.com/docs/en/goal)
- [@official@Prompt-based hooks](https://code.claude.com/docs/en/hooks-guide#prompt-based-hooks)