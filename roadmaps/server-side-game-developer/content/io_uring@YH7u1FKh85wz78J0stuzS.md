# io_uring

io_uring is a Linux kernel interface for asynchronous I/O that uses shared ring buffers between kernel and user space to submit and complete I/O operations with minimal system call overhead. It significantly reduces context switch costs for high-throughput game server networking on Linux.

Visit the following resources to learn more:

- [@official@Linux io_uring_enter](https://man7.org/linux/man-pages/man2/io_uring_enter.2.html)
- [@official@io_uring(7) Linux Manual Page - man7.org](https://man7.org/linux/man-pages/man7/io_uring.7.html)
- [@article@Efficient Networking with io_uring](https://lwn.net/Articles/776703/)
- [@article@io_uring by Example: Introduction - Unixism](https://unixism.net/2020/04/io-uring-by-example-part-1-introduction/)
- [@article@Why You Should Use io_uring for Network I/O - Red Hat](https://developers.redhat.com/articles/2023/04/12/why-you-should-use-iouring-network-io)