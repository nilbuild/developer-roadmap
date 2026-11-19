# check_pgactivity

`check_pgactivity` is a monitoring plugin for PostgreSQL that is compatible with Nagios and other monitoring systems that use the Nagios plugin format, such as Icinga. Each check, called a service, inspects one aspect of the database server, for example the number of connections, long-running queries, locks, replication lag, WAL file accumulation, table bloat, or the age of the last backup, and returns an OK, WARNING, or CRITICAL status based on thresholds you configure. This lets DBAs plug PostgreSQL health checks into their existing alerting setup instead of building custom scripts.

Visit the following resources to learn more:

- [@opensource@OPMDG/check_pgactivity](https://github.com/OPMDG/check_pgactivity)