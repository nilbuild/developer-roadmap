# Data Transfer

TCP data transfer moves a byte stream reliably from sender to receiver, with the stack splitting data into segments, numbering them, and retransmitting any that are not acknowledged. The receiver buffers out-of-order segments and delivers them to the application in sequence order.

Visit the following resources to learn more:

- [@article@Beginner's Guide to Game Networking - pvigier's blog](https://pvigier.github.io/2019/09/08/beginner-guide-game-networking.html)
- [@article@HTTP, WebSocket, gRPC, or WebRTC — Which Protocol is Best? - GetStream](https://getstream.io/blog/communication-protocols/)
- [@article@Network Protocols behind Server Push, Online Gaming, and Emails - ByteByteGo](https://blog.bytebytego.com/p/network-protocols-behind-server-push)