# Ultrareview

Ultrareview is a deep code review that runs as a cloud session on Anthropic's infrastructure. You start it with `/code-review ultra` (`/ultrareview` is an alias when available), on your branch or on a GitHub pull request number. A fleet of reviewer agents explores the change in parallel, and each finding is independently reproduced and verified, so results focus on real bugs. A review takes roughly 15 to 25 minutes in the background, and Pro and Max accounts get three free runs before it bills as usage credits. For scripts, the `claude ultrareview` subcommand prints the findings to stdout.

Visit the following resources to learn more:

- [@official@Find bugs with ultrareview](https://code.claude.com/docs/en/ultrareview)
- [@article@Claude Code /ultra review: 5 Things You Need to Know Before Running It](https://www.mindstudio.ai/blog/claude-code-ultra-review-5-things-to-know-before-running)
- [@article@Claude Code Ultrareview: A Verified Multi-Agent Review](https://www.matthewswong.com/en/blog/claude-code-code-review-ultrareview/)
- [@video@Claude Code advanced features: /review and the new /ultrareview](https://www.youtube.com/watch?v=vzbkBc3PyUY)