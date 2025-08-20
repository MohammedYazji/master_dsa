# Graph Interview Questions

## Table of content

[1. Valid Path in Graph](#1-valid-path-in-graph-bfs-traversal)
[2. Detect Cycle in Directed Graph](#2-detect-cycle-in-directed-graph-dfs--recursion-stack)

---

## 1. Valid Path in Graph (BFS Traversal)

- **Problem Summary**

  - Given a graph and two vertices (start and end), determine if there's a valid path between them
  - Return true if path exists from start to end, otherwise return false
  - Uses BFS to explore all reachable vertices from start vertex

- **How to solve** ==Time O(v + E), Space O(V)==

1. Find Start and End Vertices

   - Locate both vertices in the graph
   - Return false if either doesn't exist

2. BFS Traversal

   - Use queue to store vertices to visit
   - Use visited set to avoid revisiting vertices
   - If we reach end vertex, path exists

- **Links**
  - [my implementation in graph class](../my_code/Data_Structures/graph/graph.py)

---

## 2. Detect Cycle in Directed Graph (DFS + Recursion Stack)

- **Problem Summary**

  - Given a directed graph, determine if it contains a cycle
  - A cycle exists if we can start from a vertex and return to it following directed edges
  - Return true if cycle exists, otherwise return false

- **How to solve**

1. DFS with Recursion Stack

   - Use visited set to track all processed vertices
   - Use recursion stack to track current path vertices

2. Cycle Detection Logic

   - If neighbor is unvisited: recursively check it
   - If neighbor is in recursion stack: cycle found
   - Remove vertex from recursion stack when backtracking

- **Links**
  - [my implementation in graph class](../my_code/Data_Structures/graph/graph.py)
