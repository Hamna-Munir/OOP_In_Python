# ===============================================================
# File: 04_Interface_in_Python.py
# Topic: Interface in Python (Using Abstraction and ABC)
# ===============================================================

"""
In Object-Oriented Programming (OOP), an **Interface** defines a 
**contract** or a **blueprint** that classes must follow.

It specifies *what* a class should do, but **not how** to do it.

In many programming languages (like Java or C#), interfaces are built-in 
language constructs. However, Python does not have a direct `interface` keyword.

Instead, Python uses **Abstract Base Classes (ABC)** from the `abc` module 
to define interfaces.
"""


# ---------------------------------------------------------------
# 1️⃣ What is an Interface?
# ---------------------------------------------------------------

"""
An Interface:
- Declares a set of methods that must be implemented in any subclass.
- Does not contain any actual implementation (only method definitions).
- Helps achieve **abstraction** and **multiple inheritance**.
- Ensures a consistent structure across multiple unrelated classes.

Think of it as a **contract**: if a class implements an interface, 
it must provide definitions for all the methods declared in it.
"""

# ---------------------------------------------------------------
# 2️⃣ Creating an Interface using Abstract Base Class (ABC)
# ---------------------------------------------------------------

from abc import ABC, abstractmethod

# Defining an Interface
class ShapeInterface(ABC):
    @abstractmethod
    def area(self):
        """Calculate area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter of the shape"""
        pass


# Implementing the Interface in Subclasses
class Rectangle(ShapeInterface):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(ShapeInterface):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.1416 * self.radius


# Usage
print("\n--- Shape Interface Example ---")
rect = Rectangle(5, 3)
circle = Circle(4)

print("Rectangle Area:", rect.area())
print("Rectangle Perimeter:", rect.perimeter())
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())


# ---------------------------------------------------------------
# 3️⃣ Interface Enforces Implementation
# ---------------------------------------------------------------

"""
If a class inherits from an interface but does not implement 
all abstract methods, Python raises an error.
"""

class IncompleteShape(ShapeInterface):
    def area(self):
        return 10
    # Missing perimeter() method → This will cause an error if instantiated

# incomplete = IncompleteShape()  # ❌ TypeError: Can't instantiate abstract class


# ---------------------------------------------------------------
# 4️⃣ Interface with Multiple Implementations (Polymorphism)
# ---------------------------------------------------------------

"""
Interfaces allow different classes to have the same set of methods 
but different implementations.

This enables **polymorphism** — you can use objects of different classes 
interchangeably as long as they follow the same interface.
"""

def shape_details(shape: ShapeInterface):
    print(f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")


print("\n--- Using Interface with Polymorphism ---")
shape_details(rect)
shape_details(circle)


# ---------------------------------------------------------------
# 5️⃣ Real-World Example: Payment System Interface
# ---------------------------------------------------------------

class PaymentInterface(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass


class CreditCardPayment(PaymentInterface):
    def make_payment(self, amount):
        print(f"Paid ${amount} using Credit Card.")


class PayPalPayment(PaymentInterface):
    def make_payment(self, amount):
        print(f"Paid ${amount} using PayPal.")


class BankTransferPayment(PaymentInterface):
    def make_payment(self, amount):
        print(f"Paid ${amount} using Bank Transfer.")


print("\n--- Payment System Interface Example ---")
payments = [
    CreditCardPayment(),
    PayPalPayment(),
    BankTransferPayment()
]

for method in payments:
    method.make_payment(500)


# ---------------------------------------------------------------
# 6️⃣ Interface vs Abstract Class
# ---------------------------------------------------------------

"""
Although both **interfaces** and **abstract classes** support abstraction, 
there are key differences:

| Feature | Abstract Class | Interface |
|----------|----------------|-----------|
| Purpose | Defines base behavior with optional implementations | Defines only method contracts |
| Methods | Can have both abstract and concrete methods | Usually has only abstract methods |
| Variables | Can have instance variables | Typically no instance variables |
| Inheritance | Single inheritance only | Can be implemented by multiple classes |
| Example | Class hierarchy (Animal → Dog, Cat) | Common behavior (Payment system) |

Python’s Abstract Base Classes (ABC) can serve as both, 
depending on how they are used.
"""


# ---------------------------------------------------------------
# 7️⃣ Multiple Interfaces Example
# ---------------------------------------------------------------

class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass


class Saveable(ABC):
    @abstractmethod
    def save_data(self):
        pass


# A class implementing multiple interfaces
class Report(Printable, Saveable):
    def print_info(self):
        print("Printing report details...")

    def save_data(self):
        print("Saving report to database.")


print("\n--- Multiple Interfaces Example ---")
r = Report()
r.print_info()
r.save_data()


# ---------------------------------------------------------------
# 8️⃣ Advantages of Using Interfaces
# ---------------------------------------------------------------

"""
✅ Promotes consistency across unrelated classes.
✅ Enables loose coupling — implementation can change without affecting other code.
✅ Supports multiple inheritance in Python.
✅ Improves modularity and scalability of large systems.
✅ Allows polymorphism — different classes can be used interchangeably.
"""


# ---------------------------------------------------------------
# 9️⃣ Key Points
# ---------------------------------------------------------------

"""
- Interfaces in Python are implemented using **Abstract Base Classes (ABC)**.
- They define **method signatures** without implementation.
- Subclasses must override all abstract methods to avoid errors.
- Interfaces promote **code reusability** and **flexibility**.
- A class can implement multiple interfaces in Python.
"""


# ===============================================================
# Summary:
# Interface → Defines a blueprint (method contracts) that must be 
# implemented by subclasses. Ensures consistency and enables polymorphism.
# ===============================================================
