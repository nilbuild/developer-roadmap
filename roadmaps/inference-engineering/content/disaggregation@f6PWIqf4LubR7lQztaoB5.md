# Disaggregation

Disaggregation separates the prefill and decode phases onto independent GPU instances that can scale separately. The prefill engine processes the input sequence and sends the resulting KV cache to the decode engine via the hardware interconnect. This removes the resource contention between compute-heavy prefill and memory-heavy decode. Disaggregation is most effective at high traffic volumes, for large models, and with prefill-heavy workloads like code editors.

Visit the following resources to learn more:

- [@article@Beyond the Buzz: A Pragmatic Take on Inference Disaggregation](https://arxiv.org/abs/2506.05508)
- [@article@Disaggregated Serving](https://llm-d.ai/docs/architecture/advanced/disaggregation)
- [@article@Disaggregated Serving in LLM Inference, Explained](https://handbook.modular.com/inference-optimization/prefill-decode-disaggregation/)
- [@article@Encoder Disaggregation in vLLM: Scaling Multimodal Serving with EPD](https://vllm.ai/blog/2026-11-11-encoder-disaggregation-epd)
- [@video@Why Separating Prefill and Decode Makes LLMs Faster | vLLM, LLM-D and NIXL](https://www.youtube.com/watch?v=BaD3CTYf6V0)