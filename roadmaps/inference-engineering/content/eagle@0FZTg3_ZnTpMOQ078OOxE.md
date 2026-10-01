# EAGLE

EAGLE is a purpose-built speculation method where a small draft model is trained to accept hidden states from the target model as input. By seeing the target's internal representations, EAGLE achieves higher acceptance rates and longer draft sequences (up to eight tokens) than using a general-purpose small model. It integrates into the same forward pass as the target model, eliminating the orchestration overhead of separate draft and target model runs.

Visit the following resources to learn more:

- [@article@EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty](https://arxiv.org/abs/2401.15077)
- [@article@EAGLE-2: Faster Inference of Language Models with Dynamic Draft Trees](https://arxiv.org/abs/2406.16858)
- [@article@EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test](https://arxiv.org/abs/2503.01840)