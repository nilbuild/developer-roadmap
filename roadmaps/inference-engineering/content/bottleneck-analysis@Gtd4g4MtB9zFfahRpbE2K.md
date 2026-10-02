# Bottleneck Analysis

Bottleneck analysis identifies whether a given inference workload is limited by compute or by memory bandwidth, which determines which optimizations will actually improve performance. The core tool is the ops:byte ratio: comparing a GPU's peak FLOPS against its peak memory bandwidth reveals the hardware's balance point, and comparing a model operation's arithmetic intensity against that balance point reveals whether it is compute-bound or memory-bound. LLM prefill and image generation are compute-bound; LLM decode is memory-bound.

Visit the following resources to learn more:

- [@article@The Next AI Bottleneck Isn’t the Model: It’s the Inference System](https://towardsdatascience.com/the-next-ai-bottleneck-isnt-the-model-its-the-inference-system/)
- [@article@Performance Analysis and Bottleneck Identification in AI Workflows](https://multicorewareinc.com/performance-analysis-and-bottleneck-identification-in-ai-workflows/)
- [@article@Distributed AI Inference: Why Placement Is the New Bottleneck](https://www.akamai.com/blog/cloud/distributed-ai-inference-why-placement-new-bottleneck)
- [@video@Inference Optimization Course](https://www.youtube.com/playlist?list=PLXV1pCewfApE)