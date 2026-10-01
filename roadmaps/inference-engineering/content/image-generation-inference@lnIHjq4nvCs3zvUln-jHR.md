# Image Generation Inference

Production image generation inference uses SGLang Diffusion, TensorRT, or hand-optimized PyTorch. The most important optimization target is the attention kernel, where FlashAttention 3 or 4 outperforms the default on Hopper and Blackwell respectively. GEMM kernels for linear layers can be quantized to FP8 safely. Torch compilation with manual kernel plugins caches the compiled engine to avoid multi-minute recompilation on every cold start.

Visit the following resources to learn more:

- [@opensource@ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- [@article@Latent Consistency Models: Synthesizing High-Resolution Images with Few-Step Inference](https://arxiv.org/abs/2310.04378)