# Proactor

The Proactor pattern handles asynchronous I/O by dispatching completion events to handlers after an operation finishes. The OS or runtime performs the I/O in the background and notifies the application on completion, as opposed to the Reactor pattern where the application initiates I/O when readiness is signaled.

Visit the following resources to learn more:

- [@article@Proactor pattern - Wikipedia](https://en.wikipedia.org/wiki/Proactor_pattern)
- [@article@The Proactor Design Pattern: Concurrency Without Threads - Boost.Asio](https://www.boost.org/doc/libs/latest/doc/html/boost_asio/overview/core/async.html)
- [@article@If the Proactor Design Pattern is superior for asynchronous I/O - Stack Overflow](https://stackoverflow.com/questions/54798087/if-the-proactor-design-pattern-is-superior-for-asyncronous-i-o-why-isnt-it-def)