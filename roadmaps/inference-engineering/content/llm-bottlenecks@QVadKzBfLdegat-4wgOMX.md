# LLM Inference Bottlenecks

LLM prefill is compute-bound because it processes the entire input sequence as one large matrix multiplication, performing many operations per byte loaded. LLM decode is memory-bound because it generates tokens one at a time via vector-matrix multiplications that require loading all model weights from memory for each token while performing relatively few arithmetic operations.

Visit the following resources to learn more:

- [@book@AI Systems Performance Engineering](https://www.oreilly.com/library/view/ai-systems-performance/9781098170202/)
- [@article@GPU Glossary](https://modal.com/gpu-glossary)