# Automatic Speech Recognition (ASR)

ASR models like Whisper take audio input and produce text transcripts. Whisper is an encoder-decoder model where the decoder, an autoregressive transformer, dominates inference time. TensorRT-LLM with in-flight batching for the decoder delivers the best performance. For real-time transcription, streaming via WebSockets with VAD-segmented chunks achieves round-trip targets of around 200 milliseconds per chunk on optimized deployments.

Visit the following resources to learn more:

- [@official@OpenAI Whisper Models on Hugging Face](https://huggingface.co/openai)
- [@official@OpenAI Whisper](https://openai.com/index/whisper/)
- [@opensource@openai/whisper](https://github.com/openai/whisper)
- [@article@Robust Speech Recognition via Large-Scale Weak Supervision (Whisper)](https://arxiv.org/abs/2212.04356)