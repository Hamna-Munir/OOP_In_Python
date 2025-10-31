# ================================================================
# Title: The __init__() Method and self in Python
# Description: Understanding object initialization and the role of 'self'
# ================================================================


# ------------------------------------------------
# What is the __init__() Method?
# ------------------------------------------------
# ➤ The __init__() method is a special (built-in) method in Python classes.
# ➤ It is automatically called when a new object of a class is created.
# ➤ It is also known as the **constructor** in other programming languages.
#
# Purpose:
# - To initialize (assign values to) the object’s attributes at creation time.
# - To perform any setup required for the object.


# Syntax:
# class ClassName:
#     def __init__(self, parameters):
#         self.attribute = value


# ------------------------------------------------
# What is 'self'?
# ------------------------------------------------
# ➤ 'self' refers to the **current instance** of the class.
# ➤ It allows you to access instance variables and methods inside the class.
# ➤ It must be the first parameter in every instance method (including __init__()).
#
# Note: You don’t pass any value for 'self' when calling methods.
# Python automatically provides it.


# ------------------------------------------------
# Example 1: Using __init__() and self
# ------------------------------------------------

class Student:
    def __init__(self, name, age):
        self.name = name   # instance variable
        self.age = age     # instance variable

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating objects (constructor is automatically called)
s1 = Student("Hamna", 20)
s2 = Student("Alia", 21)

s1.display_info()
s2.display_info()

# Output:
# Name: Hamna, Age: 20
# Name: Alia, Age: 21


# ------------------------------------------------
# Example 2: Using __init__() for Initialization
# ------------------------------------------------
# The constructor can perform calculations or process data during object creation.

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = 3.14159 * (radius ** 2)

    def show_details(self):
        print(f"Radius: {self.radius}, Area: {self.area}")

c1 = Circle(5)
c1.show_details()
# Output: Radius: 5, Area: 78.53975


# ------------------------------------------------
# Example 3: Using Default Arguments in __init__()
# ------------------------------------------------

class Book:
    def __init__(self, title, author="Unknown"):
        self.title = title
        self.author = author

    def show(self):
        print(f"Book Title: {self.title}, Author: {self.author}")

book1 = Book("Python for AI/ML", "Hamna Munir")
book2 = Book("Learning Data Science")  # uses default author

book1.show()
book2.show()
# Output:
# Book Title: Python for AI/ML, Author: Hamna Munir
# Book Title: Learning Data Science, Author: Unknown


# ------------------------------------------------
# Example 4: Understanding 'self'
# ------------------------------------------------
# The 'self' parameter is used to access object-specific data.

class Example:
    def __init__(self):
        print("Constructor called")

    def show_id(self):
        print("Object ID:", id(self))

obj1 = Example()
obj2 = Example()

obj1.show_id()
obj2.show_id()

# Output:
# Constructor called
# Constructor called
# Object ID: (unique ID for obj1)
# Object ID: (unique ID for obj2)


# ------------------------------------------------
# Example 5: Difference Between Class and Instance Variables
# ------------------------------------------------

class Car:
    wheels = 4   # class variable (shared by all objects)

    def __init__(self, brand, color):
        self.brand = brand   # instance variable
        self.color = color   # instance variable

    def show_info(self):
        print(f"Brand: {self.brand}, Color: {self.color}, Wheels: {Car.wheels}")

car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

car1.show_info()
car2.show_info()
# Output:
# Brand: Toyota, Color: Red, Wheels: 4
# Brand: Honda, Color: Blue, Wheels: 4


# ------------------------------------------------
# Summary
# ------------------------------------------------
# - __init__() is a special method called automatically when an object is created.
# - It is used to initialize instance variables.
# - 'self' represents the current object and allows access to its data.
# - Each object has its own copy of instance variables.
# - Class variables are shared among all objects.
# - Constructors make object initialization organized and readable.
# ------------------------------------------------
