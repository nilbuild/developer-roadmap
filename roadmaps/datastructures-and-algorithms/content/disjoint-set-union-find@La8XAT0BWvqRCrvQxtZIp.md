# Disjoint Set (Union-Find)

A disjoint set, or union-find structure, tracks a collection of non-overlapping sets and supports two operations: union, which merges two sets, and find, which identifies which set an element belongs to. With path compression and union by rank, both operations run in nearly constant time. It is used in Kruskal's algorithm and cycle detection.