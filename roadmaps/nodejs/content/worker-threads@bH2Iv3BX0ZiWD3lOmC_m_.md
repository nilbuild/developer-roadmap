# Worker Threads

Worker threads execute JavaScript in parallel within a Node.js process. They are useful for CPU-intensive tasks; the built-in asynchronous I/O APIs are generally more efficient for I/O-intensive work. Workers communicate through messages and can transfer `ArrayBuffer` instances or share `SharedArrayBuffer` memory. A worker can exit naturally when its event loop has no active work, so it does not have to be explicitly terminated. Shared memory still requires synchronization.

Visit the following resources to learn more:

- [@official@Worker Threads](https://nodejs.org/api/worker_threads.html#worker-threads)
