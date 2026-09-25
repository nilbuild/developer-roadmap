# Geospatial Indexes

Redis Geospatial Indexes store geographic coordinates (longitude and latitude) and support queries like finding all locations within a given radius. Internally, coordinates are encoded as Sorted Set scores using the Geohash algorithm. This allows spatial proximity queries to be answered using range scans.

Visit the following resources to learn more:

- [@official@Geospatial Indexing](https://redis.io/docs/latest/develop/interact/search-and-query/indexing/geoindex/)
- [@article@Geospatial Indexes in Redis](https://codesignal.com/learn/courses/redis-data-structures-beyond-basics/lessons/introduction-to-geospatial-indexes-in-redis-using-java)