# pg_restore

`pg_restore` is the PostgreSQL utility for restoring a database from an archive created by `pg_dump` in one of the non-plain formats (custom, directory, or tar). Plain SQL dumps are restored with `psql` instead. Because these archive formats store each object separately, `pg_restore` can be selective: it can restore only certain schemas or tables, restore just the schema or just the data, or produce a table of contents with `--list` that you edit and pass back with `--use-list` to control exactly what is restored and in what order. It can also restore in parallel with `--jobs` when the archive is in the custom or directory format, which greatly shortens restore times for large databases.

Visit the following resources to learn more:

- [@official@pg_restore](https://www.postgresql.org/docs/current/app-pgrestore.html)
- [@article@A guide to pg_restore](https://www.timescale.com/learn/a-guide-to-pg_restore-and-pg_restore-example)