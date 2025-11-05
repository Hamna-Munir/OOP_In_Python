# ================================================
# File: 02_Types_of_Inheritance.py
# Topic: Types of Inheritance in Python
# ================================================

"""
In Object-Oriented Programming (OOP), **Inheritance** allows a class (child class)
to reuse and extend the functionality of another class (parent class).

Python supports **multiple types of inheritance**, enabling developers to create
complex and flexible class hierarchies.

Each type defines how classes relate to each other and how attributes/methods
are inherited.
"""

# ------------------------------------------------
# 1️⃣ What is Inheritance (Recap)
# ------------------------------------------------
# - **Inheritance** enables one class to derive attributes and methods from another.
# - The class being inherited from is called the **Parent (Base) Class**.
# - The class that inherits is called the **Child (Derived) Class**.
#
# Benefits:
# - Promotes code reusability.
# - Reduces duplication.
# - Improves organization and scalability.

# Syntax:
#     class Parent:
#         ...
#     class Child(Parent):
#         ...


# ------------------------------------------------
# 2️⃣ Types of Inheritance in Python
# ------------------------------------------------
# Python supports the following types of inheritance:
#
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance
#
# Each type is explained below with examples.


# ------------------------------------------------
# 3️⃣ Single Inheritance
# ------------------------------------------------
# A child class inherits from only one parent class.

class Parent:
    def show_parent(self):
        print("This is the Parent class.")

class Child(Parent):
    def show_child(self):
        print("This is the Child class.")

# Usage
print("----- Single Inheritance -----")
c = Child()
c.show_parent()   # Inherited from Parent
c.show_child()    # Defined in Child


# ------------------------------------------------
# 4️⃣ Multiple Inheritance
# ------------------------------------------------
# A child class inherits from **more than one parent class**.
# Python supports multiple inheritance directly.

class Father:
    def skills(self):
        print("Father: Knows driving and gardening.")

class Mother:
    def hobbies(self):
        print("Mother: Enjoys cooking and painting.")

class Child(Father, Mother):
    def talents(self):
        print("Child: Plays football and studies well.")

# Usage
print("\n----- Multiple Inheritance -----")
child = Child()
child.skills()    # From Father
child.hobbies()   # From Mother
child.talents()   # From Child


# ------------------------------------------------
# 5️⃣ Multilevel Inheritance
# ------------------------------------------------
# A class inherits from another class, which itself is inherited from another.
# This creates a chain of inheritance.

class Grandparent:
    def family_origin(self):
        print("Family origin: Lahore")

class Parent(Grandparent):
    def family_name(self):
        print("Family name: Khan")

class Child(Parent):
    def family_member(self):
        print("Family member: Hamna")

# Usage
print("\n----- Multilevel Inheritance -----")
person = Child()
person.family_origin()   # Inherited from Grandparent
person.family_name()     # Inherited from Parent
person.family_member()   # Defined in Child


# ------------------------------------------------
# 6️⃣ Hierarchical Inheritance
# ------------------------------------------------
# Multiple child classes inherit from the same parent class.

class Animal:
    def sound(self):
        print("Animals make sounds.")

class Dog(Animal):
    def bark(self):
        print("Dog barks: Woof!")

class Cat(Animal):
    def meow(self):
        print("Cat meows: Meow!")

class Cow(Animal):
    def moo(self):
        print("Cow moos: Moo!")

# Usage
print("\n----- Hierarchical Inheritance -----")
dog = Dog()
cat = Cat()
cow = Cow()

dog.sound()
dog.bark()

cat.sound()
cat.meow()

cow.sound()
cow.moo()


# ------------------------------------------------
# 7️⃣ Hybrid Inheritance
# ------------------------------------------------
# A combination of two or more types of inheritance.
# This often includes multiple and multilevel inheritance in the same hierarchy.
#
# Python uses **Method Resolution Order (MRO)** to determine the order of method lookup
# when multiple inheritance paths exist.

class A:
    def feature(self):
        print("Feature from class A")

class B(A):
    def feature(self):
        print("Feature from class B")

class C(A):
    def feature(self):
        print("Feature from class C")

class D(B, C):
    def feature(self):
        print("Feature from class D")

# Usage
print("\n----- Hybrid Inheritance -----")
d = D()
d.feature()    # Calls D’s feature() method

# Method Resolution Order
print("MRO:", D.mro())   # Shows order Python follows to resolve methods


# ------------------------------------------------
# 8️⃣ Method Resolution Order (MRO)
# ------------------------------------------------
# MRO defines the sequence in which Python looks for methods and attributes
# when multiple inheritance is used.
#
# Python follows the **C3 Linearization Algorithm**, also known as **C3 MRO**.
#
# You can view the MRO of a class using:
#   ClassName.mro()  or  ClassName.__mro__
#
# Example above prints the MRO order for class D.


# ------------------------------------------------
# 9️⃣ Practical Example: Real-World Use of Inheritance
# ------------------------------------------------

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def show_info(self):
        print(f"Employee Name: {self.name}, ID: {self.emp_id}")

class Developer(Employee):
    def __init__(self, name, emp_id, programming_language):
        super().__init__(name, emp_id)
        self.programming_language = programming_language

    def show_developer_info(self):
        self.show_info()
        print(f"Programming Language: {self.programming_language}")

class Manager(Employee):
    def __init__(self, name, emp_id, team_size):
        super().__init__(name, emp_id)
        self.team_size = team_size

    def show_manager_info(self):
        self.show_info()
        print(f"Team Size: {self.team_size}")

# Usage
print("\n----- Real-World Example -----")
dev = Developer("Ali", 101, "Python")
mgr = Manager("Sara", 102, 5)

dev.show_developer_info()
mgr.show_manager_info()


# ------------------------------------------------
# 🔟 Advantages of Using Different Inheritance Types
# ------------------------------------------------
# - **Single Inheritance:** Simple, easy to manage, clear relationships.
# - **Multiple Inheritance:** Allows combining behaviors from multiple sources.
# - **Multilevel Inheritance:** Useful for hierarchical models.
# - **Hierarchical Inheritance:** Encourages shared base functionality.
# - **Hybrid Inheritance:** Flexible but must be used carefully (due to MRO complexity).


# ------------------------------------------------
# 11️⃣ Best Practices
# ------------------------------------------------
# - Use single or multilevel inheritance for simplicity.
# - Use multiple inheritance only when logically necessary.
# - Always understand MRO before implementing complex hierarchies.
# - Prefer composition over inheritance if the relationship is not “is-a”.


# ================================================
# Summary:
# Python supports five types of inheritance:
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance
#
# - Inheritance improves code reusability, scalability, and organization.
# - Always design hierarchies logically to maintain readability.
# ================================================
