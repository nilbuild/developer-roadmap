# Speculative Decoding

Speculative decoding takes advantage of spare compute during memory-bound decode by generating multiple draft tokens and validating them in a single forward pass. If the target model accepts N draft tokens, the forward pass produces N+1 tokens instead of one. The performance gain depends on draft token cost, draft sequence length, and acceptance rate, which decreases at higher temperatures and larger batch sizes.

Visit the following resources to learn more:

- [@article@Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192)
- [@article@Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads](https://arxiv.org/abs/2401.10774)