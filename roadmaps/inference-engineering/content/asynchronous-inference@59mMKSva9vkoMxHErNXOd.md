# Asynchronous Inference

Asynchronous inference is a fire-and-forget request model where the client submits a job, receives an immediate acknowledgment, and retrieves the result later via a webhook. It is suited for throughput-sensitive, latency-insensitive workloads like bulk document embedding or corpus transcription. Async jobs have much longer time limits than synchronous requests and require robust server-side queuing.

Visit the following resources to learn more:

- [@article@Using asynchronous inference in production](https://www.baseten.co/blog/using-asynchronous-inference-in-production/)
- [@article@Asynchronous Inference: Methods & Applications](https://www.emergentmind.com/topics/asynchronous-inference)