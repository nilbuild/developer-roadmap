# OBB

An OBB (Oriented Bounding Box) is a rectangular bounding volume that can rotate freely to match the orientation of the object it encloses. Compared to an AABB, an OBB typically provides a tighter fit, reducing false positives in collision tests. Intersection tests between OBBs are more expensive than AABB tests, usually implemented using SAT.

Visit the following resources to learn more:

- [@article@OBB vs OBB Collision Detection](https://gamedev.stackexchange.com/questions/25397/obb-vs-obb-collision-detection)
- [@article@Oriented Bounding Box](https://gamedev.stackexchange.com/questions/49041/oriented-bounding-box-how-to)