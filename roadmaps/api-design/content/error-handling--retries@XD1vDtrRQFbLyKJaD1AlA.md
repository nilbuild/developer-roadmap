# Error Handling / Retries

Error handling and retries decide how an API and its clients behave when something goes wrong. On the server, good error handling means validating input early, returning the correct HTTP status code (`4xx` for client mistakes, `5xx` for server faults) and a consistent, machine-readable error body, such as the Problem Details format, so clients can react programmatically. On the client, only transient failures like timeouts, `429 Too Many Requests`, `502`, `503` and `504` are worth retrying, while errors such as `400` or `404` will fail again. Retries should be capped, spaced out with exponential backoff and jitter so many clients don't retry at the same moment, respect the `Retry-After` header when the server sends one, and be used only for idempotent requests (or ones protected by an idempotency key) so a repeated call can't cause duplicate side effects.

Visit the following resources to learn more:

- [@article@Timeouts, retries, and backoff with jitter - AWS Builders' Library](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)
- [@article@Exponential Backoff and Jitter - AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/)
- [@article@Retry-After header - MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Retry-After)
- [@article@How To Improve Your Backend By Adding Retries to Your API Calls](https://hackernoon.com/how-to-improve-your-backend-by-adding-retries-to-your-api-calls-83r3udx)
- [@video@How to Make Resilient Web Applications with Retries](https://www.youtube.com/watch?v=Gly94hp3Eec)