# for_each

The `for_each` meta-argument creates one instance of a resource or module for each item in a map or set of strings. Each instance is keyed by the map key or set value, making it easier to manage and reference individual items than with `count`. It is generally preferred over `count` when creating resources from a collection.

Visit the following resources to learn more:

- [@official@Terraform Docs - for_each](https://developer.hashicorp.com/terraform/language/meta-arguments/for_each)
- [@article@Terraform by Example - for_each](https://www.terraformbyexample.com/for_each)
- [@video@Terraform for loops](https://www.youtube.com/watch?v=4qO7WK6D3cA)