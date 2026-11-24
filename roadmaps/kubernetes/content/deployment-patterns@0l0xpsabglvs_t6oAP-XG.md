# Deployment Patterns

Deployment patterns describe how a new version of an application replaces the running one, and each pattern trades rollout speed against downtime, extra capacity and how many users a bad release can reach. A Kubernetes Deployment has two built-in strategies: `RollingUpdate`, the default, which replaces old Pods with new ones a few at a time, and `Recreate`, which stops all old Pods before starting new ones. Blue-green and canary deployments build on these primitives by running two versions side by side and controlling which one receives traffic, usually through Services, an Ingress controller or a service mesh.

Visit the following resources to learn more:

- [@official@Deployment Strategy - Kubernetes Documentation](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#strategy)
- [@article@Blue Green Deployment - Martin Fowler](https://martinfowler.com/bliki/BlueGreenDeployment.html)
- [@article@Canary Release - Martin Fowler](https://martinfowler.com/bliki/CanaryRelease.html)