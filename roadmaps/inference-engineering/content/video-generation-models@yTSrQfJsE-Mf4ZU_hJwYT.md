# Video Generation Models

Video generation models extend image generation to three-dimensional latent space, representing width, height, and time simultaneously. They run the same number of denoising steps as image models but process far more data per step. Attention over the full video latent space dominates compute time, making video generation the most resource-intensive common inference workload.

Visit the following resources to learn more:

- [@article@Video Diffusion Models](https://arxiv.org/abs/2204.03458)
- [@article@Imagen Video: High Definition Video Generation with Diffusion Models](https://arxiv.org/abs/2210.02303)