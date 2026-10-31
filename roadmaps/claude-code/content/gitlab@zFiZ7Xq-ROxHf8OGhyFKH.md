# GitLab CI/CD

Claude Code GitLab CI/CD runs Claude Code in GitLab pipeline jobs. You add a job to `.gitlab-ci.yml` that installs the CLI and runs `claude -p`, with your API key stored as a masked CI/CD variable. Claude can turn issues into merge requests, fix bugs and answer `@claude` mentions when you connect a webhook or listener to trigger the pipeline. It can also run through Amazon Bedrock or Google Cloud with OIDC instead of stored keys. The integration is in beta and maintained by GitLab.

Visit the following resources to learn more:

- [@official@Claude Code GitLab CI/C](https://code.claude.com/docs/en/gitlab-ci-cd)
- [@article@Secure every commit to production with Claude and GitLab](https://about.gitlab.com/blog/claude-security-and-gitlab/)
- [@video@How To Use Claude Code With GitLab (Full Guide) \[Step By Step Guide\]](https://www.youtube.com/watch?v=-t8Lk16YQpo)