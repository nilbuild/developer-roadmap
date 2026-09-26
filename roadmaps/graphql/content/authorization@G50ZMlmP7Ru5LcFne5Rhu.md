# GraphQL Over SSE Authorization

Authorization for GraphQL over Server-Sent Events (SSE) involves verifying a client's identity and permissions before establishing a persistent stream of data. Since standard HTTP headers are only sent during the initial handshake of an SSE connection, authentication tokens are typically passed via query parameters or specialized sub-protocols when the request is first initiated. Once the connection is established, the server enforces access control rules to ensure that the events pushed to the client match the data the user is authorized to receive.

Visit the following resources to learn more:

- [@official@Get Started with Authorization](https://graphql.org/learn/authorization/)
- [@feed@Explore top posts about Authorization](https://app.daily.dev/tags/authorization?ref=roadmapsh)