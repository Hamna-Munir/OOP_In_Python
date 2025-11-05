# ================================================
# File: 07_Hierarchical_Inheritance.py
# Topic: Hierarchical Inheritance in Python
# ================================================

"""
**Hierarchical Inheritance** is a type of inheritance in which **multiple child
classes inherit from a single parent class**.

It represents a tree-like structure where one base class acts as a common parent
for multiple subclasses.

This type of inheritance promotes **code reusability** because common
attributes and methods can be defined in the parent class and shared by all child
classes.

Diagrammatically:

            Parent
           /   |   \
     Child1  Child2  Child3
"""

# ------------------------------------------------
# 1️⃣ What is Hierarchical Inheritance?
# ------------------------------------------------
# - One parent class → multiple child classes.
# - Each child class can have its own unique properties or methods.
# - All child classes share the common functionality of the parent class.
#
# Example:
#     class Parent:
#         ...
#     class Child1(Parent):
#         ...
#     class Child2(Parent):
#         ...
#
# Here, both Child1 and Child2 inherit from Parent.


# ------------------------------------------------
# 2️⃣ Basic Example of Hierarchical Inheritance
# ------------------------------------------------

class Animal:
    def speak(self):
        print("Animals make sounds.")

class Dog(Animal):
    def speak(self):
        print("Dog barks.")

class Cat(Animal):
    def speak(self):
        print("Cat meows.")

class Cow(Animal):
    def speak(self):
        print("Cow moos.")

# Usage
print("----- Basic Example of Hierarchical Inheritance -----")
dog = Dog()
cat = Cat()
cow = Cow()

dog.speak()
cat.speak()
cow.speak()


# ------------------------------------------------
# 3️⃣ Example: Shared Attributes and Methods
# ------------------------------------------------
# All subclasses inherit the parent’s constructor and methods.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):
    def fuel_type(self):
        print("Car uses petrol or diesel.")

class Bike(Vehicle):
    def fuel_type(self):
        print("Bike uses petrol.")

class ElectricScooter(Vehicle):
    def fuel_type(self):
        print("Electric scooter uses battery power.")

# Usage
print("\n----- Example: Vehicle Hierarchy -----")
c = Car("Toyota")
b = Bike("Yamaha")
e = ElectricScooter("Tesla")

c.show_brand()
c.fuel_type()

b.show_brand()
b.fuel_type()

e.show_brand()
e.fuel_type()


# ------------------------------------------------
# 4️⃣ Real-World Example: Educational Roles
# ------------------------------------------------

class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name: {self.name}")

class Student(Person):
    def study(self):
        print(f"{self.name} is studying.")

class Teacher(Person):
    def teach(self):
        print(f"{self.name} is teaching a class.")

class Staff(Person):
    def manage(self):
        print(f"{self.name} is managing school operations.")

# Usage
print("\n----- Real-World Example: Educational Hierarchy -----")
s = Student("Hamna")
t = Teacher("Ali")
m = Staff("Sara")

s.show_name()
s.study()

t.show_name()
t.teach()

m.show_name()
m.manage()


# ------------------------------------------------
# 5️⃣ Constructor Behavior in Hierarchical Inheritance
# ------------------------------------------------
# Each child class inherits the constructor of the parent class unless
# it defines its own constructor.

class Parent:
    def __init__(self):
        print("Parent constructor called.")

class Child1(Parent):
    def __init__(self):
        super().__init__()
        print("Child1 constructor called.")

class Child2(Parent):
    pass   # No custom constructor, will use Parent’s constructor.

# Usage
print("\n----- Constructor Behavior in Hierarchical Inheritance -----")
obj1 = Child1()
obj2 = Child2()


# ------------------------------------------------
# 6️⃣ Hierarchical Inheritance and Method Overriding
# ------------------------------------------------
# Each child class can override a method from the parent class
# to provide its own specialized behavior.

class Shape:
    def area(self):
        print("Area: Depends on shape type.")

class Circle(Shape):
    def area(self):
        print("Area of Circle = π * r²")

class Rectangle(Shape):
    def area(self):
        print("Area of Rectangle = length * width")

class Triangle(Shape):
    def area(self):
        print("Area of Triangle = ½ * base * height")

# Usage
print("\n----- Method Overriding in Hierarchical Inheritance -----")
shapes = [Circle(), Rectangle(), Triangle()]
for shape in shapes:
    shape.area()


# ------------------------------------------------
# 7️⃣ Advantages of Hierarchical Inheritance
# ------------------------------------------------
# ✅ Code Reusability — Parent’s code is shared across multiple subclasses.
# ✅ Simplifies maintenance — Common functionality in one place.
# ✅ Logical structure — Models relationships where several entities share a base type.
# ✅ Extensibility — New subclasses can be added without modifying existing ones.


# ------------------------------------------------
# 8️⃣ Disadvantages of Hierarchical Inheritance
# ------------------------------------------------
# ⚠️ Tight coupling — All child classes depend on the parent class.
# ⚠️ If parent implementation changes, all child classes may be affected.
# ⚠️ Difficult to manage if the number of subclasses becomes large.
# ⚠️ Limited flexibility if subclasses have drastically different behaviors.


# ------------------------------------------------
# 9️⃣ Best Practices
# ------------------------------------------------
# - Keep the parent class focused on common attributes and methods only.
# - Avoid unnecessary or unrelated subclasses.
# - Override parent methods only when necessary.
# - Prefer composition if classes are not logically related.


# ================================================
# Summary:
# - Hierarchical Inheritance → Multiple child classes inherit from one parent.
# - Promotes reusability and shared functionality.
# - Child classes can have their own methods or override parent ones.
# - Use for “one-to-many” relationships in class design.
# ================================================
