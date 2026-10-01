# Streaming and Protocol Support

Text streaming over HTTP is sufficient for LLM chat applications. For real-time voice and video applications, WebSockets provide a persistent bidirectional connection for continuous unstructured data like audio chunks. gRPC provides bidirectional streaming for structured service-to-service communication with schema enforcement. Each WebSocket connection holds a slot on the server, and the concurrency limit must be set to match the GPU's sustainable load.

Visit the following resources to learn more:

- [@article@AI for Web Devs: Faster Responses with HTTP Streaming](https://austingil.com/ai-for-web-devs-streaming/)