# Quantization

Quantization converts model weights and other values from their native precision to a lower-precision format. Cutting precision in half doubles memory bandwidth for decode and enables twice the FLOPS for prefill on compatible Tensor Cores. The tradeoff is potential quality loss from reduced numerical precision, which can compound across the many calculations in a forward pass.

Visit the following resources to learn more:

- [@opensource@AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration](https://github.com/mit-han-lab/llm-awq)
- [@opensource@bitsandbytes](https://github.com/TimDettmers/bitsandbytes)
- [@opensource@SmoothQuant](https://github.com/mit-han-lab/smoothquant)
- [@article@GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers](https://arxiv.org/abs/2210.17323)
- [@article@LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale](https://arxiv.org/abs/2208.07339)
- [@article@SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot](https://arxiv.org/abs/2301.00774)