# FlashAttention

FlashAttention is a series of hand-optimized CUDA kernels that compute attention with fewer reads and writes to GPU memory by fusing the attention algorithm into a single kernel. Standard attention stores intermediate matrices to memory between steps; FlashAttention eliminates those round-trips. FlashAttention 3 targets Hopper GPUs and FlashAttention 4 targets Blackwell GPUs.

Visit the following resources to learn more:

- [@opensource@Dao-AILab/flash-attention](https://github.com/Dao-AILab/flash-attention)
- [@article@FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135)
- [@video@Flash Attention: The Fastest Attention Mechanism?](https://www.youtube.com/watch?v=eJn6zsbrqUM)
- [@video@FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning](https://www.youtube.com/playlist?list=PLBWdTDczuFNrxnetcH-5CVLRP1u4Ua87m)