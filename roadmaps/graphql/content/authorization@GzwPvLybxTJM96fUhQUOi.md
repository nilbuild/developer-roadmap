# Authorization in GraphQL Over WebSockets

Authorization in GraphQL over WebSockets involves validating that a client has the necessary permissions to maintain a persistent connection and receive specific real-time updates. Since standard HTTP headers are typically only sent during the initial handshake, authorization is often handled during the connection initialization phase by passing authentication tokens through connection parameters. Once the connection is established, the server verifies these credentials against the requested operations to ensure that data access remains secure throughout the lifecycle of the subscription.

Visit the following resources to learn more:

- [@official@Get Started with Authorization](https://graphql.org/learn/authorization/)
- [@feed@Explore top posts about Authorization](https://app.daily.dev/tags/authorization?ref=roadmapsh)