# include_once
 
`include_once` works like `include` but skips inclusion if the file has already been loaded. It avoids redeclaring functions or classes when the same file is referenced multiple times across a codebase. It emits a warning rather than a fatal error if the file is not found.

Visit the following resources to learn more:

- [@official@include_once](https://www.php.net/manual/en/function.include-once.php)