# Connection

A TCP connection is established through a three-way handshake (SYN, SYN-ACK, ACK) and torn down through a four-way FIN exchange. The connection state machine tracks phases from LISTEN through ESTABLISHED to TIME_WAIT, and understanding it helps diagnose issues like half-open connections and port exhaustion on game servers.

Visit the following resources to learn more:

- [@official@Connection management in HTTP/1.x - MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Connection_management_in_HTTP_1.x)
- [@article@Persistent vs Non-Persistent Connections - DEV Community](https://dev.to/ibmdeveloper/persistent-vs-non-persistent-connections-creating-a-multiplayer-game-server-episode-2-5cm1)
- [@article@Game Server Protocols: Starting out - 1024 Monkeys](https://1024monkeys.wordpress.com/2015/01/03/game-server-protocols-part-1-starting-out/)