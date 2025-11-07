# ===============================================================
# File: 02_Abstract_Base_Class_ABC_Module.py
# Topic: Abstract Base Classes (ABC Module) in Python
# ===============================================================

"""
In Python, **Abstract Base Classes (ABC)** provide a blueprint for other classes.

They are defined in the built-in `abc` (Abstract Base Class) module and 
are used to enforce that certain methods must be implemented in child classes.

Using ABCs helps in designing structured, consistent, and extendable OOP systems.
"""


# ---------------------------------------------------------------
# 1️⃣ Importing the ABC Module
# ---------------------------------------------------------------

"""
The `abc` module provides two key components:
- **ABC**: A helper class used to define abstract base classes.
- **@abstractmethod**: A decorator used to mark methods as abstract.
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------------
# 2️⃣ Defining an Abstract Base Class
# ---------------------------------------------------------------

"""
To define an abstract base class:
1. Inherit from `ABC`.
2. Use `@abstractmethod` for methods that must be implemented by subclasses.
"""

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter of the shape"""
        pass


# ---------------------------------------------------------------
# 3️⃣ Attempting to Instantiate an Abstract Class
# ---------------------------------------------------------------

"""
You **cannot** create an object of an abstract class directly.
The following will raise an error:

    s = Shape()  ❌
    TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter
"""

# s = Shape()  # Uncommenting this line will raise an error


# ---------------------------------------------------------------
# 4️⃣ Implementing Abstract Methods in Subclasses
# ---------------------------------------------------------------

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.1416 * self.radius


# Usage
rect = Rectangle(5, 3)
circle = Circle(4)

print("Rectangle Area:", rect.area())          # Output: 15
print("Rectangle Perimeter:", rect.perimeter())  # Output: 16

print("Circle Area:", circle.area())            # Output: 50.2656
print("Circle Perimeter:", circle.perimeter())  # Output: 25.1328


# ---------------------------------------------------------------
# 5️⃣ Abstract Class with Both Abstract and Concrete Methods
# ---------------------------------------------------------------

"""
An abstract class can also contain **concrete methods** (normal methods with implementation)
along with abstract ones. This is useful for providing shared behavior.
"""

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def sleep(self):
        print("All animals need sleep.")


class Dog(Animal):
    def make_sound(self):
        print("Woof Woof!")


# Usage
dog = Dog()
dog.make_sound()   # Output: Woof Woof!
dog.sleep()        # Output: All animals need sleep.


# ---------------------------------------------------------------
# 6️⃣ Why Use Abstract Base Classes?
# ---------------------------------------------------------------

"""
Abstract Base Classes are essential when:
- You want to enforce a common interface for all derived classes.
- You want to prevent direct instantiation of incomplete (base) classes.
- You need polymorphic behavior across multiple subclasses.

They are widely used in frameworks, libraries, and large-scale systems
to ensure a predictable structure and consistency.
"""


# ---------------------------------------------------------------
# 7️⃣ Real-World Example of ABC
# ---------------------------------------------------------------

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

    def payment_info(self):
        print("Processing secure payments through multiple gateways.")


class PayPal(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Paid ${amount} using PayPal.")


class Stripe(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Paid ${amount} using Stripe.")


# Usage
paypal = PayPal()
stripe = Stripe()

paypal.process_payment(1200)
stripe.process_payment(850)

paypal.payment_info()

"""
Output:
Paid $1200 using PayPal.
Paid $850 using Stripe.
Processing secure payments through multiple gateways.
"""


# ---------------------------------------------------------------
# 8️⃣ Key Points
# ---------------------------------------------------------------

"""
- Abstract classes define a common structure for subclasses.
- Use `ABC` and `@abstractmethod` from the `abc` module.
- Abstract classes **cannot be instantiated directly**.
- Subclasses must **override all abstract methods**.
- Abstract classes can also include normal (concrete) methods.
- They promote **code consistency** and **enforce design rules**.
"""


# ===============================================================
# Summary:
# Abstract Base Class (ABC) → Defines a blueprint that forces subclasses 
# to implement specific methods.
# ===============================================================
