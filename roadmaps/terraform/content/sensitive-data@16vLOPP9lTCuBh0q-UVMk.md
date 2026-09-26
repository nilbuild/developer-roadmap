# Sensitive Data

Terraform state may contain sensitive data such as passwords, private keys, and tokens returned by provider APIs. State files should be stored securely, with access restricted to authorized users and systems. Remote backends with encryption at rest and access controls are strongly recommended for any production use.

Visit the following resources to learn more:

- [@official@Sensitive data in state](https://developer.hashicorp.com/terraform/language/state/sensitive-data)
- [@official@Handling Sensitive Values in State](https://developer.hashicorp.com/terraform/plugin/best-practices/sensitive-state)
- [@video@Terraform — Protecting Sensitive Data](https://www.youtube.com/watch?v=yLc1YkB7DFo)