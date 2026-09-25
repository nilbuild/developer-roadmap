# Selective Acknowledgement

Selective Acknowledgment (SACK) is a TCP extension that lets the receiver report exactly which segments arrived, so the sender can retransmit only the missing ones rather than everything after the first loss. It significantly improves throughput on lossy connections.

Visit the following resources to learn more:

- [@article@RFC 2018 - TCP Selective Acknowledgment Options - IETF](https://datatracker.ietf.org/doc/html/rfc2018)
- [@article@RFC 3517: A Conservative Selective Acknowledgment (SACK)-based Loss Recovery Algorithm - IETF](https://www.rfc-editor.org/rfc/rfc3517.html)
- [@article@RFC 2883: An Extension to SACK for D-SACK - IETF](https://www.hjp.at/doc/rfc/rfc2883.html)