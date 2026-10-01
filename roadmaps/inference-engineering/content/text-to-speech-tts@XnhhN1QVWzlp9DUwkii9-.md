# Text-to-Speech (TTS)

Modern TTS models like Orpheus TTS are fine-tuned LLMs with an expanded vocabulary that includes audio tokens. They generate audio token sequences decoded to waveforms by a small audio decoder. The key performance metrics are time to first byte of audio (TTFB) and the number of concurrent real-time streams a single GPU replica can sustain, rather than raw token throughput.