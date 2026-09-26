# Keep framework code distant

Keeping framework code distant is a design practice that aims to decouple core business logic from the specific libraries or frameworks being used. It involves wrapping third-party tools within abstraction layers, such as interfaces or adapter classes, so that the application remains agnostic of the framework’s internal implementation. This approach ensures that if a framework needs to be updated, replaced, or removed, the impact on the codebase is minimized because the business rules are not directly tied to external dependencies.

Visit the following resources to learn more:

- [@article@Clean architecture](https://pusher.com/tutorials/clean-architecture-introduction/)
- [@feed@Explore top posts about General Programming](https://app.daily.dev/tags/general-programming?ref=roadmapsh)