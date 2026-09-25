# $_REQUEST

`$_REQUEST` merges the contents of `$_GET`, `$_POST`, and `$_COOKIE` into a single superglobal array. Because it combines multiple sources, it is less predictable and generally avoided in favor of using `$_GET` or `$_POST` directly. The order of precedence among sources is controlled by `php.ini`.

Visit the following resources to learn more:

- [@official@$_REQUEST](https://www.php.net/manual/en/reserved.variables.request.php)