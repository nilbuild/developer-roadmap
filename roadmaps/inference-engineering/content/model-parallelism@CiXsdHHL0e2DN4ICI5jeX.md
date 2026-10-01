# Model Parallelism

When a model is too large to fit on a single GPU, or when serving latency requires more compute than one device can provide, model parallelism distributes the workload across multiple GPUs or nodes. This group covers the three parallelism strategies and their trade-offs in terms of communication overhead, latency, and hardware requirements.