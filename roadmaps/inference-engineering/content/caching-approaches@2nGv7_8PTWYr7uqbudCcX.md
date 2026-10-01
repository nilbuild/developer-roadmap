# Caching Approaches

KV cache reuse is the primary caching strategy in LLM inference, covering both prefix caching (reusing cached KV values across requests that share a common prefix) and KV cache offloading (moving less-used cache blocks to slower storage tiers to free GPU VRAM). A related concern is cache-aware routing, which directs requests to replicas most likely to already hold the relevant cached prefix.

Visit the following resources to learn more:

- [@opensource@LMCache](https://github.com/LMCache/LMCache)
- [@article@CacheBlend: Fast Large Language Model Serving for RAG with Cached Knowledge Fusion](https://arxiv.org/abs/2405.16444)
- [@article@What is Prompt Caching?](https://www.ibm.com/think/topics/prompt-caching)
- [@video@What is Prompt Caching? Optimize LLM Latency with AI Transformers](https://www.youtube.com/watch?v=u57EnkQaUTY)