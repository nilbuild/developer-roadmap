# WSA-Poll

WSAPoll is the Windows implementation of the POSIX poll API for socket readiness monitoring. It allows a server to monitor multiple sockets for read/write readiness in a single call, though for high-connection-count servers, IOCP is generally preferred.

Visit the following resources to learn more:

- [@official@Microsoft WSA-Poll Documentation](https://learn.microsoft.com/en-us/windows/win32/api/winsock2/nf-winsock2-wsapoll)
- [@article@WSAPoll is Broken - Daniel Stenberg](https://daniel.haxx.se/blog/2012/10/10/wsapoll-is-broken/)
- [@article@WSAPOLLFD Structure - Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/api/winsock2/ns-winsock2-wsapollfd)
- [@article@WSAPoll Sample Code - Microsoft Windows Classic Samples](https://github.com/microsoft/Windows-classic-samples/blob/main/Samples/Win7Samples/netds/winsock/wsapoll/poll.cpp)