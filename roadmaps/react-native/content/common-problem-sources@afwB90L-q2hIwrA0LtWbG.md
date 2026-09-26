# Common Problem Sources in React Native Performance

Performance issues in React Native often stem from an overloaded JavaScript thread, which handles business logic, API calls, and state management. When this thread becomes blocked by heavy computations or excessive re-renders, the user interface feels unresponsive or choppy. Other frequent causes include inefficient list rendering, large image assets that consume excessive memory, and unnecessary communication overhead between the JavaScript bridge and the native modules. Identifying these bottlenecks involves analyzing how components update their state and ensuring that resource-intensive tasks are offloaded to native code or handled asynchronously.

Visit the following resources to learn more:

- [@official@Performance Problems](https://reactnative.dev/docs/performance#common-sources-of-performance-problems)