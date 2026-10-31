# Code Review on PRs

Code Review on pull requests is a managed service that reviews every pull request in your GitHub repositories without a workflow file. Several agents read the diff with the surrounding code, a verification step removes false positives, and the review posts inline comments ranked by severity, a summary and a check run. It never approves or blocks a pull request, so the merge decision stays with your team. An Owner of a Team or Enterprise organization turns it on, picks a review level (quick, standard or deep) and tunes what gets flagged with a `REVIEW.md` file. Anyone with write access can request a review with an `@claude review` comment.

Visit the following resources to learn more:

- [@official@Code Review](https://code.claude.com/docs/en/code-review)
- [@official@Set up Code Review](https://code.claude.com/docs/en/code-review-setup)
- [@official@Customize Code Review](https://code.claude.com/docs/en/code-review-customize)
- [@article@Claude Code Review: /code-review for Diffs and PRs](https://claudcod.com/blog/claude-code-review-command/)