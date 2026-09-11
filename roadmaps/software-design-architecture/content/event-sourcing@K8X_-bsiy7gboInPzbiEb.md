# Event Sourcing

Event sourcing stores the state of an application as a sequence of events rather than storing only the current state. Each change to the system is captured as an immutable event, and the current state is derived by replaying those events in order. This approach provides a complete audit trail of every change and makes it possible to reconstruct past states, though it requires careful handling of event versioning and storage growth over time.

Visit the following resources to learn more:

- [@article@Event Sourcing Pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing)
- [@video@Event Sourcing Example & Explained](https://www.youtube.com/watch?v=AUj4M-st3ic&list=PLThyvG1mlMzkRKJnhzvxtSAbY8oxENLUQ&ab_channel=CodeOpinion)
- [@video@Event Sourcing Explained Using Football](https://www.youtube.com/watch?v=xPmQxYIi5fA&list=PLCl5BUbK0jXt5l18S5UNAoUc4eQ2PJDye)
- [@feed@Explore top posts about Architecture](https://app.daily.dev/tags/architecture?ref=roadmapsh)