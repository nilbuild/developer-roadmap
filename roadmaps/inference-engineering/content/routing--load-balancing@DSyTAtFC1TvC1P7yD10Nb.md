# Routing and Load Balancing

Routers make request-level decisions about which replica to send a request to, considering factors like KV cache prefix match and LoRA availability. Load balancers make system-level decisions to distribute traffic evenly across replicas. In systems with prefix caching, naive round-robin load balancing misses cache opportunities; intelligent routing increases cache hit rates and reduces TTFT.

Visit the following resources to learn more:

- [@book@Designing Data-Intensive Applications](https://dataintensive.net/)
- [@book@Site Reliability Engineering](https://sre.google/books/)
- [@article@The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783)