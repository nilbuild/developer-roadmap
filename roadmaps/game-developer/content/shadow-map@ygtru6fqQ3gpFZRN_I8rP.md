# Shadow Map

A shadow map is a depth texture rendered from the light's point of view, used to determine which parts of the scene are in shadow when rendering from the camera. Each fragment is compared to the stored depth value; if it is farther from the light than what the shadow map records, it is shadowed. Shadow maps are the most common real-time shadowing technique and come in several variants including cascaded shadow maps and cube shadow maps for point lights.

Visit the following resources to learn more:

- [@article@Shadow Mapping Techniques](https://dev.to/hayyanstudio/shadow-mapping-techniques-implementing-shadows-in-3d-scenes-using-shadow-mapping-46hl/)
- [@article@A Beginner's Guide to Shadow Mapping](https://gamedev.net/blog/2080/entry-2261232-shadow-mapping-part-1-pcf-and-vsms/)