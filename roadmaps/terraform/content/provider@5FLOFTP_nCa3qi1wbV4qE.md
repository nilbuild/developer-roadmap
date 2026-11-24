# provider

The `provider` meta-argument assigns a specific provider configuration to a resource when multiple configurations of the same provider exist. This is common when managing resources across multiple regions or accounts within the same Terraform workspace. The value must match an alias defined in a `provider` block.

Visit the following resources to learn more:

- [@article@Terraform by Example - provider](https://www.terraformbyexample.com/providers/)