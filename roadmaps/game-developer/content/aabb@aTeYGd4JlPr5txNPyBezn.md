# AABB

An AABB (Axis-Aligned Bounding Box) is a rectangular bounding volume whose edges are always aligned with the world coordinate axes. It is one of the simplest and fastest bounding volume types to compute and test for overlap. Because it does not rotate with the object, it must be recalculated whenever the object moves or rotates, which makes it most efficient for static or slowly moving objects.

Visit the following resources to learn more:

- [@article@Axis-Aligned Bounding Box](https://gdbooks.gitbooks.io/3dcollisions/content/Chapter1/aabb.html)