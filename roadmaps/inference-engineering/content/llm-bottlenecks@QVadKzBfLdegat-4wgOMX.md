# LLM Inference Bottlenecks

LLM prefill is compute-bound because it processes the entire input sequence as one large matrix multiplication, performing many operations per byte loaded. LLM decode is memory-bound because it generates tokens one at a time via vector-matrix multiplications that require loading all model weights from memory for each token while performing relatively few arithmetic operations.

Visit the following resources to learn more:

- [@book@AI Systems Performance Engineering](https://www.oreilly.com/library/view/ai-systems-performance/9781098170202/)
- [@article@Common Bottlenecks in LLM Inference at Scale (And How to Fix Them)](https://www.yottalabs.ai/post/common-bottlenecks-in-llm-inference-at-scale-and-how-to-fix-them)
- [@article@GPU Glossary](https://modal.com/gpu-glossary)
- [@article@The Hidden Bottlenecks in LLM Inference and How to Fix Them](https://www.digitalocean.com/community/conceptual-articles/bottlenecks-llm-inference-optimization)