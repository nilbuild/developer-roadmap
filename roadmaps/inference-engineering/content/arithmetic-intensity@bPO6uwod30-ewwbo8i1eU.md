# Arithmetic Intensity

Arithmetic intensity is a property of an algorithm: the number of floating-point operations performed per byte of memory read or written. A large matrix multiplication has high arithmetic intensity because the same weights participate in many operations per load; a decode forward pass has low arithmetic intensity because each weight is loaded from VRAM and used once per token. Comparing a workload's arithmetic intensity against the GPU's ops:byte ratio is the fastest way to diagnose whether adding compute or adding bandwidth would help.

Visit the following resources to learn more:

- [@article@A guide to LLM inference and performance](https://www.baseten.co/blog/llm-transformer-inference-guide/)
- [@article@Arithmetic Intensity : Understand Op limits — Memory or Compute](https://medium.com/better-ml/arithmetic-intensity-understand-op-limits-memory-or-compute-342fd15342bb)
- [@article@Arithmetic Intensity Explained: The Formula and Why It Predicts GPU Speedup](https://ayoob.ai/blog/webgpu-matrix-multiplication-gemm-arithmetic-intensity)
- [@video@Compute-Bound or Memory-Bound? Arithmetic Intensity Explained](https://www.youtube.com/watch?v=jCUWDXVohTY)