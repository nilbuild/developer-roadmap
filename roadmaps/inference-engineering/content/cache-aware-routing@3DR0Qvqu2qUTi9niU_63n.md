# Cache-Aware Routing

In deployments with multiple replicas, cache-aware routing directs requests to the replica most likely to have a matching prefix already in its KV cache. Without this, a user in a long conversation may hit different replicas each turn, getting cache misses that increase latency. A global KV cache stored on networked SSD allows all replicas to eventually access any cached sequence.

Visit the following resources to learn more:

- [@article@Why Agentic Inference Needs Prefix-Aware Routing Infrastructure](https://www.coreweave.com/blog/why-agentic-inference-needs-prefix-aware-routing-infrastructure)
- [@article@Enabling inference at massive scale with hybrid storage for KV cache offloading.](https://www.seagate.com/es/es/resources/enabling-inference-at-massive-scale-with-hybrid-storage-for-kv-cache-offloading/)
- [@article@KV Cache Aware Routing](https://docs.vllm.ai/projects/production-stack/en/vllm-stack-0.1.5/tutorials/kvaware.html)