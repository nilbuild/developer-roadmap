# Memory Management

Redis provides several tools for managing memory usage. The `maxmemory` directive caps the amount of RAM Redis can use, and `maxmemory-policy` determines what happens when the limit is reached (e.g., evicting least-recently-used keys). Commands like `MEMORY USAGE` and `DEBUG OBJECT` help inspect per-key memory consumption.

Visit the following resources to learn more:

- [@official@MEMORY USAGE Command](https://redis.io/docs/latest/commands/memory-usage/)
- [@official@MEMORY STATS Command](https://redis.io/docs/latest/commands/memory-stats/)
- [@article@Memory Management Best Practices](https://cloud.google.com/memorystore/docs/redis/memory-management-best-practices)