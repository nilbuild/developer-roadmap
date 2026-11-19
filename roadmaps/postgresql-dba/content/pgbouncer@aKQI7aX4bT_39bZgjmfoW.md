# PgBouncer

PgBouncer is a lightweight connection pooler for PostgreSQL. Every PostgreSQL connection is a separate server process that uses memory, so applications that open many short-lived connections can overwhelm the database. PgBouncer sits between clients and the server and lets many client connections share a small pool of real server connections. It supports three pooling modes: session pooling, where a client keeps a server connection until it disconnects; transaction pooling, where a server connection is only assigned for the duration of a transaction; and statement pooling, the most aggressive mode, which disallows multi-statement transactions. Transaction pooling gives the biggest gains but breaks features that depend on session state, such as session-level advisory locks or `SET` commands that are expected to persist, so applications need to be checked before switching to it.

Visit the following resources to learn more:

- [@official@PgBouncer Website](https://www.pgbouncer.org/)
- [@opensource@pgbouncer/pgbouncer](https://github.com/pgbouncer/pgbouncer)