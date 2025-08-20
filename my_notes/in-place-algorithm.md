---
type: note
title: in-place-algorithm
tags:
  - dsa
date: 2025-08-14
status: done
related:
  - "[[space-complexity]]"
course: "[[DSA-Notes]]"
---
# In-Place Algorithms

> **In-place algorithms** **modify the input data directly using only O(1) extra memory**, trading original data preservation for memory efficiency.

- for example we can sort the array in place O(1) without creating a new sorted array O(n)
## Why to use it?

- Use **O(1) extra space** only
- **Modify input directly, no copies**
- **Memory usage doesn't grow with input size**

> **In Short**:

**Pros:** 
- Memory efficient, faster 
**Cons:** 
- Destroys original data

## Examples

- **Bubble Sort** - swap adjacent elements
- **Array reversal** - swap from ends
- **Remove duplicates** - overwrite array
- **String reversal** - swap characters

## In conclusion

> swap or change the original data without creating new variable like temp or new array