# ================================================
# File: 04_Polymorphism_in_Inheritance.py
# Topic: Polymorphism in Inheritance
# ================================================

"""
In Object-Oriented Programming (OOP), **Polymorphism** means "many forms."
It allows the same method name to behave differently based on the object 
that calls it.

When combined with **Inheritance**, polymorphism allows subclasses to provide 
their own version of a method defined in the parent class — this is known as 
**runtime polymorphism** or **method overriding**.

Polymorphism helps achieve flexibility and reusability in code, as the same
interface can be used for different underlying forms (objects).
"""

# ------------------------------------------------
# 1️⃣ Example: Polymorphism through Method Overriding
# ------------------------------------------------

class Animal:
    def speak(self):
        print("Animals make sounds")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

class Cow(Animal):
    def speak(self):
        print("Cow moos")

# Each subclass has its own implementation of 'speak'
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.speak()

# Output:
# Dog barks
# Cat meows
# Cow moos


# ------------------------------------------------
# 2️⃣ Polymorphism in Action — Common Interface, Different Behavior
# ------------------------------------------------
"""
All classes share a common interface (`speak()`), but each one provides
a unique implementation. This demonstrates polymorphism — one method name,
many behaviors.
"""

class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most birds can fly, but some cannot.")

class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly high.")

class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")

# Usage
bird1 = Bird()
bird2 = Sparrow()
bird3 = Ostrich()

bird1.intro()
bird1.flight()

bird2.intro()
bird2.flight()

bird3.intro()
bird3.flight()

# Output:
# There are many types of birds.
# Most birds can fly, but some cannot.
# There are many types of birds.
# Sparrows can fly high.
# There are many types of birds.
# Ostriches cannot fly.


# ------------------------------------------------
# 3️⃣ Polymorphism Using a Common Function
# ------------------------------------------------
"""
We can also use a single function that takes different class objects
and calls their specific implementation dynamically.
"""

def animal_sound(animal):
    animal.speak()

# Works for any class that defines a speak() method
dog = Dog()
cat = Cat()

animal_sound(dog)  # Output: Dog barks
animal_sound(cat)  # Output: Cat meows


# ------------------------------------------------
# 4️⃣ Example: Polymorphism with Built-in Functions
# ------------------------------------------------
"""
Many Python built-in functions also exhibit polymorphism.

For example:
- The `len()` function can be used with strings, lists, tuples, etc.
- The same function behaves differently based on the type of object.
"""

print(len("Hamna"))          # Output: 5  (Length of string)
print(len([10, 20, 30, 40])) # Output: 4  (Length of list)
print(len((1, 2)))           # Output: 2  (Length of tuple)


# ------------------------------------------------
# 5️⃣ Example: Real-World Polymorphism in Inheritance
# ------------------------------------------------

class Employee:
    def role(self):
        print("General Employee Role")

class Developer(Employee):
    def role(self):
        print("Writes and maintains code")

class Designer(Employee):
    def role(self):
        print("Designs UI/UX interfaces")

class Manager(Employee):
    def role(self):
        print("Manages teams and projects")

# Using Polymorphism
employees = [Developer(), Designer(), Manager()]

for emp in employees:
    emp.role()

# Output:
# Writes and maintains code
# Designs UI/UX interfaces
# Manages teams and projects


# ------------------------------------------------
# 6️⃣ Polymorphism with Abstract Classes (Advanced Example)
# ------------------------------------------------
"""
Polymorphism can also be implemented using **abstract classes**.
Abstract classes define a common interface that subclasses must implement.
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method to be implemented by subclasses

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Usage
shapes = [Rectangle(5, 10), Circle(7)]

for shape in shapes:
    print("Area:", shape.area())

# Output:
# Area: 50
# Area: 153.86


# ------------------------------------------------
# 7️⃣ Key Points of Polymorphism in Inheritance
# ------------------------------------------------
"""
✔ The same method name can have different implementations in derived classes.
✔ It allows dynamic (runtime) method resolution — the correct method is chosen at runtime.
✔ It increases flexibility, reusability, and maintainability of code.
✔ Polymorphism is achieved mainly through **method overriding**.
✔ Abstract classes help enforce a common interface across subclasses.
"""


# ------------------------------------------------
# 8️⃣ Polymorphism Summary Table
# ------------------------------------------------
"""
| Feature                         | Description                                         |
|----------------------------------|-----------------------------------------------------|
| Concept                          | One interface, many forms                           |
| Achieved through                 | Method Overriding in Inheritance                    |
| Type                             | Runtime Polymorphism                                |
| Common use case                  | Calling the same method on objects of different classes |
| Example                          | animal.speak() works for Dog, Cat, Cow, etc.       |
"""


# ================================================
# Summary:
# - Polymorphism allows one method name to perform different tasks.
# - It is achieved through inheritance and method overriding.
# - Enables writing flexible and extensible OOP code.
# - Abstract classes can define common behavior for all subclasses.
# ================================================
