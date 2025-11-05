# ================================================
# File: 06_Multilevel_Inheritance.py
# Topic: Multilevel Inheritance in Python
# ================================================

"""
**Multilevel Inheritance** is a type of inheritance in which a class inherits from
another derived class, forming a chain of inheritance.

In other words:
    - A class (Child) inherits from another class (Parent),
    - Which itself inherits from another class (Grandparent).

This allows the lowest-level class to access the properties and methods of all
its ancestors in the hierarchy.

It is useful for representing hierarchical relationships, such as
"Grandparent → Parent → Child".
"""

# ------------------------------------------------
# 1️⃣ What is Multilevel Inheritance?
# ------------------------------------------------
# - A derived class acts as a base class for another derived class.
# - It creates a chain of inheritance.
#
# Example:
#     class A:
#         ...
#     class B(A):
#         ...
#     class C(B):
#         ...
#
# Here, C inherits from B, and B inherits from A.
# So, C indirectly inherits all members of A.


# ------------------------------------------------
# 2️⃣ Basic Example of Multilevel Inheritance
# ------------------------------------------------

class Grandparent:
    def show_grandparent(self):
        print("Grandparent: Family tradition and values.")

class Parent(Grandparent):
    def show_parent(self):
        print("Parent: Responsible and caring.")

class Child(Parent):
    def show_child(self):
        print("Child: Curious and learning.")

# Usage
print("----- Basic Example of Multilevel Inheritance -----")
obj = Child()
obj.show_grandparent()
obj.show_parent()
obj.show_child()


# ------------------------------------------------
# 3️⃣ Example: Inheriting Attributes and Methods
# ------------------------------------------------

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print(f"Vehicle Brand: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show_model(self):
        print(f"Car Model: {self.model}")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def show_details(self):
        self.show_brand()
        self.show_model()
        print(f"Battery Capacity: {self.battery_capacity} kWh")

# Usage
print("\n----- Example: Vehicle Hierarchy -----")
tesla = ElectricCar("Tesla", "Model S", 100)
tesla.show_details()


# ------------------------------------------------
# 4️⃣ Real-World Example: Education System
# ------------------------------------------------

class Person:
    def __init__(self, name):
        self.name = name

    def show_person(self):
        print(f"Name: {self.name}")

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def show_student(self):
        print(f"Student ID: {self.student_id}")

class GraduateStudent(Student):
    def __init__(self, name, student_id, research_topic):
        super().__init__(name, student_id)
        self.research_topic = research_topic

    def show_research(self):
        print(f"Research Topic: {self.research_topic}")

# Usage
print("\n----- Real-World Example: Education Hierarchy -----")
grad = GraduateStudent("Hamna", "S1023", "Artificial Intelligence")
grad.show_person()
grad.show_student()
grad.show_research()


# ------------------------------------------------
# 5️⃣ Multilevel Inheritance and Constructors
# ------------------------------------------------
# In multilevel inheritance, when a derived class is created,
# constructors are called automatically from the top of the hierarchy
# to the bottom (Parent → Child).

class A:
    def __init__(self):
        print("A: Constructor called.")

class B(A):
    def __init__(self):
        super().__init__()
        print("B: Constructor called.")

class C(B):
    def __init__(self):
        super().__init__()
        print("C: Constructor called.")

# Usage
print("\n----- Constructor Order in Multilevel Inheritance -----")
c = C()


# ------------------------------------------------
# 6️⃣ Method Overriding in Multilevel Inheritance
# ------------------------------------------------
# A child class can override a method inherited from any ancestor.
# When called on the most derived object, the **lowest-level implementation** executes.

class Animal:
    def speak(self):
        print("Animals make sounds.")

class Mammal(Animal):
    def speak(self):
        print("Mammals make warm sounds.")

class Dog(Mammal):
    def speak(self):
        print("Dog barks loudly!")

# Usage
print("\n----- Method Overriding in Multilevel Inheritance -----")
dog = Dog()
dog.speak()   # Calls Dog’s overridden version


# ------------------------------------------------
# 7️⃣ Accessing Parent Methods using super()
# ------------------------------------------------
# Each level can use `super()` to call the parent’s version of a method.

class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        super().greet()
        print("Hello from B")

class C(B):
    def greet(self):
        super().greet()
        print("Hello from C")

# Usage
print("\n----- Using super() Across Multiple Levels -----")
obj = C()
obj.greet()


# ------------------------------------------------
# 8️⃣ Advantages of Multilevel Inheritance
# ------------------------------------------------
# ✅ Promotes code reusability — derived classes reuse code from ancestors.
# ✅ Supports hierarchical representation — models natural parent–child relationships.
# ✅ Allows gradual enhancement of class features at each level.


# ------------------------------------------------
# 9️⃣ Disadvantages of Multilevel Inheritance
# ------------------------------------------------
# ⚠️ Increases complexity in the class hierarchy.
# ⚠️ Debugging becomes harder when methods are overridden at multiple levels.
# ⚠️ Changes in base classes can affect all derived classes.
# ⚠️ Should be used only when there is a logical hierarchical relationship.


# ------------------------------------------------
# 🔟 Best Practices
# ------------------------------------------------
# - Keep inheritance chains short (prefer two or three levels maximum).
# - Use clear, meaningful relationships between classes.
# - Use `super()` to maintain consistent initialization and method calls.
# - Prefer composition when the relationship is not truly hierarchical.


# ================================================
# Summary:
# - Multilevel Inheritance → Chain of inheritance (Grandparent → Parent → Child)
# - Enables hierarchical class design and code reuse.
# - Constructors and methods are executed in order (top to bottom).
# - Use carefully to avoid deep or complex hierarchies.
# ================================================
