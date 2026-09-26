# AB Pruning

Alpha-beta pruning is an optimization of the minimax algorithm that eliminates branches of the game tree that cannot influence the final decision. It maintains two values, alpha and beta, representing the minimum score the maximizing player is assured and the maximum score the minimizing player is assured. When a node's score falls outside this window, its subtree is pruned, significantly reducing the search space without affecting the result.

Visit the following resources to learn more:

- [@article@AB Pruning](https://en.wikipedia.org/wiki/Alpha-beta_pruning)
- [@article@Alpha-Beta Pruning: A Deep Dive into its History](https://dev.to/vedantasati03/alpha-beta-pruning-a-deep-dive-into-its-history-implementation-and-functionality-4ojf)