# Image Generation Architecture

Image generation models are pipelines of multiple components: a text encoder that converts the prompt into conditioning, a denoising model that iteratively refines a latent representation from noise into an image, and a variational autoencoder that converts the final latent to pixels. The denoising model is the largest and most compute-intensive component and runs up to 100 forward passes per image generation.

Visit the following resources to learn more:

- [@article@Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239)
- [@article@High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752)
- [@article@SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis](https://arxiv.org/abs/2307.01952)
- [@article@Scalable Diffusion Models with Transformers (DiT)](https://arxiv.org/abs/2212.09748)