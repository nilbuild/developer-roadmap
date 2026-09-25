# Pub/Sub Messaging

Redis Pub/Sub allows publishers to send messages to named channels and subscribers to receive them in real time. It follows a fire-and-forget model: messages are delivered to active subscribers but are not stored if no subscriber is listening. This pattern works well for live notifications, chat systems, and broadcasting events.

Visit the following resources to learn more:

- [@official@Redis Pub/Sub](https://redis.io/docs/latest/develop/interact/pubsub/)
- [@official@PUBLISH Command](https://redis.io/docs/latest/commands/publish/)
- [@official@SUBSCRIBE Command](https://redis.io/docs/latest/commands/subscribe/)
- [@official@UNSUBSCRIBE Command](https://redis.io/docs/latest/commands/unsubscribe/)