# Recursion Interview Questions

> In interviews, when you solve a recursion question, the interviewer often asks:
>   > \_"Can you optimize it?"
>   >
>   >
>   > So always think:

- Can I avoid **recomputing the same values**?
    - Can I use **memorization** or **iteration**?
    - Is there a **more space-efficient** solution?

## Table of content

- [Enhancing Fibonacci](#enhancing-fibonacci)
  - [1. Naive Recursive Solution](#1-naive-recursive-solution)
  - [2. Memorization (Top-Down Dynamic Programming)](#2-memorization-top-down-dynamic-programming)
  - [3. Iterative (Bottom-Up Dynamic Programming)](#3-iterative-bottom-up-dynamic-programming)
  - [Summary](#summary)
- [Check my another recursion functions implementation folder](#check-my-another-recursion-functions-implementation-folder)

---

- A very common example is the **Fibonacci sequence** — be ready to explain and optimize all versions!

---

## Enhancing Fibonacci

> **Fibonacci problem:**

> Given `n`, return the `n-th` number in the Fibonacci sequence:

> `0, 1, 1, 2, 3, 5, 8, 13, ...`

---

### 1. Naive Recursive Solution

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

- **Time:** `O(2^n)`
- **Space:** `O(n)`
- Very inefficient — it **recomputes the same values again and again.**

---

### 2. Memorization (Top-Down Dynamic Programming)

> Store already-computed values in a dictionary to avoid repeated work.

```python
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
```

- **Time:** `O(n)`
- **Space:** `O(n)` (due to the memo dictionary and call stack)
- Much faster — avoids redundant calls

---

### 3. Iterative (Bottom-Up Dynamic Programming)

> Start from the bottom (`0 → n`) and build up using variables.

```python
def fib(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
```

- **Time:** `O(n)`
- **Space:** `O(1)`
- Best performance — no recursion, no dictionary

---

### Summary

| Version         | Time Complexity | Space Complexity | Notes                         |
| --------------- | --------------- | ---------------- | ----------------------------- |
| Naive Recursive | O(2^n)          | O(n)             | Bad Performance               |
| Memorized       | O(n)            | O(n)             | Efficient with recursion      |
| Iterative       | O(n)            | O(1)             | Best - fast & memory friendly |

---

## Check my another recursion functions implementation folder

[here](../my_code/Algorithms/recursion/)
