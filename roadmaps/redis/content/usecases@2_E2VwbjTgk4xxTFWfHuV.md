# Usecases

Strings are used to store cached HTML fragments, serialized JSON objects, session tokens, and numeric counters. Their simplicity and the availability of atomic operations make them the default choice when none of the more specialized types are needed. Any data that fits in a single scalar value is a candidate for the String type.