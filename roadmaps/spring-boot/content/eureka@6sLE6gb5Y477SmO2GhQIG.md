# Eureka

Eureka is a service discovery tool from Netflix, integrated into Spring Cloud, that lets microservices register themselves and find other services by name instead of hardcoded addresses. Each service instance registers with a Eureka server on startup and sends periodic heartbeats to confirm it is still available. Other services query the Eureka server to look up healthy instances of a service before making a request, which supports load balancing and failover.

Visit the following resources to learn more:

- [@article@Introduction to Spring Cloud Netflix – Eureka](https://www.baeldung.com/spring-cloud-netflix-eureka)
- [@article@Spring Boot - Eureka Server](https://www.tutorialspoint.com/spring_boot/spring_boot_eureka_server.htm)
- [@video@Introducing Spring Cloud EUREKA](https://www.youtube.com/watch?v=1uNo1NrqsX4)