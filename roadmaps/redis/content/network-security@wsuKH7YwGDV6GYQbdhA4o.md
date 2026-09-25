# Network Security

Network security for Redis involves restricting access using firewalls, binding Redis to specific interfaces, and using private networks or VPNs. Redis should never be exposed directly to the public internet without authentication. The `bind` directive and firewall rules are the first line of defense.

Visit the following resources to learn more:

- [@official@Redis Authentication](https://redis.io/docs/latest/operate/oss_and_stack/management/security/#authentication)
- [@official@Redis Network Security](https://redis.io/docs/latest/operate/rc/security/database-security/network-security/)