# Spatial Partitioning

Spatial partitioning divides a scene into regions to accelerate queries like collision detection, ray casting, and visibility culling. By organizing objects into a structure that reflects their position in space, the engine can quickly discard large portions of the scene that are irrelevant to a given query. Common data structures include grids, octrees, BSP trees, and BVHs.

Visit the following resources to learn more:

- [@article@Spatial Partitioning](https://en.wikipedia.org/wiki/Space_partitioning)
- [@article@Spatial Partitioning in Game Programming](https://gameprogrammingpatterns.com/spatial-partition.html)