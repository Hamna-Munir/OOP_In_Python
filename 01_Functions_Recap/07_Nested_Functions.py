# ------------------------------------------------------------
# File: 07_Nested_Functions.py
# Topic: Nested Functions in Python
# ------------------------------------------------------------

# ------------------------------------------------------------
# 1. What are Nested Functions?
# ------------------------------------------------------------
# ➤ A nested function is a function defined inside another function.
# ➤ The outer function can call the inner function.
# ➤ Inner (nested) functions are useful for organizing code,
#   encapsulating logic, and creating closures.

# Basic Example:
def outer_function():
    print("This is the outer function.")

    def inner_function():
        print("This is the inner function.")

    inner_function()  # Calling the inner function from within the outer one

outer_function()
# Output:
# This is the outer function.
# This is the inner function.


# ------------------------------------------------------------
# 2. Why Use Nested Functions?
# ------------------------------------------------------------
# - To divide complex tasks into smaller, manageable units.
# - To create helper functions that are only used inside another function.
# - To protect inner logic from being accessed globally.
# - To implement *closures* (functions that remember values from enclosing scopes).


# ------------------------------------------------------------
# 3. Accessing Outer Function Variables
# ------------------------------------------------------------
# ➤ Inner functions can access variables from their enclosing (outer) function.

def greet_user(name):
    message = "Welcome"

    def display_message():
        print(message, name)

    display_message()

greet_user("Hamna")
# Output: Welcome Hamna


# ------------------------------------------------------------
# 4. Returning a Nested Function
# ------------------------------------------------------------
# ➤ An outer function can return its inner function.
# ➤ This is useful for *closures* and *decorators*.

def outer():
    def inner():
        print("Inner function has been returned!")
    return inner

returned_function = outer()  # Call outer; returns inner
returned_function()
# Output:
# Inner function has been returned!


# ------------------------------------------------------------
# 5. Example: Closure
# ------------------------------------------------------------
# ➤ A closure is formed when a nested function “remembers” the variables
#   from its enclosing scope even after the outer function has finished execution.

def multiplier(factor):
    def multiply(number):
        return number * factor  # 'factor' remembered from enclosing scope
    return multiply

times_two = multiplier(2)
times_three = multiplier(3)

print(times_two(5))    # Output: 10
print(times_three(5))  # Output: 15


# ------------------------------------------------------------
# 6. Nested Functions with Parameters
# ------------------------------------------------------------
# ➤ You can pass parameters to both the outer and inner functions.

def power(base):
    def exponent(exp):
        return base ** exp
    return exponent

result = power(2)
print(result(3))  # Output: 8


# ------------------------------------------------------------
# 7. Scope Behavior in Nested Functions
# ------------------------------------------------------------
# ➤ The inner function can read variables from the outer function,
#   but cannot modify them unless you use the 'nonlocal' keyword.

def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        print("Count =", count)

    return increment

counter_func = counter()
counter_func()  # Output: Count = 1
counter_func()  # Output: Count = 2


# ------------------------------------------------------------
# 8. Nested Functions vs Normal Functions
# ------------------------------------------------------------
# - Normal functions can be accessed globally (once defined).
# - Nested functions exist only within their enclosing function.
# - They help create isolated, reusable logic without global exposure.


# ------------------------------------------------------------
# 9. Best Practices
# ------------------------------------------------------------
# ✔ Use nested functions for internal tasks only.
# ✔ Keep the code readable — avoid excessive nesting.
# ✔ Prefer returning nested functions when closures or decorators are needed.
# ✔ Use 'nonlocal' only when modification of outer variables is necessary.


# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------
# - A nested function is defined inside another function.
# - It can access variables from the enclosing scope.
# - Outer functions can return inner functions (closures).
# - Useful for encapsulation, decorators, and small reusable logic.
# ------------------------------------------------------------
