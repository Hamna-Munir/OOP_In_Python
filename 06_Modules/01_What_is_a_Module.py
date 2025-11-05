# ================================================
# File: 01_What_is_a_Module.py
# Topic: Introduction to Modules in Python
# ================================================

"""
A **module** in Python is a file that contains Python code — functions, classes, or variables — 
which can be imported and reused in other programs.

Modules help in:
✅ Organizing code logically
✅ Avoiding code duplication
✅ Making large programs easy to maintain
✅ Enabling code reusability across multiple projects

By dividing code into multiple modules, developers can manage complexity and 
focus on specific functionality in each part of a program.
"""

# ------------------------------------------------
# 1️⃣ What is a Module?
# ------------------------------------------------
# A module is simply a `.py` file that can be imported into another Python script.
# For example, if you have a file named `math_utils.py`, you can import it using:
# import math_utils

# Example content of math_utils.py:
# --------------------------------
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b

# Then in another file:
# --------------------------------
# import math_utils
# print(math_utils.add(10, 5))   # Output: 15

# ------------------------------------------------
# 2️⃣ Built-in Modules
# ------------------------------------------------
# Python comes with several built-in modules that provide ready-to-use functionality.

import math
import random
import datetime
import os

print("----- Built-in Modules Examples -----")

# Using the math module
print("Square root of 25:", math.sqrt(25))
print("Pi value:", math.pi)

# Using the random module
print("Random number between 1 and 10:", random.randint(1, 10))

# Using datetime module
print("Current date and time:", datetime.datetime.now())

# Using os module
print("Current working directory:", os.getcwd())

# ------------------------------------------------
# 3️⃣ Custom Modules
# ------------------------------------------------
# You can create your own module and use it in other Python files.

# Example: Create a file named `my_module.py` with the following content:
#
# def greet(name):
#     print(f"Hello, {name}! Welcome to Python Modules.")
#
# def square(num):
#     return num ** 2
#
# Now you can import it in another file using:
# import my_module
#
# my_module.greet("Hamna")
# print(my_module.square(5))

# ------------------------------------------------
# 4️⃣ Importing Modules
# ------------------------------------------------
# There are different ways to import modules in Python:

# Example 1: Import the whole module
import math
print("\nUsing Example 1 - import math")
print(math.factorial(5))

# Example 2: Import a specific function from a module
from math import sqrt
print("\nUsing Example 2 - from math import sqrt")
print(sqrt(49))

# Example 3: Import with alias (nickname)
import math as m
print("\nUsing Example 3 - import math as m")
print(m.pow(2, 3))

# Example 4: Import all names (not recommended)
from math import *
print("\nUsing Example 4 - from math import *")
print(sin(0))

# ------------------------------------------------
# 5️⃣ Module Search Path
# ------------------------------------------------
# When you import a module, Python searches for it in specific directories.
# You can check them using:
import sys
print("\nModule Search Path:")
print(sys.path)

# ------------------------------------------------
# 6️⃣ Advantages of Using Modules
# ------------------------------------------------
# ✅ Code Reusability — Write once, use anywhere.
# ✅ Code Organization — Logical separation of functionality.
# ✅ Maintenance — Easier to debug and update code.
# ✅ Namespace Management — Avoids naming conflicts.
# ✅ Extensibility — Enables modular project development.

# ------------------------------------------------
# 7️⃣ Example: Combining Built-in and Custom Modules
# ------------------------------------------------
# Suppose we use both built-in and user-defined functions together.

import math

def area_of_circle(radius):
    return math.pi * (radius ** 2)

def print_area(name, radius):
    print(f"{name}'s circle area with radius {radius} is {area_of_circle(radius):.2f}")

print("\n----- Example: Combining Built-in and Custom Logic -----")
print_area("Hamna", 5)

# ================================================
# Summary:
# - A module is a file containing Python code (functions, classes, etc.).
# - Built-in modules like math, random, datetime are available by default.
# - Custom modules can be created by saving code in separate files.
# - Use import statements to access module functionality.
# ================================================
