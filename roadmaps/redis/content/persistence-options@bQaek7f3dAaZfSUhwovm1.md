# Persistence Options

Redis offers multiple strategies for persisting in-memory data to disk so it can be recovered after a restart. The two main mechanisms are RDB snapshots and the Append-Only File. Each has different trade-offs between performance, durability, and recovery speed.

Visit the following resources to learn more:

- [@official@Data Persistence](https://redis.io/docs/latest/operate/rc/databases/configuration/data-persistence/)
- [@official@Redis Persistence](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/)