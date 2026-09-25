# Expiration

Key expiration in Redis is set using `EXPIRE`, `PEXPIRE`, `EXPIREAT`, or `PEXPIREAT`, depending on whether the timeout is in seconds, milliseconds, or as a Unix timestamp. Once a key expires, Redis removes it lazily on access or actively through a background process. Expiration is applied to the key as a whole, not to individual fields.

Visit the following resources to learn more:

- [@official@PEXPIRE](https://redis.io/docs/latest/commands/pexpire/)
- [@official@EXPIRE](https://redis.io/docs/latest/commands/expire/)