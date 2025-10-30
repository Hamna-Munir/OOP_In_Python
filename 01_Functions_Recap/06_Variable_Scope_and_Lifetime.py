# ------------------------------------------------------------
# File: 06_Variable_Scope_and_Lifetime.py
# Topic: Variable Scope and Lifetime in Python
# ------------------------------------------------------------

# ------------------------------------------------------------
# 1. What is Variable Scope?
# ------------------------------------------------------------
# ➤ The *scope* of a variable determines where it can be accessed within a program.
# ➤ Python has four types of scopes, often remembered by the rule:
#    LEGB → Local, Enclosing, Global, Built-in
#
# ➤ Each function or block of code creates its own scope.

# Example of different scopes:
x = 10  # Global variable

def example():
    y = 5  # Local variable
    print("Inside function, y =", y)
    print("Inside function, x =", x)  # Accessing global variable

example()
print("Outside function, x =", x)
# Output:
# Inside function, y = 5
# Inside function, x = 10
# Outside function, x = 10


# ------------------------------------------------------------
# 2. Types of Scopes (LEGB Rule)
# ------------------------------------------------------------

# L → Local: Defined inside a function
# E → Enclosing: Inside nested functions
# G → Global: Declared at the top level of a module or file
# B → Built-in: Predefined names in Python (like len(), print(), etc.)


# ------------------------------------------------------------
# Local Scope Example
# ------------------------------------------------------------
def local_scope_example():
    name = "Hamna"  # Local variable
    print("Inside function:", name)

local_scope_example()
# print(name)  # ❌ Error — variable not accessible outside function
# Output: Inside function: Hamna


# ------------------------------------------------------------
# Global Scope Example
# ------------------------------------------------------------
# Variables declared outside all functions have global scope.

language = "Python"

def show_language():
    print("Programming Language:", language)

show_language()
print("Accessed globally:", language)
# Output:
# Programming Language: Python
# Accessed globally: Python


# ------------------------------------------------------------
# 3. The 'global' Keyword
# ------------------------------------------------------------
# ➤ Used to modify a global variable inside a function.

count = 0

def increment():
    global count  # Declare that we’ll use the global 'count'
    count += 1
    print("Inside function, count =", count)

increment()
print("Outside function, count =", count)
# Output:
# Inside function, count = 1
# Outside function, count = 1


# ------------------------------------------------------------
# 4. Enclosing Scope (Nested Functions)
# ------------------------------------------------------------
# ➤ When a function is defined inside another function,
#    the inner function can access variables from the enclosing (outer) function.

def outer_function():
    message = "Outer Variable"

    def inner_function():
        print("Accessing from inner function:", message)

    inner_function()

outer_function()
# Output: Accessing from inner function: Outer Variable


# ------------------------------------------------------------
# 5. The 'nonlocal' Keyword
# ------------------------------------------------------------
# ➤ Used to modify a variable in the *enclosing* (but not global) scope.

def outer():
    value = "outer"

    def inner():
        nonlocal value
        value = "modified in inner"
        print("Inner value:", value)

    inner()
    print("Outer value after modification:", value)

outer()
# Output:
# Inner value: modified in inner
# Outer value after modification: modified in inner


# ------------------------------------------------------------
# 6. Built-in Scope
# ------------------------------------------------------------
# ➤ Python has built-in names that are always available globally (e.g., len, max, print).
# ➤ You can override them, but it’s not recommended.

# Example (avoid this!)
len = 100
# print(len([1, 2, 3]))  # ❌ Error — 'len' is now an integer, not a function
del len  # Remove redefinition to restore built-in behavior
print(len([1, 2, 3]))  # ✅ Output: 3


# ------------------------------------------------------------
# 7. Variable Lifetime
# ------------------------------------------------------------
# ➤ The *lifetime* of a variable is the period during which it exists in memory.
# ➤ Global variables exist until the program ends.
# ➤ Local variables exist only while the function is executing.

def demo_lifetime():
    temp = 42  # Created when function starts
    print("Inside function, temp =", temp)

demo_lifetime()
# print(temp)  # ❌ Error — 'temp' no longer exists
# Output: Inside function, temp = 42


# ------------------------------------------------------------
# 8. Best Practices
# ------------------------------------------------------------
# ✔ Keep variable scopes as small as possible (prefer local over global).
# ✔ Use 'global' and 'nonlocal' carefully to avoid confusion.
# ✔ Avoid reusing built-in names.
# ✔ Understand scope to prevent unexpected bugs in nested functions.


# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------
# - Scope defines where a variable is accessible (LEGB rule).
# - Lifetime defines how long a variable exists in memory.
# - 'global' modifies global variables inside a function.
# - 'nonlocal' modifies enclosing variables in nested functions.
# - Use proper scope management for clean, bug-free code.
# ------------------------------------------------------------
