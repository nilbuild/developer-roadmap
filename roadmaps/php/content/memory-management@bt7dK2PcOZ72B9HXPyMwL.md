# Memory Management
 
PHP allocates and frees memory automatically, but developers can influence it. The `memory_limit` directive in `php.ini` caps memory per request. Unset large variables with `unset()` when no longer needed. For long-running scripts or batch jobs, careful object lifecycle management prevents memory exhaustion.

Visit the following resources to learn more:

- [@official@Memory Management](https://www.php.net/manual/en/features.gc.php)