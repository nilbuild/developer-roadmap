# Barrier

A barrier is a synchronization point where all participating threads must arrive before any of them can proceed. It is used in game server simulation loops where multiple threads compute a phase of game logic and must all finish before the next phase begins.

Visit the following resources to learn more:

- [@official@Synchronization Primitives Overview - Microsoft .NET](https://learn.microsoft.com/en-us/dotnet/standard/threading/overview-of-synchronization-primitives)
- [@article@Synchronization Primitives in C++20 - KDAB](https://www.kdab.com/synchronization-primitives-in-c20/)
- [@article@Multithreading for Game Engines - Vulkan Guide](https://www.vkguide.dev/docs/extra-chapter/multithreading/)