# ------------------------------------------------------------
# File: 05_Lambda_Functions.py
# Topic: Lambda (Anonymous) Functions in Python
# ------------------------------------------------------------

# ------------------------------------------------------------
# 1. What is a Lambda Function?
# ------------------------------------------------------------
# A lambda function is a small, anonymous function — meaning it has no name.
# It can have any number of arguments but only one expression.
# It is commonly used for short, simple operations.

# Syntax:
# lambda arguments : expression

# Example:
square = lambda x: x ** 2
print("Square of 5:", square(5))  # Output: 25


# ------------------------------------------------------------
# 2. Lambda vs Normal Function
# ------------------------------------------------------------

# Normal function
def add(a, b):
    return a + b

# Lambda function (single line)
add_lambda = lambda a, b: a + b

print("Normal Function:", add(2, 3))   # Output: 5
print("Lambda Function:", add_lambda(2, 3))  # Output: 5


# ------------------------------------------------------------
# 3. Why Use Lambda Functions?
# ------------------------------------------------------------
# Lambda functions are used when:
# - A short, one-time function is needed.
# - You don’t want to formally define a function using 'def'.
# - You’re working with functions like map(), filter(), or sorted().

# Example: Using lambda for quick inline operations
double = lambda x: x * 2
print("Double of 10:", double(10))  # Output: 20


# ------------------------------------------------------------
# 4. Lambda with Multiple Arguments
# ------------------------------------------------------------

multiply = lambda x, y: x * y
print("Product:", multiply(4, 5))  # Output: 20


# ------------------------------------------------------------
# 5. Lambda with No Arguments
# ------------------------------------------------------------

greet = lambda: "Hello, Hamna!"
print(greet())  # Output: Hello, Hamna!


# ------------------------------------------------------------
# 6. Lambda Inside Other Functions
# ------------------------------------------------------------
# Lambda functions are often defined inside another function
# to perform quick, temporary computations.

def power_function(n):
    return lambda x: x ** n  # Returns a lambda function

square = power_function(2)
cube = power_function(3)

print("Square of 4:", square(4))  # Output: 16
print("Cube of 4:", cube(4))      # Output: 64


# ------------------------------------------------------------
# 7. Lambda with map(), filter(), and reduce()
# ------------------------------------------------------------
# Lambdas are very commonly used with these built-in higher-order functions.

# (1) Using map() with lambda
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("Squares:", squared)  # Output: [1, 4, 9, 16, 25]

# (2) Using filter() with lambda
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", evens)  # Output: [2, 4]

# (3) Using reduce() with lambda
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print("Product of all numbers:", product)  # Output: 120


# ------------------------------------------------------------
# 8. Lambda with Conditional Expression
# ------------------------------------------------------------
# Lambda functions can include short conditional (ternary) expressions.

max_num = lambda a, b: a if a > b else b
print("Maximum of (10, 5):", max_num(10, 5))  # Output: 10


# ------------------------------------------------------------
# 9. Limitations of Lambda Functions
# ------------------------------------------------------------
# - Only one expression allowed (no multiple statements)
# - Cannot include complex logic like loops or multiple returns
# - Less readable if overused

# Example (not recommended)
# complicated = lambda x: (x ** 2, x ** 3, x ** 4)  # Avoid such complex lambdas


# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------
# - Lambda functions are anonymous, single-expression functions.
# - Syntax: lambda arguments : expression
# - Commonly used with map(), filter(), reduce(), and sorting.
# - Use them for short, simple tasks — not as replacements for normal functions.
