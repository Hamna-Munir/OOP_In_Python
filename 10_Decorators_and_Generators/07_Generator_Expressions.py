# ================================================================
# File: 07_Generator_Expressions.py
# Topic: Understanding Generator Expressions in Python
# ================================================================

"""
Generator Expressions are a **concise way** to create generators in Python.

They look similar to **list comprehensions**, but instead of creating an entire list
in memory, they generate **items lazily**, one by one, using the generator protocol.

✅ Generator Expression Syntax:
    (expression for item in iterable if condition)

✅ List Comprehension Syntax:
    [expression for item in iterable if condition]

📘 Key Difference:
- List comprehension → returns a list (stores all items in memory).
- Generator expression → returns a generator (produces items on demand).
"""

# ------------------------------------------------
# 1️⃣ Example: List Comprehension vs Generator Expression
# ------------------------------------------------

# List comprehension (creates the full list immediately)
squares_list = [x ** 2 for x in range(5)]
print("List Comprehension:", squares_list)  # Output: [0, 1, 4, 9, 16]

# Generator expression (creates items one by one)
squares_gen = (x ** 2 for x in range(5))
print("Generator Expression:", squares_gen)  # Output: <generator object ...>

# Access items using next()
print(next(squares_gen))  # Output: 0
print(next(squares_gen))  # Output: 1
print(next(squares_gen))  # Output: 4
print(next(squares_gen))  # Output: 9
print(next(squares_gen))  # Output: 16
try:
    print(next(squares_gen))  # Raises StopIteration
except StopIteration:
    print("Generator exhausted.")


# ------------------------------------------------
# 2️⃣ Memory Efficiency Comparison
# ------------------------------------------------
"""
Let's compare memory usage between list comprehension and generator expression.

We'll use a large range of numbers and check how much memory is consumed.
"""

import sys

list_comp = [x for x in range(1000000)]
gen_expr = (x for x in range(1000000))

print("\nMemory Used by List Comprehension:", sys.getsizeof(list_comp), "bytes")
print("Memory Used by Generator Expression:", sys.getsizeof(gen_expr), "bytes")

# ✅ Generator expression consumes constant (very small) memory,
#    regardless of data size.


# ------------------------------------------------
# 3️⃣ Using Generator Expressions in Loops
# ------------------------------------------------

numbers = (x for x in range(1, 6))
for n in numbers:
    print("Generated:", n)

# Generator is exhausted after the loop
print("Trying again after loop:")
for n in numbers:
    print(n)  # No output because generator is exhausted


# ------------------------------------------------
# 4️⃣ Using Generator Expressions with Built-in Functions
# ------------------------------------------------
"""
Generators can be directly used with functions like sum(), max(), min(), etc.
These functions internally consume the generator.
"""

print("\nSum of squares:", sum(x ** 2 for x in range(10)))
print("Max square:", max(x ** 2 for x in range(10)))
print("Count of even numbers:", sum(1 for x in range(10) if x % 2 == 0))


# ------------------------------------------------
# 5️⃣ Combining Generators with Any() and All()
# ------------------------------------------------
"""
Generators are very efficient with logical checks.
They stop evaluating as soon as the condition is met (short-circuiting).
"""

nums = [2, 4, 6, 8, 10]

print("\nAre all numbers even?", all(n % 2 == 0 for n in nums))
print("Is there any odd number?", any(n % 2 != 0 for n in nums))


# ------------------------------------------------
# 6️⃣ Example: Reading File Lines Lazily
# ------------------------------------------------
"""
Instead of loading the entire file into memory, use a generator expression
to process lines one at a time.
"""

# Example (uncomment when testing with a file)
# with open("large_data.txt", "r") as file:
#     line_lengths = (len(line) for line in file)
#     total_chars = sum(line_lengths)
#     print("Total characters in file:", total_chars)


# ------------------------------------------------
# 7️⃣ Example: Filtering and Transforming Data Stream
# ------------------------------------------------
"""
Generator expressions can be chained to build data pipelines efficiently.
"""

data = [1, 2, 3, 4, 5, 6]

# Step 1: Filter even numbers
even_nums = (x for x in data if x % 2 == 0)

# Step 2: Square each even number
squared_evens = (x ** 2 for x in even_nums)

print("\nSquared even numbers:", list(squared_evens))


# ------------------------------------------------
# 8️⃣ Nested Generator Expressions
# ------------------------------------------------
"""
Just like nested loops, you can nest generator expressions.
"""

pairs = ((x, y) for x in range(3) for y in range(3))
print("All pairs:", list(pairs))


# ------------------------------------------------
# 9️⃣ Infinite Generators Example
# ------------------------------------------------
"""
Generator expressions can work with itertools to handle infinite streams efficiently.
"""

import itertools

infinite_naturals = (x for x in itertools.count(1))
print("\nFirst 5 numbers from infinite generator:")
for i in itertools.islice(infinite_naturals, 5):
    print(i)


# ------------------------------------------------
# 🔟 Key Takeaways
# ------------------------------------------------
"""
✅ Generator expressions are a compact way to define generators.
✅ They are memory-efficient (lazy evaluation).
✅ They work perfectly with functions like sum(), max(), any(), all().
✅ Once exhausted, they cannot be reused.
✅ Useful for large datasets, streaming data, or pipelines.
"""

# ================================================================
# Summary:
# (expression for item in iterable if condition)
# → Returns a generator (lazy, memory-efficient)
#
# Example:
#   squares = (x**2 for x in range(10))
#   print(sum(squares))
# ================================================================
