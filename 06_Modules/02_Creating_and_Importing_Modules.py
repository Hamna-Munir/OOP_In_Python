# ================================================
# File: 02_Creating_and_Importing_Modules.py
# Topic: Creating and Importing Modules in Python
# ================================================

"""
In Python, a **module** is a file that contains Python code (functions, classes, variables)
that can be reused in other programs.

You can create your own modules to:
- Reuse code across multiple programs
- Organize large codebases
- Improve maintainability and readability
"""

# ------------------------------------------------
# 1️⃣ Creating a Custom Module
# ------------------------------------------------
# Suppose we create a separate file named `my_module.py` in the same directory.

# Content of my_module.py:
# ------------------------------------------------
# def greet(name):
#     print(f"Hello, {name}! Welcome to Python Modules.")
#
# def add(a, b):
#     return a + b
#
# PI = 3.14159
#
# class Calculator:
#     def multiply(self, x, y):
#         return x * y
# ------------------------------------------------
# Save that file as `my_module.py`.
#
# Now we can import and use it below.
# (For demonstration purposes, we will simulate it by defining it here.)

# --- Simulated my_module content (for demo in this single file) ---
def greet(name):
    print(f"Hello, {name}! Welcome to Python Modules.")

def add(a, b):
    return a + b

PI = 3.14159

class Calculator:
    def multiply(self, x, y):
        return x * y
# -----------------------------------------------------------------


# ------------------------------------------------
# 2️⃣ Importing and Using a Custom Module
# ------------------------------------------------
print("----- Example 1: Importing and using module content -----")

# Using directly since we defined it in this file (as if imported)
greet("Hamna")
print("Sum:", add(10, 5))
print("PI value:", PI)

calc = Calculator()
print("Multiplication:", calc.multiply(3, 4))


# ------------------------------------------------
# 3️⃣ Importing Specific Functions or Classes
# ------------------------------------------------
print("\n----- Example 2: Importing specific items from a module -----")

# In a real scenario, this would be:
# from my_module import greet, Calculator
# But since everything is in this file, we use directly:
greet("Ali")

calc2 = Calculator()
print("Multiplication (again):", calc2.multiply(6, 7))


# ------------------------------------------------
# 4️⃣ Using Aliases (Module Nicknames)
# ------------------------------------------------
print("\n----- Example 3: Using module aliases -----")

# You can rename imported modules for convenience:
# import my_module as mm
# mm.greet("Sara")
# print(mm.add(2, 3))

# For demonstration:
def alias_example():
    print("Hello, Sara! Welcome to Python Modules (alias example).")
    print("Sum:", 2 + 3)

alias_example()


# ------------------------------------------------
# 5️⃣ Understanding __name__ and __main__
# ------------------------------------------------
print("\n----- Example 4: The __name__ and __main__ concept -----")

def example_function():
    print("This function runs only if the file is imported or executed accordingly.")

if __name__ == "__main__":
    print("This file is being executed directly.")
else:
    print("This file is being imported as a module.")


# ------------------------------------------------
# 6️⃣ Importing from Subdirectories (Packages)
# ------------------------------------------------
"""
Python allows organizing multiple modules into **packages** — which are directories 
containing an `__init__.py` file.

Example Folder Structure:
-------------------------
project/
│
├── main.py
└── utils/
    ├── __init__.py
    └── math_utils.py

Inside math_utils.py:
---------------------
def square(n):
    return n ** 2

Inside main.py:
---------------
from utils import math_utils
print(math_utils.square(5))    # Output: 25
"""

print("\n----- Example 5: Simulating package import (concept) -----")

def square(n):
    return n ** 2

print("Square of 5:", square(5))


# ------------------------------------------------
# 7️⃣ Reloading a Module
# ------------------------------------------------
print("\n----- Example 6: Reloading a module -----")

import importlib
# In a real case:
# import my_module
# importlib.reload(my_module)

print("Reloading example (simulated): importlib.reload(my_module)")


# ------------------------------------------------
# 8️⃣ Complete Demonstration
# ------------------------------------------------
print("\n----- Example 7: Full Demonstration of Module Usage -----")

# Simulate area and perimeter functions from another module
def area_of_circle(radius):
    return 3.14159 * radius * radius

def perimeter_of_circle(radius):
    return 2 * 3.14159 * radius

r = 5
print("Area:", area_of_circle(r))
print("Perimeter:", perimeter_of_circle(r))


# ------------------------------------------------
# 9️⃣ Advantages of Using Modules
# ------------------------------------------------
"""
✅ Code Reusability — Write once, use many times.
✅ Code Organization — Keeps related functions and classes together.
✅ Maintenance — Update one module and reflect changes everywhere.
✅ Namespace Management — Avoid naming conflicts.
✅ Collaboration — Team members can work on separate modules independently.
"""


# ================================================
# Summary:
# - A module is a file (.py) containing reusable code.
# - Use `import` or `from ... import ...` to include modules.
# - `__name__ == "__main__"` lets code run only when executed directly.
# - Organize related modules into packages for better structure.
# ================================================
