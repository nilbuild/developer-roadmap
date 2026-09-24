# -replace option in apply

The `-replace` flag on `terraform apply` forces Terraform to destroy and recreate a specific resource even if no configuration changes would normally trigger replacement. It is used to resolve issues with a corrupted or degraded resource that needs to be rebuilt. This replaces the older `taint` command.

Visit the following resources to learn more:

- [@official@Forcing Re-creation of Resources](https://developer.hashicorp.com/terraform/cli/state/taint)
- [@article@Terraform Taint, Untaint, Replace – How to Use It (Examples)](https://spacelift.io/blog/terraform-taint)
- [@video@Terraform Taint Is Bad Actually - Use Replace Instead](https://www.youtube.com/watch?v=v_T1fuYGjV0)