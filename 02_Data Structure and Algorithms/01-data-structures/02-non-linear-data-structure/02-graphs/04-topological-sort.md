# Topological Sort
Topological sort is an algorithm for ordering the vertices of a directed acyclic graph (DAG) in a linear sequence such that for every directed edge `u` to `v`, vertex `u` comes before vertex `v` in the ordering. This is particularly useful in scenarios like scheduling tasks, where certain tasks must be completed before others.

- Topological sort algorithms can find topological orderings of graphs in `O(V + E)` time.
- Algorithms like Tarjan's strongly connected components algorithm can be used to find if a graph is a DAG and to perform topological sorting.
- All trees are DAGs, and thus can be topologically sorted.
- There are multiple valid topological orderings for a given DAG

# Topological Sort Algorithms
1. Pick an unvisited node
2. Do DFS from that node, marking nodes as visited
3. When you finish visiting a node, add it to the front of a list
4. Repeat until all nodes are visited