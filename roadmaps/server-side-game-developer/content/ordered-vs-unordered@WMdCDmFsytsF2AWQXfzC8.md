# Ordered vs Not Ordered

Ordered delivery means packets are received and passed to the application in the sequence they were sent; unordered delivery allows packets to be processed as they arrive. TCP enforces ordering; UDP does not. For time-sensitive game updates, processing the most recent packet immediately (unordered) is often preferable to waiting for a retransmit.

Visit the following resources to learn more:

- [@article@UDP vs. TCP - Gaffer on Games](http://vodacek.zvb.cz/archiv/685.html)
- [@article@TCP vs UDP: Key Differences Explained - Digital Samba](https://www.digitalsamba.com/blog/tcp-and-udp-protocols)
- [@article@TCP vs UDP - Understanding the differences and use cases - Ostinato](https://ostinato.org/guides/tcp-vs-udp-understanding-differences-and-use-cases)