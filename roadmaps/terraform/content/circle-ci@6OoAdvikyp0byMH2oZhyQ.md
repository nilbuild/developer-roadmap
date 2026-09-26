# Circle CI

CircleCI can execute Terraform pipelines using orbs or custom job configurations. Jobs are defined in a `.circleci/config.yml` file and run in containers with the Terraform binary installed. It supports parallel jobs, caching, and approval steps that can be used to gate a `terraform apply` behind a manual review.

Visit the following resources to learn more:

- [@official@Deploy Infrastructure with Terraform and CircleCI](https://developer.hashicorp.com/terraform/tutorials/automation/circle-ci)
- [@opensource@CircleCI Terraform Orb](https://circleci.com/developer/orbs/orb/circleci/terraform)
- [@article@How I deployed terraform resources with CircleCI](https://medium.com/nerd-for-tech/how-i-deployed-terraform-resources-with-circleci-628aa29ed514)