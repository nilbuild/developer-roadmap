# Headless mode

Headless mode runs Claude Code without the interactive interface by passing the -p (or --print) flag with a prompt. It is part of the Agent SDK and is meant for scripts and CI/CD pipelines. Output can be plain text, json or stream-json, and --json-schema forces the result into a defined structure. Flags like --allowedTools, --permission-mode and --bare control which tools can run and how fast the session starts. For full programmatic control with callbacks and message objects, the Python and TypeScript Agent SDK packages offer the same agent loop.

Visit the following resources to learn more:

- [@official@Run Claude Code programmatically](https://code.claude.com/docs/en/headless)
- [@article@Headless Mode: Unleash AI in Your CI/CD Pipeline](https://dev.to/rajeshroyal/headless-mode-unleash-ai-in-your-cicd-pipeline-1imm)
- [@video@Building headless automation with Claude Code | Code w/ Claude](https://www.youtube.com/watch?v=dRsjO-88nBs)