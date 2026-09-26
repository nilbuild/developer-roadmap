# Unit Testing

Unit tests for Terraform validate individual modules in isolation, checking that inputs produce the expected plan output without provisioning real resources. The native `terraform test` command introduced in Terraform 1.6 supports this by running configurations in a controlled context. Tools like Terratest can also be used for more complex scenarios.

Visit the following resources to learn more:

- [@official@Integration or Unit Testing](https://developer.hashicorp.com/terraform/language/tests#integration-or-unit-testing)
- [@article@Terraform Unit Tests](https://www.hashicorp.com/blog/testing-hashicorp-terraform#unit-tests)