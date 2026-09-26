# Sourcemaps

Sourcemaps are files that act as a bridge between your bundled, minified JavaScript code and the original source code you actually wrote. When an error occurs in a production environment, the stack trace typically points to the transformed bundle, which is difficult to read. By using sourcemaps, developer tools can map these obfuscated locations back to the exact files and line numbers in your original project, making it much easier to identify and fix bugs.

Visit the following resources to learn more:

- [@official@SourceMaps](https://reactnative.dev/docs/debugging-release-builds#enabling-source-maps)
- [@article@Source Maps (MDN)](https://developer.mozilla.org/en-US/docs/Tools/Debugger/How_to/Use_a_source_map)