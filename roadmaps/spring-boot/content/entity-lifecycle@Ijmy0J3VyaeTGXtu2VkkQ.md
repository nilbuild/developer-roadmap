# Entity lifecycle

Entity lifecycle describes the different states an object managed by Hibernate can go through: transient, persistent, detached, and removed. A transient entity exists only in memory and is not tracked by Hibernate, while a persistent entity is attached to a session and synchronized with the database. Knowing these states helps developers understand when changes to an object are actually saved, and when it needs to be reattached or merged back into a session.

Visit the following resources to learn more:

- [@article@Hibernate Entity Lifecycle & and its state](https://www.baeldung.com/hibernate-entity-lifecycle)