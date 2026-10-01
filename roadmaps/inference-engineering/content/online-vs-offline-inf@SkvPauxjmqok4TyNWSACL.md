# Online vs. Offline Inference

Online inference serves real-time user-facing requests where latency matters. Offline inference processes large batches of data asynchronously where throughput and cost matter more than per-request speed. The same model, like Whisper for transcription, may need separate deployments for each use case because the optimal configurations differ significantly.

Visit the following resources to learn more:

- [@article@Production ML systems: Static versus dynamic inference](https://developers.google.com/machine-learning/crash-course/production-ml-systems/static-vs-dynamic-inference)
- [@article@Trade-offs in Online vs Offline Model Inference](https://bugfree.ai/knowledge-hub/trade-offs-online-vs-offline-model-inference)
- [@video@Offline Recurrence for Improved Online Inference](https://www.youtube.com/watch?v=bwvE1KvLzLQ)