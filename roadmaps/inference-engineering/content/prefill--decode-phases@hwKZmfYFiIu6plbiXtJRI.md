# Prefill and Decode Phases

LLM inference has two distinct phases. Prefill processes the entire input sequence in parallel to build the KV cache and is compute-bound. Decode generates output tokens one at a time by reading model weights from memory and is memory-bound. Each phase has different bottlenecks and responds to different optimization techniques.

Visit the following resources to learn more:

- [@article@Prefill vs Decode: LLM Inference Phases Explained](https://redis.io/blog/prefill-vs-decode/)
- [@article@Understanding the Two Key Stages of LLM Inference: Prefill and Decode(Part-1)](https://medium.com/@sailakkshmiallada/understanding-the-two-key-stages-of-llm-inference-prefill-and-decode-29ec2b468114)
- [@video@Why LLMs Read Fast but Write Slowly - Prefill vs Decode](https://www.youtube.com/watch?v=hmMgTgQpO38)