# Stack Data Structure

## Table of Contents

1. [What is a Stack](#what-is-a-stack)
2. [How it Works](#how-it-works)
3. [Common applications on stack](#common-applications-on-stack)
4. [Time Complexity](#time-complexity)
5. [Implementations](#implementations)
6. [Summary](#summary)
7. [Interview Questions](#interview-questions)

---

## What is a Stack

> A **stack** is a linear data structure that follows the **LIFO** (Last In, First Out) principle.

That means the **last** item you add is the **first** one you remove.

---

## How it Works

Imagine it like a **stack of books**:

- You can **only add** a book to the **top** of the stack.
- When removing a book, you **must take the top one first**.

![stack-structure](../attachment/images/stack-structure.svg)

---

## Common applications on stack

- **Function call management** and \*\*Recursive function
  - each function call will add to the stack
  - then pop from it when finish execution
- **Undo/Redo**
- **Browser history**
- **Expression parsing & evaluation**

---

## Time Complexity

| Operation    | Complexity | Notes                      |
| ------------ | ---------- | -------------------------- |
| `push`       | **O(1)**   | Add element to top         |
| `pop`        | **O(1)**   | Remove top element         |
| `peek`/`top` | **O(1)**   | View top without removing  |
| `search`     | **O(n)**   | must loop over all items   |
| `access`     | **O(n)**   | no index access like array |

---

## Implementations

Some programming languages have a **built-in Stack** (e.g., Java’s `Stack` class),  
but **JavaScript** and **Python** don’t have one — you can implement it yourself.

---

### 1. Dynamic Array Implementation

- Create a **class** with a normal array inside with simple array operations like

  - Implement only **stack-specific** operations:
    - `push` / `append` → Add to top
    - `pop` → Remove top
    - `peek` → Return the top element without removing it
    - `isEmpty` → Check if stack has no elements
    - `size` → Return current stack length
    - `printStack` → Visualize elements

- [Dynamic Array Implementation](../my_code/Data_Structures/stack_and_queue/stack_Array_implemetation.py)
- [Dynamic Array Implementation with Resizing Strategy](../my_code/Data_Structures/stack_and_queue/stack_Array_implemetation_with_resizing_strategy.py)

---

### 2. Linked List Implementation

1. Create **two classes**: `Node` and `Stack`.
2. **Node** contains:
   - `data`
   - `next` pointer
3. **Stack** contains:
   - `top` pointer (head of list)
4. Implement the same methods as the dynamic array version, but using **linked list operations**.

- [Linked List Implementation](../my_code/Data_Structures/stack_and_queue/stack_list_implementation_top.py)

---

## Summary

- **stack is**
  - A LIFO (Last In, First Out) data structure.
- **Access**
  - Only the top element is accessible directly.

## Interview Questions

- [Stack Interview Questions](./stack-interview.md)
