# Mutex

A mutex (mutual exclusion lock) ensures only one thread at a time can execute a critical section. Threads attempting to acquire a held mutex are blocked until the holder releases it. Mutexes protect shared data structures in game servers from concurrent modification.

Visit the following resources to learn more:

- [@official@Using mutexes - IBM](https://www.ibm.com/docs/en/aix/7.1.0?topic=programming-using-mutexes)
- [@article@Mutex Objects - Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/sync/mutex-objects)
- [@article@Synchronization - CS 341](https://cs341.cs.illinois.edu/coursebook/Synchronization)