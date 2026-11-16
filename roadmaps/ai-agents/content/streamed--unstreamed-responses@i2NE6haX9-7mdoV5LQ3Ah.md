# Streamed vs Unstreamed Responses

An unstreamed response waits until the model finishes generating the entire output before returning anything to the caller. A streamed response sends tokens back as they are generated, so the caller can start displaying or processing output immediately. Streaming improves perceived responsiveness in user facing applications, while unstreamed responses are simpler to handle when the full output is needed before continuing.

Visit the following resources to learn more:

- [@article@Streaming Responses in AI: How AI Outputs Are Generated in Real Time](https://dev.to/pranshu_kabra_fe98a73547a/streaming-responses-in-ai-how-ai-outputs-are-generated-in-real-time-18kb)
- [@article@AI for Web Devs: Faster Responses with HTTP Streaming](https://austingil.com/ai-for-web-devs-streaming/)
- [@article@Master the OpenAI API: Stream Responses](https://www.toolify.ai/gpts/master-the-openai-api-stream-responses-139447)