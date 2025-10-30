# ----------------------------------------------------------
# File Name: 03_Function_Arguments.py
# Topic: Function Arguments in Python
# ----------------------------------------------------------
# Author: Hamna Munir
# Repository: OOP_In_Python
# ----------------------------------------------------------

# ----------------------------------------------------------
#   What are Function Arguments?
# ----------------------------------------------------------
# ➤ Arguments are values passed to a function when it is called.
# ➤ They allow us to pass data into a function so it can perform its task.
# ➤ The values inside the parentheses of the function call are called *arguments*,
#    and the names inside the function definition are called *parameters*.

# Example:
def greet(name):
    print("Hello,", name)

greet("Hamna")
# Output: Hello, Hamna

# ----------------------------------------------------------
#   Types of Function Arguments in Python
# ----------------------------------------------------------
# Python supports 5 main types of arguments:
# 1️⃣ Positional Arguments
# 2️⃣ Keyword Arguments
# 3️⃣ Default Arguments
# 4️⃣ Variable-Length Arguments (*args)
# 5️⃣ Keyword Variable-Length Arguments (**kwargs)
# ----------------------------------------------------------


# ----------------------------------------------------------
#   1️⃣ Positional Arguments
# ----------------------------------------------------------
# ➤ Arguments are passed in the same order as parameters are defined.
# ➤ The position of each argument matters.

def student_info(name, age, course):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")

student_info("Hamna", 20, "AI/ML")
# Output:
# Name: Hamna
# Age: 20
# Course: AI/ML

# If you change the order, output will change:
student_info("AI/ML", 20, "Hamna")
# Output:
# Name: AI/ML
# Age: 20
# Course: Hamna


# ----------------------------------------------------------
#   2️⃣ Keyword Arguments
# ----------------------------------------------------------
# ➤ You can specify which parameter receives which value by using the parameter name.
# ➤ The order no longer matters.

student_info(name="Hamna", course="Python", age=20)
# Output:
# Name: Hamna
# Age: 20
# Course: Python


# ----------------------------------------------------------
#   3️⃣ Default Arguments
# ----------------------------------------------------------
# ➤ You can assign default values to parameters.
# ➤ If no argument is passed for that parameter, the default value is used.

def greet_user(name, message="Welcome to Python!"):
    print(f"Hello, {name}. {message}")

greet_user("Hamna")
# Output: Hello, Hamna. Welcome to Python!

greet_user("Hamna", "Hope you're enjoying learning functions.")
# Output: Hello, Hamna. Hope you're enjoying learning functions.


# ----------------------------------------------------------
#   4️⃣ Variable-Length Arguments (*args)
# ----------------------------------------------------------
# ➤ Sometimes we don’t know how many arguments will be passed.
# ➤ Using *args allows a function to accept any number of positional arguments.
# ➤ Inside the function, args is treated as a tuple.

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Sum:", total)

add_numbers(5, 10)
# Output: Sum: 15

add_numbers(1, 2, 3, 4, 5)
# Output: Sum: 15


# ----------------------------------------------------------
#   5️⃣ Keyword Variable-Length Arguments (**kwargs)
# ----------------------------------------------------------
# ➤ Allows passing a variable number of keyword arguments.
# ➤ Inside the function, kwargs is treated as a dictionary.

def display_student(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_student(name="Hamna", age=20, course="Python", city="Faisalabad")
# Output:
# name: Hamna
# age: 20
# course: Python
# city: Faisalabad


# ----------------------------------------------------------
#   Mixing Different Types of Arguments
# ----------------------------------------------------------
# When combining multiple argument types, the correct order is:
# 1. Positional Arguments
# 2. *args
# 3. Keyword Arguments
# 4. **kwargs

def full_function(name, *skills, role="Student", **details):
    print("Name:", name)
    print("Role:", role)
    print("Skills:", skills)
    print("Details:", details)

full_function("Hamna", "Python", "AI", "ML", role="Developer", city="Faisalabad", age=20)
# Output:
# Name: Hamna
# Role: Developer
# Skills: ('Python', 'AI', 'ML')
# Details: {'city': 'Faisalabad', 'age': 20}


# ----------------------------------------------------------
#   Argument Unpacking
# ----------------------------------------------------------
# ➤ You can use * and ** to unpack iterables (lists, tuples, dictionaries)
#    into function arguments.

def display(a, b, c):
    print(a, b, c)

values = [10, 20, 30]
display(*values)
# Output: 10 20 30

info = {"a": 100, "b": 200, "c": 300}
display(**info)
# Output: 100 200 300


# ----------------------------------------------------------
#   Summary:
# ----------------------------------------------------------
# ✔ Positional Arguments → Follow order of parameters.
# ✔ Keyword Arguments → Specify parameter names explicitly.
# ✔ Default Arguments → Provide fallback values if none are given.
# ✔ *args → For variable number of positional arguments.
# ✔ **kwargs → For variable number of keyword arguments.
# ✔ Order: Positional → *args → Keyword → **kwargs
# ✔ Argument unpacking allows passing iterables easily using * or **.
# ----------------------------------------------------------
