# SET

`SET` stores a string value at a key, replacing any existing value. It accepts options for setting expiration (`EX`, `PX`), and conditional flags (`NX` to set only if the key does not exist, `XX` to set only if it does). This makes `SET` versatile enough to handle both simple assignments and atomic conditional writes.

Visit the following resources to learn more:

- [@official@SET](https://redis.io/docs/latest/commands/set/)