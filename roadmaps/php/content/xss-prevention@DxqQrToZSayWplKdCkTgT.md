# XSS Prevention
 
Cross-Site Scripting (XSS) occurs when untrusted data is rendered in the browser as executable script. The primary defense in PHP is escaping output with `htmlspecialchars()` when rendering user-supplied content in HTML. Content Security Policy headers provide an additional layer of protection at the browser level.

Visit the following resources to learn more:

- [@official@Special Charsets](https://www.php.net/manual/en/function.htmlspecialchars.php)