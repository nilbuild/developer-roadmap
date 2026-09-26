# Secret Management

Secrets such as API keys, passwords, and certificates should never be stored in Terraform configuration files or committed to version control. Common approaches include injecting secrets via environment variables, using a secrets manager like HashiCorp Vault or AWS Secrets Manager as a data source, or using a backend that encrypts sensitive state values.

Visit the following resources to learn more:

- [@official@Inject Secrets with Vault](https://developer.hashicorp.com/terraform/tutorials/secrets)
- [@article@Terraform Secrets - How to manage them](https://spacelift.io/blog/terraform-secrets)
- [@article@A comprehensive guide to managing secrets in your Terraform code](https://blog.gruntwork.io/a-comprehensive-guide-to-managing-secrets-in-your-terraform-code-1d586955ace1)