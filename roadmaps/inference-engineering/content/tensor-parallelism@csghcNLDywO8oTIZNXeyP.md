# Tensor Parallelism

Tensor Parallelism splits each layer's weight matrices across multiple GPUs and distributes the matmul computation. Each GPU handles a shard of each layer and the results are combined via an all-reduce operation before the next layer. It reduces per-user latency by sharing both VRAM and compute across GPUs, but requires fast NVLink interconnects and is not well-suited for multi-node deployments.

Visit the following resources to learn more:

- [@opensource@NVIDIA/Megatron-LM](https://github.com/NVIDIA/Megatron-LM)
- [@article@Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism](https://arxiv.org/abs/1909.08053)