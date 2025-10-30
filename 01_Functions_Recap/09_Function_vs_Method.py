# ================================================================
# Title: Function vs Method in Python
# Description: Difference between functions and methods with examples
# ================================================================


# ------------------------------------------------
# What is a Function?
# ------------------------------------------------
# A function is a block of code that performs a specific task.
# It is defined using the 'def' keyword and can be called independently.

def greet(name):
    return f"Hello, {name}!"

print(greet("Hamna"))  # Calling a function


# ------------------------------------------------
# What is a Method?
# ------------------------------------------------
# A method is similar to a function, but it is associated with an object.
# It is defined within a class and can only be called using an instance (object) of that class.

class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):  # Method defined inside a class
        return f"Hello, {self.name}! Welcome to Python OOP."


student1 = Student("Hamna")
print(student1.greet())  # Calling a method through an object


# ------------------------------------------------
# Key Differences Between Functions and Methods
# ------------------------------------------------
# 1. Definition:
#    - Functions are defined using 'def' outside any class.
#    - Methods are defined inside a class.
#
# 2. Calling:
#    - Functions are called directly using their name.
#    - Methods are called through an object (instance of a class).
#
# 3. Association:
#    - Functions are not tied to any particular object or data type.
#    - Methods are associated with objects and can access instance data via 'self'.
#
# 4. Example:
#    Function: len([1, 2, 3])
#    Method: [1, 2, 3].append(4)

# ------------------------------------------------
# Example of Built-in Function vs Built-in Method
# ------------------------------------------------

# Built-in Function
numbers = [10, 20, 30]
print(len(numbers))  # len() is a function

# Built-in Method
numbers.append(40)   # append() is a method
print(numbers)


# ------------------------------------------------
# Summary
# ------------------------------------------------
# - Functions are independent and perform a specific task.
# - Methods are dependent on the object and operate on its data.
# - Understanding this difference is crucial when moving into OOP (Object-Oriented Programming).
