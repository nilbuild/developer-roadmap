# Image Optimization

Angular's `NgOptimizedImage` directive makes it easy to follow performance best practices when loading images. You enable it by importing `NgOptimizedImage` and replacing the `src` attribute with `ngSrc`. The directive lazy-loads images by default, lets you mark the most important image (such as the Largest Contentful Paint element) with the `priority` attribute so it loads eagerly with a high fetch priority, requires `width` and `height` (or `fill`) to prevent layout shifts, and can generate responsive `srcset` values automatically when used with an image CDN loader. In development mode it also warns about common mistakes, such as images that are much larger than their rendered size.

Visit the following resources to learn more:

- [@official@Image Optimization](https://angular.dev/guide/image-optimization)
- [@article@Automatic Adjustments in Angular's optimized images](https://medium.com/ngconf/automatic-adjustments-in-angulars-optimized-images-0034335e0374)
- [@article@Boost your application's performance with NgOptimizedImage](https://angular.love/en/boost-your-applications-performance-with-ngoptimizedimage)