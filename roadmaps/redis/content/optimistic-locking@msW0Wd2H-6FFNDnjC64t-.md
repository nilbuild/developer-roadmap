# Optimistic Locking

Optimistic locking in Redis uses `WATCH` to detect concurrent modifications without holding a lock. The client reads a value, prepares a transaction, and calls `EXEC`: if the watched key changed since `WATCH`, the transaction is retried. This approach avoids blocking other clients while still preventing conflicting updates.

Visit the following resources to learn more:

- [@official@Optimistic Locking using CHECK & SET](https://redis.io/docs/latest/develop/interact/transactions/#optimistic-locking-using-check-and-set)
- [@official@WATCH Command](https://redis.io/docs/latest/commands/watch/)
- [@official@MULTI Command](https://redis.io/docs/latest/commands/multi/)