# select

`select` is a POSIX system call that monitors a set of file descriptors for readiness to read, write, or error. It has a hard limit on the number of file descriptors it can monitor and is generally replaced by poll or epoll in modern high-concurrency game servers.

Visit the following resources to learn more:

- [@official@Linux select API](https://man7.org/linux/man-pages/man2/select.2.html)
- [@official@select() - IBM Documentation](https://www.ibm.com/docs/en/zos/3.1.0?topic=functions-select-suspend-execution-pending-multiple-descriptors)
- [@article@I/O Multiplexing: The select and poll Functions - Shichao's Notes](https://notes.shichao.io/unp/ch6/)
- [@article@Linux select() - Synchronous I/O Multiplexing - phoenixNAP](https://phoenixnap.com/kb/linux-select)