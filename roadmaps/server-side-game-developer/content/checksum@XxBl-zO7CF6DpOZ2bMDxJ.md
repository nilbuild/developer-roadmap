# Checksum

A TCP checksum covers the header and payload, allowing receivers to detect in-transit corruption. Unlike UDP, the TCP checksum is mandatory and is computed over a pseudo-header that includes source and destination IP addresses in addition to the segment data.

Visit the following resources to learn more:

- [@official@Computing the Internet Checksum RFC 1071 - IETF](https://datatracker.ietf.org/doc/html/rfc1071)
- [@article@Internet Checksum - Wikipedia](https://en.wikipedia.org/wiki/Internet_checksum)
- [@article@Transmission Control Protocol - Wikipedia](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)