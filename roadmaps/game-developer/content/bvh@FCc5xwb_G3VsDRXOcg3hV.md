# BVH

A BVH (Bounding Volume Hierarchy) is a tree structure where leaf nodes contain individual objects and each internal node contains a bounding volume that encloses all its children. BVHs are widely used for ray tracing and broad-phase collision detection. Traversal is fast because entire subtrees can be discarded when the query does not intersect a node's bounding volume.

Visit the following resources to learn more:

- [@opensource@UnityBoundingVolumeHeirachy](https://github.com/rossborchers/UnityBoundingVolumeHeirachy)