# Async/Await

An `async` function always returns a promise. Inside an async function, `await` pauses execution until a promise settles, then yields its fulfillment value or throws its rejection reason. It suspends the function rather than blocking the event loop, so other work can continue. Code before the first `await` still runs synchronously.

Visit the following resources to learn more:

- [@official@Async/Await Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
- [@article@More on async await](https://javascript.info/async-await)
- [@video@Using async await](https://www.youtube.com/watch?v=V_Kr9OSfDeU)
