# TensorRT

TensorRT is NVIDIA's high-performance inference runtime that compiles PyTorch or ONNX models into optimized engines using fused kernels, quantization, and hardware-specific tuning. It is the standard choice for image and video generation models and for any workload where maximum throughput on NVIDIA hardware is the primary goal. Compiled engines are cached to disk, eliminating recompilation overhead on subsequent cold starts.

Visit the following resources to learn more:

- [@official@TensorRT Documentation](https://docs.nvidia.com/deeplearning/tensorrt/)