# Video Processing for VLMs

One second of video contains 24 frames, each requiring roughly 1,000 tokens to represent at full resolution. This makes video inputs extremely long-context workloads. Frame rate reduction and downsampling are practically mandatory for running video through a VLM in a single request. Prefix caching and chunked prefill become critical for managing the resulting multi-thousand-token sequences.

Visit the following resources to learn more:

- [@opensource@Awesome LLMs for Video Understanding](https://github.com/yunlong10/Awesome-LLMs-for-Video-Understanding)