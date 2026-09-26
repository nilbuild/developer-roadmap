# Resource Lifecycle

The lifecycle meta-argument controls how Terraform manages a resource across plan and apply operations. Common settings include `create_before_destroy`, which ensures a replacement resource is created before the old one is removed, `prevent_destroy`, which blocks accidental deletion, and `ignore_changes`, which tells Terraform to ignore drift on specific attributes.

Visit the following resources to learn more:

- [@official@How Terraform Applies a Configuration](https://developer.hashicorp.com/terraform/language/resources/behavior#how-terraform-applies-a-configuration)
- [@official@The lifecycle Meta-Argument](https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle)
- [@article@@Article@Terraform Resource Lifecycle Meta-Argument](https://spacelift.io/blog/terraform-resource-lifecycle)