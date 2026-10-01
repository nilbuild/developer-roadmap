# Grace and Vera CPUs

NVIDIA's ARM-based Grace and Vera CPUs connect to their paired GPUs via NVLink Chip-to-Chip at up to 900 GB/s, far higher than standard PCIe connections. This high-bandwidth CPU-GPU link makes offloading KV caches and LoRA weights to CPU memory practical, since data can be retrieved quickly enough to remain on the critical path. Grace pairs with Hopper and Blackwell; Vera pairs with the upcoming Rubin architecture.

Visit the following resources to learn more:

- [@official@NVIDIA Grace CPU](https://www.nvidia.com/en-us/data-center/grace-cpu/)