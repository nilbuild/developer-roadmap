# Password Hashing
 
PHP provides `password_hash()` to securely hash passwords using bcrypt or Argon2. The resulting hash includes the algorithm, cost factor, and salt, so no separate salt storage is needed. `password_verify()` checks a plaintext password against a stored hash. Using MD5 or SHA1 for passwords is insecure and should be avoided.

Visit the following resources to learn more:

- [@official@Password Hashing](https://www.php.net/manual/en/function.password-hash.php)