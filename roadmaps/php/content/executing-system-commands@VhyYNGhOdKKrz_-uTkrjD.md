# Executing System Commands
 
PHP can run shell commands using functions like `exec()`, `shell_exec()`, `system()`, and `passthru()`. Each differs in how it captures and returns output. User input must never be passed unsanitized to these functions, as it can lead to command injection. `escapeshellarg()` and `escapeshellcmd()` help sanitize arguments safely.

Visit the following resources to learn more:

- [@official@Exec Function](https://www.php.net/manual/en/ref.exec.php)