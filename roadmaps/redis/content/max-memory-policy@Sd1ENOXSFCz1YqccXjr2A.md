# Max Memory Policy

The `maxmemory-policy` setting controls how Redis selects keys to evict when the memory limit is reached. Options include evicting the least recently used key (`allkeys-lru`), evicting keys with TTLs set (`volatile-lru`), or returning errors instead of evicting (`noeviction`). Choosing the right policy depends on whether all data is equally valuable or only cached data is expendable.

Visit the following resources to learn more:

- [@official@Database Memory Limits](https://redis.io/docs/latest/operate/rs/databases/memory-performance/memory-limit/)
- [@official@Eviction Policy](https://redis.io/docs/latest/operate/rs/databases/memory-performance/eviction-policy/)