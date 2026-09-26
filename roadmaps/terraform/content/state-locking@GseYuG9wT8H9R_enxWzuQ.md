# State Locking

State locking prevents two Terraform operations from modifying state at the same time. When supported by the backend, Terraform acquires a lock before writing to state and releases it when the operation completes. If a lock is not released due to a crash or error, it can be manually removed with the `force-unlock` command.

Visit the following resources to learn more:

- [@official@State - Locking](https://developer.hashicorp.com/terraform/language/state/locking)
- [@official@State Storage and Locking](https://developer.hashicorp.com/terraform/language/state/backends)
- [@video@Terraform - State locking](https://www.youtube.com/watch?v=QdDCUpggmrw)