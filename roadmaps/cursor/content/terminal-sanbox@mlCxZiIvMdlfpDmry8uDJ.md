# Terminal Sandbox

The terminal sandbox runs agent shell commands with read and write access inside your workspace and with the network blocked by default. On macOS it uses Seatbelt, and on Linux it uses Landlock and seccomp. A command that needs more access runs outside the sandbox only after you approve it.

Visit the following resources to learn more:

- [@official@Run modes](https://cursor.com/docs/agent/security/run-modes)
- [@official@Terminal tool](https://cursor.com/docs/agent/tools/terminal)