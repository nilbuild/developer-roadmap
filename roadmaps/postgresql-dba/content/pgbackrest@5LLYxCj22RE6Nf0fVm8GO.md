# pgBackRest: A Comprehensive Backup and Recovery Solution

pgBackRest is an open-source backup and restore tool for PostgreSQL designed to work reliably with large databases. It supports full, differential, and incremental backups, and it archives WAL so you can perform point-in-time recovery (PITR). Backup and restore operations can run in parallel and are compressed, checksummed, and optionally encrypted. Backups can be stored in a local or remote repository, including object storage such as Amazon S3, Azure Blob Storage, and Google Cloud Storage, and multiple repositories can be used at the same time. Features such as delta restore, which only rewrites files that have changed, and backups taken from a standby server make it a common choice for production PostgreSQL deployments.

Visit the following resources to learn more:

- [@official@pgBackRest documentation](https://pgbackrest.org)
- [@opensource@pgbackrest/pgbackrest](https://github.com/pgbackrest/pgbackrest)