# Creating Local Modules

Local modules are directories containing Terraform configuration files that are referenced using a relative file path in a `module` block. They allow you to break a large configuration into smaller, self-contained units. Inputs are passed via variables and outputs are declared for the parent module to consume.

Visit the following resources to learn more:

- [@official@Build and use a local module](https://developer.hashicorp.com/terraform/tutorials/modules/module-create)
- [@article@How to create reusable infrastructure with Terraform modules](https://blog.gruntwork.io/how-to-create-reusable-infrastructure-with-terraform-modules-25526d65f73d)
- [@video@Creating a module in Terraform](https://www.youtube.com/watch?v=OeL2AlsdNaQ)