# API Clients and Communication

API clients in ASP.NET Core are components used to send HTTP requests to external web services and receive responses. The framework provides the `IHttpClientFactory` to manage the lifetime and configuration of `HttpClient` instances, which helps prevent socket exhaustion and DNS issues. Developers use these tools to consume RESTful endpoints, handle serialization of JSON data, and manage cross-service communication within a distributed application architecture.

Visit the following resources to learn more:

- [@article@How to Call a Web API From a .NET Client](https://learn.microsoft.com/en-us/aspnet/web-api/overview/advanced/calling-a-web-api-from-a-net-client)
- [@article@Overview of Web API REST Service in ASP.NET](https://www.c-sharpcorner.com/article/consuming-asp-net-web-api-rest-service-in-asp-net-mvc-using-http-client/)
- [@article@Building an ASP.NET Web API With ASP.NET](https://www.toptal.com/asp-dot-net/asp-net-web-api-tutorial)