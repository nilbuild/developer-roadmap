# CCD

Continuous Collision Detection (CCD) prevents fast-moving objects from tunneling through thin geometry by testing for collisions along the entire swept path of an object between frames, rather than just at the start and end positions. Without CCD, a bullet or fast projectile can pass entirely through a wall in a single time step. CCD is more expensive than discrete detection and is typically enabled selectively for fast-moving objects.

Visit the following resources to learn more:

- [@article@Continuous Collision Detection](https://docs.unity3d.com/Manual/ContinuousCollisionDetection.html)