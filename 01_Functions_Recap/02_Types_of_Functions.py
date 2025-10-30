# ----------------------------------------------------------
# File Name: 02_Types_of_Functions.py
# Topic: Types of Functions in Python
# ----------------------------------------------------------
# Author: Hamna Munir
# Repository: OOP_In_Python
# ----------------------------------------------------------

# ----------------------------------------------------------
#   What are Functions?
# ----------------------------------------------------------
# ➤ A function is a reusable block of code that performs a specific task.
# ➤ In Python, functions help reduce redundancy and improve modularity.
# ➤ There are mainly three types of functions:
#       1. Built-in Functions
#       2. User-defined Functions
#       3. Anonymous (Lambda) Functions
# ----------------------------------------------------------


# ----------------------------------------------------------
#   1️⃣ Built-in Functions
# ----------------------------------------------------------
# ➤ These are predefined functions that come with Python.
# ➤ You can use them directly without defining them.
# ➤ Examples: print(), len(), max(), min(), type(), int(), str(), etc.

# Example:
numbers = [10, 20, 5, 30]

print(len(numbers))     # Returns the number of items → Output: 4
print(max(numbers))     # Returns the largest number → Output: 30
print(min(numbers))     # Returns the smallest number → Output: 5
print(sum(numbers))     # Returns the sum of numbers → Output: 65
print(type(numbers))    # Returns the type of object → Output: <class 'list'>


# ----------------------------------------------------------
#   2️⃣ User-defined Functions
# ----------------------------------------------------------
# ➤ These are functions created by the programmer.
# ➤ They are used to perform specific tasks as per the program’s need.
# ➤ Syntax:
#     def function_name(parameters):
#         # code block
#         return value

# Example 1:
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

print(add(5, 7))
# Output: 12


# Example 2:
def find_even_numbers(limit):
    """Prints even numbers up to the given limit."""
    for i in range(1, limit + 1):
        if i % 2 == 0:
            print(i, end=" ")

find_even_numbers(10)
# Output: 2 4 6 8 10


# ----------------------------------------------------------
#   3️⃣ Anonymous Functions (Lambda Functions)
# ----------------------------------------------------------
# ➤ Anonymous functions are small, one-line functions created using the keyword `lambda`.
# ➤ They don’t need a name (unlike functions defined using def).
# ➤ Commonly used for short, simple tasks or inside other functions.

# Syntax:
# lambda arguments: expression

# Example 1:
square = lambda x: x ** 2
print(square(5))
# Output: 25

# Example 2:
add_numbers = lambda a, b: a + b
print(add_numbers(3, 7))
# Output: 10

# Example 3 (used with map()):
nums = [1, 2, 3, 4, 5]
squared_nums = list(map(lambda x: x ** 2, nums))
print(squared_nums)
# Output: [1, 4, 9, 16, 25]


# ----------------------------------------------------------
#   Difference Between def and lambda
# ----------------------------------------------------------
# | Feature             | def Function              | lambda Function             |
# |----------------------|---------------------------|------------------------------|
# | Syntax               | Uses `def` keyword        | Uses `lambda` keyword        |
# | Name                 | Has a name                | Anonymous (no name)          |
# | Body                 | Can contain many lines    | Single-line expression only  |
# | Use Case             | Reusable, complex logic   | Short, simple logic          |
# ----------------------------------------------------------


# ----------------------------------------------------------
#   Example: Using Lambda Inside Another Function
# ----------------------------------------------------------
def apply_operation(a, b, operation):
    """Applies a given lambda operation to two numbers."""
    return operation(a, b)

# Passing lambda as an argument
result = apply_operation(10, 5, lambda x, y: x * y)
print(result)
# Output: 50


# ----------------------------------------------------------
#   Summary:
# ----------------------------------------------------------
# ✔ Built-in Functions → Already provided by Python (e.g., len(), max(), type())  
# ✔ User-defined Functions → Created using def for specific tasks  
# ✔ Lambda Functions → Small, anonymous, single-line functions  
# ✔ Functions make programs modular, readable, and reusable
# ----------------------------------------------------------
