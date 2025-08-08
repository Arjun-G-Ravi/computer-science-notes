# Tree Invariants
Tree invariants are properties that must hold true for a binary search tree to maintain its structure and properties. Some common invariants include:
- The left subtree of a node contains only nodes with values less than the node's value.
- The right subtree of a node contains only nodes with values greater than the node's value.
- The left and right subtrees of each node are also binary search trees.
- The height of the left and right subtrees of any node differ by at most one (for balanced trees like AVL trees).
- The in-order traversal of a binary search tree produces a sorted sequence of values.
- The depth of the tree is minimized to ensure efficient search operations.

# Tree Rotations
Tree rotations are operations that change the structure of a binary tree without affecting the in-order sequence of the nodes. They are commonly used in self-balancing binary search trees to maintain balance after insertions or deletions.
Rotations can be classified into four types:
- Left Rotation
- Right Rotation
- Left-Right Rotation
- Right-Left Rotation
