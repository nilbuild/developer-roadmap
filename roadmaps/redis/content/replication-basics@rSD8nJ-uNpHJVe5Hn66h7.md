# Replication Basics

Redis replication allows one primary instance to replicate its data to one or more replica instances in real time. Replicas receive a stream of write commands from the primary and apply them to maintain an identical dataset. Replication is asynchronous by default and is the foundation for high availability setups.

Visit the following resources to learn more:

- [@official@Redis Replication](https://redis.io/docs/latest/operate/oss_and_stack/management/replication/)