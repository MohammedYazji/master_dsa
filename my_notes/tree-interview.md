# Trees Interview Questions

## Table of Contents

<!-- need some fixes [in-progress] -->

[1. Implement tree traversals](#1-tree-traversals-inorder-preorder-postorder)
[2. Validate if a binary tree is BST](#2-validate-if-a-binary-tree-is-bst)
[3. Compute the Height of a Binary Tree](#3-compute-height-of-a-binary-tree)

---

## 1. Tree Traversals (Inorder, Preorder, Postorder)

- **Problem:** Visit all nodes of a binary tree in a specific order.
- **Traversals:**
  1. **Inorder (Left → Node → Right)**
  2. **Preorder (Node → Left → Right)**
  3. **Postorder (Left → Right → Node)**
- **How to implement:**
  - **Recursive:** call the function on left, right, and print node in correct order
  - **Iterative:** use a stack (Preorder and Inorder) or two stacks (Postorder)
- **Time:** O(n) | **Space:** O(h) for recursion stack

- **implemented in recursive way in my BT and BST Classes**
  [BT Code](../my_code/Data_Structures/tree/binary_tree.py)
  [BST Code](../my_code/Data_Structures/tree/binary_search_tree_recursion.py)

---

## 2. Validate if a Binary Tree is BST

- **Problem:** Check if a binary tree satisfies BST property.
- **BST property:** left < node < right for all nodes
- **How to solve:**

  1. Use **recursion with min/max limits**

     - Pass allowed range for each node
     - If node.val not in range → not BST

  2. Or **Inorder Traversal:**

     - Traverse inorder → values must be increasing

- **Time:** O(n) | **Space:** O(h)

- **implemented in my BT class**
  [BST Code](../my_code/Data_Structures/tree/binary_search_tree_recursion.py)

---

## 3. Compute Height of a Binary Tree

- **Problem:** Find the height (max depth) from root to leaf
- **How to solve:**
  - **Recursive:**
    ```
    height(node) = 1 + max(height(node.left), height(node.right))
    ```
  - **Iterative:** BFS/Queue level by level → count levels
- **Time:** O(n) | **Space:** O(h)

- **implemented in my BT class**
  [BT Code](../my_code/Data_Structures/tree/binary_tree.py)
