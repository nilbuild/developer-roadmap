# N-gram Speculation

N-gram speculation builds a dictionary during prefill that maps token prefixes to observed n-gram continuations from the input. During decode, generated tokens are looked up in this dictionary and matching suffixes become draft tokens with no separate model required. It is most effective for code completion, where output frequently mirrors input syntax, and can produce very long draft sequences with high acceptance rates in that domain.

Visit the following resources to learn more:

- [@article@Break the Sequential Dependency of LLM Inference Using Lookahead Decoding](https://arxiv.org/abs/2402.02057)