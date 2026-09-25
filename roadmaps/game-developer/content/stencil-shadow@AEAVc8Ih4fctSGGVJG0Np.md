# Stencil Shadow

Stencil shadows, also called shadow volumes, are a technique where the shadow boundary of an object is extruded into a volume and used to mark shadowed pixels in the stencil buffer. For each fragment, the algorithm counts how many shadow volumes surround it to determine whether it is in shadow. This method produces sharp, accurate shadows but is expensive for complex geometry.

Visit the following resources to learn more:

- [@article@Stencil Shadows Implementation](https://devforum.roblox.com/t/stencil-shadows-implementation/2079287)