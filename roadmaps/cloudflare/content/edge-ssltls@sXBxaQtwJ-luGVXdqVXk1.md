# Edge SSL/TLS
 
Cloudflare terminates SSL/TLS connections at the edge, handling certificate management and protocol negotiation before traffic reaches the origin. Workers run after TLS termination, meaning they always receive decrypted requests over HTTPS.

Visit the following resources to learn more:

- [@official@Get Started with SSL/TLS - Cloudflare Docs](https://developers.cloudflare.com/ssl/get-started/)
- [@official@Edge Certificates · Cloudflare SSL/TLS](https://developers.cloudflare.com/ssl/edge-certificates/)