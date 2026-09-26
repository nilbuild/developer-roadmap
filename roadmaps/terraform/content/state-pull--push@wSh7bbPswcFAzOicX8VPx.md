# state pull / push

`terraform state pull` downloads the current remote state and prints it to stdout. `terraform state push` uploads a local state file to the configured backend, overwriting the remote state. These commands are used for manual state recovery or migration and should be used with caution.

Visit the following resources to learn more:

- [@official@Command - State pull](https://developer.hashicorp.com/terraform/cli/commands/state/pull)
- [@official@Command - State push](https://developer.hashicorp.com/terraform/cli/commands/state/push)
- [@article@Migrate Workspace State Using Terraform State Push / Pull](https://support.hashicorp.com/hc/en-us/articles/360001151948-Migrate-Workspace-State-Using-Terraform-State-Push-Pull)