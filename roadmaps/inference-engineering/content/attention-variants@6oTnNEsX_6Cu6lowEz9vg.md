# Attention Variants

Newer attention algorithms reduce the quadratic time complexity of standard attention. Sliding window attention limits each token to attending to the nearest w tokens, turning O(N²) into O(Nw). Linear attention approximates the softmax with a linear-time kernel. Compressed attention periodically compresses earlier context. These variants trade off some quality for better scaling on long sequences.

Visit the following resources to learn more:

- [@article@Longformer: The Long-Document Transformer](https://arxiv.org/abs/2004.05150)
- [@article@Reformer: The Efficient Transformer](https://arxiv.org/abs/2001.04451)
- [@article@Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation](https://arxiv.org/abs/2108.12409)
- [@article@Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752)