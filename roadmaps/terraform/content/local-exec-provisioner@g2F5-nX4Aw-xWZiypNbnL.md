# local-exec provisioner

The `local-exec` provisioner runs a command on the machine executing Terraform, not on the remote resource. It is used for tasks like triggering an external API, running a local script, or writing data to a file. The command runs in a shell, and the working directory defaults to the Terraform configuration directory.

Visit the following resources to learn more:

- [@official@local-exec Provisioner](https://developer.hashicorp.com/terraform/language/resources/provisioners/local-exec)
- [@article@Local-Exec Provisioner](https://learning-ocean.com/tutorials/terraform/terraform-local-exec-provisioner/)
- [@video@Terraform - Local exec](https://www.youtube.com/watch?v=2dVq8L2LBc0)