# Writing Custom Kernels

Custom kernels are written when existing libraries do not fully utilize a GPU's capabilities for a specific operation or architecture. Most production kernels are written in C++ using CUTLASS and CuTe for GEMM-style operations and FlashInfer for attention variants; Triton offers a Python-based alternative with a lower barrier to entry. Writing an effective kernel requires understanding the target GPU's memory hierarchy, SM occupancy, and Tensor Core instruction set — skills that sit at the intersection of software and hardware.

Visit the following resources to learn more:

- [@book@CUDA by Example: An Introduction to General-Purpose GPU Programming](https://developer.nvidia.com/cuda-example)
- [@official@CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-programming-guide/)
- [@official@cuBLAS Documentation](https://docs.nvidia.com/cuda/cublas/)
- [@opensource@NVIDIA/cutlass](https://github.com/NVIDIA/cutlass)
- [@opensource@deepseek-ai/DeepGEMM](https://github.com/deepseek-ai/DeepGEMM)
- [@article@FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving](https://arxiv.org/abs/2501.01005)