# epoll

epoll is the Linux kernel's scalable I/O event notification mechanism. Unlike select and poll, it uses event-triggered notifications and does not require iterating over all monitored file descriptors on each call, enabling efficient handling of tens of thousands of concurrent connections.

Visit the following resources to learn more:

- [@official@Linux epoll API](https://man7.org/linux/man-pages/man7/epoll.7.html)
- [@article@Understanding epoll for Scalable Network Servers](https://medium.com/@copyconstruct/the-method-to-epolls-madness-d9d2d6378642)
- [@article@epoll vs select vs poll](https://devarea.com/linux-io-multiplexing-select-vs-poll-vs-epoll/)