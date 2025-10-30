# ------------------------------------------------------------
# File: 04_Return_Values.py
# Topic: Return Values in Python Functions
# ------------------------------------------------------------

# ------------------------------------------------------------
# 1. What is a Return Statement?
# ------------------------------------------------------------
# The 'return' statement is used in a function to send data back
# to the caller. It also ends the function execution immediately.

def add(a, b):
    return a + b   # Returns the sum to the caller

result = add(5, 3)
print("Result:", result)  # Output: 8

# If a function does not have a return statement, it returns None by default.

def greet():
    print("Hello!")  # No return statement

val = greet()
print("Return Value:", val)  # Output: None


# ------------------------------------------------------------
# 2. Returning Multiple Values
# ------------------------------------------------------------
# Python allows returning more than one value by separating them with commas.
# Internally, these are packed into a tuple.

def calculate(a, b):
    sum_ = a + b
    diff = a - b
    prod = a * b
    return sum_, diff, prod  # Returns a tuple

result = calculate(10, 5)
print("Tuple Result:", result)
print("Sum:", result[0], "Difference:", result[1], "Product:", result[2])

# You can also unpack multiple return values.
s, d, p = calculate(10, 5)
print("Sum:", s)
print("Difference:", d)
print("Product:", p)


# ------------------------------------------------------------
# 3. Returning Lists, Dictionaries, or Other Collections
# ------------------------------------------------------------
# You can return any type of Python object — lists, tuples, sets, dictionaries, etc.

def get_student_info():
    student = {
        "name": "Hamna",
        "age": 20,
        "course": "Python OOP"
    }
    return student

info = get_student_info()
print("Student Info:", info)
print("Name:", info["name"])


# ------------------------------------------------------------
# 4. Return vs Print
# ------------------------------------------------------------
# 'print()' displays data on the screen.
# 'return' sends data back to the caller for further use.

def square(num):
    print(num ** 2)  # Just prints the value, does not return it

def cube(num):
    return num ** 3  # Returns value to the caller

square(4)           # Output: 16 (only displays)
result = cube(3)
print("Cube:", result)  # Output: Cube: 27


# ------------------------------------------------------------
# 5. Early Return
# ------------------------------------------------------------
# You can use multiple return statements to exit a function early
# based on some condition.

def divide(a, b):
    if b == 0:
        return "Error: Division by zero not allowed"
    return a / b

print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: Error: Division by zero not allowed


# ------------------------------------------------------------
# 6. Returning None Explicitly
# ------------------------------------------------------------
# If you return without a value, Python automatically returns None.

def do_nothing():
    return

print(do_nothing())  # Output: None


# ------------------------------------------------------------
# 7. Nested Return Example
# ------------------------------------------------------------
# Return values can also be results of other functions.

def multiply(a, b):
    return a * b

def area_of_rectangle(length, width):
    return multiply(length, width)  # Returning result from another function

print("Area:", area_of_rectangle(4, 6))  # Output: 24


# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------
# - The 'return' statement sends data from a function to the caller.
# - If no return statement is used, the function returns None.
# - Multiple values can be returned as a tuple.
# - 'return' is used for logic, 'print' is used for display.
# - You can return any data type or even the result of another function.
