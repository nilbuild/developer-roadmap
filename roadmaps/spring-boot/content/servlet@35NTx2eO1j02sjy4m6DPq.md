# Servlet

A servlet is a Java class that handles requests and generates responses within a web server, following the Java Servlet API. It works by receiving an HTTP request from a servlet container, such as Tomcat, processing it through a `service` method, and writing back a response. Spring MVC builds on top of servlets, using a single central servlet, `DispatcherServlet`, to route requests to application code instead of requiring developers to write servlets directly.

Visit the following resources to learn more:

- [@official@The DispatcherServlet](https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-servlet.html)
- [@article@DispatcherServlet and web.xml in Spring Boot](https://www.baeldung.com/spring-boot-dispatcherservlet-web-xml)