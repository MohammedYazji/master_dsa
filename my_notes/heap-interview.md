# Heap Interview Questions

## Table of content

[1. Heap Sort](#1-heap-sort)
[2. Get K Minimum Values from Heap](#2-get-k-minimum-values-from-heap)

---

## 1. Heap Sort

- **Problem Summary**

  - Sort an array using the heap data structure
  - Build a max heap from the array, then repeatedly extract the maximum element
  - Time complexity: O(n log n), Space complexity: O(1) for in-place version

- **How to solve**

1. Build min/max heap

   - Convert array into max, or min heap structure
   - Start from last non-leaf node and heapify down

2. Extract Elements

   - Swap root (min) with last element
   - Reduce heap size and heapify down
   - Repeat until heap is empty

- **Links**
  - [my implementation](../my_code/Data_Structures/heap/heap_sort.py)

---

## 2. Get K Minimum Values from Heap

- **Problem Summary**

  - Extract the k smallest elements from a min heap
  - Two variations: get k values as list, or get the k-th minimum value
  - Should not modify the original heap

- **How to solve**

1. Copy Original Heap

   - Create copy to avoid modifying original
   - Use copy for extraction operations

2. Extract K Times
   - For k values: pop k times and store in array
   - For k-th value: pop k times, return the k-th popped value

- **Links**
  - [my implementation](../my_code/Data_Structures/heap/get_k_minimum_value_from_heap.py)
