# Parallelism

Terraform applies resource changes in parallel by default, up to a configurable limit controlled by the `-parallelism` flag. Increasing parallelism can speed up large deployments but may hit API rate limits. Lowering it can reduce throttling errors when working with providers that enforce strict rate limits.

Visit the following resources to learn more:

- [@official@Walking the graph](https://developer.hashicorp.com/terraform/internals/graph#walking-the-graph)
- [@article@Considerations when setting the TFE_PARALLELISM environment variable](https://support.hashicorp.com/hc/en-us/articles/10348130482451-Considerations-when-setting-the-TFE-PARALLELISM-environment-variable)