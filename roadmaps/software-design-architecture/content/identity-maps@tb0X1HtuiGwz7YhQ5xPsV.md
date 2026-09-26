# Identity Maps

An identity map is a pattern that keeps track of every object loaded from a database during a single unit of work, mapping each object to its unique identifier. When the same object is requested again, the identity map returns the existing instance instead of loading a new copy from the database. This avoids duplicate objects representing the same underlying data and helps maintain consistency when multiple parts of the code work with the same record.

Visit the following resources to learn more:

- [@article@Overview of Identity map pattern](https://en.wikipedia.org/wiki/Identity_map_pattern)
- [@video@Tutorial - Identity Map Design Pattern](https://youtube.com/watch?v=erDxkIyNudY)