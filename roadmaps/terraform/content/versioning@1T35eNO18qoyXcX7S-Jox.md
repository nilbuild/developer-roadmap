# Versioning

State files can be versioned using backends that support versioning, such as S3 with versioning enabled. Keeping a history of state versions allows you to roll back to a previous state if a bad apply corrupts or loses data. Terraform Cloud and Enterprise provide built-in state history and the ability to restore past versions.

Visit the following resources to learn more:

- [@official@State Versions API](https://developer.hashicorp.com/terraform/cloud-docs/api-docs/state-versions)