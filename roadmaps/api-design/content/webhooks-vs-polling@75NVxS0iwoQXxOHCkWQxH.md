# Webhooks vs Polling in API Design

Webhooks and polling are two ways for a client to learn about changes on a server. With polling, the client repeatedly asks the server whether anything has changed, so it controls the request rate but wastes calls when nothing is new and only sees a change on its next check. With webhooks, the server sends an HTTP request to a URL the client registered as soon as an event happens, which is faster and cheaper but requires the receiver to be publicly reachable and to handle delivery problems. Webhook delivery is usually at-least-once, so events can arrive more than once or out of order: receivers should verify each request's signature (typically an HMAC of the payload using a shared secret), respond quickly with a `2xx` status and process the event in the background, and ignore events whose ID they have already handled. Many integrations combine both approaches, using webhooks for real-time updates and occasional polling to catch any events that were missed. The right choice depends on how often data changes, how quickly the client needs to know, and the load each approach puts on both sides.

Visit the following resources to learn more:

- [@opensource@Standard Webhooks - Specification and Libraries](https://github.com/standard-webhooks/standard-webhooks)
- [@article@When to Use Webhooks, WebSocket, Pub/Sub, and Polling](https://hookdeck.com/webhooks/guides/when-to-use-webhooks)
- [@article@Polling vs webhooks: when to use one over the other](https://www.merge.dev/blog/webhooks-vs-polling)
- [@article@Best practices for using webhooks - GitHub Docs](https://docs.github.com/en/webhooks/using-webhooks/best-practices-for-using-webhooks)
- [@article@Validating webhook deliveries - GitHub Docs](https://docs.github.com/en/webhooks/using-webhooks/validating-webhook-deliveries)