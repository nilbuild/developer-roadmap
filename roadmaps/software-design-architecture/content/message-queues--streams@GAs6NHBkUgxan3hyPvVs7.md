# Message Queues Streams

Message queues and streams are infrastructure components that store and pass messages between producers and consumers, allowing them to operate independently and at different speeds. A queue typically delivers each message to one consumer and removes it once processed, while a stream keeps an ordered log of events that multiple consumers can read and replay. Tools like RabbitMQ, Kafka, and Amazon SQS implement these patterns to support asynchronous, decoupled communication between services.

Visit the following resources to learn more:

- [@article@System Design — Message Queues](https://medium.com/must-know-computer-science/system-design-message-queues-245612428a22)
- [@article@Overview of Message Queue pattern](https://badia-kharroubi.gitbooks.io/microservices-architecture/content/patterns/communication-patterns/message-queue-pattern.html)