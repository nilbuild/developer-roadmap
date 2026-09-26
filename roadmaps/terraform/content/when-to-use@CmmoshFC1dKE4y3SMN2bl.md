# When to Use?

Provisioners are appropriate when no provider resource or data source can accomplish the required task and the action must happen at resource creation or destruction time. Common use cases include running initialization scripts on a new server or notifying an external system after a resource is created. They should be avoided when alternatives exist because they add complexity and are harder to test.

Visit the following resources to learn more:

- [@article@Why You should Use Terraform Provisioners as a Final Option](https://thomasthornton.cloud/2023/05/11/my-thoughts-on-why-you-should-use-terraform-provisioners-as-a-final-option/)
- [@article@Why Terraform Provisioners Are The Last Resort?](https://k21academy.com/terraform-iac/terraform-provisioners/)