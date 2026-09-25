# Reliability

IP itself provides no delivery guarantees; packets can be lost, duplicated, or reordered without notification to the sender. Applications requiring reliability must use TCP or implement their own acknowledgment and retransmission logic over UDP.

Visit the following resources to learn more:

- [@article@Reliability at the Transport Layer - Williams College](https://www.cs.williams.edu/~tom/courses/336/outlines/lect28_2.html)
- [@article@Reliable Bytes: How TCP Ensures Trustworthy Data Transfer - ITU Online](https://www.ituonline.com/blogs/reliable-bytes-how-tcp-ensures-trustworthy-data-transfer-across-the-internet/)
- [@article@Game Networking - Gaffer On Games](https://gafferongames.com/categories/game-networking/)