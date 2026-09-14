# Expiring Data with TTL Indexes

TTL (Time-To-Live) indexes are a special type of index that automatically remove documents from a collection after a certain amount of time has passed or at a specific clock time. By defining a TTL index on a field containing date values, the database background process continuously monitors the collection and deletes documents once the specified duration has elapsed. This feature is commonly used for managing temporary data like session logs, cached items, or temporary verification tokens that are no longer needed after a set period.

Visit the following resources to learn more:

- [@official@Expire Data from Collections by Setting TTL](https://www.mongodb.com/docs/manual/tutorial/expire-data/)
- [@article@Understanding TTL in MongoDB](https://medium.com/@darshitanjaria/understanding-ttl-in-mongodb-automatically-expiring-documents-e8b1defc1158)
- [@article@Understanding MongoDB Indexes and Expiry](https://stenzr.medium.com/understanding-mongodb-indexes-and-expiry-019831790542)