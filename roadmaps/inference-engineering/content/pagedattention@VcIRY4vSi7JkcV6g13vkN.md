# PagedAttention

PagedAttention stores the KV cache in fixed-size pages rather than a single contiguous memory block, allowing it to be distributed across GPU memory without fragmentation. It uses a lookup table to access pages on demand, reducing memory waste from over-allocation and enabling more requests to share GPU memory. It is the memory management technique that made vLLM's high throughput possible.

Visit the following resources to learn more:

- [@article@Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180)