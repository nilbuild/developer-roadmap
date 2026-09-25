# Spinlock

A spinlock is a lock where the waiting thread repeatedly checks (spins) whether the lock is available rather than sleeping. It avoids the overhead of sleeping and waking but wastes CPU cycles while spinning, making it suitable only for very short critical sections.

Visit the following resources to learn more:

- [@article@Kernel Locks - IBM](https://www.ibm.com/docs/en/aix/7.2?topic=concepts-kernel-locks)
- [@article@Spinlock - Wikipedia](https://en.wikipedia.org/wiki/Spinlock)
- [@article@Introduction to Spin Locks - Microsoft Learn](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/introduction-to-spin-locks)