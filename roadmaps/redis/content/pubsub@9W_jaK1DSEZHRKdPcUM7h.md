# Pub/Sub

Redis Pub/Sub is a messaging pattern where publishers send messages to channels and subscribers receive them in real time. There is no message storage: if a subscriber is offline when a message is published, it will not receive it. This distinguishes Pub/Sub from Streams, which persist messages.

Visit the following resources to learn more:

- [@official@Pub/Sub in Redis](https://redis.io/docs/latest/develop/interact/pubsub/)