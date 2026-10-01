# Client Latency Overhead

Establishing a new connection between a client and inference server takes tens of milliseconds for TLS handshake, which can represent ten percent or more of a tight latency budget. Session reuse across requests eliminates this overhead for returning clients. Standard SDKs like the OpenAI SDK handle session reuse automatically; custom clients must implement it explicitly.