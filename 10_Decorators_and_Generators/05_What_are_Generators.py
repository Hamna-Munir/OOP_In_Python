# ================================================================
# File: 05_What_are_Generators.py
# Topic: Introduction to Generators in Python
# ================================================================

"""
In Python, **generators** are a special kind of iterable that allow you to
generate values **on the fly** instead of storing them all in memory.

They are used when dealing with **large datasets**, **infinite sequences**, or
when you want to **stream data efficiently** without loading everything at once.

A generator is created using:
    - The `yield` keyword inside a function.
    - The `()` syntax with generator expressions.

Unlike normal functions, a generator **remembers its state** between executions.
It produces one item at a time and pauses execution until the next item is requested.
"""

# ------------------------------------------------
# 1️⃣ Normal Function vs Generator Function
# ------------------------------------------------
"""
A normal function returns a single value using `return`.
A generator function uses `yield` to produce a sequence of values, one by one.
"""

def normal_function():
    return [1, 2, 3, 4]

print("Normal function output:", normal_function())

# Generator function
def generator_function():
    for i in range(1, 5):
        yield i

print("Generator object:", generator_function())
# Output: <generator object generator_function at 0x...>

# To get values from a generator, use `next()`
gen = generator_function()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
print(next(gen))  # Output: 4
# If called again, it raises StopIteration


# ------------------------------------------------
# 2️⃣ Iterating Over a Generator using a for Loop
# ------------------------------------------------
"""
Generators are iterators, so you can loop through them directly using `for`.
Once exhausted, they cannot be reused unless recreated.
"""

for value in generator_function():
    print("Generated value:", value)


# ------------------------------------------------
# 3️⃣ How Generators Save Memory
# ------------------------------------------------
"""
Generators are **memory efficient** because they don't store all values in memory.
They generate values one at a time as needed.
"""

import sys

# List comprehension
list_comp = [i for i in range(1000000)]
print("Memory used by list comprehension:", sys.getsizeof(list_comp), "bytes")

# Generator expression
gen_exp = (i for i in range(1000000))
print("Memory used by generator expression:", sys.getsizeof(gen_exp), "bytes")


# ------------------------------------------------
# 4️⃣ Example: Fibonacci Series Generator
# ------------------------------------------------
"""
Let's create a generator that yields Fibonacci numbers one by one.
"""

def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print("Fibonacci Sequence:")
for num in fibonacci(10):
    print(num, end=" ")
print()


# ------------------------------------------------
# 5️⃣ Example: Infinite Sequence Generator
# ------------------------------------------------
"""
Generators can produce **infinite sequences** — something impossible with lists.
"""

def infinite_numbers(start=1):
    while True:
        yield start
        start += 1

print("First 5 numbers from infinite generator:")
gen = infinite_numbers()
for _ in range(5):
    print(next(gen))


# ------------------------------------------------
# 6️⃣ Generator Expression
# ------------------------------------------------
"""
Generator expressions are a concise way to create generators, similar to list comprehensions.
Syntax: (expression for item in iterable)
"""

squares_gen = (x * x for x in range(1, 6))
print("Squares using generator expression:")
for num in squares_gen:
    print(num)


# ------------------------------------------------
# 7️⃣ Combining Generators with Functions
# ------------------------------------------------
"""
Generators can be chained or combined to build data pipelines.
"""

def even_numbers(limit):
    for num in range(limit):
        if num % 2 == 0:
            yield num

def square_numbers(numbers):
    for num in numbers:
        yield num ** 2

# Chaining generators
even_square_gen = square_numbers(even_numbers(10))
print("Squares of even numbers:")
for val in even_square_gen:
    print(val)


# ------------------------------------------------
# 8️⃣ Generator Lifecycle and `StopIteration`
# ------------------------------------------------
"""
When a generator has no more values to yield, it raises `StopIteration`.
You can handle it manually if needed.
"""

def small_gen():
    yield 1
    yield 2

g = small_gen()
print(next(g))  # Output: 1
print(next(g))  # Output: 2
try:
    print(next(g))  # Raises StopIteration
except StopIteration:
    print("Generator exhausted!")


# ------------------------------------------------
# 9️⃣ Use Case: Reading Large Files Line by Line
# ------------------------------------------------
"""
Generators are ideal for reading files efficiently without loading the entire content.
"""

def read_file_line_by_line(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()

# Example usage (uncomment when using an actual file):
# for line in read_file_line_by_line("large_data.txt"):
#     print(line)


# ------------------------------------------------
# 🔟 Key Takeaways
# ------------------------------------------------
"""
✅ Generators produce data lazily — only when needed.
✅ They are memory-efficient and suitable for big data or streams.
✅ Use `yield` instead of `return` to create a generator.
✅ Generators can be combined to form pipelines.
✅ Once exhausted, a generator cannot be reused.
✅ Use `next()` to manually iterate and handle `StopIteration`.
"""


# ================================================================
# Summary:
# Generators → Functions that yield one value at a time (lazy evaluation)
# Use Cases → Large datasets, streaming data, infinite sequences
# Syntax → yield keyword or (expression for item in iterable)
# ================================================================
