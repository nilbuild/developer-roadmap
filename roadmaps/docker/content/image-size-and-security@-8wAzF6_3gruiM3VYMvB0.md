# Reducing Image Size

Reducing Docker image size is crucial for optimizing storage, transfer speeds, and deployment times. Key strategies include using minimal base images like Alpine Linux, leveraging multi-stage builds to exclude unnecessary build tools, removing unnecessary files and packages, and minimizing the number of layers by combining commands.

Visit the following resources to learn more:

- [@official@Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)
- [@official@Docker Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [@course@Docker Multi-Stage Builds & Image Optimization (Hands-on)](https://prepare.sh/tutorial/docker-multi-stage-builds-image-optimization)