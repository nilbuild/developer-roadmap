# Development / Release Workflow

A development and release workflow defines how code moves from an engineer's local machine to production. This includes branching strategies, code review gates, staging environments, and deployment processes. One branching strategy is trunk-based development, where engineers merge small changes to the main branch at least once a day and often hide unfinished work behind feature flags, which separates deploying code from releasing features. Engineering managers ensure the workflow is documented, consistently followed, and adjusted when it creates friction.

Visit the following resources to learn more:

- [@article@Patterns for Managing Source Code Branches - Martin Fowler](https://martinfowler.com/articles/branching-patterns.html)
- [@article@Trunk-Based Development - DORA](https://dora.dev/capabilities/trunk-based-development/)
- [@article@Trunk-Based Development with Feature Flags - Unleash](https://docs.getunleash.io/guides/trunk-based-development)