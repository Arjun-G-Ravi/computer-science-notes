# Common problems in Graph Theory

### 1. Shortest Path Problem
`Given a weighted graph, find the shortest path between two vertices.`

Algorithms:
- BFS (for unweighted graphs)
- Dijkstra's Algorithm (for weighted graphs with non-negative weights)
- Bellman-Ford Algorithm (for graphs with negative weights)
- Floyd-Warshall Algorithm (for all pairs shortest paths)
- A* Algorithm (for heuristic-based shortest path finding)

### 2. Connectivity Problem
`Determine if there is a path between two vertices in a graph.`

Algorithms:
- Search algorithms like BFS or DFS can be used to check connectivity.
- Union-Find (Disjoint Set Union) can be used to determine connectivity in undirected graphs.
### 3. Detecting Negative Cycles
`Check if a graph contains a cycle with a negative total weight.`This can through off many algorithms, especially those that rely on shortest paths.

Algorithms:
- Bellman-Ford Algorithm
- Floyd-Warshall Algorithm 

### 4. Strongly Connected Components (SCC)
`Find all strongly connected components in a directed graph.`
A strongly connected component is a maximal subgraph where every vertex is reachable from every other vertex in the component.

Algorithms:
- Kosaraju's Algorithm
- Tarjan's Algorithm

### 5. Traveling Salesman Problem (TSP)
`Find the shortest possible route that visits each vertex exactly once and returns to the origin vertex.`

Algorithms:
- Held-Karp Algorithm (Dynamic Programming approach)
- Branch and Bound methods
- Approximation algorithms (e.g., Nearest Neighbor, Minimum Spanning Tree-based heuristics)

### 6. Bridge and Articulation Point Finding
`Identify bridges (edges whose removal increases the number of connected components) and articulation points (vertices whose removal increases the number of connected components) in a graph.`

### 7. Minimum Spanning Tree (MST)
`Find a subset of edges that connects all vertices with the minimum total edge weight.`

Algorithms:
- Prim's Algorithm
- Kruskal's Algorithm
- Borůvka's Algorithm

### 8. Network Flow Problems
`Find the maximum flow in a flow network.`
This involves finding the maximum flow from a source vertex to a sink vertex in a directed graph with capacities on edges.

Algorithms:
- Ford-Fulkerson Method
- Edmonds-Karp Algorithm (a specific implementation of Ford-Fulkerson using BFS)
- Dinic's Algorithm