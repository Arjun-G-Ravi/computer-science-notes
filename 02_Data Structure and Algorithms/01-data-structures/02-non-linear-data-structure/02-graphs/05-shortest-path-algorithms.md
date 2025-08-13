# Single Source Shortest Path Algorithms
- Used on DAGs to find the shortest path from a source vertex to all other vertices.
- Uses topological sorting to find the paths efficiently.
- Then, it relaxes the edges in topological order to find the shortest paths.

# Dijkstra's Algorithm
- It is a single-source shortest path algorithm that finds the shortest path from a source vertex to all other vertices in a weighted graph with non-negative weights.
- It uses a priority queue to explore the closest vertex first.
- Time complexity is `O((V + E) log V)`
- Greedy

### Algorithm Steps
1. Initialize distances from the source to all vertices as infinite, except for the source vertex which is set to zero.
2. Use a priority queue to store vertices based on their current shortest distance.
3. While the priority queue is not empty:
   - Extract the vertex with the minimum distance. # greedy
   - For each adjacent vertex, if the distance through the current vertex is shorter than the known distance, update the distance and add the vertex to the priority queue.

# Bellman-Ford Algorithm
- It is a single-source shortest path algorithm that `can handle graphs with negative weights`.
- Time complexity is `O(V * E)` # worse than Dijkstra's
### Algorithm Steps
1. Initialize distances from the source to all vertices as infinite, except for the source vertex which is set to zero.
2. For each vertex, relax all edges up to `V-1` times:
   - For each edge `(u, v)`, if the distance to `v` through `u` is shorter than the known distance, update the distance to `v`.
3. After `V-1` iterations, check for negative weight cycles by trying to relax the edges again. If any distance can still be updated, a negative weight cycle exists.