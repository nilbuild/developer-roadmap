# CQRS

Command Query Responsibility Segregation, or CQRS, separates the operations that change data, called commands, from the operations that read data, called queries, often using different models for each. This separation allows the read and write sides of a system to be optimized, scaled, and even stored independently. CQRS is often paired with event sourcing, since events naturally represent the commands that changed the system's state.

Visit the following resources to learn more:

- [@article@Get Started with CQRS Pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs)
- [@article@CQRS Software Architecture Pattern: The Good, Bad, and the Ugly](https://betterprogramming.pub/cqrs-software-architecture-pattern-the-good-the-bad-and-the-ugly-e9d6e7a34daf)