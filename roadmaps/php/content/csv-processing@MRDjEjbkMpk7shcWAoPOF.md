# CSV Processing

PHP handles CSV files using `fgetcsv()` to read rows as arrays and `fputcsv()` to write arrays as CSV lines. For reading an entire CSV into memory, `array_map('str_getcsv', file($path))` is a common shortcut. CSV is widely used for data exports and imports between systems.

Visit the following resources to learn more:

- [@official@CSV Processing](https://php.net/manual/en/ref.fileinfo.php)