# Compute

A GPU's compute capability is determined by its Streaming Multiprocessors (SMs), each containing CUDA Cores for general arithmetic and Tensor Cores for matrix multiply-accumulate operations. Tensor Cores are the primary resource for inference, executing the matmuls that make up the majority of forward pass computation. GPU compute is measured in peak Tensor Core FLOPS at a given precision, and roughly doubles with each new NVIDIA architecture generation.

Visit the following resources to learn more:

- [@article@Understanding GPU Architecture: Structure, Layers, and Performance Explained](https://www.scalecomputing.com/resources/understanding-gpu-architecture)
- [@article@What Is GPU Computing and How Does It Work? A Complete Guide](https://factory.fpt.ai/ai-insights/what-is-gpu-computing)
- [@video@Understanding NVIDIA GPU Hardware as a CUDA C Programmer](https://www.youtube.com/watch?v=1Goq8Yc3dfo)
- [@video@Fundamentals of GPU Architecture](https://www.youtube.com/playlist?list=PLxNPSjHT5qvscDTMaIAY9boOOXAJAS7y4)