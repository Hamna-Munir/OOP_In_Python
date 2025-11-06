# ================================================
# File: 05_Real_World_Examples_of_Polymorphism.py
# Topic: Real-World Examples of Polymorphism
# ================================================

"""
In Object-Oriented Programming, **Polymorphism** allows the same method name
to perform different actions depending on the object that calls it.

Real-world software systems often use polymorphism to build flexible,
scalable, and maintainable code structures.

Below are several practical examples showing how polymorphism works
in real-life applications.
"""

# ------------------------------------------------
# 1️⃣ Example: Polymorphism in a Payment System
# ------------------------------------------------
"""
In a payment processing system, different payment methods (CreditCard, PayPal, BankTransfer)
can implement a common interface called 'pay()'. The actual behavior depends
on which object is used.
"""

class Payment:
    def pay(self, amount):
        raise NotImplementedError("Subclass must implement abstract method")

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Processing PayPal payment of ${amount}")

class BankTransferPayment(Payment):
    def pay(self, amount):
        print(f"Processing bank transfer payment of ${amount}")

# Polymorphic behavior
payments = [
    CreditCardPayment(),
    PayPalPayment(),
    BankTransferPayment()
]

for method in payments:
    method.pay(500)

# Output:
# Processing credit card payment of $500
# Processing PayPal payment of $500
# Processing bank transfer payment of $500


# ------------------------------------------------
# 2️⃣ Example: Polymorphism in a Vehicle System
# ------------------------------------------------
"""
Vehicles share common functionality, but each vehicle type has a unique way
of implementing certain features such as start() or fuel_type().
"""

class Vehicle:
    def start(self):
        print("Starting the vehicle...")

class Car(Vehicle):
    def start(self):
        print("Car engine started with key ignition.")

class Bike(Vehicle):
    def start(self):
        print("Bike started with self-start button.")

class ElectricScooter(Vehicle):
    def start(self):
        print("Electric scooter powered on silently.")

# Using Polymorphism
vehicles = [Car(), Bike(), ElectricScooter()]

for v in vehicles:
    v.start()

# Output:
# Car engine started with key ignition.
# Bike started with self-start button.
# Electric scooter powered on silently.


# ------------------------------------------------
# 3️⃣ Example: Polymorphism in File Handling
# ------------------------------------------------
"""
Polymorphism can be used when dealing with different types of files
(e.g., TextFile, CSVFile, JSONFile) — all of which share the same interface
for reading data but have different internal implementations.
"""

class File:
    def read(self):
        raise NotImplementedError("Subclasses must override read()")

class TextFile(File):
    def read(self):
        print("Reading data from a text file...")

class CSVFile(File):
    def read(self):
        print("Reading data from a CSV file...")

class JSONFile(File):
    def read(self):
        print("Reading data from a JSON file...")

files = [TextFile(), CSVFile(), JSONFile()]

for file in files:
    file.read()

# Output:
# Reading data from a text file...
# Reading data from a CSV file...
# Reading data from a JSON file...


# ------------------------------------------------
# 4️⃣ Example: Polymorphism in a Notification System
# ------------------------------------------------
"""
Different notification types (Email, SMS, Push Notification)
can share a common interface `send_notification()`.
Each class defines how that notification is sent.
"""

class Notification:
    def send_notification(self, message):
        raise NotImplementedError("Subclasses must override send_notification()")

class EmailNotification(Notification):
    def send_notification(self, message):
        print(f"Sending Email: {message}")

class SMSNotification(Notification):
    def send_notification(self, message):
        print(f"Sending SMS: {message}")

class PushNotification(Notification):
    def send_notification(self, message):
        print(f"Sending Push Notification: {message}")

notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for n in notifications:
    n.send_notification("Your order has been shipped!")

# Output:
# Sending Email: Your order has been shipped!
# Sending SMS: Your order has been shipped!
# Sending Push Notification: Your order has been shipped!


# ------------------------------------------------
# 5️⃣ Example: Polymorphism in a Media Player
# ------------------------------------------------
"""
A media player application can play multiple types of media.
Each media type (Audio, Video, Streaming) can have its own implementation
of the play() method.
"""

class Media:
    def play(self):
        raise NotImplementedError("Subclasses must implement play()")

class Audio(Media):
    def play(self):
        print("Playing audio file...")

class Video(Media):
    def play(self):
        print("Playing video file...")

class Streaming(Media):
    def play(self):
        print("Streaming media online...")

media_files = [Audio(), Video(), Streaming()]

for m in media_files:
    m.play()

# Output:
# Playing audio file...
# Playing video file...
# Streaming media online...


# ------------------------------------------------
# 6️⃣ Example: Polymorphism with Employee Roles
# ------------------------------------------------
"""
In a company system, each employee type performs a different role,
but all share a common interface — the work() method.
"""

class Employee:
    def work(self):
        raise NotImplementedError("Subclass must implement work()")

class Developer(Employee):
    def work(self):
        print("Developer is writing code.")

class Designer(Employee):
    def work(self):
        print("Designer is creating visuals.")

class Tester(Employee):
    def work(self):
        print("Tester is testing software.")

employees = [Developer(), Designer(), Tester()]

for emp in employees:
    emp.work()

# Output:
# Developer is writing code.
# Designer is creating visuals.
# Tester is testing software.


# ------------------------------------------------
# 7️⃣ Advantages of Using Polymorphism in Real Projects
# ------------------------------------------------
"""
✔ Reduces code duplication by defining a common interface.
✔ Makes the code more flexible and scalable.
✔ Enables easy maintenance and extension — new subclasses can be added without modifying existing code.
✔ Improves readability and design through abstraction and generalization.
✔ Allows systems to handle objects of different classes in a uniform way.
"""


# ------------------------------------------------
# 8️⃣ Summary Table
# ------------------------------------------------
"""
| Real-World Scenario     | Common Interface     | Example Classes                    |
|--------------------------|----------------------|------------------------------------|
| Payment System           | pay()                | CreditCardPayment, PayPalPayment   |
| Vehicle System           | start()              | Car, Bike, ElectricScooter         |
| File Handling            | read()               | TextFile, CSVFile, JSONFile        |
| Notification System      | send_notification()  | Email, SMS, PushNotification       |
| Media Player             | play()               | Audio, Video, Streaming            |
| Employee Management      | work()               | Developer, Designer, Tester        |
"""


# ================================================
# Summary:
# - Polymorphism enables one interface to represent many forms.
# - It is widely used in real-world applications such as payments,
#   notifications, file handling, and employee management.
# - Enhances flexibility, maintainability, and scalability in software design.
# ================================================
