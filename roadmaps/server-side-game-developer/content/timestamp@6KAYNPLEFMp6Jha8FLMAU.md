# Timestamp

The TCP timestamp option records send times in packets, allowing more accurate round-trip time estimation and enabling the PAWS (Protection Against Wrapped Sequence numbers) mechanism. It helps the stack reject old duplicate segments on high-speed links where sequence numbers can wrap quickly.

Visit the following resources to learn more:

- [@article@Unix time - Wikipedia](https://en.wikipedia.org/wiki/Unix_time)
- [@article@Best practices for timestamps and time zones in databases - Tinybird](https://www.tinybird.co/blog/database-timestamps-timezones)
- [@article@A Practical Guide to Timezones for Developers - Ryan Thomson](https://www.ryanthomson.net/articles/practical-guide-timezones/)