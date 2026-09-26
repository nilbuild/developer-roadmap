# Writing Files
 
PHP writes to files using `file_put_contents()` for simple writes or `fopen()` with `fwrite()` for more control. The `FILE_APPEND` flag appends to an existing file instead of overwriting it. File locking with `LOCK_EX` prevents race conditions when multiple processes write concurrently.

Visit the following resources to learn more:

- [@official@Writing Files](https://www.php.net/manual/en/function.fwrite.php)