# Deployment Strategies

Deployment strategies control how new application versions are released to minimize risk and downtime. A blue/green deployment maintains two identical environments and switches all traffic from old to new instantly, with fast rollback by switching back. A canary deployment routes a small percentage of traffic to the new version first, monitors for errors, and gradually increases the percentage before full rollout. Rolling deployments replace instances one at a time. Each strategy trades deployment speed for risk control.

Visit the following resources to learn more:

- [@course@Deployment strategies: Types, trade-offs, and how to choose](https://circleci.com/blog/deployment-strategies-types-trade-offs-and-how-to-choose/#c-consent-modal)
- [@article@CI/CD deployment: top 6 strategies and how to make them work](https://octopus.com/devops/ci-cd/ci-cd-deployment/)
- [@video@Top 5 Most-Used Deployment Strategies](https://www.youtube.com/watch?v=AWVTKBUnoIg)