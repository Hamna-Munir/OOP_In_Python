# ----------------------------------------------------------
# File Name: 01_What_is_a_Function.py
# Topic: Introduction to Functions in Python
# ----------------------------------------------------------
# Author: Hamna Munir
# Repository: OOP_In_Python
# ----------------------------------------------------------

# ----------------------------------------------------------
#   What is a Function?
# ----------------------------------------------------------
# ➤ A function is a block of reusable code that performs a specific task.
# ➤ It helps reduce repetition, improves readability, and makes programs modular.
# ➤ Functions allow us to group related code together and use it whenever needed.
# ➤ In Python, functions are defined using the `def` keyword.

# Syntax:
# def function_name(parameters):
#     """docstring (optional)"""
#     # code block
#     return value


# ----------------------------------------------------------
#   Example 1: A Simple Function
# ----------------------------------------------------------
def greet():
    """This function prints a simple greeting message."""
    print("Hello, welcome to Python functions!")


# Calling the function
greet()
# Output:
# Hello, welcome to Python functions!


# ----------------------------------------------------------
#   Why Use Functions?
# ----------------------------------------------------------
# 1️⃣ To avoid code repetition.
# 2️⃣ To make programs easier to read and maintain.
# 3️⃣ To divide complex problems into smaller tasks (modularity).
# 4️⃣ To reuse logic multiple times without rewriting the code.


# ----------------------------------------------------------
#   Example 2: Function with Parameters
# ----------------------------------------------------------
def greet_user(name):
    """Function that takes one argument and prints a greeting."""
    print("Hello,", name, "! Welcome to Python learning.")


# Calling the function with an argument
greet_user("Hamna")
# Output:
# Hello, Hamna ! Welcome to Python learning.


# ----------------------------------------------------------
#   Example 3: Function with Return Value
# ----------------------------------------------------------
def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b


# Storing the returned value
result = add_numbers(10, 20)
print("Sum:", result)
# Output:
# Sum: 30


# ----------------------------------------------------------
#   Example 4: Functions Help Avoid Code Duplication
# ----------------------------------------------------------
# Without function:
print("Square of 2 =", 2 ** 2)
print("Square of 3 =", 3 ** 2)
print("Square of 4 =", 4 ** 2)

# With function:
def square(num):
    """Returns the square of a number."""
    return num ** 2


for i in range(2, 5):
    print(f"Square of {i} = {square(i)}")

# Output:
# Square of 2 = 4
# Square of 3 = 9
# Square of 4 = 16


# ----------------------------------------------------------
#   Example 5: Function Documentation (Docstring)
# ----------------------------------------------------------
# ➤ A docstring is a short description written below the function definition.
# ➤ It explains what the function does and is accessible using the __doc__ attribute.

def multiply(x, y):
    """This function returns the product of two numbers."""
    return x * y


print(multiply.__doc__)
# Output:
# This function returns the product of two numbers.


# ----------------------------------------------------------
#   Summary:
# ----------------------------------------------------------
# ✔ Functions organize and reuse code.
# ✔ Defined using the 'def' keyword.
# ✔ May or may not take arguments.
# ✔ May or may not return a value.
# ✔ Help make programs modular and efficient.
# ----------------------------------------------------------
