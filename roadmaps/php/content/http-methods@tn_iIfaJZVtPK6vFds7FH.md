# HTTP Methods

HTTP defines methods that indicate the intended action for a request. GET retrieves data, POST submits data, PUT replaces a resource, PATCH updates part of a resource, and DELETE removes a resource. PHP primarily handles GET and POST natively through superglobals; other methods are read from `$_SERVER['REQUEST_METHOD']` and the request body.

Visit the following resources to learn more:

- [@official@HTTP Methods](https://www.php.net/manual/en/reserved.variables.server.php)