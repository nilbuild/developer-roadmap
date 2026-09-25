# Reactor

The Reactor pattern dispatches events to handlers based on I/O readiness. A central event loop monitors sockets using mechanisms like select, poll, epoll, or kqueue, and calls the appropriate handler when a socket is ready to read or write without blocking.

Visit the following resources to learn more:

- [@article@Reactor Pattern - Wikipedia](https://en.wikipedia.org/wiki/Reactor_pattern)
- [@article@Blocking vs Non-Blocking - Node.js Docs](https://nodejs.org/en/learn/asynchronous-work/overview-of-blocking-vs-non-blocking)
- [@article@Reactor Pattern in Java - Java Design Patterns](https://java-design-patterns.com/patterns/reactor/)