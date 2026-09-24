# lifecycle

The `lifecycle` block inside a resource configures how Terraform handles creation, updates, and deletion of that resource. It supports arguments like `create_before_destroy`, `prevent_destroy`, `ignore_changes`, and `replace_triggered_by`. These settings give you fine-grained control over resource replacement behavior.

Visit the following resources to learn more:

- [@official@Terraform Docs - lifecycle](https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle)
- [@article@Terraform Resource Lifecycle](https://spacelift.io/blog/terraform-resource-lifecycle)
- [@article@Understanding the Lifecycle Block](https://dev.to/pwd9000/terraform-understanding-the-lifecycle-block-4f6e)