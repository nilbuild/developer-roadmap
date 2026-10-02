# Mixture of Experts (MoE)

Mixture of Experts models replace dense linear layers with a set of smaller expert matrices, activating only a subset of experts per token via a learned router. A model like Qwen3-235B activates only 22 billion of its 235 billion parameters per forward pass, making single-user inference efficient. In batched production serving, different tokens activate different experts, so nearly all parameters are active across the batch.

Visit the following resources to learn more:

- [@article@Mixture of Experts Explained](https://huggingface.co/blog/moe)
- [@article@Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538)
- [@video@What is Mixture of Experts?](https://www.youtube.com/watch?v=sYDlVVyJYn4)
- [@video@A Visual Guide to Mixture of Experts (MoE) in LLMs](https://www.youtube.com/watch?v=sOPDGQjFcuM)