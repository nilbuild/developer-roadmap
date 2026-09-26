# Public Subnet

A public subnet has a route to an Internet Gateway, making resources inside it reachable from the internet when they have a public IP. Load balancers and bastion hosts are commonly placed in public subnets. Instances in a public subnet still require a security group configured to allow inbound traffic.

Visit the following resources to learn more:

- [@official@Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)