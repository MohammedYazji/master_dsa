# Recursion

## Table of content

- [What is Recursion](#what-is-recursion)
- [How It Works](#how-it-works-the-stack)
- [Two Rules for Recursion](#two-rules-for-recursion)
- [Common Mistakes](#common-mistakes)
- [Two Ways to Write Recursive Functions](#two-ways-to-write-recursive-functions)
- [Notes](#important-notes)
- [Implementation](#implementation)
- [Interview Questions](#interview-questions)

## What is Recursion?

> A function that **calls itself** to solve a problem by breaking it into smaller pieces.

Think of it like **Russian dolls** - each doll contains a smaller version of itself!

---

## How It Works (The Stack)

- In almost all programming languages, there is a built-in data structure that manages what happens when functions are called — called the [stack](./stack.md).
  - The stack follows LIFO (Last In, First Out) order: the last function called is the first one to finish.
- Every time a function calls another function (including itself in recursion), a stack frame is added ("pushed") to the stack, storing information like local variables and where to return after finishing.
- When a function finishes, its stack frame is removed ("popped") from the stack.
- This structure keeps track of active function calls and their execution order.
- In recursion, the stack grows with each recursive call until the base case is reached, then unwinds as calls complete.

---

## Two Rules for Recursion

### 1. Base Case - The Stop Point

- The base case is the condition that stops the recursion.
     - Without a base case, the function would call itself forever and cause a stack overflow.
     - This is the most important concept in recursion because it prevents infinite loops.

### 2. Different Input in Each Call

- Each recursive call must work with a different input, moving closer to the base case.
     - This ensures that after some number of calls, the base case is met, and recursion ends.

### Example

```python
def countdown(num):
    # Rule 1: Base case - STOP when num is 0
    if num == 0:
        print("Done!")
        return

    print(num)
    # Rule 2: Change input - make it smaller
    countdown(num - 1)

# countdown(3) prints: 3, 2, 1, Done!
```

---

## common mistakes

- **Stack overflow** ⇒ happens when recursion never ends (infinite calls)
- Forgetting to return in base case or returning the same input, so base case never reached

---

## Two Ways to Write Recursive Functions

### 1. Helper Function

**When to use:**

- When we want to use recursion and return a list or build up a result, not just a single value.
- It helps organize the recursive logic by:
  - Creating an outer function that holds the result list.
  - Using an inner helper function to do the recursion.
- This approach avoids using global variables and keeps everything clean and contained.

**Example**

```python
def collect_odds(input_list):
    # This list will store our final output
    my_list = []
    # helper recursion method to not mutate the list above
    def helper(helper_input):
        # Base case: if the list is empty, stop recursion
        if len(helper_input) == 0:
            return

        # If the first element is odd, add it to the my_list list
        if helper_input[0] % 2 != 0:
            my_list.append(helper_input[0])

        # Recursive call with the rest of the list
        helper(helper_input[1:])
       
    # Start the recursion
    helper(input_list)

    return my_list
```

**Explanation**

1. We define an outer function collect_odds(input_list) that:
   - Creates an empty list result to store odd numbers.
        - Defines a helper function helper() inside it.
2. The helper:
      - Checks if the input is empty (base case).
      - If the first element is odd, it's added to result.
      - Then it recursively processes the rest of the list using helper_input[1:].

3. Finally, the result list is returned from the outer function after recursion finishes.

### 2. Pure Recursion

**it’s just regular recursion.**

**When to use:** We don’t use an outer helper function — instead, the recursive logic and result-building all happen in one function.

**Example**

```python
def find_odd_numbers(numbers):
    if len(numbers) == 0:  # Base case
        return []

	# Recursive logic
    if numbers[0] % 2 == 1:
	    # If first number is odd,
	    # Include the current odd number and recurse on the rest
        return [numbers[0]] + find_odd_numbers(numbers[1:])
    else:  # If first number is even, skip it
        return find_odd_numbers(numbers[1:])
```

**Explain**

1. Base case:
   - If the list is empty, we return an empty list to stop recursion.
2. Recursive case:
   - If the first element is odd:
     - We return a new list containing it, plus the result of the recursive call on the rest of the list.
   - If the first element is even:
      - We just skip it and recurse on the rest of the list.

---

---

## Important Notes

- Recursion is a function calling itself with smaller input each time.
- Don't forget the **base case**
- The call stack tracks each call (LIFO).
- change input each call
- Use helper method when building array or string
- Pure recursion returns results directly and avoids external mutations.
- \*\*Avoid recursion unless necessary
  - Recursion increases both **time and space complexity**
  - so Prefer **loops** if the problem can be solved without recursion.

## Implementation

[Check my recursion functions folder](../my_code/Algorithms/recursion/)

- include many common recursion problems

## Interview Questions

[Recursion Interview Questions](./recursion-interview.md)
