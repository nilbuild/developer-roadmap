# $_GET

`$_GET` contains variables passed to the script via URL query parameters. For a URL like `page.php?id=5&lang=en`, `$_GET['id']` returns `5`. Query string data should always be validated and sanitized before use, as it is user-supplied input.

Visit the following resources to learn more:

- [@official@$_GET](https://www.php.net/manual/en/reserved.variables.get.php)