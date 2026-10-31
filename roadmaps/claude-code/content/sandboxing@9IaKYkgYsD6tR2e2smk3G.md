# Sandboxing

The sandboxed Bash tool wraps the shell commands Claude runs, and the processes they start, in an operating-system boundary. By default, commands can write only to the working directory, a temp directory and directories you add, while most reads stay allowed except denied paths like credential files. Network connections go through a proxy that checks each host against an allowlist of domains, which starts empty. You turn it on with `/sandbox` or the `sandbox` setting. It uses Seatbelt on macOS and bubblewrap on Linux and WSL2, and it is not available on native Windows.

Visit the following resources to learn more:

- [@official@Configure the sandboxed Bash tool](https://code.claude.com/docs/en/sandboxing)
- [@official@Security](https://code.claude.com/docs/en/security)
- [@article@Claude Code Sandboxing](https://cobusgreyling.medium.com/claude-code-sandboxing-b33d42b61888)