# Reasoning Models

Reasoning models generate an intermediate thinking sequence before producing their final output, adding a third token sequence alongside the input and output. This reasoning trace increases total token count significantly and changes inference economics: TTFT is higher, total latency is longer, and output token costs dominate. Inference engineers must account for the variable and sometimes very long reasoning sequences when sizing infrastructure and setting latency budgets.

Visit the following resources to learn more:

- [@article@Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903)
- [@article@What is a reasoning model?](https://www.ibm.com/think/topics/reasoning-model)
- [@video@What Are Large Reasoning Models (LRMs)? Smarter AI Beyond LLMs](https://www.youtube.com/watch?v=enLbj0igyx4)
- [@video@How do thinking and reasoning models work?](https://www.youtube.com/watch?v=xCRvOUykOX0)