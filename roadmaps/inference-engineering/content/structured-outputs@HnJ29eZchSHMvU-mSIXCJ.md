# Structured Outputs
 
Structured outputs constrain model generation to a defined schema — typically JSON, a specific data type, or a function signature — so that downstream code can parse the result directly without a repair pass. Major inference engines including vLLM and SGLang ship structured output as a first-class feature. The tradeoff is that a schema guarantees the shape of the output, not its correctness: if the model's best answer does not naturally conform to the schema, forcing conformance can affect response quality.

Visit the following resources to learn more:

- [@official@vLLM Structured Outputs](https://docs.vllm.ai/en/latest/features/structured_outputs.html)
- [@official@SGlang Structured Outputs](https://docs.sglang.ai/advanced_features/structured_outputs.html)
- [@opensource@Outlines: structured generation](https://github.com/dottxt-ai/outlines)
- [@opensource@Guidance: guided generation](https://github.com/guidance-ai/guidance)
- [@article@Structured Output Engineering for Production LLMs: Beyond JSON Mode](https://www.bigyan.dev/blog/structured-output-engineering-production-llm/)