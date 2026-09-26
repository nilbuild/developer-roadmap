# Limits

DynamoDB has several limits to be aware of. Item size is capped at 400KB. A single partition can handle up to 3,000 read capacity units or 1,000 write capacity units per second. Query and scan operations can return up to 1MB of data per call, requiring pagination for larger result sets.

Visit the following resources to learn more:

- [@official@Limit Settings](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html)