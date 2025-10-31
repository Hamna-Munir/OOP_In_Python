# ================================================================
# Title: Creating and Using Objects in Python
# Description: Understanding how to create objects and use them effectively
# ================================================================


# ------------------------------------------------
# What is an Object?
# ------------------------------------------------
# ➤ An object is an **instance of a class**.
# ➤ It is a real-world entity that has attributes (data) and behaviors (methods).
# ➤ Each object of a class has its own copy of the instance variables defined in the class.
#
# In short:
# A class defines the structure, and an object is the actual implementation of that structure.


# ------------------------------------------------
# How to Create an Object?
# ------------------------------------------------
# Syntax:
# object_name = ClassName(arguments)
#
# The constructor (__init__()) method is automatically called when an object is created.


# ------------------------------------------------
# Example 1: Creating and Using an Object
# ------------------------------------------------

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating objects of the Student class
student1 = Student("Hamna", 20)
student2 = Student("Alia", 21)

# Using the objects to access data
student1.show_info()
student2.show_info()

# Output:
# Name: Hamna, Age: 20
# Name: Alia, Age: 21


# ------------------------------------------------
# Example 2: Accessing Object Attributes
# ------------------------------------------------
# Attributes (variables) can be accessed using the dot (.) operator.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Creating an object
car1 = Car("Toyota", "Corolla")

# Accessing attributes
print(car1.brand)
print(car1.model)

# Output:
# Toyota
# Corolla


# ------------------------------------------------
# Example 3: Calling Methods Using an Object
# ------------------------------------------------
# Methods are also accessed using the dot (.) operator.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius ** 2

circle1 = Circle(5)
print("Area of circle:", circle1.calculate_area())
# Output: Area of circle: 78.53975


# ------------------------------------------------
# Example 4: Multiple Objects of the Same Class
# ------------------------------------------------
# You can create many objects from the same class.
# Each object will have its own set of data.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")

emp1 = Employee("Hamna", 70000)
emp2 = Employee("Ali", 60000)
emp3 = Employee("Sara", 75000)

emp1.show_details()
emp2.show_details()
emp3.show_details()

# Output:
# Employee Name: Hamna, Salary: 70000
# Employee Name: Ali, Salary: 60000
# Employee Name: Sara, Salary: 75000


# ------------------------------------------------
# Example 5: Modifying and Deleting Object Attributes
# ------------------------------------------------
# ➤ You can modify object attributes directly.
# ➤ You can also delete them using the del keyword.

class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city

person1 = Person("Hamna", "Lahore")
print(person1.name, person1.city)
# Output: Hamna Lahore

# Modifying attribute
person1.city = "Islamabad"
print(person1.name, person1.city)
# Output: Hamna Islamabad

# Deleting an attribute
del person1.city

# Deleting an entire object
del person1


# ------------------------------------------------
# Example 6: Checking Attributes and Objects
# ------------------------------------------------
# Python provides built-in functions for working with objects:
# - hasattr(obj, 'attribute')
# - getattr(obj, 'attribute', default)
# - setattr(obj, 'attribute', value)
# - delattr(obj, 'attribute')

class Student:
    def __init__(self, name):
        self.name = name

student = Student("Hamna")

print(hasattr(student, "name"))       # True
print(getattr(student, "name"))       # Hamna
setattr(student, "age", 22)           # Add new attribute
print(student.age)                    # 22
delattr(student, "name")              # Delete attribute


# ------------------------------------------------
# Example 7: Using Objects Inside Other Objects
# ------------------------------------------------
# Objects can be used as attributes inside other objects.

class Address:
    def __init__(self, city, country):
        self.city = city
        self.country = country

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def show_details(self):
        print(f"Name: {self.name}, City: {self.address.city}, Country: {self.address.country}")

addr = Address("Lahore", "Pakistan")
person = Person("Hamna", addr)
person.show_details()

# Output: Name: Hamna, City: Lahore, Country: Pakistan


# ------------------------------------------------
# Summary
# ------------------------------------------------
# - An object is an instance of a class.
# - Objects are created by calling the class as a function.
# - Use the dot (.) operator to access variables and methods.
# - Each object has its own data and can be modified independently.
# - Attributes can be added, changed, or deleted dynamically.
# - Objects can also be composed of other objects.
# ------------------------------------------------
