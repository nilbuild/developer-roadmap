# @MockBean Annotation

In Spring Boot 3.x, `@MockBean` lets tests register a Mockito mock in the Spring `ApplicationContext`, replacing an existing bean when one matches. It was deprecated in Spring Boot 3.4 and removed in Spring Boot 4.0. Use Spring Framework's `@MockitoBean` instead, typically on a field in a test class, or on a test class with its `types` attribute. Migration is not always a direct replacement: unlike `@MockBean`, `@MockitoBean` cannot be declared on `@Configuration` classes.

Visit the following resources to learn more:

- [@official@Spring Boot 3.4 `@MockBean` API](https://docs.spring.io/spring-boot/3.4/api/java/org/springframework/boot/test/mock/mockito/MockBean.html)
- [@official@Spring Boot 4.0 Migration Guide](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide)
- [@official@Spring Framework `@MockitoBean` Documentation](https://docs.spring.io/spring-framework/reference/testing/annotations/integration-spring/annotation-mockitobean.html)
