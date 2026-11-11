# login

`agent login` opens your default browser so you can sign in to Cursor, and stores the credentials locally. If the browser does not open, run `NO_OPEN_BROWSER=1 agent login` to print the URL. For scripts and CI, set the `CURSOR_API_KEY` environment variable or pass `--api-key` instead. Your login is stored locally until you log out.

Visit the following resources to learn more:

- [@official@CLI authentication](https://cursor.com/docs/cli/reference/authentication)