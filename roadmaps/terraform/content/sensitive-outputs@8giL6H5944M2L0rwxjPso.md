# Sensitive Outputs

Marking an output as sensitive tells Terraform to redact its value from CLI output and logs. The value is still stored in state and can be accessed programmatically. This is commonly used for passwords, tokens, and other secrets that should not appear in plain text in terminal output.

Visit the following resources to learn more:

- [@official@Suppressing values in CLI output](https://developer.hashicorp.com/terraform/language/values/outputs#sensitive-suppressing-values-in-cli-output)
- [@article@How to output sensitive data in Terraform](https://support.hashicorp.com/hc/en-us/articles/5175257151891-How-to-output-sensitive-data-with-Terraform)