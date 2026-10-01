# KV Cache

The KV cache stores the key and value tensors computed during attention for each previously processed token. Without it, attention would require recomputing every prior token on each decode step, making inference prohibitively slow. The KV cache lives in GPU memory and its size grows with sequence length and batch size, making it a major target for memory management techniques.

Visit the following resources to learn more:

- [@article@Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180)