# DBVT

A DBVT (Dynamic Bounding Volume Tree) is a variant of BVH designed for scenes where objects move frequently. Rather than rebuilding the entire tree on each frame, a DBVT supports incremental updates by reinserting or refitting only the affected nodes. The Bullet physics engine popularized this approach for real-time dynamic collision broadphase.

Visit the following resources to learn more:

- [@article@DBVT](https://sopiro.github.io/DynamicBVH/)
- [@article@Dynamic Bounding Volume Hierarchies](https://box2d.org/files/ErinCatto_DynamicBVH_Full.pdf)