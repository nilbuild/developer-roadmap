# Memory

GPU memory determines what fits on a single device and how fast data can move through the compute units. VRAM capacity sets the upper limit on model size and KV cache; VRAM bandwidth determines how quickly the decode phase can load weights per token. Modern datacenter GPUs use high-bandwidth memory (HBM) in generations HBM3, HBM3e, and HBM4, stacked directly on the GPU die to maximize bandwidth.

Visit the following resources to learn more:

- [@article@What is GPU Memory and Why it Matters for LLM Inference](https://www.bentoml.com/blog/what-is-gpu-memory-and-why-it-matters-for-llm-inference)
- [@article@What is GPU Memory (VRAM)?](https://www.ertas.ai/glossary/gpu-memory)
- [@video@NPU vs. CPU vs. GPU vs. TPU: AI Hardware Compared](https://www.youtube.com/watch?v=d3SqH0UBLEY&t=58s)
- [@video@Memory Hierarchy | GPU Programming](https://www.youtube.com/watch?v=Zrbw0zajhJM)