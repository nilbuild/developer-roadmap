# Long-Context vs RAG

Large context windows make it possible to put whole documents into a prompt instead of retrieving pieces. Long context is simpler and works well for a limited set of documents, but it costs more per request and quality can drop as the input grows. RAG scales to large collections and keeps the context small, but depends on retrieval finding the right passages. When using long context, place the documents first and the question last.

Visit the following resources to learn more:

- [@official@Long context prompting tips - Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/long-context-tips)
- [@article@What is long context, and why does it matter for your AI? - Google Cloud](https://cloud.google.com/transform/the-prompt-what-are-long-context-windows-and-why-do-they-matter)
- [@article@Is RAG Dead? The Rise of Context Engineering and Semantic Layers for Agentic AI - Towards Data Science](https://towardsdatascience.com/beyond-rag/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- [@video@Deep Dive into Long Context](https://www.youtube.com/watch?v=NHMJ9mqKeMQ)