# Descriptor

A socket descriptor (or file descriptor on Unix-like systems) is an integer handle returned by the OS when a socket is created. All subsequent socket operations (bind, connect, send, recv, close) reference this descriptor, and the OS uses it to track the socket's state and buffers.

Visit the following resources to learn more:

- [@article@open(2) - Linux Manual Page - man7.org](https://man7.org/linux/man-pages/man2/open.2.html)
- [@article@C++ Socket Programming - TutorialsPoint](https://www.tutorialspoint.com/cplusplus/cpp_socket_programming.htm)
- [@article@Read from a File or Socket - IBM Documentation](https://www.ibm.com/docs/en/zos/3.1.0?topic=functions-read-read-from-file-socket)