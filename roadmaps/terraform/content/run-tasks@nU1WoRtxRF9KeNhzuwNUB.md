# Run Tasks

Run Tasks are integrations that execute external services at specific points in the Terraform run lifecycle, such as after a plan or before an apply. They can be used to trigger security scans, cost checks, or custom validation logic. Run tasks return a pass or fail result that can block or allow the apply from proceeding.

Visit the following resources to learn more:

- [@official@Run Tasks](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/settings/run-tasks)
- [@official@Terraform Registry - Run Tasks](https://registry.terraform.io/browse/run-tasks)
- [@official@Run Tasks API](https://developer.hashicorp.com/terraform/cloud-docs/api-docs/run-tasks/run-tasks)