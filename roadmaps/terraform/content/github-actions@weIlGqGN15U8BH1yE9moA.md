# GitHub Actions

GitHub Actions can run Terraform commands as part of a workflow triggered by pull requests or pushes. Workflows are defined in YAML files and can use community actions from the GitHub Marketplace or call the Terraform CLI directly. Secrets for provider credentials are stored in the repository settings and injected as environment variables.

Visit the following resources to learn more:

- [@official@GitHub Actions](https://docs.github.com/en/actions)
- [@official@Automate Terraform with GitHub Actions](https://developer.hashicorp.com/terraform/tutorials/automation/github-actions)
- [@opensource@setup-terraform](https://github.com/hashicorp/setup-terraform)
- [@article@Terraform with GitHub Actions : How to Manage & Scale](https://spacelift.io/blog/github-actions-terraform)