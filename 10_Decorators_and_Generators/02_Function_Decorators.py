# ================================================================
# File: 02_Function_Decorators.py
# Topic: Function Decorators in Python
# ================================================================

"""
In Python, **function decorators** are the most common type of decorators.

They are functions that take another function as input, extend or modify its
behavior, and return a new function.

Function decorators help in:
    - Logging
    - Timing execution
    - Validating inputs
    - Access control
    - Performance measurement

They provide a clean, reusable, and readable way to modify function behavior.
"""

# ------------------------------------------------
# 1️⃣ Basic Structure of a Function Decorator
# ------------------------------------------------
"""
A decorator takes a function, wraps it inside another function (the 'wrapper'),
and returns that wrapper.
"""

def my_decorator(func):
    def wrapper():
        print("Before the function executes.")
        func()
        print("After the function executes.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, world!")

say_hello()

# Output:
# Before the function executes.
# Hello, world!
# After the function executes.


# ------------------------------------------------
# 2️⃣ Function Decorator with Arguments
# ------------------------------------------------
"""
When the function being decorated takes arguments, the wrapper must accept *args and **kwargs.
"""

def argument_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' called with arguments {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@argument_decorator
def add(a, b):
    print(f"Result: {a + b}")

add(10, 20)
# Output:
# Function 'add' called with arguments (10, 20) and {}
# Result: 30


# ------------------------------------------------
# 3️⃣ Decorator Returning Modified Value
# ------------------------------------------------
"""
A decorator can also alter or enhance the return value of the original function.
"""

def double_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Original result: {result}")
        return result * 2
    return wrapper

@double_result
def get_number():
    return 5

print(get_number())  # Output: 10


# ------------------------------------------------
# 4️⃣ Decorators with Parameters
# ------------------------------------------------
"""
Sometimes, we want to pass parameters to the decorator itself.
This requires an extra outer function (a decorator factory).
"""

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                print(f"Execution {i + 1} of {n}:")
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Welcome to Python Decorators!")

greet()

# Output:
# Execution 1 of 3:
# Welcome to Python Decorators!
# Execution 2 of 3:
# Welcome to Python Decorators!
# Execution 3 of 3:
# Welcome to Python Decorators!


# ------------------------------------------------
# 5️⃣ Real-World Example — Execution Time Measurement
# ------------------------------------------------
"""
A decorator can measure how long a function takes to run.
This is useful in performance testing and optimization.
"""

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' executed in {end - start:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    print("Finished slow operation.")

slow_function()

# Output:
# Finished slow operation.
# Function 'slow_function' executed in 1.0001 seconds


# ------------------------------------------------
# 6️⃣ Real-World Example — Authorization Decorator
# ------------------------------------------------
"""
Decorators can control access to functions based on user permissions.
"""

def authorize(role_required):
    def decorator(func):
        def wrapper(user_role):
            if user_role == role_required:
                print(f"Access granted for role: {user_role}")
                return func(user_role)
            else:
                print(f"Access denied for role: {user_role}")
        return wrapper
    return decorator

@authorize("admin")
def delete_user(role):
    print(f"{role} is deleting a user record...")

delete_user("admin")   # Access granted
delete_user("guest")   # Access denied


# ------------------------------------------------
# 7️⃣ Real-World Example — Input Validation
# ------------------------------------------------
"""
Decorators can validate inputs before running the function.
"""

def validate_positive(func):
    def wrapper(*args):
        if any(a < 0 for a in args):
            print("Error: Negative values are not allowed.")
            return
        return func(*args)
    return wrapper

@validate_positive
def calculate_area(length, width):
    print(f"Area = {length * width}")

calculate_area(5, 3)    # Valid input
calculate_area(-2, 4)   # Invalid input


# ------------------------------------------------
# 8️⃣ Chaining Multiple Decorators
# ------------------------------------------------
"""
Multiple decorators can be applied to the same function.
They execute from top to bottom.
"""

def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

def exclaim(func):
    def wrapper():
        result = func()
        return result + "!!!"
    return wrapper

@uppercase
@exclaim
def message():
    return "decorators are powerful"

print(message())
# Output: DECORATORS ARE POWERFUL!!!


# ------------------------------------------------
# 9️⃣ functools.wraps — Preserving Function Metadata
# ------------------------------------------------
"""
When a function is decorated, its metadata (like name and docstring) gets replaced by the wrapper’s.
To preserve the original information, we use functools.wraps.
"""

from functools import wraps

def info_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}() ...")
        return func(*args, **kwargs)
    return wrapper

@info_decorator
def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

print(multiply(4, 5))
print(multiply.__name__)       # multiply
print(multiply.__doc__)        # Multiplies two numbers.


# ------------------------------------------------
# 🔟 Key Takeaways
# ------------------------------------------------
"""
✅ Function decorators wrap and modify other functions dynamically.
✅ Use @decorator_name syntax to apply decorators.
✅ You can pass parameters to decorators by creating a decorator factory.
✅ Decorators can:
   - Validate data
   - Measure execution time
   - Log events
   - Restrict access
✅ Use functools.wraps to preserve original function metadata.
✅ Multiple decorators can be stacked to combine behaviors.
"""


# ================================================================
# Summary:
# Function Decorators → Extend or modify function behavior dynamically.
# Common Uses → Logging, timing, validation, access control.
# Syntax → @decorator_name
# Best Practice → Use functools.wraps to retain function info.
# ================================================================
