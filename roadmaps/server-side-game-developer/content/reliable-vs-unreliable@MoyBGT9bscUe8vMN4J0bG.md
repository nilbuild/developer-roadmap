# Reliable vs Unreliable

Reliable protocols retransmit lost data until acknowledged; unreliable protocols send data once and discard it on loss. Game networking often mixes both: reliable channels for critical events (player joining, scoring) and unreliable channels for frequent position updates where staleness matters more than loss.

Visit the following resources to learn more:

- [@article@Introduction to TCP and UDP - NetworkLessons](https://networklessons.com/network-fundamentals/introduction-to-tcp-and-udp)
- [@article@TCP vs UDP: Understanding Network Protocol Fundamentals - PAIML](https://paiml.com/blog/2025-02-26-tcp-vs-udp-fundamentals/)
- [@article@TCP vs UDP: Speed, Reliability, and Application Trade-offs - Patsnap](https://eureka.patsnap.com/article/tcp-vs-udp-speed-reliability-and-application-trade-offs)