# Vision Language Models (VLMs)

VLMs combine a large language model with a small vision encoder that converts input images or video into a sequence of visual tokens. A high-resolution image typically adds about 1,000 tokens to the input sequence. All LLM inference optimization techniques apply to VLMs, but longer sequences make quantization, prefix caching, and disaggregation especially important.

Visit the following resources to learn more:

- [@course@A Multimodal World - Hugging Face Computer Vision Course](https://huggingface.co/learn/computer-vision-course/en/unit4/multimodal-models/a_multimodal_world)
- [@article@BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models](https://arxiv.org/abs/2301.12597)
- [@article@Visual Instruction Tuning](https://arxiv.org/abs/2304.08485)
- [@article@Segment Anything](https://arxiv.org/abs/2304.02643)
- [@article@SpecVLM: Fast Speculative Decoding in Vision-Language Models](https://arxiv.org/abs/2509.11815)