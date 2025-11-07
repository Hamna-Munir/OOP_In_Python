# ===============================================================
# File: 05_Real_World_Examples_of_Abstraction.py
# Topic: Real-World Examples of Abstraction in Python (OOP)
# ===============================================================

"""
In Object-Oriented Programming (OOP), **Abstraction** allows us to
hide complex implementation details and expose only the **necessary functionality**.

In real-world software, abstraction is used everywhere — in APIs, 
frameworks, libraries, and operating systems.

This file demonstrates how abstraction is applied to practical, 
real-world problems in software design.
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------------
# 1️⃣ Real-World Example 1: Payment Processing System
# ---------------------------------------------------------------

"""
In real-world applications, multiple payment methods (Credit Card, PayPal, etc.)
are provided to users. However, each has a different implementation.

Using abstraction, we can define a common interface for all payment types.
"""

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


class BankTransferPayment(Payment):
    def make_payment(self, amount):
        print(f"Processing bank transfer of ${amount}...")


# Usage
print("\n--- Real-World Example 1: Payment Processing ---")
payments = [
    CreditCardPayment(),
    PayPalPayment(),
    BankTransferPayment()
]

for method in payments:
    method.make_payment(500)

"""
Output:
Processing credit card payment of $500...
Processing PayPal payment of $500...
Processing bank transfer of $500...
"""


# ---------------------------------------------------------------
# 2️⃣ Real-World Example 2: Vehicle Control System
# ---------------------------------------------------------------

"""
A vehicle may be a car, bike, or airplane. Each has its own mechanism to start and stop,
but from a user’s perspective, they all perform the same operation: start and stop.

We can use abstraction to hide the underlying details and provide a simple interface.
"""

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car engine started...")

    def stop(self):
        print("Car stopped.")


class Airplane(Vehicle):
    def start(self):
        print("Airplane engines activated, ready for takeoff...")

    def stop(self):
        print("Airplane engines shut down.")


# Usage
print("\n--- Real-World Example 2: Vehicle Control ---")
vehicles = [Car(), Airplane()]
for v in vehicles:
    v.start()
    v.stop()


# ---------------------------------------------------------------
# 3️⃣ Real-World Example 3: Data Storage System
# ---------------------------------------------------------------

"""
Applications often save data in different formats such as 
databases, files, or cloud storage. Each has a different implementation.

Abstraction lets developers work with a single interface
without worrying about where or how data is stored.
"""

class DataStorage(ABC):
    @abstractmethod
    def save_data(self, data):
        pass


class LocalDatabase(DataStorage):
    def save_data(self, data):
        print(f"Saving '{data}' to local database...")


class CloudStorage(DataStorage):
    def save_data(self, data):
        print(f"Uploading '{data}' to cloud storage...")


class FileStorage(DataStorage):
    def save_data(self, data):
        print(f"Writing '{data}' to local file...")


# Usage
print("\n--- Real-World Example 3: Data Storage ---")
storages = [LocalDatabase(), CloudStorage(), FileStorage()]

for s in storages:
    s.save_data("UserProfileData")


# ---------------------------------------------------------------
# 4️⃣ Real-World Example 4: Notification System
# ---------------------------------------------------------------

"""
When sending notifications, the delivery mechanism (Email, SMS, Push Notification)
may differ, but the interface remains the same — `send_notification()`.

This abstraction helps in building scalable and easily maintainable systems.
"""

class Notification(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass


class EmailNotification(Notification):
    def send_notification(self, message):
        print(f"Sending EMAIL: {message}")


class SMSNotification(Notification):
    def send_notification(self, message):
        print(f"Sending SMS: {message}")


class PushNotification(Notification):
    def send_notification(self, message):
        print(f"Sending PUSH notification: {message}")


# Usage
print("\n--- Real-World Example 4: Notification System ---")
notifiers = [EmailNotification(), SMSNotification(), PushNotification()]

for n in notifiers:
    n.send_notification("System update available!")


# ---------------------------------------------------------------
# 5️⃣ Real-World Example 5: Shape Area Calculator
# ---------------------------------------------------------------

"""
This is one of the most common abstraction examples in OOP.

We define a base class `Shape` with abstract methods for `area()` and `perimeter()`.
Different shapes implement these methods according to their formulas.
"""

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


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
print("\n--- Real-World Example 5: Shape Area Calculator ---")
rect = Rectangle(5, 3)
circle = Circle(4)

print(f"Rectangle Area: {rect.area()} | Perimeter: {rect.perimeter()}")
print(f"Circle Area: {circle.area()} | Perimeter: {circle.perimeter()}")


# ---------------------------------------------------------------
# 6️⃣ Benefits of Abstraction in Real-World Applications
# ---------------------------------------------------------------

"""
✅ Simplifies complex systems by exposing only necessary details.
✅ Improves flexibility — changes in implementation don’t affect user interaction.
✅ Enhances code reusability through common interfaces.
✅ Encourages modular and maintainable design.
✅ Protects sensitive logic from direct access or modification.
"""


# ---------------------------------------------------------------
# 7️⃣ Key Takeaways
# ---------------------------------------------------------------

"""
- Abstraction hides implementation details and exposes only functionality.
- Achieved in Python using **Abstract Base Classes (ABC)** and **@abstractmethod**.
- Commonly used in:
    → Payment gateways
    → Data access layers
    → Notification systems
    → Device controllers
    → Web APIs and frameworks
- Allows you to change “how it works” without changing “how it’s used”.
"""


# ===============================================================
# Summary:
# Real-World Abstraction → Simplifies complex systems by defining 
# interfaces that focus on what actions can be done, not how they are done.
# ===============================================================
