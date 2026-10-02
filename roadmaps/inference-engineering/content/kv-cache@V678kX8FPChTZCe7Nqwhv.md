# KV Cache

The KV cache stores the key and value tensors computed during attention for each previously processed token. Without it, attention would require recomputing every prior token on each decode step, making inference prohibitively slow. The KV cache lives in GPU memory and its size grows with sequence length and batch size, making it a major target for memory management techniques.

Visit the following resources to learn more:

- [@article@Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180)
- [@article@KV Caching Explained: Optimizing Transformer Inference Efficiency](https://huggingface.co/blog/not-lain/kv-caching)
- [@video@How KV Cache Speeds Up LLMs for Faster AI Models on GPUs](https://www.youtube.com/watch?v=o0gkdZBtwEg)
- [@video@The KV Cache: Memory Usage in Transformers](https://www.youtube.com/watch?v=80bIUggRJf4)