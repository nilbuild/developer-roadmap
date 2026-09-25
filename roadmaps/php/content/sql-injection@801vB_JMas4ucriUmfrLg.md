# SQL Injection
 
SQL injection occurs when unvalidated user input is interpolated directly into a SQL query, allowing attackers to manipulate the query. The fix is to use prepared statements with parameterized queries through PDO or MySQLi. Never construct SQL strings by concatenating user input directly.

Visit the following resources to learn more:

- [@official@SQL Injection](https://www.php.net/manual/en/security.database.sql-injection.php)