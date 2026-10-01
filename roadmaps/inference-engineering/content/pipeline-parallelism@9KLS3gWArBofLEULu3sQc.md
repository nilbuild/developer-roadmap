# Pipeline Parallelism

Pipeline Parallelism splits an LLM's layers into sequential stages and assigns each stage to a different GPU or node. Unlike Tensor Parallelism, each GPU holds complete layers rather than layer fragments. It introduces pipeline bubbles where GPUs wait for preceding stages, reducing efficiency. It is used for multi-node inference with dense models, typically combined with Tensor Parallelism within each node.

Visit the following resources to learn more:

- [@opensource@NVIDIA/Megatron-LM](https://github.com/NVIDIA/Megatron-LM)
- [@article@Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism](https://arxiv.org/abs/1909.08053)