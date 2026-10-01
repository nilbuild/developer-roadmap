# KV Cache Storage

KV caches can be stored in GPU VRAM (fastest, tens to hundreds of gigabytes), CPU RAM (slower, hundreds of gigabytes to terabytes), local SSD, or networked SSD. Moving less frequently accessed KV blocks to slower storage frees VRAM for active requests. NVIDIA Dynamo's KV Block Manager provides APIs for managing KV blocks across these storage tiers transparently.

Visit the following resources to learn more:

- [@opensource@LMCache](https://github.com/LMCache/LMCache)
- [@article@CacheBlend: Fast Large Language Model Serving for RAG with Cached Knowledge Fusion](https://arxiv.org/abs/2405.16444)