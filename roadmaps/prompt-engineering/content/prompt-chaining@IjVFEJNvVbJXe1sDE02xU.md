# Prompt Chaining

Prompt chaining splits a large task into a sequence of smaller prompts, where the output of one step becomes the input of the next. Each step is simpler, easier to test and easier to fix. A typical chain is extract, then analyze, then write. You can also add a check between steps to stop errors from carrying forward.

Visit the following resources to learn more:

- [@official@Chain complex prompts for stronger performance - Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/chain-prompts)
- [@article@Prompt Chaining - DAIR.AI](https://www.promptingguide.ai/techniques/prompt_chaining)
- [@article@Building effective agents - Anthropic](https://www.anthropic.com/engineering/building-effective-agents)