# Transactions

A transaction is a group of database operations that are executed as a single unit, so that either all of them succeed or none of them take effect. Spring manages transactions declaratively through the `@Transactional` annotation, which wraps a method in a transaction and rolls back changes if an exception occurs. This keeps data consistent even when multiple related operations, like debiting one account and crediting another, need to happen together.

Visit the following resources to learn more:

- [@official@Hibernate Transactions](https://docs.hibernate.org/orm/current/userguide/html_single/#transactions)
- [@article@Hibernate Transaction Management](https://www.javaguides.net/2018/12/hibernate-transaction-management-tutorial.html)