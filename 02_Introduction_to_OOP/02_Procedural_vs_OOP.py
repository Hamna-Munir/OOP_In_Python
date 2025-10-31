# ================================================================
# Title: Procedural Programming vs Object-Oriented Programming
# Description: Understanding the key differences between the two paradigms
# ================================================================


# ------------------------------------------------
# What is Procedural Programming?
# ------------------------------------------------
# Procedural Programming is a programming paradigm based on the concept of
# procedures (also called routines, subroutines, or functions).
# 
# The main idea is to write a sequence of instructions to perform a task.
# Data and functions are kept separate.
#
# Key Characteristics:
# - Focuses on *functions* and *procedures*.
# - Data is passed from one function to another.
# - Code is written step-by-step (top-down approach).
# - Reusability and scalability are limited.


# Example: Procedural Programming

name = "Ali"
age = 20

def display_person(name, age):
    return f"Name: {name}, Age: {age}"

def birthday(age):
    return age + 1

print(display_person(name, age))
age = birthday(age)
print(display_person(name, age))


# ------------------------------------------------
# What is Object-Oriented Programming (OOP)?
# ------------------------------------------------
# Object-Oriented Programming organizes code around *objects* rather than functions.
# Each object contains both data (attributes) and behavior (methods).
#
# Key Characteristics:
# - Focuses on *objects* and *classes*.
# - Data and methods are encapsulated together.
# - Encourages reusability through inheritance.
# - Supports abstraction, encapsulation, inheritance, and polymorphism.


# Example: Object-Oriented Programming

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"Name: {self.name}, Age: {self.age}"

    def birthday(self):
        self.age += 1

# Creating an object
person1 = Person("Ali", 20)

print(person1.display())
person1.birthday()
print(person1.display())


# ------------------------------------------------
# Comparison Summary
# ------------------------------------------------
# | Feature                   | Procedural Programming        | Object-Oriented Programming     |
# |----------------------------|-------------------------------|----------------------------------|
# | Focus                     | Functions / Procedures         | Objects and Classes              |
# | Data & Functions           | Separate                      | Combined within objects          |
# | Code Reusability           | Limited                       | High (via inheritance)           |
# | Approach                   | Top-Down                      | Bottom-Up                        |
# | Data Security              | Weak                          | Strong (Encapsulation)           |
# | Example Languages          | C, Pascal                     | Python, Java, C++                |


# ------------------------------------------------
# Summary
# ------------------------------------------------
# - Procedural programming is simpler and suitable for small programs.
# - OOP is more powerful and scalable for large, complex systems.
# - Python supports both paradigms, but OOP is preferred for modern software design.
