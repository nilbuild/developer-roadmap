# Constrained Decoding
 
Constrained decoding is the mechanism that enforces structured outputs at the token level. At each sampling step, logits for tokens that would violate the active schema or grammar are masked to zero before sampling, so only valid continuations can be selected. Grammar compilation adds overhead to time to first token, and the interaction with speculative decoding is important to note: some engines disable speculation under hard constraints because draft token acceptance rates drop sharply when only a narrow set of tokens is valid at each step. .

Visit the following resources to learn more:

- [@opensource@Guidance: guided generation](https://github.com/guidance-ai/guidance)
- [@opensource@Outlines: structured generation](https://github.com/dottxt-ai/outlines)
- [@article@A Guide to Structured Generation Using Constrained Decoding](https://www.aidancooper.co.uk/constrained-decoding/)
- [@article@Constrained decoding definition](https://www.sanity.io/glossary/constrained-decoding)