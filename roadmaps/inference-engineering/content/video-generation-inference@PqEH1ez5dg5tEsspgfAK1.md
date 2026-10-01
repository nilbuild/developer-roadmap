# Video Generation Inference

Video generation models run on full nodes of eight GPUs with a batch size of one because the latent space is too large to batch effectively. Attention over the three-dimensional video latent space consumes 70 to 80 percent of compute time and is the primary optimization target. Attention caching techniques that reuse outputs from previous timesteps or transformer layers can improve speed by 30 to 40 percent.

Visit the following resources to learn more:

- [@opensource@Cache-DiT](https://github.com/vipshop/cache-dit)
- [@opensource@TeaCache: Timestep Embedding Tells: It's Time to Cache for Video Diffusion Model](https://github.com/ali-vilab/TeaCache)
- [@article@SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration](https://arxiv.org/abs/2410.02367)