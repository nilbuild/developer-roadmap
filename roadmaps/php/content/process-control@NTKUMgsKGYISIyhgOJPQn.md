# Process Control
 
PHP can manage processes using the PCNTL extension, which provides functions for forking, signaling, and waiting on child processes. Process control is used in CLI scripts and long-running daemons. Signal handling with `pcntl_signal()` allows graceful shutdown or custom responses to OS signals like SIGTERM.

Visit the following resources to learn more:

- [@official@Process Control](https://www.php.net/manual/en/ref.pcntl.php)