# Hollywood Principle

The Hollywood Principle is a design strategy that dictates that high-level components should control the flow of an application while low-level components are only called upon when needed. Instead of low-level modules actively polling or calling higher-level functions, the system informs the lower-level parts of the application when it is their turn to execute. This approach minimizes dependencies and prevents tight coupling, as lower-level modules do not need to know about the internal logic or the existence of the components that invoke them.

Visit the following resources to learn more:

- [@video@Tutorial - Hollywood Principle](https://www.youtube.com/watch?v=lRuygpsXE5s)