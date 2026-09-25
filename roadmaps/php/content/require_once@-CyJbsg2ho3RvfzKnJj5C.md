# require_once
 
`require_once` works like `require` but checks whether the file has already been included and skips it if so. This prevents duplicate declarations of classes, functions, or constants when the same file might be included from multiple places. It is commonly used in class autoloading and bootstrap files.

Visit the following resources to learn more:

- [@official@require_once](https://www.php.net/manual/en/function.require-once.php)