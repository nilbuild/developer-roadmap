# Planner Executor

A planner executor architecture splits an agent into two roles: a planner that breaks a goal down into a sequence of steps, and an executor that carries out each step and reports back the result. This separation lets the planner focus on high level strategy while the executor handles the details of each individual action. It can make an agent's behavior easier to reason about and debug compared to a single combined loop.

Visit the following resources to learn more:

- [@article@Plan-and-Execute Agents](https://blog.langchain.dev/planning-agents/)
- [@article@Plan and Execute: AI Agents Architecture](https://medium.com/@shubham.ksingh.cer14/plan-and-execute-ai-agents-architecture-f6c60b5b9598)