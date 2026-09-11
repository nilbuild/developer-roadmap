# JSON Serialization and Deserialization

JSON serialization and deserialization is the process of converting Dart objects into JSON strings for network transmission and transforming JSON data received from an API back into usable Dart objects. In Flutter, this is typically handled by mapping data fields to class properties using the `json_serializable` package or by manually defining `fromJson` and `toJson` methods. This workflow ensures that raw data from web services is safely structured and type-checked before being used within an application.

Visit the following resources to learn more:

- [@official@JSON and serialization](https://docs.flutter.dev/development/data-and-backend/json)
- [@official@Using JSON](https://dart.dev/guides/json)