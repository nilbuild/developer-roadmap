# Proxy
 
Proxy is a function that runs before a request completes, letting you inspect and modify the request or response. It replaces Middleware, which served the same purpose in earlier versions of Next.js. It runs on Vercel's Edge Runtime, so you can rewrite URLs, redirect requests, set headers, or check authentication before a page or API route renders. Common uses include protecting routes based on login state, A/B testing, and localization based on request headers.

Visit the following resources to learn more:

- [@official@Proxy for App Router](https://nextjs.org/docs/app/getting-started/proxy)
- [@official@Proxy for Pages Router](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy)
- [@article@Why Next.js Renamed Middleware to Proxy (And Why It Matters)](https://medium.com/skillstuff/why-next-js-renamed-middleware-to-proxy-and-why-it-matters-2d6697ca3fe1)
- [@video@Next.js 16 Middleware DEPRECATED - Authentication In Proxy Or Data Access Layer?](https://www.youtube.com/watch?v=zNgCFXZLoRk)