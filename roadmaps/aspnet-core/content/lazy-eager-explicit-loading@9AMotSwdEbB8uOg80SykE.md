# Lazy, Eager, and Explicit Loading

Loading patterns in Entity Framework Core determine how and when related data is retrieved from the database when querying a primary entity. Eager loading fetches related data immediately as part of the initial query using the `Include` method. Lazy loading automatically retrieves related data from the database only at the moment a navigation property is accessed in the code. Explicit loading allows developers to manually trigger the retrieval of related data for an entity that has already been loaded, typically using the `Entry` API. Each approach offers a different trade-off between database round-trips and the amount of data transferred, allowing developers to optimize application performance based on specific data access requirements.

Visit the following resources to learn more:

- [@article@Eager Loading & Lazy Loading](https://www.c-sharpcorner.com/article/eager-loading-lazy-loading-and-explicit-loading-in-entity-framework/)
- [@article@Difference between Eager and Lazy Loading](https://stackoverflow.com/questions/31366236/lazy-loading-vs-eager-loading)
- [@article@Working With Lazy & Eager Loading in Entity Framework](https://dzone.com/articles/working-with-lazy-loading-and-eager-loading-in-ent)