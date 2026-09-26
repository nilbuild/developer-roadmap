# Authentication

HCP Terraform authenticates users and services through API tokens. User tokens are generated in the account settings and used for CLI access. Service account tokens are used in CI/CD pipelines. The `terraform login` command stores credentials locally for CLI use.

Visit the following resources to learn more:

- [@official@HCP Authentication](https://developer.hashicorp.com/hcp/docs/cli/commands/auth/login)
- [@official@Authenticate with HCP](https://registry.terraform.io/providers/hashicorp/hcp/latest/docs/guides/auth)
- [@opensource@hashicorp/hcp-auth-login](https://github.com/hashicorp/hcp-auth-action)