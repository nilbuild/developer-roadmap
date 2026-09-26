# Best Practices for State

State should never be stored in version control, as it may contain sensitive values and is not designed for manual editing. Use a remote backend with locking and versioning enabled. Keep state files small by splitting large configurations into smaller modules with independent state, and run `terraform refresh` carefully as it overwrites state with live data.

Visit the following resources to learn more:

- [@article@Managing Terraform State – Best Practices & Examples](https://spacelift.io/blog/terraform-state)
- [@article@Best Practices for Terraform State File Management](https://www.cloudthat.com/resources/blog/best-practices-for-terraform-state-file-management)
- [@video@Managing Terraform State Files - What are your options?](https://www.youtube.com/watch?v=keiIyarEKf8)