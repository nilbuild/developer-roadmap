# state force-unlock

`terraform state force-unlock` manually releases a state lock that was not properly released after an interrupted operation. It requires the lock ID, which is displayed in the error message shown when a lock conflict is detected. This command should only be used when you are certain no other Terraform operation is running.

Visit the following resources to learn more:

- [@official@Command: force-unlock](https://developer.hashicorp.com/terraform/cli/commands/force-unlock)
- [@article@Terraform force-unlock command](https://spacelift.io/blog/terraform-force-unlock)
- [@video@Terraform — Force Unlock](https://www.youtube.com/watch?v=qVs9pLaXSeg)