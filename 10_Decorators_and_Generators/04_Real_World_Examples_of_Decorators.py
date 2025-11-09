# ================================================================
# File: 04_Real_World_Examples_of_Decorators.py
# Topic: Real-World Applications of Decorators in Python
# ================================================================

"""
Decorators are widely used in real-world Python applications for:
    - Logging and debugging
    - Authorization and access control
    - Performance monitoring
    - Input validation
    - Memoization (caching)
    - Retrying failed operations
    - Registering functions or classes automatically

Below are professional, real-world style examples demonstrating these concepts.
"""

# ------------------------------------------------
# 1️⃣ Logging Function Calls
# ------------------------------------------------
"""
In large applications, logging helps trace the execution of important functions.
"""

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned: {result}")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b

@log_function_call
def multiply(a, b):
    return a * b

add(5, 10)
multiply(3, 4)


# ------------------------------------------------
# 2️⃣ Authorization (Access Control)
# ------------------------------------------------
"""
Used in APIs and web applications to check user permissions before executing code.
"""

def require_admin(func):
    def wrapper(user_role, *args, **kwargs):
        if user_role != "admin":
            print("[ACCESS DENIED] Only admins can perform this action.")
            return None
        print("[ACCESS GRANTED] Welcome, Admin.")
        return func(user_role, *args, **kwargs)
    return wrapper

@require_admin
def delete_user(user_role, username):
    print(f"User '{username}' has been deleted successfully.")

delete_user("admin", "Touseef")
delete_user("guest", "Hareem")


# ------------------------------------------------
# 3️⃣ Performance Measurement
# ------------------------------------------------
"""
Decorators can be used to calculate how long a function takes to execute.
"""

import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] Function '{func.__name__}' executed in {(end - start):.5f} seconds.")
        return result
    return wrapper

@measure_time
def slow_function():
    time.sleep(1.5)
    print("Processing complete.")

slow_function()


# ------------------------------------------------
# 4️⃣ Input Validation
# ------------------------------------------------
"""
Used to ensure correct data before function execution.
"""

def validate_inputs(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError("[ERROR] All arguments must be numbers.")
        return func(*args, **kwargs)
    return wrapper

@validate_inputs
def divide(a, b):
    return a / b

print("Division result:", divide(10, 2))
# Uncomment below line to see validation in action
# divide("ten", 2)


# ------------------------------------------------
# 5️⃣ Retry Logic for Fault Tolerance
# ------------------------------------------------
"""
In real systems, some operations (like network requests) can fail temporarily.
A retry decorator helps automatically re-attempt a failed operation.
"""

def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    print(f"[Attempt {attempt}] Running {func.__name__}...")
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"[ERROR] {e}. Retrying...")
                    time.sleep(0.5)
            print("[FAILURE] All attempts failed.")
        return wrapper
    return decorator

@retry(3)
def unstable_operation():
    import random
    if random.choice([True, False]):
        raise ValueError("Network error")
    print("Operation successful!")

unstable_operation()


# ------------------------------------------------
# 6️⃣ Caching (Memoization)
# ------------------------------------------------
"""
Memoization stores results of expensive function calls to improve performance.
"""

def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            print(f"[CACHE HIT] Returning cached result for {args}")
            return cache[args]
        print(f"[CACHE MISS] Calculating result for {args}")
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci(10):", fibonacci(10))
print("Fibonacci(10):", fibonacci(10))  # Cached


# ------------------------------------------------
# 7️⃣ API Rate Limiting (Simplified)
# ------------------------------------------------
"""
Prevents a function from being called too frequently.
Commonly used in web APIs or background tasks.
"""

def rate_limit(seconds):
    last_called = [0]
    def decorator(func):
        def wrapper(*args, **kwargs):
            now = time.time()
            if now - last_called[0] < seconds:
                print("[RATE LIMIT] Too many calls. Please wait.")
                return None
            last_called[0] = now
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(3)
def send_message():
    print("Message sent!")

send_message()
time.sleep(1)
send_message()  # Blocked due to rate limit
time.sleep(3)
send_message()  # Allowed again


# ------------------------------------------------
# 8️⃣ Automatic Function Registration
# ------------------------------------------------
"""
Useful in plugin systems — automatically registers functions for later use.
"""

registry = {}

def register(func):
    registry[func.__name__] = func
    print(f"[REGISTERED] Function '{func.__name__}' added to registry.")
    return func

@register
def greet_user():
    print("Hello, user!")

@register
def say_goodbye():
    print("Goodbye, user!")

print("Registered Functions:", list(registry.keys()))


# ------------------------------------------------
# 9️⃣ Class-Level Example: Logging Method Calls
# ------------------------------------------------
"""
Combining OOP and decorators — logs whenever a method is called.
"""

def log_methods(cls):
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value):
            def wrapper(self, *args, func=attr_value, name=attr_name, **kwargs):
                print(f"[METHOD LOG] {cls.__name__}.{name} called.")
                return func(self, *args, **kwargs)
            setattr(cls, attr_name, wrapper)
    return cls

@log_methods
class Student:
    def study(self):
        print("Student is studying.")

    def sleep(self):
        print("Student is sleeping.")

s = Student()
s.study()
s.sleep()


# ------------------------------------------------
# 🔟 Debugging and Tracing Example
# ------------------------------------------------
"""
Decorators can trace execution paths for debugging complex logic.
"""

def trace(func):
    def wrapper(*args, **kwargs):
        print(f"[TRACE] Entering {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[TRACE] Exiting {func.__name__}")
        return result
    return wrapper

@trace
def complex_calculation(x, y):
    time.sleep(0.5)
    return x ** 2 + y ** 2

print("Result:", complex_calculation(3, 4))


# ------------------------------------------------
# ✅ Summary
# ------------------------------------------------
"""
✔ Decorators are powerful tools used in real-world applications for:
   - Logging, validation, caching, timing, and retrying
   - Authorization and access control
   - API rate limiting and error handling
   - Function or class registration
   - Debugging and tracing execution flow

✔ They make code cleaner, reusable, and easier to maintain.

Best Practice:
    - Use functools.wraps to preserve metadata.
    - Keep decorators lightweight and modular.
    - Avoid side effects (like global variable modifications) inside decorators.
"""

# ================================================================
# End of File
# ================================================================
