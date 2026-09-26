# Windows

On Windows, thread-local storage is accessed via the `TlsAlloc`, `TlsSetValue`, and `TlsGetValue` APIs, or the `__declspec(thread)` keyword for static TLS. Windows fiber APIs also allow cooperative multitasking within a single thread.

Visit the following resources to learn more:

- [@article@Windows Game Development Guide - Microsoft Learn](https://learn.microsoft.com/en-us/windows/uwp/gaming/e2e)
- [@article@How to Set Up a Dedicated Game Server - Intel](https://www.intel.com/content/www/us/en/gaming/resources/game-server.html)
- [@article@Game Development Kit (GDK) Documentation - Microsoft Learn](https://learn.microsoft.com/en-us/gaming/gdk/)