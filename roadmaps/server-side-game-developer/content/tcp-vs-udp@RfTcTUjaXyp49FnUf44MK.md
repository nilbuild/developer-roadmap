# TCP vs UDP

TCP and UDP serve different purposes in game networking. TCP guarantees ordered, reliable delivery at the cost of latency introduced by retransmissions and congestion control; UDP offers lower latency with no built-in guarantees, requiring the application to handle reliability where needed. Most real-time games use UDP for game state and TCP (or a reliable layer over UDP) for control messages.

Visit the following resources to learn more:

- [@article@TCP or UDP for a Multiplayer Game? - StackExchange](https://softwareengineering.stackexchange.com/questions/342254/tcp-or-udp-for-a-multiplayer-game)
- [@article@Game Servers: UDP vs TCP - 1024 Monkeys](https://1024monkeys.wordpress.com/2014/04/01/game-servers-udp-vs-tcp/)
- [@article@Part IV: Great TCP-vs-UDP Debate - IT Hare](https://ithare.com/64-network-dos-and-donts-for-game-engines-part-iv-great-tcp-vs-udp-debate/)