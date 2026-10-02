# Diffusion Models

Diffusion models generate images by starting from random noise and iteratively denoising it over 30 to 50 steps, guided by a text prompt. Each step runs the denoiser twice, once with conditioning and once without, to apply classifier-free guidance. The entire process operates in a low-dimensional latent space rather than full pixel space to make attention computationally feasible.

Visit the following resources to learn more:

- [@article@What are diffusion models?](https://www.ibm.com/think/topics/diffusion-models)
- [@video@Diffusion Models for AI Image Generation](https://www.youtube.com/watch?v=x2GRE-RzmD8)
- [@video@How AI Image Generators Work (Stable Diffusion / DALL-E)](https://www.youtube.com/watch?v=1CIpzeNxIhU)