# Expo Tradeoffs

Expo is a managed framework that simplifies React Native development by providing a set of pre-built tools, libraries, and services. While it offers a faster development cycle and easier configuration, it comes with specific limitations regarding native code control. Developers using Expo cannot easily add custom native modules that require direct modification of the Android or iOS project files without using the "eject" process or development builds. Furthermore, the reliance on the Expo SDK means that project updates must align with their release schedule, which can occasionally lead to dependency conflicts when using highly specific third-party native libraries.

Visit the following resources to learn more:

- [@article@Should you use Expo or Bare React Native?](https://medium.com/@andrew.chester/should-you-use-expo-or-bare-react-native-8dd400f4a468/)