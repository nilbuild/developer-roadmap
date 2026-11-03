# Skills

A skill is a folder with a `SKILL.md` file that teaches Codex a repeatable workflow. The file needs a `name` and a `description`, and it can include scripts, references and assets. Codex loads only the name and description at first, and reads the full file when you pick the skill or the task matches it. In ChatGPT you type `@` to choose a skill, and in the CLI and IDE extension you use `$skill-name` or `/skills`. Skills live in `.agents/skills` in your repository, in your home folder and in an admin location, and plugins can package them for sharing.

Visit the following resources to learn more:

- [@official@Build skills](https://learn.chatgpt.com/docs/build-skills)