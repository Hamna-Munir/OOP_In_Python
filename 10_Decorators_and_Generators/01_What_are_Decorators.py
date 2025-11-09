# ================================================================
# File: 01_What_are_Decorators.py
# Topic: Introduction to Decorators in Python
# ================================================================

"""
Decorators are one of the most powerful and elegant features in Python.

A **decorator** is a special function that allows you to **modify or extend the behavior**
of another function or method — without permanently changing its code.

They are widely used for:
    - Logging
    - Authentication
    - Performance measurement
    - Access control
    - Caching
    - Validation

In simple terms:
    Decorators "wrap" a function, run some code **before** and/or **after** it, 
    and optionally modify the result.
"""

# ------------------------------------------------
# 1️⃣ Basic Function Review (Before Decorators)
# ------------------------------------------------
"""
Let's start with a simple example to recall how functions work.
"""

def greet():
    print("Hello, welcome to Python OOP learning!")

greet()  # Output: Hello, welcome to Python OOP learning!


# ------------------------------------------------
# 2️⃣ Functions are First-Class Citizens in Python
# ------------------------------------------------
"""
In Python:
- Functions can be assigned to variables.
- Functions can be passed as arguments to other functions.
- Functions can be returned from other functions.

This flexibility enables decorators.
"""

def hello():
    return "Hello, world!"

say = hello          # Assign function to variable
print(say())         # Output: Hello, world!


# ------------------------------------------------
# 3️⃣ Passing a Function as an Argument
# ------------------------------------------------
"""
We can pass one function to another, and the inner function can call it.
"""

def display(func):
    print("Executing function passed as argument...")
    print(func())

def welcome():
    return "Welcome to OOP in Python!"

display(welcome)
# Output:
# Executing function passed as argument...
# Welcome to OOP in Python!


# ------------------------------------------------
# 4️⃣ Creating a Simple Decorator
# ------------------------------------------------
"""
A decorator is simply a function that takes another function as input,
adds some extra behavior, and returns a new function.
"""

def decorator_function(original_function):
    def wrapper_function():
        print("Before executing the original function...")
        original_function()
        print("After executing the original function...")
    return wrapper_function

# Using the decorator manually
def say_hello():
    print("Hello!")

decorated_function = decorator_function(say_hello)
decorated_function()

# Output:
# Before executing the original function...
# Hello!
# After executing the original function...


# ------------------------------------------------
# 5️⃣ Using @decorator Syntax (Syntactic Sugar)
# ------------------------------------------------
"""
Python provides a cleaner way to apply decorators using the '@' symbol.
This syntax is equivalent to manually wrapping a function.
"""

@decorator_function
def greet_user():
    print("Good to see you!")

# Equivalent to: greet_user = decorator_function(greet_user)
greet_user()

# Output:
# Before executing the original function...
# Good to see you!
# After executing the original function...


# ------------------------------------------------
# 6️⃣ Decorators with Arguments
# ------------------------------------------------
"""
If the original function takes arguments, we must allow the wrapper
to accept them as well using *args and **kwargs.
"""

def decorator_with_args(original_function):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {original_function.__name__}")
        return original_function(*args, **kwargs)
    return wrapper

@decorator_with_args
def add(a, b):
    print(f"The sum is: {a + b}")

add(10, 20)
# Output:
# Calling function: add
# The sum is: 30


# ------------------------------------------------
# 7️⃣ Real-World Example: Logging Decorator
# ------------------------------------------------
"""
Decorators are very useful for logging or tracking function behavior.
"""

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Function '{func.__name__}' called with arguments: {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Function '{func.__name__}' completed.")
        return result
    return wrapper

@log_function_call
def multiply(x, y):
    print(f"Result: {x * y}")
    return x * y

multiply(5, 4)
# Output:
# [LOG] Function 'multiply' called with arguments: (5, 4) {}
# Result: 20
# [LOG] Function 'multiply' completed.


# ------------------------------------------------
# 8️⃣ Applying Multiple Decorators
# ------------------------------------------------
"""
You can stack multiple decorators on a single function.
They execute from top to bottom.
"""

def decorator_one(func):
    def wrapper():
        print("Decorator One executed.")
        func()
    return wrapper

def decorator_two(func):
    def wrapper():
        print("Decorator Two executed.")
        func()
    return wrapper

@decorator_one
@decorator_two
def say_hi():
    print("Hi, everyone!")

# Equivalent to: say_hi = decorator_one(decorator_two(say_hi))
say_hi()

# Output:
# Decorator One executed.
# Decorator Two executed.
# Hi, everyone!


# ------------------------------------------------
# 9️⃣ Decorators with Return Values
# ------------------------------------------------
"""
A decorator can also modify or return values from the wrapped function.
"""

def square_decorator(func):
    def wrapper(num):
        result = func(num)
        print(f"Original result: {result}")
        squared = result ** 2
        print(f"Squared result: {squared}")
        return squared
    return wrapper

@square_decorator
def get_number(num):
    return num

get_number(5)
# Output:
# Original result: 5
# Squared result: 25


# ------------------------------------------------
# 🔟 Key Takeaways
# ------------------------------------------------
"""
✅ Decorators are functions that modify the behavior of other functions.
✅ They use the syntax '@decorator_name' above a function definition.
✅ They are widely used in Python frameworks (Flask, Django, FastAPI, etc.).
✅ Decorators can:
   - Add logging
   - Handle permissions
   - Measure execution time
   - Validate data
✅ You can apply multiple decorators to the same function.
"""


# ================================================================
# Summary:
# Decorators → Functions that wrap other functions to extend behavior.
# Syntax → @decorator_name
# Common Uses → Logging, validation, authentication, and performance tracking.
# ================================================================
