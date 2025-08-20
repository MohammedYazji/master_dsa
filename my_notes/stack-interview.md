# Stack Interview Questions

## Table of Contents

[1. Valid Parentheses](#1-valid-parentheses)
[2. Min Stack](#2-min-stack)
[3. Evaluate Reverse Polish Notation](#3-evaluate-reverse-polish-notation)
[4. Implement stack using queue](#4-implement-stack-using-queue)
[5. Resizing Strategy in Array Implementation](#5-resizing-strategy-in-array-implementation)

---

## 1. Valid Parentheses

- **Problem Summary**

  - Given a **string** containing just the characters `(`, `)`, `{`, `}`, `[` and `]`, determine if the input string is valid. An input string is valid if open brackets are closed by the same type of brackets, and in the correct order.

- **How to Solve** ==T O(n), S => O(n) => Stack take O(n)==

  - Use a stack to keep track of opening brackets.
    - for each character if its an opening bracket add it to the stack
  - When a closing bracket appears, check if it matches the top of the stack.
    - if yes so pop the last one [the opening one]
    - If not, or stack is empty, return false.
  - At the end, stack should be empty if all brackets are matched.

- **Links**
  [LeetCode #20 - Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)
  [Youtube Video](https://www.youtube.com/watch?v=WTzjTskDFMg)
  [my implementation](../my_code/Data_Structures/stack_and_queue/valid_parentheses_stack.py)

---

## 2. Min Stack

- **Problem Summary**

  - Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

- **How to Solve**

  - just implement another stack and make the top of it to be the minimum value always

- **Links**
  [LeetCode](https://leetcode.com/problems/min-stack/description/)
  [Youtube Video](https://www.youtube.com/watch?v=qkLl7nAwDPo&t=500s)

---

## 3. Evaluate Reverse Polish Notation

- **Problem Summary**

  - You are given an array of strings `tokens` that represents an arithmetic expression in a [Reverse Polish Notation](http://en.wikipedia.org/wiki/Reverse_Polish_notation).

  - Evaluate the expression. Return *an integer that represents the value of the expression*.
  - **Note**
    - The division between two integers always **truncates toward zero**.

- **How to Solve** ==Time => O(n), Space => O(n)==

  - in simple when we will loop over the array
    - if we found a number push it to the stack
    - until we reach to an operator
      - so pop the last two numbers then make the process after that push the result again to the stack

- **Links**
  [LeetCode](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)
  [Youtube Video](https://www.youtube.com/watch?time_continue=174&v=iu0082c4HDE&embeds_referring_euri=https%3A%2F%2Fneetcode.io%2F)
  [my implementation](<../my_code/Data_Structures/stack_and_queue/Evaluate_Reverse_Polish_Notation_(Postfix).py>)

---

## 4. Implement stack using queue

- **Problem Summary**

  - Implement a stack using **one or two queues**. The stack should support these operations:

  - `push(x)` — Push element x onto stack.
  - `pop()` — Removes the element on top of the stack.
  - `top()` — Get the top element.
  - `empty()` — Return whether the stack is empty.

### How to Solve

Stacks are **LIFO** (Last In First Out), while queues are **FIFO** (First In First Out). To simulate a stack using queues, you need to reverse the order of elements stored in the queue(s).

#### Two common approaches:

##### 1. **Using Two Queues**

- Use two queues.
- For `push` enqueue all new elements normally
- For `pop` move all elements except the last one from the first to the second queue, then dequeue the last element from the first queue

##### 2. **Using One Queue**

- Use one queue.
- For `push`, enqueue normally.
- For `pop`, dequeue all elements except the last pushed one, enqueue them back to the queue, and dequeue the last element (which acts as the top).

- **Links**

[LeetCode](https://leetcode.com/problems/implement-stack-using-queues/description/)

- **my implementation**
  - [using two queues](../my_code/Data_Structures/stack_and_queue/stack_using_two_queues.py)
  - [using one queues](../my_code/Data_Structures/stack_and_queue/stack_using_queue.py)

---

## 5. Resizing Strategy in Array Implementation

- **Problem Summary**

You have a stack implemented using a fixed-size array. When the array fills up, how do you efficiently allow the stack to grow dynamically?

- **How to Solve**

Since array have fixed capacity, to allow the stack to grow:

- **Resize the array by allocating a new larger array**, typically doubling the current size.
- **Copy all elements** from the old array into the new array.
- Replace the old array reference with the new one.
- Continue normal push/pop operations.

This strategy is called **dynamic array resizing** or **[amortized resizing](./amortized-analysis.md)**.

- **Links**

- [my implementation](../my_code/Data_Structures/stack_and_queue/stack_Array_implemetation_with_resizing_strategy.py)
