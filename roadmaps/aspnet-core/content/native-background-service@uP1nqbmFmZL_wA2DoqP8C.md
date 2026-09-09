# Native Background Service

A Native Background Service is a class in ASP.NET Core that implements the `IHostedService` interface or inherits from the `BackgroundService` base class to execute long-running tasks in the background. These services run independently of the request-response cycle, allowing the application to perform periodic operations like data cleanup, message queue processing, or scheduled report generation. The framework manages the lifecycle of these services, ensuring they start when the application host begins and shut down gracefully when the host stops.

Visit the following resources to learn more:

- [@article@Background tasks with hosted services in ASP.NET](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/hosted-services?view=aspnetcore-7.0&tabs=visual-studio)
- [@article@BackgroundService in ASP.NET Core](https://medium.com/@daniel.sagita/backgroundservice-for-a-long-running-work-3debe8f8d25b)
- [@video@Tutorial on Background Tasks in ASP.NET](https://youtube.com/watch?v=rugxQIH_p3A)