# Latency Percentiles

Mean latency hides outliers. LLM response times follow a right-skewed distribution, so engineers measure P50, P90, P95, and P99. A P99 of several seconds means one in a hundred users has a poor experience even if the median is fast. Reducing P90/P99 latency is as important as reducing average latency.

Visit the following resources to learn more:

- [@article@Percentiles vs averages: why your latency dashboard lies](https://clickhouse.com/resources/engineering/percentiles-vs-averages)
- [@article@Latency percentiles for load testing analysis](https://gatling.io/blog/latency-percentiles-for-load-testing-analysis)
- [@video@Mastering Latency Metrics: P90, P95, P99 | System Design](https://www.youtube.com/watch?v=lJ4NEMNBeS4)