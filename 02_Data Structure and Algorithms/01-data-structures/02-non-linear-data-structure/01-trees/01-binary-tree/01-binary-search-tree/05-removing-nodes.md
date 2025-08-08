# Removing nodes from a BST

We first find the node to be removed by comparing its value with the values of existing nodes, starting from the root. Once we locate the node, we handle three cases based on the number of children the node has:
- **Node with no children (leaf node)**: Simply remove the node.
- **Node with one child**: Remove the node and link its parent directly to its child.
- **Node with two children**: Remove the node and replace it with its in-order predecessor (`the maximum value in its left subtree`) or in-order successor (`the minimum value in its right subtree`).