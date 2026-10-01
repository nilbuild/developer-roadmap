# Instances and Interconnects

Within a node, NVLink connects GPUs one-to-one at up to 1800 GB/s on Blackwell, and NVSwitch creates an all-to-all fabric across all eight GPUs. Between nodes, InfiniBand provides inter-node connectivity at substantially lower bandwidth than NVLink. Multi-Instance GPU (MIG) partitions a single GPU into up to seven isolated slices, each with dedicated compute and memory, allowing small models to run on fractions of a high-end GPU without resource contention.

Visit the following resources to learn more:

- [@official@NVLink and NVSwitch](https://www.nvidia.com/en-us/data-center/nvlink/)
- [@official@NVIDIA InfiniBand](https://www.nvidia.com/en-us/networking/products/infiniband/)