# Autoscaling

Autoscaling dynamically adjusts the number of active model replicas to match incoming traffic, maintaining latency SLAs while minimizing idle GPU spend. Kubernetes is the standard orchestration layer, scaling replicas within a cluster based on traffic signals and utilization metrics. Key configuration parameters are min replicas, max replicas, the autoscaling window, the scale-down delay, and the concurrency target per replica.

Visit the following resources to learn more:

- [@book@Designing Data-Intensive Applications](https://dataintensive.net/)
- [@book@Site Reliability Engineering](https://sre.google/books/)
- [@article@The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783)