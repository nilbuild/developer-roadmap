# Context Budgeting

Context budgeting is deciding how many tokens each part of the context gets. System prompt, tools, retrieved documents, history and the model's reply all compete for the same window and add to cost and latency. A budget forces choices about what to keep, trim or retrieve on demand, and it helps keep quality steady in long-running tasks.

Visit the following resources to learn more:

- [@article@LLM Cost Optimization: 5 Levers That Cut API Spend 70-85% - Morph](https://www.morphllm.com/llm-cost-optimization)
- [@article@The LLM Inference Trilemma: Throughput, Latency, Cost - DigitalOcean](https://www.digitalocean.com/blog/llm-inference-tradeoffs)
- [@article@Context Budget Allocation: Spending Every Token Wisely¶](https://agentpatterns.ai/context-engineering/context-budget-allocation/)