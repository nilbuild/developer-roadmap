# File Extensions

File extensions like `.ios.js` and `.android.js` allow React Native to automatically select the correct implementation based on the platform where the application is running. When you import a module with these specific extensions, the packager detects the operating system and loads the file that matches the target platform. This mechanism enables developers to maintain separate logic or UI components for iOS and Android within the same codebase while keeping imports clean and simple.

Visit the following resources to learn more:

- [@official@Platform-Specific Code](https://reactnative.dev/docs/platform-specific-code)
- [@official@App Extensions](https://reactnative.dev/docs/app-extensions)