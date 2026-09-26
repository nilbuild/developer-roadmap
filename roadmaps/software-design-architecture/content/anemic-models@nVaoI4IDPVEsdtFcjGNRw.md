# Anemic Models

Anemic models are domain objects that contain little or no business logic, acting primarily as simple data holders with public getters and setters. In this design, the actual behavior and decision-making logic are placed in separate service classes, which interact with the data objects to perform operations. While this approach separates data from logic, it often leads to a procedural style of programming where the richness of the domain model is lost and the responsibility for maintaining data integrity is shifted to external services.

Visit the following resources to learn more:

- [@article@Overview of Anemic Domain Model](https://en.wikipedia.org/wiki/Anemic_domain_model)