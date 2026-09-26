# Connection Pooling
 
Connection pooling reuses existing database connections instead of opening a new connection for each request. PHP itself is stateless per request, so persistent connections (`PDO::ATTR_PERSISTENT`) simulate pooling within a single process. External poolers like PgBouncer handle true connection pooling for high-traffic applications using PostgreSQL.

Visit the following resources to learn more:

- [@official@Connection Pooling](https://www.php.net/manual/en/oci8.connection.php)
- [@official@Database Extensions](https://www.php.net/manual/en/refs.database.php)