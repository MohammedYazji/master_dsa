# Space Complexity

## Table of Content

1. [What's This About](#whats-this-about)
2. [Time vs Space](#time-vs-space)
3. [The Tricky Part - What Counts](#the-tricky-part---what-counts)
4. [How to calculate space complexity](#how-to-calculate-space-complexity)
5. [Examples](#examples)
6. [Important Notes and Summary](#important-notes-and-summary)

---

## What's This About

So I've been learning about [time complexity](../my_notes/asymptotic-analysis.md) (how long code takes to run), but turns out there's also **space complexity** - basically "**how much extra memory does my code need?**"

- right machines storage nowadays is massive but we also need to care about **space complexity**
  - Why??
    - **Mobile apps** can't use tons of memory
    - in **interviews** ask about **time and space**
    - and many more...

---

## Time vs Space

**Time Complexity:**

> How does runtime change as input gets bigger?

- O(n) = takes longer with more data
- We count operations (loops, comparisons, etc.)

**Space Complexity:**

> How much EXTRA memory do I need as input gets bigger

- O(n) = need more memory with more data
- We count variables, arrays, objects we create

---

## The Tricky Part - What Counts

Here's what confused me at first: **we DON'T count the input!**

```python
def double_everything(arr):  # arr doesn't count toward space complexity!
    new_list = []            # This DOES count!
    for num in arr:
        new_list.append(num * 2)
    return new_list          # This DOES count!
```

**Why?**

- Because we assume the input already exists and we count it in the time complexity
  - We only care about **EXTRA memory our algorithm needs.**

This is called [Auxiliary Space Complexity](../my_notes/auxiliary-space-complexity.md)

---

## How to calculate space complexity

**O(1) Space (Constant):**

- Just using a few variables that **don't grow**
- [[in-place-algorithm|In place]] operations (modifying the input)
- Mathematical calculations

**O(n) Space (Linear):**

- Creating a new **array/list** the **same size as input**
- Storing results that grow with input like **strings**
- Recursive calls (each call **uses stack space under the hood!**)

**O(n²) Space (Quadratic):**

- Creating a **2D array** where both dimensions depend on n

| What I Create                            | Space Used |
| ---------------------------------------- | ---------- |
| `x = 5` (numbers, booleans)              | O(1)       |
| `name = "hello"` (string of length n)    | O(n)       |
| `my_list = [1,2,3]` (list of n items)    | O(n)       |
| `my_dict = {"a": 1}` (dict with n items) | O(n)       |

**In Short:**

- If it grows with input size, it's probably O(n).
- If it's always the same size, it's O(1).

> So `n` is the input for our algorithm

---

## Examples

### 1. Simple Variable

```python
def sum_array(arr):
    total = 0        # O(1) - just one number
    for num in arr:
        total += num
    return total     # O(1) - returning one number

# Space complexity: O(1)
```

No matter if the array has 10 or 10,000 items, I only create one `total` variable.

### 2. Creating a New Array

```python
def double_array(arr):
    doubled = []                    # O(n) - will grow to size n
    for num in arr:
        doubled.append(num * 2)
    return doubled                  # O(n) - returning array of size n

# Space complexity: O(n)
```

I'm creating a new array that's the same size as the input. That's O(n) extra space.

- so I assigned in the memory n of address

### 3. Multiple Variables

```python
def analyze_array(arr):
    max_val = arr[0]      # O(1)
    min_val = arr[0]      # O(1)
    sum_val = 0           # O(1)

    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
        sum_val += num

    return max_val, min_val, sum_val  # O(1) - just 3 values

# Space complexity: O(1) + O(1) + O(1) = O(1)
```

Even though I have multiple variables, they're all constants - **doesn't matter how big the input is**.

### 4. The Sneaky One

```python
def reverse_string(s):
    result = ""              # Starts as O(1)
    for char in s:
        result = char + result   # This rebuilds the string each time!
    return result            # O(n)

# Space complexity: O(n)
```

This one tricked me! Even though I'm just updating one variable, strings in Python are immutable, so each concatenation creates a new string. By the end, `result` is size n.

---

## Important Notes and Summary

**Time complexity**

- How long does this take
  **Space complexity**
- How much extra memory do I need?

For space complexity:

- **Don't count inputs** [Auxiliary Space Complexity](../my_notes/auxiliary-space-complexity.md)
- Just Count what your algorithm creates
  - **Count new variables** => do they grow with input size
  - **Count new data structures =>** arrays, objects
  - Remember **recursion**
    - each call **uses stack** space
  - Remember strings
    - concatenation will take O(n)

**Most common mistake I made:**

- Forgetting that each recursive call uses O(1) stack space, so if you have n recursive calls, that's **O(n) space**

**Don't use more space**

1. instead of use variables to store everything try to return the value immediately from the function [I know It's constant and not matter 😅 but whatever do this plz]
2. sort [in-place](../my_notes/in-place-algorithm.md) (O(1) space) instead of create a new sorted array (O(n) space)
