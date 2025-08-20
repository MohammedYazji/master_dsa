# Hash Interview Questions

## Table of Contents

[1. Two Sum](#1-two-sum)
[2. First non-repeating character](#2-first-non-repeating-character)
[3. duplicate detection](#3-duplicate-detection)

---

## 1. Two Sum

### Problem Summary

- Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

### How to Solve

- **naive solution using nested loop** ==T => O(n^2)==
  - use nested loop to iterate over the element and each element after it
    - so if the sum of these two elements same as the target key => return True
- **using hash** ==T => O(n)==
  - make a hash to keep track of each character complement to reach the target
  - loop over the array
    - and calc the rest to reach the target key
    - if this rest number in the hash
      - so return True because we found the complement
    - else insert the number itself then move forward to next one
  - finally if we exit the loop without return anything so return False

### Links

[LeetCode](https://leetcode.com/problems/two-sum/description/) > [CodeWars](https://www.codewars.com/kata/54d81488b981293527000c8f/)

**My Implementation**

- [naive](../my_code/Data_Structures/hash_tables/two_sum_naive.py)
- [hash_two_sum](../my_code/Data_Structures/hash_tables/two_sum_enhanced.py)

---

## 2. First non-repeating character

### Problem Summary

- Given a string `s`, find the **first** non-repeating character in it and return its index. If it **does not** exist, return `-1`

### How to Solve

- we need two for loops ==T => O(n)==
  - first loop to iterate over the string and store in my hash map each character with it's frequency
    - so if character exist before increment it's value by one
    - if not there
      - add it with initial value 1
  - the other loop to loop over the array again and check the current character value in the map if equal one return it

### Links

[LeetCode](https://leetcode.com/problems/first-unique-character-in-a-string/description/)
[CodeWars](https://www.codewars.com/kata/52bc74d4ac05d0945d00054e)

**My Implementation**

- [First non_repeating Character](../my_code/Data_Structures/hash_tables/first_non_repeating_char.py)

---

## 3. duplicate detection

### Problem Summary

### How to Solve

### Links

[LeetCode](https://leetcode.com/problems/first-unique-character-in-a-string/description/)
[CodeWars](https://www.codewars.com/kata/52bc74d4ac05d0945d00054e)

**My Implementation**

- [duplicate detection](../my_code/Data_Structures/hash_tables/duplicate_detection.py)
