# Hierarchical Organization of Data Structures

## 1. Linear Data Structures
- **Array**: A collection of elements stored in contiguous memory, accessed by index.
  - Static Array: Fixed size, allocated at compile time.
  - Dynamic Array: Resizable, allocated at runtime
  -  Suffix Array: A sorted array of all suffixes of a string, enabling efficient string operations.
- **Linked List**: A sequence of nodes, each containing data and a reference to the next node.
  - Singly Linked List
  - Doubly Linked List
  - Circular Linked List
- **Stack**: A LIFO (Last In, First Out) structure where elements are added and removed from the top.
- **Queue**: A FIFO (First In, First Out) structure where elements are added at the rear and removed from the front.
  - Circular Queue
  - Priority Queue
  - Deque (Double-Ended Queue)

## 2. Non-Linear Data Structures
- **Tree**: A hierarchical structure with nodes connected by edges, starting from a root node.
  - **Binary Tree**: A tree where each node has at most two children (left and right).
    - **Binary Search Tree (BST)**: A binary tree where the left child is smaller and the right child is larger than the parent.
      - **AVL Tree**: A self-balancing BST where the height difference between subtrees is at most one.
      - **Red-Black Tree**: A self-balancing BST with nodes colored red or black for balance.
      - **Splay Tree**: A self-adjusting BST where recently accessed nodes move to the root.
    - **B-Tree**: A balanced tree with multiple keys per node, optimized for disk storage.
      - **B+ Tree**: A B-Tree variant where leaf nodes store all data, used in databases.
    - **Segment Tree**: A tree for storing intervals, enabling efficient range queries.
    - **Fenwick Tree (Binary Indexed Tree)**: A compact structure for prefix sum calculations.
    - **Quad Tree**: A tree with four children per node, used for 2D spatial indexing.
    - **K-D Tree**: A binary tree for organizing k-dimensional points, enabling spatial searches.
  - **Trie**: A tree-like structure for storing strings, with nodes representing prefixes.
    - **Suffix Tree**: A compressed trie of all suffixes of a string, for fast pattern matching.
    - **Radix/Patricia Tree**: An optimized trie for efficient string storage and retrieval.
  - **Heap**: A tree-based structure where the parent is larger (max-heap) or smaller (min-heap) than its children.
    - Binary Heap
    - Binomial Heap
    - Fibonacci Heap

- **Graph**: A collection of nodes connected by edges, representing relationships.
  - Directed Graph
  - Undirected Graph
  - Weighted Graph
  - **Disjoint Set (Union-Find)**: A structure for tracking elements in disjoint sets, supporting union and find operations.

## 3. Associative Data Structures
- **Hash Table**: A structure mapping keys to values using a hash function for fast lookup.
  - **Set**: A collection of unique elements, often implemented with hash tables or trees.
  - **Map/Dictionary**: A collection of key-value pairs with unique keys for efficient retrieval.
  - **LRU Cache**: A hash table and doubly linked list for tracking least-recently-used items.
- **Bloom Filter**: A probabilistic structure for testing set membership with minimal space.
- **Skip List**: A probabilistic layered linked list for fast search, insertion, and deletion.