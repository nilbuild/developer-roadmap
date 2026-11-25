# Strangler Fig

The strangler fig pattern migrates a legacy system one piece of functionality at a time instead of rewriting it all at once. A facade or proxy in front of the legacy system routes each request either to the old code or to the new service that replaces it, so clients keep using the same interface. Once all functionality has moved, the legacy system is decommissioned and the facade removed.

Visit the following resources to learn more:

- [@article@Strangler Fig - Martin Fowler](https://martinfowler.com/bliki/StranglerFigApplication.html)
- [@article@What is Strangler fig?](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig)
- [@article@Strangler fig pattern - AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/strangler-fig.html)
- [@article@Strangler Fig Routing with Feature Flags - Unleash](https://docs.getunleash.io/guides/feature-flags-for-migrations#strangler-fig)