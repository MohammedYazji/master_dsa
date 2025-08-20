# Amortized Analysis

## What is Amortized Analysis?

> It's a way to **average out the cost** of operations over time — especially when **some operations are expensive**, but they **don't happen often**.

## Real-Life Analogy:

Imagine you're filling a bag with stones:

- Each time you add a stone, it takes **1 second**.
- But when the bag is full, you need a **new bag** and **move all the stones** — which takes more time.

Still, **on average**, each stone didn’t take much time. That’s **amortized cost**.

## In Dynamic Arrays:

- When the array is full and you insert a new item:
  - A **new bigger array** is created (usually double size).
  - All old elements are **copied** to the new array.
  - This copying is **expensive**: `O(n)`
- But this only happens **rarely** (after doubling).

So, even though **one insert is O(n)**, the **average (amortized) cost is O(1)**.

## In Short:

| Operation        | Cost        |
| ---------------- | ----------- |
| Regular insert   | O(1)        |
| Resize insert    | O(n)        |
| Amortized insert | **O(1)** ✅ |

> Because resizing doesn't happen every time.

## Conclusion:

> Amortized analysis helps explain that **even if one operation is expensive**, the **average cost per operation stays low**.

---
