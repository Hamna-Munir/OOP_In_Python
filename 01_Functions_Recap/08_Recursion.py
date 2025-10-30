# ------------------------------------------------------------
# File: 08_Recursion.py
# Topic: Recursion in Python
# ------------------------------------------------------------

# ------------------------------------------------------------
# 1. What is Recursion?
# ------------------------------------------------------------
# ➤ Recursion is a programming technique where a function calls itself
#   directly or indirectly to solve a problem.
# ➤ It is often used to solve problems that can be broken down
#   into smaller, similar subproblems.

# Example: A simple recursive function
def greet():
    print("Hello")
    # greet()  # Uncommenting this will cause infinite recursion

# greet()  # Be careful to define a base condition to avoid infinite recursion.


# ------------------------------------------------------------
# 2. Key Components of Recursion
# ------------------------------------------------------------
# Every recursive function must have:
# 1. A **base condition** – to stop the recursion.
# 2. A **recursive call** – where the function calls itself.

# Example: Counting down from 5 to 1
def countdown(n):
    if n == 0:
        print("Time’s up!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)
# Output:
# 5
# 4
# 3
# 2
# 1
# Time’s up!


# ------------------------------------------------------------
# 3. How Recursion Works (Step-by-Step)
# ------------------------------------------------------------
# Example: Factorial using recursion
# n! = n × (n-1) × (n-2) × ... × 1

def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

print("Factorial of 5:", factorial(5))
# Output: Factorial of 5: 120

# Function flow:
# factorial(5)
# = 5 * factorial(4)
# = 5 * 4 * factorial(3)
# = 5 * 4 * 3 * factorial(2)
# = 5 * 4 * 3 * 2 * factorial(1)
# = 5 * 4 * 3 * 2 * 1
# = 120


# ------------------------------------------------------------
# 4. Recursion vs Iteration
# ------------------------------------------------------------
# Both recursion and iteration (loops) can solve similar problems.
# Example: Factorial using loop

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Factorial (loop):", factorial_iterative(5))
# Output: Factorial (loop): 120


# ------------------------------------------------------------
# 5. Recursive Example: Fibonacci Series
# ------------------------------------------------------------
# Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
# Formula: F(n) = F(n-1) + F(n-2)

def fibonacci(n):
    if n <= 0:
        return "Invalid Input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci(7):", fibonacci(7))
# Output: Fibonacci(7): 8


# ------------------------------------------------------------
# 6. Recursion with Return Values
# ------------------------------------------------------------
# ➤ Recursive functions can return values to the previous function call.
# ➤ Each recursive layer waits for the inner call to complete.

def sum_natural(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural(n - 1)

print("Sum of first 5 numbers:", sum_natural(5))
# Output: Sum of first 5 numbers: 15


# ------------------------------------------------------------
# 7. Indirect Recursion
# ------------------------------------------------------------
# ➤ A function can call another function which in turn calls the first one.

def function_a(x):
    if x > 0:
        print("A:", x)
        function_b(x - 1)

def function_b(x):
    if x > 0:
        print("B:", x)
        function_a(x - 1)

function_a(3)
# Output:
# A: 3
# B: 2
# A: 1


# ------------------------------------------------------------
# 8. Advantages and Disadvantages of Recursion
# ------------------------------------------------------------

# ✅ Advantages:
# - Code is simpler and cleaner for repetitive, self-similar problems.
# - Useful in problems like factorial, tree traversal, searching, etc.

# ❌ Disadvantages:
# - Uses more memory due to function call stack.
# - May cause "RecursionError" if base case is missing or recursion is too deep.
# - Sometimes slower than loops due to overhead.


# ------------------------------------------------------------
# 9. Limiting Recursion Depth
# ------------------------------------------------------------
# Python limits how deep recursion can go to prevent infinite loops.

import sys
print("Default recursion limit:", sys.getrecursionlimit())

# You can change it using:
# sys.setrecursionlimit(2000)
# (Use carefully, as increasing too much may crash the program)


# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------
# - Recursion: Function calling itself.
# - Must have a base case to stop recursion.
# - Common examples: Factorial, Fibonacci, Sum, Tree Traversal.
# - Recursive calls build a *call stack* in memory.
# - Use recursion when the problem has a self-repetitive structure.
# ------------------------------------------------------------
