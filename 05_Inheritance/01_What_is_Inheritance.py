# ================================================
# File: 01_What_is_Inheritance.py
# Topic: Understanding Inheritance in Python
# ================================================

"""
In Object-Oriented Programming (OOP), **Inheritance** is one of the core principles.
It allows a class (called the *child class* or *derived class*) to **inherit** 
attributes and methods from another class (called the *parent class* or *base class*).

Inheritance promotes **code reusability**, **modularity**, and **hierarchical organization**.
It also supports **extensibility**, meaning new classes can build upon existing ones 
without rewriting code.
"""

# ------------------------------------------------
# 1️⃣ What is Inheritance?
# ------------------------------------------------
# Inheritance allows one class to derive or inherit properties (variables)
# and behaviors (methods) from another class.
#
# Syntax:
#     class Parent:
#         # Parent class code
#
#     class Child(Parent):
#         # Child class inherits from Parent

# Example:
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

# Child class inherits from Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")

# Usage
dog = Dog("Buddy")
dog.eat()   # Inherited method from Animal
dog.bark()  # Method defined in Dog


# ------------------------------------------------
# 2️⃣ Why Use Inheritance?
# ------------------------------------------------
# 1. **Code Reusability** – Reuse existing logic instead of rewriting it.
# 2. **Extensibility** – Easily add new functionality.
# 3. **Maintainability** – Changes in the parent automatically reflect in child classes.
# 4. **Hierarchy Representation** – Models real-world relationships (e.g., Animal → Dog → Puppy).


# ------------------------------------------------
# 3️⃣ Example: Real-World Analogy
# ------------------------------------------------
# Base class (Parent)
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# Derived class (Child)
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)   # Call parent constructor
        self.doors = doors

    def show_details(self):
        self.show_info()                 # Access parent method
        print(f"Doors: {self.doors}")

# Usage
car = Car("Toyota", "Corolla", 4)
car.show_details()


# ------------------------------------------------
# 4️⃣ The super() Function
# ------------------------------------------------
# The `super()` function is used to call methods from the parent class inside the child class.
# It is commonly used to invoke the parent constructor (`__init__`) or other parent methods.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"Employee: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)      # Calls Employee.__init__()
        self.department = department

    def show(self):
        super().show()                      # Calls Employee.show()
        print(f"Department: {self.department}")

# Usage
mgr = Manager("Hamna", 85000, "IT")
mgr.show()


# ------------------------------------------------
# 5️⃣ Inheritance Hierarchy
# ------------------------------------------------
# Inheritance allows creating a hierarchy of classes that share behavior.
#
# Example:
#   LivingBeing (base)
#       └── Animal
#             └── Dog
#                   └── Puppy
#
# Each subclass inherits from its parent and can add new behaviors.

class LivingBeing:
    def breathe(self):
        print("Breathing...")

class Animal(LivingBeing):
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def bark(self):
        print("Barking...")

class Puppy(Dog):
    def play(self):
        print("Playing...")

# Usage
puppy = Puppy()
puppy.breathe()   # Inherited from LivingBeing
puppy.eat()       # Inherited from Animal
puppy.bark()      # Inherited from Dog
puppy.play()      # Defined in Puppy


# ------------------------------------------------
# 6️⃣ Key Terms
# ------------------------------------------------
# - **Base Class (Parent)**: The class being inherited from.
# - **Derived Class (Child)**: The class that inherits from another class.
# - **super()**: A built-in function used to access the parent class.
# - **Method Overriding**: A child class can redefine a parent’s method to change its behavior.
# - **Code Reusability**: The biggest advantage of inheritance.


# ------------------------------------------------
# 7️⃣ Best Practices for Inheritance
# ------------------------------------------------
# - Use inheritance when there is an "is-a" relationship between classes.
#   Example: Dog is an Animal, Car is a Vehicle.
# - Avoid deep inheritance chains (they reduce clarity).
# - Keep parent classes general and child classes specific.
# - Prefer **composition** over inheritance when possible if the relationship is not "is-a".


# ------------------------------------------------
# 8️⃣ Advantages and Limitations
# ------------------------------------------------
#   Advantages:
#   - Promotes code reuse.
#   - Reduces redundancy.
#   - Enables polymorphism (same interface, different behavior).
#   - Easier maintenance.
#
#   Limitations:
#   - Tight coupling between parent and child classes.
#   - Changes in base class can impact all subclasses.
#   - Can become complex in deep hierarchies.


# ================================================
# Summary:
# Inheritance allows one class to acquire properties and behaviors of another.
# - Parent → Base Class (provides attributes/methods)
# - Child → Derived Class (inherits and extends functionality)
# - Promotes code reuse, maintainability, and hierarchy modeling.
# ================================================
