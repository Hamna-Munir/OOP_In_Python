# ================================================
# File: 09_Hybrid_Inheritance.py
# Topic: Hybrid Inheritance in Python
# ================================================

"""
**Hybrid Inheritance** is a combination of two or more types of inheritance.
It occurs when a class is derived using more than one inheritance pattern
(such as single, multiple, multilevel, or hierarchical) within the same program.

Hybrid inheritance is often used in complex systems where classes share 
relationships that do not fit a single inheritance model.

However, when using hybrid inheritance, one must handle the **Method Resolution Order (MRO)** 
carefully to avoid ambiguity in calling methods.
"""

# ------------------------------------------------
# 1️⃣ What is Hybrid Inheritance?
# ------------------------------------------------
# Hybrid Inheritance = Combination of:
#   - Single Inheritance
#   - Multiple Inheritance
#   - Multilevel Inheritance
#   - Hierarchical Inheritance
#
# Example structure:
#
#        A
#       / \
#      B   C
#       \ /
#        D
#
# Here:
# - B and C inherit from A (hierarchical)
# - D inherits from both B and C (multiple)
# This is a classic example of **Hybrid Inheritance**.

# ------------------------------------------------
# 2️⃣ Basic Example of Hybrid Inheritance
# ------------------------------------------------

class A:
    def show(self):
        print("Class A: Base class")

class B(A):
    def show(self):
        print("Class B: Derived from A")

class C(A):
    def show(self):
        print("Class C: Derived from A")

class D(B, C):
    def show(self):
        print("Class D: Derived from B and C (Hybrid Inheritance)")

# Usage
print("----- Basic Example of Hybrid Inheritance -----")
obj = D()
obj.show()

# You can check the MRO (Method Resolution Order) using:
print("\nMethod Resolution Order (MRO):")
print(D.__mro__)


# ------------------------------------------------
# 3️⃣ Understanding MRO (Method Resolution Order)
# ------------------------------------------------
# MRO defines the order in which Python searches for methods
# when multiple inheritance is involved.
#
# The search order is determined using the **C3 Linearization algorithm**.
# It ensures:
#   - Consistent method resolution
#   - No ambiguity in method calls
#
# You can view it using `ClassName.__mro__` or `ClassName.mro()`

class X:
    def show(self):
        print("Class X")

class Y(X):
    def show(self):
        print("Class Y")

class Z(X):
    def show(self):
        print("Class Z")

class P(Y, Z):
    pass

print("\n----- Understanding MRO Example -----")
p = P()
p.show()  # Executes Y.show() since Y appears before Z in the MRO

print("MRO for Class P:")
print(P.__mro__)


# ------------------------------------------------
# 4️⃣ Example: Real-World Scenario — Education System
# ------------------------------------------------
# Hybrid structure:
#   Person
#    /   \
#  Teacher  Student
#     \     /
#     TeachingAssistant

class Person:
    def __init__(self, name):
        self.name = name

    def show_role(self):
        print(f"{self.name} is a person.")

class Teacher(Person):
    def teach(self):
        print(f"{self.name} is teaching a class.")

class Student(Person):
    def study(self):
        print(f"{self.name} is studying.")

class TeachingAssistant(Teacher, Student):
    def assist(self):
        print(f"{self.name} is assisting in both teaching and learning.")

# Usage
print("\n----- Real-World Example: Education System (Hybrid Inheritance) -----")
ta = TeachingAssistant("Hamna")
ta.show_role()
ta.teach()
ta.study()
ta.assist()

print("\nMRO for TeachingAssistant:")
print(TeachingAssistant.__mro__)


# ------------------------------------------------
# 5️⃣ Example: Vehicle System (Combination of Hierarchical + Multiple)
# ------------------------------------------------

class Engine:
    def start_engine(self):
        print("Engine started.")

class ElectricEngine(Engine):
    def charge_battery(self):
        print("Battery charged.")

class FuelEngine(Engine):
    def fill_fuel(self):
        print("Fuel tank filled.")

class HybridCar(ElectricEngine, FuelEngine):
    def drive(self):
        print("Hybrid car is now driving using both electric and fuel power.")

# Usage
print("\n----- Example: Vehicle System (HybridCar) -----")
hybrid = HybridCar()
hybrid.start_engine()
hybrid.charge_battery()
hybrid.fill_fuel()
hybrid.drive()

print("\nMRO for HybridCar:")
print(HybridCar.__mro__)


# ------------------------------------------------
# 6️⃣ When to Use Hybrid Inheritance
# ------------------------------------------------
# ✅ Use Hybrid Inheritance when:
#   - You need to model complex relationships between classes.
#   - You want to reuse code across multiple levels and types of classes.
#   - Classes share common behavior but also require specialized functionality.
#
# ⚠️ Avoid if:
#   - The hierarchy becomes confusing or too deep.
#   - Method conflicts occur frequently.
#   - Composition (has-a relationship) can solve the problem more cleanly.


# ------------------------------------------------
# 7️⃣ Advantages of Hybrid Inheritance
# ------------------------------------------------
# ✅ Combines the benefits of multiple inheritance types.
# ✅ Promotes maximum code reuse and flexibility.
# ✅ Models real-world complex relationships effectively.
# ✅ MRO ensures predictable method resolution.


# ------------------------------------------------
# 8️⃣ Disadvantages of Hybrid Inheritance
# ------------------------------------------------
# ⚠️ Complex MRO — Harder to trace method calls.
# ⚠️ High coupling — Changes in one parent may affect multiple child classes.
# ⚠️ Risk of ambiguity if same methods exist in multiple parents.
# ⚠️ Difficult to maintain large hybrid hierarchies.


# ------------------------------------------------
# 9️⃣ Best Practices
# ------------------------------------------------
# - Keep inheritance trees as flat as possible.
# - Always check the MRO when using multiple or hybrid inheritance.
# - Avoid redefining the same methods in unrelated classes.
# - Use `super()` instead of calling parent classes explicitly.
# - Prefer composition when inheritance creates unnecessary complexity.


# ================================================
# Summary:
# - Hybrid Inheritance → Combination of multiple inheritance types.
# - MRO determines the method search order.
# - Useful for modeling complex real-world systems.
# - Must be used carefully to avoid ambiguity and complexity.
# ================================================
