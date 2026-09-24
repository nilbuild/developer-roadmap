# Splitting State Files

Large Terraform configurations can be split into multiple state files by organizing resources into separate workspaces or root modules. This reduces the blast radius of plan and apply operations, speeds up plans, and makes it easier for teams to work independently on different parts of the infrastructure.

Visit the following resources to learn more:

- [@article@How to split state files](https://support.hashicorp.com/hc/en-us/articles/7955227415059-How-to-Split-State-Files)
- [@article@Introducing terraform-state-split](https://www.shebanglabs.io/moving-terraform-resources-between-different-states/)
- [@video@Organizing Terraform with multiple states](https://www.youtube.com/watch?v=5TfgdKXr45I)