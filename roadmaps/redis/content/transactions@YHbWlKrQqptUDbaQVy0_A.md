# Transactions

Redis Transactions group a sequence of commands that execute atomically using `MULTI` and `EXEC`. All commands queued between these two are executed in order without interruption from other clients. If a client disconnects before calling `EXEC`, the queued commands are discarded.

Visit the following resources to learn more:

- [@official@Transactions](https://redis.io/docs/latest/develop/interact/transactions/)
- [@official@MULTI](https://redis.io/docs/latest/commands/multi/)
- [@official@EXEC](https://redis.io/docs/latest/commands/exec/)
- [@official@DISCARD](https://redis.io/docs/latest/commands/discard/)
- [@official@WATCH](https://redis.io/docs/latest/commands/watch/)