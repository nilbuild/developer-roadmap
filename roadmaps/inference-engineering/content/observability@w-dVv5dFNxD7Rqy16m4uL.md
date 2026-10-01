# Observability

Inference observability tracks total request volume, input and output sequence lengths, response codes, latency percentiles (P50, P90, P99 of TTFT, TPS, and end-to-end latency), replica count, GPU utilization, and queue depth. These metrics are interdependent; a latency spike could come from long input sequences, high concurrency, or a hardware issue. Observability must integrate with existing tooling like Grafana, Datadog, and PagerDuty to put inference metrics in context.

Visit the following resources to learn more:

- [@official@NVIDIA Nsight Systems](https://developer.nvidia.com/nsight-systems)