# Linked List Interview Questions

## Table of Contents

[1. Reverse a linked list in-place](#1-reverse-a-linked-list-in-place)
[2. Merge Two Sorted Lists](#2-merge-two-sorted-lists)
[3. Remove Duplicates from Sorted List](#3-remove-duplicates-from-sorted-list)
[4. Detect Loop in Linked List (Floyd's Detection)](#4-detect-loop-in-linked-list-floyds-detection)
[5. Is Perfectly Circular Linked List](#5-is-perfectly-circular-linked-list)
[6. Find The Middle Node of Linked List](#6-find-the-middle-node-of-linked-list)
[7. Reverse Circular linked list in-place](#7-reverse-circular-linked-list-in-place)
[8. Delete Node Without Head Pointer](#8-delete-node-without-head-pointer)
[9. Reorder List](#9-reorder-list)
[10. Josephus Elimination Game](#10-josephus-elimination-game)
[11. Reverse Doubly Linked List](#11-reverse-doubly-linked-list)
[12. Sorted Circular Linked List](#12-sorted-circular-linked-list)
[13. Reduce Singly Linked List to Non-Decreasing Sequence](#13-reduce-singly-linked-list-to-non-decreasing-sequence)
[14. Insertion Sort on Singly Linked List](#14-insertion-sort-on-singly-linked-list)
[15. Remove Nth Node From End of List](#15-remove-nth-node-from-end-of-list)

---

## 1. Reverse a linked list in-place

- **Problem Summary**

  - Given the `head` of a singly linked list, reverse the list [in-place](./in-place-algorithm.md) without create a new one, and return *the reversed list*.

- **How to solve**
  1.  **Iteratively** ==T => O(n), M => O(1)== [in-place](./in-place-algorithm.md)
      - make two pointers
        - **previous** and set it as None to set the first node to point into None
        - **current** and set it as head to start looping
      - then loop over the list element by element
        - so in each loop we need to
          1.  store the next node to not lost the rest of the list
          2.  make the current node refer into the **previous** node
        - then we finish process this node so
          - set the **previous** node to be the **current** one
          - and move the **current** one to be the **next node** to process it
      - finally when we exit the loop so current will be None, and previous is the old last node [the new head]
        - so update the head and return it
  2.  **Recursive** ==T => O(n), M => O(n)== using stack each call
      - each recursive function need **base case**
        - so the **base case** here is when we reach the **last node**, or if we have just one node return the head
          - so when reach it return it to be the **new head** (the new list)
        - in each recursion call we will return the new reversed list to update it with the last added node each call
          - then lets change the links
            - for each call get the next of the current node
            - which is the last node in the new reversed list
              `front = head.next`
            - then make this last node in the new reversed list point into the current node
              `current <==> front node of the new reversed list`
              `front.next = head`
            - and make the current node to point into None
              `None <== current <== front node of the new reversed list`
              `head.next = None`
        - finally return the new head
- **Links**
  - [LeetCode](https://leetcode.com/problems/reverse-linked-list/description/)
  - [Youtube Video1](https://www.youtube.com/watch?v=D2vI2DNJGd8)
  - [Youtube Video2](https://www.youtube.com/watch?v=G0_I-ZF0S38&t=301s)
  - My Implementation
    - [my implementation Iteratively](../my_code/Data_Structures/linked_list/singly_linked_list/reverse_linked_list_iteratively.py)
    - [my implementation Recursion](../my_code/Data_Structures/linked_list/singly_linked_list/reverse_linked_list_recursive.py)

---

## 2. Merge Two Sorted Lists

- **Problem Summary**

  - You are given the heads of two sorted linked lists `list1` and `list2`.
  - Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.
  - Return *the head of the merged linked list*.

- **How to solve**
  1.  **Iteratively** ==T => O(n), M => O(1)==
      - first make a new node instance to store the two merge lists
      - start looping over the new list
        - the loop continuous as long as neither list is empty
          - If one of them becomes None, we exit the loop
            - because there's nothing to compare in these lists
        - in each loop add the smallest value from both lists to be the next node in our new list, and move the head of this list by one
          - also after each loop done we need to move the current pointer in the new list to add a new node in the next iteration
      - when we exit the loop so we have one of the list get empty
        - so check if list1 still has nodes add all remaining items to the current pointer of our new list
        - and same for list2
      - finally return the node after the new node we created
      - Why?!
        - because we initialize new node as 0 to make node
          - but we don't need the zero just start from after it
- **Links**
  - [LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/description/)
  - [Youtube Video1](https://www.youtube.com/watch?v=XIdigk956u0)
  - [Youtube Video2](https://www.youtube.com/watch?v=5Rec4JS9H5o)
  - [my implementation](../my_code/Data_Structures/linked_list/singly_linked_list/merge_two_lists.py)

---

## 3. Remove Duplicates from Sorted List

- **Problem Summary**

  - Given the `head` of a sorted linked list, *delete all duplicates such that each element appears only once*. Return *the linked list **sorted** as well*.

- **How to solve**
  1.  **Iteratively** ==T => O(n), M => O(1)== No extra space
      - loop over the whole list
      - in each iteration:
        - if the data of the current node is the same of the next one
          - ==JUMP:== make the current point into the next node of the next node
        - else just move normal step and move current pointer one step forward to keep looping
      - finally return the head
- **Links**
  - [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/)
  - [Youtube Video1](https://www.youtube.com/watch?v=Nvf9Yt1EElg)
  - [my implementation](../my_code//Data_Structures/linked_list/singly_linked_list/remove_duplicates_from_sorted_list.py)

---

## 4. Detect Loop in Linked List (Floyd's Detection)

- **Problem Summary**

  - Given `head`, the head of a linked list, determine if the linked list has a cycle in it.
  - Return `true` *if there is a cycle in the linked list*. Otherwise, return `false`.

- **How to solve**
  1.  **Using Two Pointers**
  - using two pointers slow, fast
    if meat together so its cycle
- **Links**
  - [LeetCode](https://leetcode.com/problems/linked-list-cycle/description/)
  - [my implementation](../my_code/Data_Structures/linked_list/singly_linked_list/detect_loop_linked_list.py)

---

## 5. Is Perfectly Circular Linked List

- **Problem Summary**

  - Check if the given linked list is circular [the tail refer into the head]
  - return true if it's circular, false otherwise

- **How to solve**
  1.  Keep looping while we still in the linked list, and at the same time the current pointer not equal the head
      1. so after exit the loop
         1. if the current at same place of the head => **circular**
         2. if not so its not circular because current now is **None**
- **Links**
  - **My implementation**
    - [my implementation](../my_code/Data_Structures/linked_list/singly_linked_list/is_perfectly_circular_linked_list.py)

---

## 6. Find The Middle Node of Linked List

- **Problem Summary**

  - Given the `head` of a singly linked list, return *the middle node of the linked list*.
  - If there are two middle nodes, return **the second middle** node.

- **How to solve** [in interviews prefer the first solution]

  1.  **Use slow and fast pointer approach.** ==T => O(n), M => O(1)==
      - make two pointers
        - the first one will step just step each time
        - while the other will walk two steps each time
      - when the fast pointer [which walk two steps each time] reach the end **None** so at this time the slow one will be at the middle of the list so return it.
  2.  **calc the length then loop until the middle node** ==T => O(n), M => O(1)==
      - Calc the length first,
        1.  calc the length by looping over the list and increment the length on each node
        2.  then make counter start from 0 until reach the length // 2
        3.  after finish the loop return the middle node

- **Links**
  - [**LeetCode**](https://leetcode.com/problems/middle-of-the-linked-list/description/)
  - **my implementation**
  - [1. implementation with two pointers](../my_code/Data_Structures/linked_list/singly_linked_list/middle_of_linked_list_slow_fast_pointers.py)
  - [2. implementation with calc length](../my_code/Data_Structures/linked_list/singly_linked_list/middle_of_linked_list_length_solution.py)

---

## 7. Reverse Circular linked list in-place

- **Problem Summary**

  - Given the `head` of a Circular singly linked list, reverse the list [in-place](./in-place-algorithm.md)without create a new one, and return *the reversed list*.

- **How to solve**

  1.  **Iteratively** ==T => O(n), M => O(1)==
      - make two pointers
        - **previous** and set it as the list **tail** to set the first node to point into the **tail**
        - **current** and set it as head to start looping
      - then loop over the list element by element
        - so in each loop we need to
          1.  store the next node to not lost the rest of the list
          2.  make the current node refer into the **previous** node
        - then we finish process this node so
          - set the **previous** node to be the **current** one
          - and move the **current** one to be the **next node** to process it
      - finally when we exit the loop so we need to swap the pointers of head and tail then return the new head

- **Links**
  - [my implementation](../my_code/Data_Structures/linked_list/singly_linked_list/reverse_circular_linked_list.py)

---

## 8. Delete Node Without Head Pointer

- **Problem Summary**

  - This problem requires deleting a node from a singly linked list
  - but **you're NOT given the head pointer** — **only the node to delete.**
  - We cannot traverse the list or find the previous node
  - So, we can't use a full LinkedList class with head reference

- **How to solve** ==T => O(1), M => O(1)==

  1.  to solve this problem we need to copy the value from the next node into the current one.
  2.  then skip the next node
  3.  make the current node point into the next_node next ==JUMP==
  4.  This works only if the node is NOT the tail.

- **Links**
  - [my implementation](../my_code/Data_Structures/linked_list/singly_linked_list/delete_node_without_head_pointer.py)

---

## 9. Reorder List

- **Problem Summary**

  - You are given the head of a singly linked-list. The list can be represented as:
  - L0 → L1 → … → Ln - 1 → Ln
  - _Reorder the list to be on the following form:_
  - L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
  - You may not modify the values in the list's nodes. Only nodes themselves may be changed.

- **How to solve** ==T => O(n), M => O(1)==
- It's three questions in one 😅
  - 1.  Find the middle using fast, slow pointers O(n)
  1.  reverse the second half using iterative with prev O(n)
  2.  merging in place O(n)
- **Links**
  [LeetCode](https://leetcode.com/problems/reorder-list/description/)

---

## 10. Josephus Elimination Game

- **Problem Summary**

  - You are given a group of n people, each assigned a unique identifier from 1 to n,
    standing in a sequence. Starting from the first person, a counting process is carried out repeatedly:
    every time, the k-th person in the sequence is removed. After each removal, counting resumes from the
    next person in line. This elimination process continues until only one person remains. Your task is to
    determine the identifier of that last remaining person.

- **How to solve** ==T => O(n \* k), M => O(1)==

  1.  first if we has just one node return it
  2.  else we need to make two pointers
      1. current pointer to start from the head
      2. and prev pointer to store later the previous node of deleted one before delete it safely
      3. If we have more than one node
         - then looping from 1 to the k - 1
           - in each loop
             - we must store the current node, to can remove it current safely
             - then move the current one step
           - when we finish the loop and reach the target node delete it
             - make the previous node point into the next node of the current ==JUMP==
             - and make the old deleted current to be the node after it to start the next loop from there
           - if I have just a node so return it

- **Links**
  - [my implementation](../my_code/Data_Structures/linked_list/singly_linked_list/Josephus_elimination_game.py)

---

## 11. Reverse Doubly Linked List

- **Problem Summary**

  - Given the `head` of a Doubly linked list, reverse the list [[in-place-algorithm|in-place]] without create a new one, and return *the reversed list*.

- **How to solve**

  1.  **Iteratively** ==T => O(n), M => O(1)== [very easy😅]
      - start looping from the head
        - while we in the list
          - for each node swap the pointers [prev, next]
          - **then we will walk backward**
            - **because the next is the previous now**
        - finally we must swap the tail with the head

- **Links**
  - [my implementation](../my_code/Data_Structures/linked_list/doubly_linked_list/doubly_linked_list.py)

---

## 12. Sorted Circular Linked List

- **Problem Summary**
  - Implement a class **SortedCircularLinkedList** that maintains elements in sorted order on each insertion.
  - The list should organize itself automatically to remain sorted after each insertion
  - Each node's next pointer should continue in sorted order, and the last node should point back to the head to preserve the circular structure.
  - Support insert method and print method to display contents
- **How to solve** ==T => O(n) per insertion, M => O(1)==
  1. **Insert Method Logic - Handle 3 main cases:**
     1. **Empty List Case:**
        - Create new node and set head to point to it
        - Make it point to itself to maintain circular structure
     2. **Single Node Case:**
        - **If new data >= head data:** insert after head
          - Head points to new node, new node points back to head
        - **If new data < head data:** insert before head (new head)
          - New node points to old head, old head points to new node
          - Update head pointer
     3. **Multiple Nodes Case:**
        - **If new data < head data:** insert before head (new head)
          - Traverse to find tail node (node before head)
          - Tail points to new node, new node points to old head
          - Update head pointer
        - **If new data >= head data:** find correct position
          - Traverse until find position where: `current.data < new_data < current.next.data`
          - Insert between current and current.next
          - If no such position found, insert at end (between tail and head)
  2. **Print Method Logic:**
     - Start from head, print first node
     - Move to next node and continue until we reach head again
     - This completes one full cycle of the circular list
- **Key Insights:**
  - Always maintain circular structure - last node points to head
  - Handle head updates carefully when inserting smaller elements
  - Use traversal to find correct insertion position for maintaining sorted order
  - Consider edge cases: empty list, single node, inserting at beginning/end
- **Links**
  - - [my implementation](../my_code/Data_Structures/linked_list/singly_linked_list/sorted_circular_linked_list.py)

---

## 13. Reduce Singly Linked List to Non-Decreasing Sequence

- **Problem Summary**
  - Given a singly linked list, repeatedly merge **adjacent nodes with the smallest sum**.
  - Each merge replaces two nodes with a single node whose value is their sum.
  - Continue until the list becomes **non-decreasing**.
  - Return the **total number of merge operations** performed.
- **How to Solve** ==Time => O(n^2), Space => O(1)==
  1. Loop until the list is non-decreasing:
     - Check if the list is already non-decreasing using `is_non_decreasing()`.
  2. In each iteration:
     - Find all **adjacent pairs** and their sums.
     - Track the pair with the **minimum sum**.
     - Replace that pair with a **new node** containing their sum:
       - If the pair is at the **head**, update `head` to the new node.
       - Else, update the `next` pointer of the previous node of the min-sum pair.
     - Increment the **operations counter** by 1.
  3. Stop when the list is non-decreasing.
- **Links**
  - [my implementation](../my_code/Data_Structures/linked_list/singly_linked_list/list_reduction_to_non_decreasing_order.py)

---

## 14. Insertion Sort on Singly Linked List

- **Problem Summary**
  - Sort a singly linked list using **Insertion Sort**.
  - Think of it like **sorting cards one by one**: pick a node and insert it into the correct position in a new sorted list.
  - Works in-place by adjusting the `next` pointers.
- **How to Solve** ==Time => O(n^2), Space => O(1)== [in-place](./in-place-algorithm.md)
  1. Initialize a **new empty list** `sorted_head`.
  2. Traverse the original list node by node (`current`):
     - Save the `next` node before moving `current`.
     - If `sorted_head` is empty or `current.data` < `sorted_head.data`:
       - Insert `current` at the **start** of the sorted list.
     - Else:
       - Traverse the sorted list to find the correct **insertion point**.
       - Insert `current` **after the correct node**.
     - Move to the next node in the original list.
  3. At the end, `sorted_head` points to the **fully sorted list**.
- **Links**
  - [my implementation](../my_code/Data_Structures/linked_list/singly_linked_list/insertion_sort_linked_list.py)

---

## 15. Remove Nth Node From End of List

- **Problem Summary**
  - Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.
- **How to Solve** ==Time => O(n), Space => O(1) few pointer==

  1. Initialize a dummy Node and set it point into the head

     - so now we can remove the head If we can
     - because we need the node before the node we want to delete

  2. then set left pointer to point into the dummy
  3. and right to point into the head
  4. then move right with n steps before moving the left
  5. Then move both first and second together until first reaches the end.

- **Links**
  - [LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)
