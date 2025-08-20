# Heap Interview Questions

## Table of content

[1. Validate AVL Tree](#1-validate-avl-tree)
[2. Range Search in AVL Tree](#2-range-search-in-avl-tree)
[3. Find k-th Smallest Element in AVL Tree](#3-find-k-th-smallest-element-in-avl-tree)

---

## 1. Validate AVL Tree

- **Problem Summary**

  - Check if a binary tree satisfies AVL tree properties
  - Each node's balance factor must be in [-1, 0, 1]
  - Balance factor = height(left subtree) - height(right subtree)
  - Return true if valid AVL tree, otherwise false

- **How to solve**

1. Check Balance Factor

   - Calculate balance factor for current node
   - Must be -1, 0, or 1 for valid AVL

2. Recursive Validation

   - Recursively check left and right subtrees
   - All subtrees must be valid AVL trees

- **Links**
  - [my implementation in avl_tree class](../my_code/Data_Structures/tree/avl_tree.py)

---

## 2. Range Search in AVL Tree

- **Problem Summary**

  - Return all values in AVL tree between [low, high] inclusive
  - Use BST properties to optimize search (skip unnecessary subtrees)
  - Test Case: Tree [40, 20, 60, 10, 30, 50, 70], range [25, 65] → [30, 40, 50, 60]

- **How to solve**

1. BST Property Optimization

   - If node > low: search left subtree
   - If node < high: search right subtree

2. In-Range Collection

   - Add node to result if low ≤ node.value ≤ high
   - Use helper function to avoid mutating original list

- **Links**
  - [my implementation in avl_tree class](../my_code/Data_Structures/tree/avl_tree.py)

---

## 3. Find k-th Smallest Element in AVL Tree

- **Problem Summary**

  - Return the k-th smallest element in AVL tree (1-indexed)
  - Use in-order traversal to get sorted sequence

- **How to solve**

1. In-Order Traversal

   - Traverse left → process node → traverse right
   - Produces sorted sequence for BST/AVL

2. Return k-th Element

   - Store all values in array during traversal
   - Return element at index k-1 (convert to 0-indexed)

- **Links**
  - [my implementation in avl_tree class](../my_code/Data_Structures/tree/avl_tree.py)
