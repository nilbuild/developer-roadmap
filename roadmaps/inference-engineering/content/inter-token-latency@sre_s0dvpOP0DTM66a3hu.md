# Inter-Token Latency (ITL)

ITL is the time between successive generated tokens during decode. An ITL of 10 milliseconds corresponds to 100 tokens per second. It is the per-step measure underlying TPS and is directly tied to how quickly the GPU can complete a single decode forward pass.

Visit the following resources to learn more:

- [@article@Inter-Token Latency - NVIDIA](https://docs.nvidia.com/nim/benchmarking/llm/latest/metrics.html#inter-token-latency)
- [@article@Inter-Token Latency](https://nhimg.org/glossary/inter-token-latency/)