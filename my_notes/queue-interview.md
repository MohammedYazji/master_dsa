# Queue Interview Questions

## Table of Contents

[#1. Implement Queue Using Stack](#1-implement-queue-using-stack)

---

## 1. Implement Queue Using Stack

- **Problem summary**

  - You need to implement a Queue (FIFO - First In, First Out) using only Stacks (LIFO - Last In, First Out).

- **How to solve it**

  - as you know Queue removes from the front, but Stack only removes from the top!

    - so use two stacks
      - the first one to adding new elements (enqueue)
        - To ADD (enqueue)
          - Just push to Stack 1
      - the second one to removing elements (dequeue)
        - To REMOVE (dequeue)
          - If Stack 2 is empty → move ALL items from Stack 1 to Stack 2 (this reverses the order)
            - then Pop from Stack 2

- **Time Complexity**
  Enqueue: O(1)
  Dequeue: O(1) [amortized](./amortized-analysis.md) (we will not take O(n) each pop but each few steps so in general O(1))

- [my implementation](../my_code/Data_Structures/stack_and_queue/queue_using_stack.py)
