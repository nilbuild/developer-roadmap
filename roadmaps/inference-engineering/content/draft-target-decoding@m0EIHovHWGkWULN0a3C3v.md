# Draft-Target Speculative Decoding

Draft-target speculation uses a small draft model, typically at least ten times smaller than the target, to generate draft tokens for the target model to verify. The draft model should share the same tokenizer and general behavior as the target, often being a smaller member of the same model family. It is the simplest speculation method to set up but introduces the most overhead due to running a separate model.

Visit the following resources to learn more:

- [@article@Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192)