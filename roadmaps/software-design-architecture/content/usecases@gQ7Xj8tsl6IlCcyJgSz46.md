# Use Cases

A use case describes a specific interaction or process that a system supports to fulfill a user's goal, often expressed as a single class or function that orchestrates the steps needed to complete that goal. It sits between the presentation layer and the domain model, coordinating calls to entities, repositories, and other services without containing the core business rules itself. This separation keeps business logic testable and independent from how a request enters the system, whether through a web request, a command line, or an API call.

Visit the following resources to learn more:

- [@article@Use Case Patterns](https://caminao.blog/how-to-implement-symbolic-representations/patterns/functional-patterns/use-case-patterns/)