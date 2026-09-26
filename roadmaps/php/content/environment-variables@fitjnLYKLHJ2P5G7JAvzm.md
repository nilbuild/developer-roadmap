# Environment Variables
 
Environment variables are key-value pairs set in the server environment and accessed in PHP via `$_ENV`, `getenv()`, or `$_SERVER`. They are the standard way to separate configuration from code, especially for secrets, database credentials, and feature flags. Libraries like Dotenv load `.env` files into the environment during local development.

Visit the following resources to learn more:

- [@official@Environment Variables](https://www.php.net/manual/en/function.putenv.php)