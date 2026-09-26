# Usecases

Streams are used for event sourcing, activity logs, and inter-service messaging where message history and replay capability matter. Consumer groups allow workloads to be distributed across multiple workers while tracking which messages each worker has processed. They fill a similar role to Kafka for lighter-weight deployments.