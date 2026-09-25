# Registered I/O

Registered I/O (RIO) is a Windows Sockets extension that reduces kernel-to-user transitions by registering fixed memory buffers with the OS. It is designed for ultra-low-latency, high-throughput network applications where minimizing system call overhead matters.

Visit the following resources to learn more:

- [@official@Microsoft Registered I/O (RIO)](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh997032(v=ws.11))
- [@article@RIO then IOCP then just plain old Winsock2](https://wirepair.org/2023/08/19/rio-then-iocp-then-just-plain-old-winsock2/)
- [@article@Windows Overlapped IO vs Registered IO (RIO) vs IOCP - Stack Overflow](https://stackoverflow.com/questions/73878597/what-are-the-differences-between-windows-overlapped-io-registered-io-rio-and)
- [@article@What is io_uring? - Lord of the io_uring](https://unixism.net/loti/what_is_io_uring.html)