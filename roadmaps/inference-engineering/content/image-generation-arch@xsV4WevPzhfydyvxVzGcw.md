# Image Generation Architecture

Image generation models are pipelines of multiple components: a text encoder that converts the prompt into conditioning, a denoising model that iteratively refines a latent representation from noise into an image, and a variational autoencoder that converts the final latent to pixels. The denoising model is the largest and most compute-intensive component and runs up to 100 forward passes per image generation.

Visit the following resources to learn more:

- [@article@Image Generation Guide](https://ai-guide.future.mozilla.org/content/image-models/)
- [@video@How AI Image Generators Work (Stable Diffusion / Dall-E)](https://www.youtube.com/watch?v=1CIpzeNxIhU)