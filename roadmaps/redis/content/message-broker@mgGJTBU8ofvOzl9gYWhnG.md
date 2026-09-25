# Message Broker

Redis can act as a lightweight message broker using its Pub/Sub system or Streams. Producers publish messages to channels or streams, and consumers receive them either in real time or by reading from a persistent log. This makes Redis useful for decoupling services in event-driven architectures.

Visit the following resources to learn more:

- [@official@PUBLISH Command](https://redis.io/docs/latest/commands/publish/)
- [@official@SUBSCRIBE Command](https://redis.io/docs/latest/commands/subscribe/)
- [@article@Redis As a Message Broker](https://medium.com/shoutloudz/redis-as-a-message-broker-d1a1aeac23c3)