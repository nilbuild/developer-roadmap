# Async errors

Asynchronous errors are handled according to the API. For promise-based code, use `.catch()` or wrap an awaited promise in `try...catch`; a surrounding `try...catch` does not catch an exception thrown later inside a callback. Error-first callbacks report failures through their first argument, and event emitters may emit an `'error'` event that needs a listener.

Visit the following resources to learn more:

- [@article@Async Errors](https://www.mariokandut.com/handling-errors-in-asynchronous-functions-node-js/)
