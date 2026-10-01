# Image and Video Generation Bottlenecks

Image and video generation models are compute-bound because each denoising step applies attention over the entire latent space in parallel, similar to LLM prefill. The models are also relatively small, so memory bandwidth is not the limiting factor. Optimizations focus on FLOPS efficiency rather than memory traffic reduction.