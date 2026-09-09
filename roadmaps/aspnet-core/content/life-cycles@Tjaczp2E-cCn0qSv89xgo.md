# Dependency Injection Life Cycles

Dependency Injection life cycles define how and when the container creates and disposes of service instances within an application. There are three primary lifetimes: Transient, which creates a new instance every time a service is requested; Scoped, which creates a single instance for the duration of a single client request; and Singleton, which creates a single shared instance the first time it is requested and uses that same instance for every subsequent request throughout the application's lifetime.

Visit the following resources to learn more:

- [@article@What are Service Life Cycles in ASP.NET Core?](https://endjin.com/blog/2022/09/service-lifetimes-in-aspnet-core)
- [@article@Learn Service Lifetimes in .NET Core](https://henriquesd.medium.com/dependency-injection-and-service-lifetimes-in-net-core-ab9189349420)
- [@video@Complete Guide to Dependency Injection Lifecycles](https://www.youtube.com/watch?v=wA5bPsv2CLA)