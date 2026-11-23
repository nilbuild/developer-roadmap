# Continuous Batching

Continuous batching operates at the token level, swapping requests in and out of the batch as they complete individual tokens rather than waiting for a full batch to finish. This keeps GPU utilization high and minimizes the latency penalty of batching compared to static or dynamic batching. All major inference engines implement continuous batching by default.

Visit the following resources to learn more:

- [@article@Continuous batching](https://huggingface.co/blog/continuous_batching)
- [@article@Continuous Batching: Optimizing LLM Inference Throughput](https://mbrenndoerfer.com/writing/continuous-batching)
- [@video@How to Scale LLM Applications With Continuous Batching!](https://www.youtube.com/watch?v=PqHVpvvHLpE)
- [@video@Continuous Batching - How LLM Servers Keep the GPU Full](https://www.youtube.com/watch?v=X8CwAqYxH1E)