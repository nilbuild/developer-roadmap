# Remote State

Remote state stores the Terraform state file in a shared, remote backend such as S3, Azure Blob Storage, or Terraform Cloud. This allows multiple team members to work with the same state and prevents conflicts from concurrent operations. Remote backends also support state locking to prevent simultaneous writes.

Visit the following resources to learn more:

- [@official@Remote state](https://developer.hashicorp.com/terraform/language/state/remote)
- [@official@The terraform_remote_state Data Source](https://developer.hashicorp.com/terraform/language/state/remote-state-data)
- [@video@Terraform remote state backends explained](https://www.youtube.com/watch?v=jSoMQCBxp7E)