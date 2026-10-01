# Diffusion Models

Diffusion models generate images by starting from random noise and iteratively denoising it over 30 to 50 steps, guided by a text prompt. Each step runs the denoiser twice, once with conditioning and once without, to apply classifier-free guidance. The entire process operates in a low-dimensional latent space rather than full pixel space to make attention computationally feasible.

Visit the following resources to learn more:

- [@article@Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239)
- [@article@High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752)
- [@article@SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis](https://arxiv.org/abs/2307.01952)
- [@article@Scalable Diffusion Models with Transformers (DiT)](https://arxiv.org/abs/2212.09748)
- [@article@How DALL-E 2 Actually Works](https://www.assemblyai.com/blog/how-dall-e-2-actually-works/)
- [@video@How AI Image Generators Work (Stable Diffusion / DALL-E)](https://www.youtube.com/watch?v=1CIpzeNxIhU)