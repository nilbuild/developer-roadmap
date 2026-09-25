# Checksum

A checksum is a small value computed from packet data and appended to it, allowing the receiver to detect corruption during transit. UDP includes a 16-bit checksum field; if the received data does not match the recomputed value, the packet is discarded.

Visit the following resources to learn more:

- [@article@User Datagram Protocol - Wikipedia](https://en.wikipedia.org/wiki/User_Datagram_Protocol)
- [@article@How is TCP and UDP Checksum Calculated - slashroot.in](https://www.slashroot.in/how-is-tcp-and-udp-checksum-calculated)
- [@article@Calculating the UDP Checksum - SecurityNik](https://www.securitynik.com/2015/08/calculating-udp-checksum-with-taste-of.html)