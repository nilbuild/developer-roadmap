# IOCP (I/O Completion Ports)

IOCP (I/O Completion Ports) is the Windows kernel mechanism for efficient asynchronous I/O. The OS posts completed I/O operations to a completion port queue, and a pool of threads dequeues and handles them. IOCP is the foundation of high-performance network servers on Windows.

Visit the following resources to learn more:

- [@official@Microsoft IOCP Documentation](https://learn.microsoft.com/en-us/windows/win32/fileio/i-o-completion-ports)
- [@article@I/O Completion Ports Advantages and Disadvantages - Stack Overflow](https://stackoverflow.com/questions/5283032/i-o-completion-ports-advantages-and-disadvantages)
- [@article@IO Completion Ports - Matt Godbolt](https://xania.org/200807/iocp)
- [@article@Asynchronous I/O in Windows for Unix Programmers - Ryan Dahl](https://tinyclouds.org/iocp-links/)