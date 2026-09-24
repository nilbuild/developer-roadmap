# Health checks

Route53 health checks monitor the availability of endpoints by sending periodic requests and checking the response. If an endpoint fails its health check, Route53 can stop routing traffic to it, which is central to failover routing policies. Health checks can target IP addresses, domain names, or other CloudWatch alarms.

Visit the following resources to learn more:

- [@official@Route53 Health Checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-health-checks.html)