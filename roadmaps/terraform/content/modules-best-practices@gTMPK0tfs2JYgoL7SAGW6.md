# Modules Best Practices

Modules should be focused on a single concern and avoid hardcoding values that callers need to control. Always declare types for input variables and provide descriptions. Version-pin external modules and keep local modules small and composable. Avoid deeply nested module hierarchies, as they are harder to debug and maintain.

Visit the following resources to learn more:

- [@official@Module Best Practices](https://developer.hashicorp.com/terraform/tutorials/modules/module#module-best-practices)
- [@article@Terraform Modules Guide: Best Practices & Examples](https://www.env0.com/blog/terraform-modules)
- [@video@Best practices for modularizing a Terraform project | PlatformCon 2023](https://www.youtube.com/watch?v=byzwaTng3ac)