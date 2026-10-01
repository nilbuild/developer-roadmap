# Containerization

Containerization packages an inference service and all its dependencies into a Docker image that runs consistently across environments. Inference containers include the CUDA toolkit, Python packages, the inference engine, and any system libraries like ffmpeg for audio processing. Using a pinned dependency tree prevents breaking changes from affecting running services and ensures reproducible builds.

Visit the following resources to learn more:

- [@official@Docker Documentation](https://docs.docker.com/)
- [@official@Kubernetes Documentation](https://kubernetes.io/docs/home/)
- [@article@What is containerization?](https://www.ibm.com/think/topics/containerization)
- [@video@Containerization Explained](https://www.youtube.com/watch?v=0qotVMX-J5s)