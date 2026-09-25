# Reliability

Reliability in UDP refers to application-level mechanisms that compensate for the protocol's lack of built-in delivery guarantees. Because UDP drops packets silently, game networking code often implements acknowledgment systems, sequence numbers, and retransmission logic to ensure critical game state reaches its destination.

Visit the following resources to learn more:

- [@article@Reliability and Congestion Avoidance over UDP - Gaffer On Games](https://gafferongames.com/post/reliability_ordering_and_congestion_avoidance_over_udp/)
- [@article@Transmission Control Protocol (TCP) - IBM](https://www.ibm.com/docs/en/zos/3.1.0?topic=protocol-transmission-control-tcp)
- [@article@UDP Packet Reliability and Re-sending - Stack Overflow](https://gamedev.stackexchange.com/questions/106722/udp-packet-reliability-and-re-sending)