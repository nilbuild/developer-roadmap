# Kruskal's Algorithm

Kruskal's algorithm builds a minimum spanning tree by sorting all edges by weight and adding each edge to the MST if it does not create a cycle. It uses a union-find structure to efficiently check for cycles. The result is the set of edges with the lowest total weight that connects all nodes.