# Model Differences

Models from different providers, and even different versions from the same provider, respond differently to the same prompt. They vary in how closely they follow instructions, how they handle formatting, how verbose they are, and how much structure they need. A prompt tuned for one model can lose quality when moved to another, so it should be retested after any model switch or upgrade. Keeping an eval set makes these changes easy to spot.

Visit the following resources to learn more:

- [@article@Prompts that work on multiple models: how to write them](https://giallostudio.it/en/blog/prompts-that-work-across-models)
- [@article@Ensuring Consistent Outputs Across Different LLMs: A Deep Dive](https://dayanand-shah.medium.com/ensuring-consistent-outputs-across-different-llms-a-deep-dive-176edff5517d)
- [@article@How To Test Prompts Across Models: Multi-Model Evaluation](https://www.promptquorum.com/prompt-engineering/how-to-test-prompts-across-models)