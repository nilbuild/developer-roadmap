# Attention Mechanism

Attention is the mechanism transformers use to relate each token to all previous tokens via query, key, and value projections. During decode, each new token attends to every prior token, and the KV cache stores precomputed keys and values to avoid recomputation. Attention is the most expensive and most heavily optimized operation in LLM inference.

Visit the following resources to learn more:

- [@article@Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [@article@What is an attention mechanism?](https://www.ibm.com/think/topics/attention-mechanism)
- [@video@Attention mechanism: Overview](https://www.youtube.com/watch?v=fjJOgb-E41w&t=1s)
- [@video@Attention in transformers, step-by-step](https://www.youtube.com/watch?v=eMlx5fFNoYc)