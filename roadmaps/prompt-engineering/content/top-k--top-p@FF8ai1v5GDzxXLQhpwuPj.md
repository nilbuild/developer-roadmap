# Top-K & Top-P

Top-K limits the choice of next token to the K most likely ones. Top-P, also called nucleus sampling, limits it to the smallest group of tokens whose combined probability reaches P. Both cut off unlikely tokens and reduce odd output. They are usually adjusted instead of temperature, not together with it.

Visit the following resources to learn more:

- [@official@Gemini API Prompting Strategies - Google](https://ai.google.dev/gemini-api/docs/prompting-strategies)
- [@article@Top K - LLM Parameter Guide - Vellum](https://www.vellum.ai/llm-parameters/top-k)
- [@article@How do Top-k and Top-p Sampling work? - Outcome School](https://outcomeschool.com/blog/how-do-top-k-and-top-p-sampling-work)
- [@article@Top P - LLM Parameter Guide - Vellum](https://www.vellum.ai/llm-parameters/top-p)
- [@video@What are the LLM's Top-P + Top-K?](https://www.youtube.com/watch?v=aDmp2Uim0zQ)