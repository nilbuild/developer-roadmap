# Sanitization Techniques
 
Sanitization removes or encodes unsafe characters from user input before using it in output, queries, or commands. PHP provides `htmlspecialchars()` to escape HTML, `strip_tags()` to remove HTML tags, and `filter_var()` with filters like `FILTER_SANITIZE_EMAIL`. Sanitization reduces the risk of XSS and injection attacks.

Visit the following resources to learn more:

- [@official@Sanitization Techniques](https://www.php.net/manual/en/function.filter-var.php)