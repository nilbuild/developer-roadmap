# Idempotency in API Design

Idempotency in API design means that making the same request several times has the same effect on the server as making it once. This is what makes retries safe: if a network error hides whether a request succeeded, the client can send it again without, for example, charging a customer twice. In HTTP, `GET`, `HEAD`, `OPTIONS`, `PUT` and `DELETE` are idempotent by definition, while `POST` and `PATCH` are not. To make a non-idempotent operation safe to retry, APIs commonly accept an idempotency key: the client generates a unique value (such as a UUID) for each logical operation and sends it in an `Idempotency-Key` header. The server stores the key with the result of the first request, returns that saved result for any repeat, rejects a reused key that comes with a different payload, and expires keys after a set period.

Visit the following resources to learn more:

- [@article@Idempotent - MDN Glossary](https://developer.mozilla.org/en-US/docs/Glossary/Idempotent)
- [@article@The Idempotency-Key HTTP Header Field - IETF Draft](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/)
- [@article@Idempotent Requests - Stripe API Reference](https://docs.stripe.com/api/idempotent_requests)
- [@article@What is idempotency?](https://blog.dreamfactory.com/what-is-idempotency)
- [@article@Idempotency Is Easy Until the Second Request Is Different](https://blog.dochia.dev/blog/idempotency/)
- [@article@Idempotent REST API](https://restfulapi.net/idempotent-rest-apis/)