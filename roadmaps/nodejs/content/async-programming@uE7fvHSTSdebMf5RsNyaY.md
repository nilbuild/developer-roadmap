# Async Programming

Asynchronous APIs let an operation complete later while other JavaScript continues to run. Declaring a function `async` does not move its code onto a background thread: it runs synchronously until it reaches an `await`, which suspends that function. Promises and `await` can express dependencies and control ordering; CPU-intensive synchronous work still blocks the event loop.

Visit the following resources to learn more:

- [@article@Introduction to Async JS](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Introducing/)
- [@video@Asynchronous Vs Synchronous Programming](https://www.youtube.com/watch?v=Kpn2ajSa92c)
