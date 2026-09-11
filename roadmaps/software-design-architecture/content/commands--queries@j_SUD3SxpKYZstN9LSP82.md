# Commands Queries

The Command and Query Responsibility Segregation (CQRS) pattern separates operations that change a system's state, called commands, from operations that read data, called queries. A command performs an action such as creating or updating a record and returns no data, while a query returns data without producing any side effects. Keeping these two categories distinct clarifies the intent of each operation and makes it easier to scale or cache reads independently of writes.

Visit the following resources to learn more:

- [@article@Get Started with CQRS Pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs)