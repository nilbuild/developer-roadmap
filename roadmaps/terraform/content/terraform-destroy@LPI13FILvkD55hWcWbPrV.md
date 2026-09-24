# terraform destroy

`terraform destroy` removes all resources managed by the current configuration. It is the equivalent of running `terraform apply` with every resource marked for deletion. Like apply, it shows a plan and prompts for confirmation before proceeding. Individual resources can also be targeted with the `-target` flag.

Visit the following resources to learn more:

- [@course@Destroy infrastructure](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/aws-destroy)
- [@official@Terraform Destroy Documentation](https://developer.hashicorp.com/terraform/cli/commands/destroy)
- [@article@How to destroy Terraform resources](https://spacelift.io/blog/how-to-destroy-terraform-resources)