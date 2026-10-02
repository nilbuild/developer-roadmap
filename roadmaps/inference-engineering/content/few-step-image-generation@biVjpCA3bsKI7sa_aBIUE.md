# Few-Step Image Generation

Few-step image generation models produce usable images in eight or fewer denoising steps by training the model to collapse the standard 30 to 50 step process into a fraction of the iterations. Techniques include latent consistency distillation and adversarial training, both of which teach the model to reach high-quality outputs in fewer passes. They are a strong fit for latency-sensitive use cases like real-time filters, but produce noticeably lower quality than full-step models and are a model selection decision rather than an inference optimization technique.

Visit the following resources to learn more:

- [@article@Latent Consistency Models: Synthesizing High-Resolution Images with Few-Step Inference](https://arxiv.org/abs/2310.04378)
- [@article@Few-Step Diffusion Models](https://www.emergentmind.com/topics/few-step-diffusion-model)