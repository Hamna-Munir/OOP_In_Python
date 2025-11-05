# ================================================
# File: 05_Multiple_Inheritance.py
# Topic: Multiple Inheritance in Python
# ================================================

"""
**Multiple Inheritance** is a feature in Object-Oriented Programming (OOP)
where a class can inherit attributes and methods from **more than one parent class**.

In Python, multiple inheritance allows a derived class to combine behaviors
from multiple base classes, promoting flexibility and code reuse.

However, it also introduces complexity—especially when multiple parent classes
have methods with the same name. Python handles this using **Method Resolution Order (MRO)**.
"""

# ------------------------------------------------
# 1️⃣ What is Multiple Inheritance?
# ------------------------------------------------
# - A class can inherit from multiple parent classes.
# - The child class gains access to all public and protected members of those parent classes.
#
# Syntax:
#     class Child(Parent1, Parent2, ...):
#         pass
#
# Example:
#     class C(A, B):
#         pass

# Simple Example:
class Father:
    def show_father(self):
        print("Father: Works as an engineer.")

class Mother:
    def show_mother(self):
        print("Mother: Is a teacher.")

class Child(Father, Mother):
    def show_child(self):
        print("Child: Loves painting and coding.")

# Usage
print("----- Basic Example of Multiple Inheritance -----")
c = Child()
c.show_father()
c.show_mother()
c.show_child()


# ------------------------------------------------
# 2️⃣ Accessing Attributes and Methods from Multiple Parents
# ------------------------------------------------
# A child class can access all attributes and methods from multiple base classes.

class Person:
    def __init__(self, name):
        self.name = name

    def display_person(self):
        print(f"Person Name: {self.name}")

class Employee:
    def __init__(self, emp_id):
        self.emp_id = emp_id

    def display_employee(self):
        print(f"Employee ID: {self.emp_id}")

class Manager(Person, Employee):
    def __init__(self, name, emp_id, department):
        # Initialize both parent classes
        Person.__init__(self, name)
        Employee.__init__(self, emp_id)
        self.department = department

    def display_manager(self):
        print(f"Department: {self.department}")

# Usage
print("\n----- Accessing Attributes from Multiple Parents -----")
m = Manager("Sara", 102, "HR")
m.display_person()
m.display_employee()
m.display_manager()


# ------------------------------------------------
# 3️⃣ Using super() in Multiple Inheritance
# ------------------------------------------------
# The `super()` function can be used in multiple inheritance, but it follows
# Python’s **Method Resolution Order (MRO)** to decide which parent method to call.

class A:
    def __init__(self):
        print("Class A initialized.")

class B(A):
    def __init__(self):
        super().__init__()
        print("Class B initialized.")

class C(A):
    def __init__(self):
        super().__init__()
        print("Class C initialized.")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("Class D initialized.")

# Usage
print("\n----- Multiple Inheritance with super() -----")
d = D()

# Display the Method Resolution Order (MRO)
print("MRO:", D.mro())


# ------------------------------------------------
# 4️⃣ Example: Combining Behaviors from Different Classes
# ------------------------------------------------

class Flyer:
    def fly(self):
        print("Can fly high in the sky.")

class Swimmer:
    def swim(self):
        print("Can swim deep in the water.")

class Duck(Flyer, Swimmer):
    def sound(self):
        print("Duck says: Quack Quack!")

# Usage
print("\n----- Combining Multiple Behaviors -----")
duck = Duck()
duck.fly()
duck.swim()
duck.sound()


# ------------------------------------------------
# 5️⃣ Diamond Problem in Multiple Inheritance
# ------------------------------------------------
# The **Diamond Problem** occurs when multiple parent classes share a common ancestor,
# leading to ambiguity in which method to call.
#
# Python resolves this issue using the **C3 Linearization Algorithm**, or **MRO (Method Resolution Order)**.

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

# Usage
print("\n----- Diamond Problem Example -----")
obj = D()
obj.show()    # Calls B’s version first due to MRO
print("MRO:", D.mro())


# ------------------------------------------------
# 6️⃣ Real-World Example: Smart Device System
# ------------------------------------------------

class Camera:
    def take_picture(self):
        print("Taking a picture...")

class Phone:
    def make_call(self, number):
        print(f"Calling {number}...")

class SmartPhone(Camera, Phone):
    def browse_internet(self):
        print("Browsing the internet...")

# Usage
print("\n----- Real-World Example: Smart Device -----")
device = SmartPhone()
device.take_picture()
device.make_call("+92-300-1234567")
device.browse_internet()


# ------------------------------------------------
# 7️⃣ Advantages of Multiple Inheritance
# ------------------------------------------------
# ✅ Code Reusability — reuse code from multiple classes.
# ✅ Flexible Design — allows combining diverse functionalities.
# ✅ Supports Complex Relationships — enables modeling real-world entities that have multiple traits.


# ------------------------------------------------
# 8️⃣ Disadvantages of Multiple Inheritance
# ------------------------------------------------
# ⚠️ Increases complexity in class hierarchies.
# ⚠️ Can cause method ambiguity if not managed carefully.
# ⚠️ Requires understanding of MRO to avoid confusion.
# ⚠️ Harder to maintain and debug when classes have overlapping method names.


# ------------------------------------------------
# 9️⃣ Best Practices
# ------------------------------------------------
# - Keep class hierarchies simple and logical.
# - Always check the MRO using `ClassName.mro()`.
# - Use `super()` to follow MRO and avoid redundant initializations.
# - Prefer composition over inheritance when multiple inheritance becomes complex.
# - Avoid diamond-shaped hierarchies unless absolutely necessary.


# ================================================
# Summary:
# - Multiple Inheritance → Inheriting from more than one parent class.
# - Python resolves ambiguity using MRO (C3 Linearization).
# - Enables combining features of multiple classes.
# - Use carefully to avoid complexity and ambiguity.
# ================================================
