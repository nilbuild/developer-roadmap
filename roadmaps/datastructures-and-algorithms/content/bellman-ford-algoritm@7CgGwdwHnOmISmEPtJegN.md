# Bellman-Ford

The Bellman-Ford algorithm finds the shortest paths from a source node in a weighted graph, including graphs with negative edge weights. It works by relaxing all edges repeatedly for n-1 iterations, where n is the number of nodes. It can also detect negative weight cycles, which make shortest paths undefined.