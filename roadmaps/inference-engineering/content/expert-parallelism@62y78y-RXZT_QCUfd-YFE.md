# Expert Parallelism

Expert Parallelism distributes MoE experts across GPUs so each GPU hosts multiple complete experts. Tokens are routed to the GPU holding their activated experts, and each expert runs independently within a single GPU without splitting across multiple. EP has lower inter-GPU communication overhead than Tensor Parallelism and scales well to multi-node deployments via InfiniBand.

Visit the following resources to learn more:

- [@opensource@NVIDIA/Megatron-LM](https://github.com/NVIDIA/Megatron-LM)
- [@article@Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism](https://arxiv.org/abs/1909.08053)