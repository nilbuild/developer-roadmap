# Max Tokens

Max tokens sets the largest number of tokens the model can generate in a response. It protects against very long outputs and limits cost. The model does not know about the limit, so a response that hits it is cut off mid-sentence. To get shorter answers that still end properly, ask for a specific length in the prompt too.

Visit the following resources to learn more:

- [@official@Token Counting - Anthropic](https://platform.claude.com/docs/en/build-with-claude/token-counting)
- [@article@Max Tokens - LLM Parameter Guide - Vellum](https://www.vellum.ai/llm-parameters/max-tokens)