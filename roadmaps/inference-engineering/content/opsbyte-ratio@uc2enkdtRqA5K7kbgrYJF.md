# Ops:Byte Ratio

The ops:byte ratio is a property of GPU hardware that expresses the balance between compute throughput and memory bandwidth. It is calculated by dividing peak FLOPS by peak memory bandwidth, and sets the threshold that separates compute-bound from memory-bound workloads on that device. Different GPU generations have very different ops:byte ratios, which is why an optimization that works well on one generation may have no effect on another.

Visit the following resources to learn more:

- [@article@A guide to LLM inference and performance](https://www.baseten.co/blog/llm-transformer-inference-guide/)
- [@article@Understanding Performance](https://docs.nvidia.com/deeplearning/performance/dl-performance-gpu-background/index.html#understand-perf)