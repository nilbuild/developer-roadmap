# HyperLogLog

HyperLogLog is a probabilistic data structure that estimates the cardinality (count of unique items) of a set using a fixed amount of memory, regardless of how many items are added. Redis implements it using at most 12 KB per key. The estimate has a standard error of about 0.81%.

Visit the following resources to learn more:

- [@official@HyperLogLog Documentation](https://redis.io/docs/latest/develop/data-types/probabilistic/hyperloglogs/)
- [@video@Redis HyperLogLog Explained](https://www.youtube.com/watch?v=MunL8nnwscQ)