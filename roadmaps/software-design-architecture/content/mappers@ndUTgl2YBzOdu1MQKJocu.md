# Mappers

A mapper converts data between two different representations, such as translating a database row into a domain object or converting a domain object into a format suitable for an API response. This separation keeps the domain model free of persistence or transport concerns, since it does not need to know how it will be stored or transmitted. Mappers are often used alongside repositories and DTOs to keep each layer of an application focused on its own representation of data.

Visit the following resources to learn more:

- [@article@Overview of Data Mapper Pattern](https://en.wikipedia.org/wiki/Data_mapper_pattern)
- [@video@Tutorial - Mappers](https://www.youtube.com/watch?v=7noMLStHcTE)