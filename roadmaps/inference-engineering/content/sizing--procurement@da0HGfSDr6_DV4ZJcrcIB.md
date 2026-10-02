# Sizing and Procurement

Estimating GPU requirements starts with VRAM: roughly 1 GB per billion parameters at FP8 for weights, plus at least 50 percent headroom for the KV cache. This total is rounded up to the nearest available instance size. Cloud GPUs are available from hyperscalers like AWS and GCP, neoclouds like CoreWeave and Nebius, and spot markets; large deployments combine reserved instances for baseline load with on-demand and spot capacity for bursts.

Visit the following resources to learn more:

- [@book@Designing Data-Intensive Applications](https://dataintensive.net/)
- [@book@Site Reliability Engineering](https://sre.google/books/)
- [@article@SemiAnalysis](https://semianalysis.com/)
- [@article@GPU Requirements for LLM Inference: Memory, Throughput, and Sizing](https://www.onesourcecloud.net/cms/gpu-requirements-llm-inference-sizing.html)
- [@article@Inference Is the New Bottleneck: How to Plan GPU Capacity for Production AI](https://clear.ml/blog/inference-is-the-new-bottleneck-how-to-plan-gpu-capacity-for-production-ai)