# Inference Engines

Inference engines are the core serving layer that takes model weights and handles requests at production scale. They implement continuous batching, memory management, parallelism, and optimization techniques so engineers do not have to implement these from scratch. This group covers the three dominant LLM engines and the orchestration platform that sits above them.