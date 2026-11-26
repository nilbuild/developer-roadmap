# SSR vs CSR vs Hydration

Server-side rendering, or SSR, generates a page's full HTML on the server before sending it to the browser, so crawlers receive complete content immediately. Client-side rendering, or CSR, sends a mostly empty page and builds the content using JavaScript in the browser, which can be harder for some crawlers to process. Hydration is a hybrid approach where a server-rendered page is sent first, then JavaScript takes over in the browser to make it interactive, aiming to combine the crawlability of SSR with the interactivity of CSR.

Visit the following resources to learn more:

- [@article@Server-Side Rendering vs Client-Side Rendering](https://strapi.io/blog/server-side-rendering-vs-client-side-rendering)
- [@article@Hydration and SEO: How it works and why it matters](https://searchengineland.com/hydration-seo-481671)
- [@video@Server Side vs Client Side Rendering - Smoljames](https://www.youtube.com/watch?v=ObrSuDYMl1s)
- [@video@Hydration Explained](https://www.youtube.com/watch?v=kZG3izJu7qE)