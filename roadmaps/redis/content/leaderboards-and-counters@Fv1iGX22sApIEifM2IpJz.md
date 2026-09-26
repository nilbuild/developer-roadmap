# Leaderboards and Counters

Sorted Sets in Redis are commonly used to implement leaderboards, where members are ranked by score and rankings update in real time. Atomic increment commands like INCR make counters accurate under concurrent writes without requiring locks. These capabilities make Redis practical for gaming scoreboards, voting systems, and rate limiting.

Visit the following resources to learn more:

- [@official@ZADD](https://redis.io/docs/latest/commands/zadd/)
- [@official@ZRANGE](https://redis.io/docs/latest/commands/zrange/)