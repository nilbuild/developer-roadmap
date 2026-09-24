# CI / CD Integration

Integrating Terraform into a CI/CD pipeline automates infrastructure changes through the same review and deployment process used for application code. A typical pipeline runs `terraform fmt`, `terraform validate`, and `terraform plan` on pull requests, and `terraform apply` on merges to the main branch. Automation reduces human error and enforces a consistent workflow.