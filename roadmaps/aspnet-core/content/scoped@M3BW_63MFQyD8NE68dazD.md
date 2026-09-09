# Scoped Service Lifetime

Scoped services are created once per client request within an ASP.NET Core application. When you register a service with a scoped lifetime, the framework generates a new instance for every individual HTTP request and shares that same instance across all components that process that specific request. This ensures that data remains consistent throughout the entire lifecycle of a single user interaction while preventing the service from persisting across different, unrelated requests.

Visit the following resources to learn more:

- [@article@Dependency Injection - What is Scope?](https://javaranch.com/journal/2008/10/dependency-injection-what-is-scope.html)
- [@article@Effective Dependency Injection Scoping](https://medium.com/android-news/effective-dependency-injection-scoping-4bac813d4491)