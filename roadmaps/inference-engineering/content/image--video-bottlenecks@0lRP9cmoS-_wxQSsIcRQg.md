# Image and Video Generation Bottlenecks

Image and video generation models are compute-bound because each denoising step applies attention over the entire latent space in parallel, similar to LLM prefill. The models are also relatively small, so memory bandwidth is not the limiting factor. Optimizations focus on FLOPS efficiency rather than memory traffic reduction.

Visit the following resources to learn more:

- [@article@How to Overcome Visual Data Bottlenecks in GenAI Development](https://wirestock.io/gen-ai-resources/how-to-overcome-visual-data-bottlenecks-in-genai-development)
- [@article@6 Limitations of Current AI Video Generation Technology and Workarounds](https://kling.ai/blog/limitations-of-current-ai-video-generation-technology)
- [@article@The biggest bottleneck in AI video generation is not the model, but the cost.](https://en.eeworld.com.cn/news/wltx/eic737186.html)
- [@video@But how do AI images and videos actually work?](https://www.youtube.com/watch?v=iv-5mZ_9CPY&t=315s)