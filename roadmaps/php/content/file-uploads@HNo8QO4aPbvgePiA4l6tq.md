# File Uploads

PHP handles file uploads through the `$_FILES` superglobal, which contains metadata about each uploaded file including its name, type, size, temporary path, and error code. Files are moved from the temp directory to a permanent location using `move_uploaded_file()`. Upload size limits are configured in `php.ini`.

Visit the following resources to learn more:

- [@official@File Uploads](https://www.php.net/manual/en/features.file-upload.php)