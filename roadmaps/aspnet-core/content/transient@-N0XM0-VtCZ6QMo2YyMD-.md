# Transient

Transient services are created every time they are requested from the service container. This lifecycle is ideal for lightweight, stateless services because a new instance is provided for every controller or service that requires it. Since these objects are not shared across different parts of the application, they avoid issues related to shared state.

Visit the following resources to learn more:

- [@article@What are Transient Dependencies?](https://blazor-university.com/dependency-injection/dependency-lifetimes-and-scopes/transient-dependencies/)
- [@article@Dependency Injection Lifetime](https://www.tektutorialshub.com/asp-net-core/asp-net-core-dependency-injection-lifetime/)
- [@video@Dependency Injection Explained with Transient](https://www.youtube.com/watch?v=NkTF_6IQPiY)