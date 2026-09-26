# Singleton

A Singleton service is created the first time it is requested or when the application starts, and the same instance is then shared across every subsequent request throughout the entire application lifetime. Because this single instance persists for the duration of the app, it is commonly used for managing shared state, configuration settings, or caching services that need to maintain data across different parts of the system.

Visit the following resources to learn more:

- [@article@What are Singleton Dependencies?](https://blazor-university.com/dependency-injection/dependency-lifetimes-and-scopes/transient-dependencies/)
- [@article@Dependency Injection Lifetime](https://www.tektutorialshub.com/asp-net-core/asp-net-core-dependency-injection-lifetime/)
- [@video@Dependency Injection Explained with Singleton](https://www.youtube.com/watch?v=NkTF_6IQPiY)