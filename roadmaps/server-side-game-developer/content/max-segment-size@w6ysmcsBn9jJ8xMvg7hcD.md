# Max Segment Size (MSS)

Max Segment Size (MSS) is a TCP option that specifies the largest payload a host is willing to receive in a single segment. Negotiated during the handshake, it is typically derived from the network's MTU minus IP and TCP header sizes, and tuning it helps avoid IP fragmentation.

Visit the following resources to learn more:

- [@official@TCP Maximum Segment Size tuning](https://www.ibm.com/docs/en/aix/7.2?topic=tuning-tcp-maximum-segment-size)
- [@article@RFC 879 - Maximum Segment Size](https://tools.ietf.org/html/rfc879)
- [@article@What is MSS (maximum segment size)?](https://www.cloudflare.com/learning/network-layer/what-is-mss/)