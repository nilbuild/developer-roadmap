# Cold Start and Limitations

A cold start happens when Lambda initializes a new execution environment for a function that has not been run recently. During initialization, the runtime and your code are loaded, which adds latency to the first invocation. Limitations include a maximum execution timeout of 15 minutes, a 10GB memory limit, and a 250MB deployment package size limit (unzipped).

Visit the following resources to learn more:

- [@official@AWS Cold Start and Limitations](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html)