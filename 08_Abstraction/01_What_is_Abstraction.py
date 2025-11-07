# ===============================================================
# File: 01_What_is_Abstraction.py
# Topic: Introduction to Abstraction in Python (OOP)
# ===============================================================

"""
In Object-Oriented Programming (OOP), **Abstraction** is the process of hiding 
unnecessary implementation details from the user and showing only the 
essential features or functionalities.

It helps reduce complexity and increases code reusability and security.

For example:
When we use a smartphone, we simply press a button to make a call.
We do not need to know how the internal circuits work — that’s **abstraction**.
"""


# ---------------------------------------------------------------
# 1️⃣ Concept of Abstraction
# ---------------------------------------------------------------

"""
Abstraction allows developers to design programs by focusing on what an 
object does instead of how it does it.

- It hides complex logic and shows only necessary methods.
- It provides a clear separation between the **interface** and the **implementation**.
- It helps in building cleaner, more maintainable code.
"""


# ---------------------------------------------------------------
# 2️⃣ Implementing Abstraction in Python
# ---------------------------------------------------------------

"""
Python does not have built-in abstract classes like Java or C++, 
but it provides the `abc` module (**Abstract Base Class**) that allows
you to define abstract classes and abstract methods.

- An **abstract class** cannot be instantiated directly.
- It may contain one or more **abstract methods** (declared but not implemented).
- Subclasses must override and implement all abstract methods.
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------------
# 3️⃣ Example: Basic Abstraction using Abstract Class
# ---------------------------------------------------------------

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


# Subclass must implement all abstract methods
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started...")

    def stop_engine(self):
        print("Car engine stopped.")


# Usage
car = Car()
car.start_engine()   # Output: Car engine started...
car.stop_engine()    # Output: Car engine stopped.


# ---------------------------------------------------------------
# 4️⃣ Abstraction Hides Implementation Details
# ---------------------------------------------------------------

"""
The user interacts only with the exposed methods (`start_engine`, `stop_engine`) 
and is unaware of how these functions are implemented internally.

This separation ensures that changes inside the class do not affect 
external code that uses it.
"""


# ---------------------------------------------------------------
# 5️⃣ Real-World Example of Abstraction
# ---------------------------------------------------------------

class Payment(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass


class CreditCardPayment(Payment):
    def make_payment(self, amount):
        print(f"Processing credit card payment of ${amount}...")


class PayPalPayment(Payment):
    def make_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}...")


# Usage
payment1 = CreditCardPayment()
payment2 = PayPalPayment()

payment1.make_payment(1000)
payment2.make_payment(500)

"""
Output:
Processing credit card payment of $1000...
Processing PayPal payment of $500...
"""


# ---------------------------------------------------------------
# 6️⃣ Advantages of Abstraction
# ---------------------------------------------------------------

"""
✅ Hides internal implementation details.
✅ Reduces complexity and improves readability.
✅ Increases security by exposing only essential features.
✅ Makes maintenance easier and code more modular.
✅ Encourages reusability through abstract base classes.
"""


# ---------------------------------------------------------------
# 7️⃣ Key Points
# ---------------------------------------------------------------

"""
- Abstraction is implemented using **Abstract Classes** and **Abstract Methods**.
- Abstract classes are defined using the `ABC` class from the `abc` module.
- The `@abstractmethod` decorator marks methods that must be implemented by subclasses.
- Objects of abstract classes cannot be created directly.
- Abstraction focuses on *what to do*, not *how to do it*.
"""


# ===============================================================
# Summary:
# Abstraction → Hiding implementation details and showing only functionality.
# ===============================================================
