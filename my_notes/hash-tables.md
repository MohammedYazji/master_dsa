# Hash Tables

## Table of Content

- [What is Hash Table?](#what-is-hash-table)
- [How Hash Tables work?](#how-hash-tables-work)
- [Hash Function Properties](#hash-function-properties)
- [The Collision Problem](#the-collision-problem)
- [Collision Handling Methods](#collision-handling-methods)
- [Time Complexity Reality](#time-complexity-reality)
- [Hash Table Types](#hash-table-types)
- [Hashable vs Non-Hashable](#hashable-vs-non-hashable)
- [Building Hash Tables](#building-hash-tables)
- [Load Factor & Resizing](#rehashing---resizing-rules)
- [Important Notes](#important-notes)
- [Summary](#summary)
- [Interview Questions](#interview-questions)

## What is Hash Table?

> A data structure that stores data as **key-value pairs** where each key acts as an index. It enhances all operations to almost **O(1) time complexity**

- Searching
- Insertion
- Deletion
- Access

> When you are in interview. The first thing to think about is [Hash Tables] because its very efficient.

## How Hash Tables work?

### Before Hash table

- When we was searching in arrays we must loop through each element
  - so this will take **O(n)**
- and that consider Inefficient for large datasets

### With Hash Tables

- each element stored at its calculated index
  - so here we know each key will stored at any index, then we go to there directly
    - so this will take **O(1)**
- Directed access using hash function
- Convert any input to a specific index position

### Hash Function Examples

#### Numbers

```python
hash[4] = 4  // store value 4 at index 4
```

#### Characters

```python
'a' = ASCII 97 → index 0 (97-97)
'b' = ASCII 98 → index 1 (98-97)
```

#### Strings

```python
"CAB" = 67 + 65 + 66 = 198
198 % 10 = 8 → store at index 8
```

#### IDs

```python
Use last digit as index (for example)
```

#### Basic Hash Function Formula

```python
index = element % array_size
```

**Example:** `10000000 % 10 = 0` (stored at index 0)

---

## Hash Function Properties

> A **hash function** is a mathematical algorithm that converts input data of any size into a fixed-size output called a hash value, hash code, or digest.

### What makes a good Hash Function?

1. **Minimize collisions** ==- different inputs rarely produce same hash==
2. **Fast calculations** - efficient to compute the index
3. **Even distribution** spread keys across table, not all in same place
   - to make the time complexity as small as possible
4. **Use Prime numbers** for better distribution
5. **Deterministic** - same input always gives same index

### Common Hash Function Types

#### 1. Division Method

```python
h(key) = key % m
```

- Where `m` is table size (preferably prime)

#### 2. Multiplication Method

```python
h(key) = floor(m × (key × A mod 1))
```

Where `A` is constant (0 < A < 1)

#### 3. String Hashing

```
hash = 0
for each character c in string:
    hash = hash + ASCII(c)
return hash % table_size
```

---

## The Collision Problem

**Problem**: Multiple elements may hash to the same index

**When hash table size increases → collisions become smaller**

## Collision Handling Methods

### 1. Replacement (Circular Way)

- Simply replace old element with new one
- **Problem**: Data loss

### 2. Open Addressing

#### Linear Probing (Poor Distribution)

- Store new element in **first free space** after collision index
- **Search Process**: Start from hash index, walk forward until found
- **Time Complexity**: Better than O(n), not quite O(1) but still better than O(log n)
- **Problem**: Multiple elements collision in same area → huge search time → clustering

my linear-probing implementation [code](../my_code/Data_Structures/hash_tables/linear_probing_hash_table.py)

#### Quadratic Probing

- **Formula**: `(index + i²) % size`
- Where `i` is attempt counter (1, 2, 3...)
- **Advantage**: Reduces clustering compared to linear probing

my quadratic-probing implementation [code](../my_code/Data_Structures/hash_tables/quadratic_probing_hash_table.py)

#### Double Hashing

- Use **two hash functions**, one spare
- Example functions:
  - `k % 7`
  - `5 - (k % 5)`

### 3. Open Hash (Separate Chaining)

#### Implementation

- Each array index contains a **bucket** (linked list)
- Colliding elements are chained together inside this index

#### Example Process

1. Element 13: `13 % 10 = 3` → goes to index 3
2. Another element hashes to index 3 → add to linked list at index 3
3. **Search**: Go to index 3, **traverse linked list**

#### Time Complexity

- **Best case**:
  - O(1) - no collisions
- **Average case**:
  - ==O(1 + α) where α = load factor==
- **Worst case**:
  - O(n) - all elements in same bucket

my chaining implementation [code](../my_code/Data_Structures/hash_tables/chaining_hash_table.py)

---

## Time Complexity Reality

### Is it Really O(1)?

**[Amortized](./amortized-analysis.md) O(1) on average**

- Right, you might loop over bucket's linked list
- But with good hash function, usually find in first attempt
- **Example**: 100,000,000,000 elements, search for 'mohamed'
  - Instead of O(n), get ~O(1)
  - Go to specific index and search there
  - Much better than looping whole array = **fast lookup**

---

## Hash Table Types

### 1. Sets

- Only keys, no values
- Check if element exists

### 2. Maps (Dictionaries)

- **Key-value pairs**
- Keys must be **hashable**
- Values can be any data type

---

## Hashable vs Non-Hashable

### Hashable (Immutable)

**Why**: Won't change in future → hash won't change

- Strings
- Integers
- Tuples

### Not Hashable (Mutable)

**Why**: Can change → hash would change

- Arrays/Lists
- Dictionaries

---

## Building Hash Tables

### Step-by-Step Process

1. **Convert all keys to integers**
   - Strings to integers also
2. **Index must be in range of m** (table size)
3. **Calculate index**: `key % m` where `m = size`
4. **Use prime numbers for m**:
   - If size = 7, keep it (already prime)
   - If size = 8, use 11 (first prime larger than 8)

---

## Load Factor & Resizing

> We just use it with Open addressing and probing

### Load Factor Formula

```
Load Factor = (Number of elements in table) / m
```

Where `m` = table size

### Rehashing - (Resizing) Rules

- **Threshold**: the **maximum load factor percentage before we resize** the hash table.
  - Keep load factor < 50%
- **When to resize**: If load factor > 50%
- **How to resize**:
  - Get first prime number after `m × 2`
  - Example: If size was 7, resize to 17

### Rehashing Process

When resizing, must **rehash** all existing elements with new table size

- make a new table with the new size then insert all elements from the old one

---

## Important Notes

- When hash table size increases → collisions become smaller
- When you are in interview. The first thing to think about is [Hash Tables] because its very efficient.
- Hash tables provide near O(1) performance when properly implemented with good hash functions and collision handling.
- when we insert still O(1) because if there's resizing I not count this
  - Why?!
    - because of [amortized-analysis](./amortized-analysis.md) right I resize the table with O(n)
      - but I'm not do this in each insert
      - I do it once after while so in general insertion will remain **O(1)**
- **We don't use threshold and resizing with open-Hashing**
  - **we just use it with open addressing**

---

## Summary

| Method            | Pros               | Cons         | Time Complexity |
| ----------------- | ------------------ | ------------ | --------------- |
| Replacement       | Simple             | Data loss    | O(1)            |
| Linear Probing    | Cache-friendly     | Clustering   | ~O(1)           |
| Quadratic Probing | Reduces clustering | More complex | ~O(1)           |
| Separate Chaining | No data loss       | Extra memory | O(1) average    |

---

## Interview Questions

- [Hash Tables Interview Questions](./hash-interview.md)
