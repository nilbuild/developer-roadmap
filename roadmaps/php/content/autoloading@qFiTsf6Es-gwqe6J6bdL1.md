# Autoloading
 
Autoloading automatically loads PHP class files when they are first used, without requiring manual `include` or `require` calls. PHP's `spl_autoload_register()` registers a custom autoloader function. Composer generates a PSR-4-compliant autoloader that maps namespaces to directory structures, which is the standard approach in modern PHP.

Visit the following resources to learn more:

- [@official@Autoloading](https://www.php.net/manual/en/language.oop5.autoload.php)