# Just-in-Time Retrieval

Just-in-time retrieval means loading information into the context only when the task needs it. The agent keeps lightweight references such as file paths, links or IDs, and fetches the full content on demand with tools. This keeps the context window small and avoids filling it with material that may never be used. The model can also explore step by step and use the structure of folders and file names as hints.

Visit the following resources to learn more:

- [@article@JIT Context: Why the Best Agents Load Late and Load Little](https://www.truefoundry.com/blog/jit-context-just-in-time-context-agents)
- [@article@Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)
- [@article@Context engineering for AI agents: a practical guide](https://mastra.ai/articles/context-engineering#query-augmentation-and-just-in-time-retrieval)