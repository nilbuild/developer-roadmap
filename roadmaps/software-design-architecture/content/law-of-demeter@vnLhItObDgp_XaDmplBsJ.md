# Law of Demeter

The Law of Demeter is a design principle that restricts how objects interact with one another to reduce system coupling. It suggests that a given method should only call methods belonging to its own class, objects created within the method, objects passed as arguments, or direct component objects. By limiting these interactions to "only talk to your immediate friends," the principle ensures that a module does not need to know the internal structure or the navigation path of the objects it interacts with. This approach makes code easier to maintain and refactor because changes to the internal implementation of one object do not propagate across the entire system.

Visit the following resources to learn more:

- [@article@@Article: Law of Demeter Explained](https://en.wikipedia.org/wiki/Law_of_Demeter)