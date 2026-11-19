# Operators in Kubernetes Deployment

A Kubernetes operator is a controller that encodes the operational knowledge of running a specific application, so Kubernetes can manage it automatically. For PostgreSQL, operators such as CloudNativePG, Crunchy Data's PGO, and Zalando's Postgres Operator let you declare a cluster in a custom resource, and the operator then handles tasks that a DBA would otherwise do by hand: provisioning primary and replica instances, configuring streaming replication, automatic failover, scheduled backups and point-in-time recovery, rolling minor-version updates, and connection pooling. This makes it practical to run highly available PostgreSQL on Kubernetes, although it still requires understanding both PostgreSQL and how the chosen operator behaves.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated Kubernetes Roadmap](https://roadmap.sh/kubernetes)
- [@official@Kubernetes](https://kubernetes.io/)
- [@opensource@cloudnative-pg/cloudnative-pg](https://github.com/cloudnative-pg/cloudnative-pg)
- [@opensource@zalando/postgres-operator](https://github.com/zalando/postgres-operator)
- [@article@Kubernetes Operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)