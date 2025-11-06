# ================================================
# File: 01_What_is_Polymorphism.py
# Topic: Introduction to Polymorphism in Python (OOP)
# ================================================

"""
In Object-Oriented Programming (OOP), **Polymorphism** means "many forms."

It allows objects of different classes to be treated as objects of a common superclass.  
In simple terms, **the same function or method name can perform different actions**
based on the object that calls it.

Polymorphism increases **code flexibility**, **reusability**, and supports the 
**Open/Closed Principle** — where code can be extended without modifying existing logic.
"""

# ------------------------------------------------
# 1️⃣ Understanding the Concept of Polymorphism
# ------------------------------------------------
# Example: The "+" operator behaves differently for numbers and strings.

print("----- Example 1: Built-in Polymorphism -----")
print(10 + 5)          # Integer addition → Output: 15
print("Hamna " + "Ali")  # String concatenation → Output: "Hamna Ali"

# Here, the same operator "+" is performing two different operations
# depending on the type of operands (int vs str).


# ------------------------------------------------
# 2️⃣ Polymorphism with Functions
# ------------------------------------------------
# A function can take arguments of different types and behave accordingly.

print("\n----- Example 2: Function Polymorphism -----")

def multiply(a, b):
    return a * b

print(multiply(3, 4))         # Integer multiplication → Output: 12
print(multiply("Hi ", 3))     # String repetition → Output: Hi Hi Hi


# ------------------------------------------------
# 3️⃣ Polymorphism with Classes and Methods
# ------------------------------------------------
# Different classes can have methods with the same name but different implementations.

print("\n----- Example 3: Class Method Polymorphism -----")

class Dog:
    def sound(self):
        return "Bark!"

class Cat:
    def sound(self):
        return "Meow!"

class Cow:
    def sound(self):
        return "Moo!"

# All objects have a `sound()` method, but each behaves differently.
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(f"{animal.__class__.__name__} sound:", animal.sound())


# ------------------------------------------------
# 4️⃣ Polymorphism using Inheritance
# ------------------------------------------------
# Polymorphism is often used through **method overriding** in inheritance.

print("\n----- Example 4: Polymorphism with Inheritance -----")

class Bird:
    def intro(self):
        print("There are many types of birds.")
    def flight(self):
        print("Most birds can fly, but some cannot.")

class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly high in the sky.")

class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")

bird1 = Sparrow()
bird2 = Ostrich()

bird1.intro()
bird1.flight()

bird2.intro()
bird2.flight()


# ------------------------------------------------
# 5️⃣ Polymorphism with a Common Interface
# ------------------------------------------------
# Suppose we have unrelated classes that share a method name.

print("\n----- Example 5: Common Interface Example -----")

class Human:
    def speak(self):
        print("Hello! I am a human.")

class Robot:
    def speak(self):
        print("Beep boop! I am a robot.")

class Alien:
    def speak(self):
        print("Greetings from outer space!")

# All classes implement 'speak()', but differently.
beings = [Human(), Robot(), Alien()]

for being in beings:
    being.speak()


# ------------------------------------------------
# 6️⃣ Polymorphism with Abstract Base Classes
# ------------------------------------------------
# In professional code, polymorphism is often implemented using abstract classes
# to enforce that all subclasses define certain methods.

print("\n----- Example 6: Polymorphism using Abstract Base Class -----")

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(f"{shape.__class__.__name__} area:", shape.area())


# ------------------------------------------------
# 7️⃣ Real-World Analogy
# ------------------------------------------------
"""
Think of a `make_sound()` method:
- A car makes a “Vroom” sound.
- A train makes a “Choo Choo” sound.
- A plane makes a “Whooosh” sound.

The action (make_sound) is the same, but behavior differs for each object.
This is the essence of polymorphism.
"""


# ------------------------------------------------
# 8️⃣ Benefits of Polymorphism
# ------------------------------------------------
"""
✅ Increases code flexibility and scalability.
✅ Simplifies code — one interface can work for multiple types.
✅ Encourages loose coupling between classes.
✅ Supports open/closed principle — extend without modifying existing code.
"""


# ================================================
# Summary:
# - Polymorphism means "many forms" — same interface, different behaviors.
# - Achieved through method overriding, common interfaces, or abstract classes.
# - Allows different classes to implement the same method uniquely.
# - Enhances flexibility, maintainability, and scalability of OOP systems.
# ================================================
