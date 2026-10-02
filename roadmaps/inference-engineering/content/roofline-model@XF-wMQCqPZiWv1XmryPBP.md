# Roofline Model

The roofline model is a visual framework for reasoning about hardware performance limits. It plots arithmetic intensity on the x-axis against achievable performance on the y-axis, with two ceilings: a diagonal memory bandwidth ceiling for low-intensity workloads and a horizontal compute ceiling for high-intensity ones. A workload's position relative to these ceilings shows not just whether it is compute-bound or memory-bound, but how far it sits from the hardware's theoretical maximum — which tells you how much headroom remains before an optimization hits a hard limit.

Visit the following resources to learn more:

- [@article@What is the roofline model?](https://modal.com/gpu-glossary/perf/roofline-model)
- [@article@Calculating inference bottlenecks](https://learn-inference.com/chapters/models/bottlenecks)
- [@video@A very short intro to the Roofline model](https://www.youtube.com/watch?v=IrkNZG8MJ64)