# ================================================
# File: 06_Advantages_of_Polymorphism.py
# Topic: Advantages of Polymorphism in Python
# ================================================

"""
**Polymorphism** is one of the core principles of Object-Oriented Programming (OOP),
along with Encapsulation, Inheritance, and Abstraction.

It allows the same method name or operator to perform different tasks
based on the object or data type that calls it.

This flexibility provides several advantages that make OOP
more efficient, maintainable, and extensible.
"""

# ------------------------------------------------
# 1️⃣ Advantage 1: Code Reusability and Maintainability
# ------------------------------------------------
"""
Polymorphism allows you to write general code that works with multiple types of objects.
You don’t have to duplicate logic for each specific class — one common interface works for all.
"""

class Bird:
    def fly(self):
        print("Some birds can fly")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow can fly high")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly")

# Same function can call the same method for different types of birds
def show_flying_ability(bird):
    bird.fly()

birds = [Sparrow(), Penguin()]

for b in birds:
    show_flying_ability(b)

# Output:
# Sparrow can fly high
# Penguins cannot fly


# ------------------------------------------------
# 2️⃣ Advantage 2: Extensibility (Easy to Add New Features)
# ------------------------------------------------
"""
New classes can be added easily without changing the existing code structure.
You just have to follow the same interface (method name).
"""

class Crow(Bird):
    def fly(self):
        print("Crow flies with loud caws")

# Adding a new class does not require modifying 'show_flying_ability' or other logic
show_flying_ability(Crow())

# Output:
# Crow flies with loud caws


# ------------------------------------------------
# 3️⃣ Advantage 3: Cleaner and More Readable Code
# ------------------------------------------------
"""
Polymorphism helps eliminate complex conditional statements (like if-else or match)
that check for object types. The code becomes cleaner and easier to maintain.
"""

# Without Polymorphism (messy)
class Dog:
    def speak(self): print("Dog barks")

class Cat:
    def speak(self): print("Cat meows")

def speak_animal(animal_type):
    if animal_type == "dog":
        print("Dog barks")
    elif animal_type == "cat":
        print("Cat meows")
    else:
        print("Unknown animal")

# With Polymorphism (clean and extensible)
def animal_sound(animal):
    animal.speak()

dog = Dog()
cat = Cat()

animal_sound(dog)   # Output: Dog barks
animal_sound(cat)   # Output: Cat meows


# ------------------------------------------------
# 4️⃣ Advantage 4: Supports Dynamic (Runtime) Behavior
# ------------------------------------------------
"""
Polymorphism allows decisions to be made at **runtime**, not compile time.
This enables **runtime flexibility** — the program determines which method
to execute while running, based on the object type.
"""

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

shapes = [Circle(7), Rectangle(5, 8)]

for shape in shapes:
    print("Area:", shape.area())

# Output:
# Area: 153.86
# Area: 40


# ------------------------------------------------
# 5️⃣ Advantage 5: Flexibility in Code Design
# ------------------------------------------------
"""
Polymorphism allows classes to share a common interface but have
different internal implementations. This makes code modular and flexible.
"""

class Payment:
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal")

def make_payment(payment_method, amount):
    payment_method.pay(amount)

# Works for any type of payment class that follows the 'pay' interface
make_payment(CreditCardPayment(), 500)
make_payment(PayPalPayment(), 750)

# Output:
# Paid $500 using Credit Card
# Paid $750 using PayPal


# ------------------------------------------------
# 6️⃣ Advantage 6: Improves Scalability and Team Collaboration
# ------------------------------------------------
"""
In large projects, polymorphism enables teams to work independently
on different modules. For example, each developer can implement a subclass
without affecting others, as long as they follow the same interface.
"""

class Report:
    def generate(self):
        pass

class PDFReport(Report):
    def generate(self):
        print("Generating PDF report...")

class ExcelReport(Report):
    def generate(self):
        print("Generating Excel report...")

# Developers can create new report types without touching existing code
reports = [PDFReport(), ExcelReport()]

for report in reports:
    report.generate()

# Output:
# Generating PDF report...
# Generating Excel report...


# ------------------------------------------------
# 7️⃣ Advantage 7: Encourages Interface Design and Abstraction
# ------------------------------------------------
"""
Polymorphism enforces a structure where classes implement common interfaces.
This promotes **abstraction** — the user focuses on *what* an object does,
not *how* it does it.
"""

from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending Email: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")

def send_notification(notification, message):
    notification.send(message)

send_notification(EmailNotification(), "Welcome to our service!")
send_notification(SMSNotification(), "Your OTP is 1234")

# Output:
# Sending Email: Welcome to our service!
# Sending SMS: Your OTP is 1234


# ------------------------------------------------
# 8️⃣ Summary of Advantages
# ------------------------------------------------
"""
| Advantage No. | Description                                           |
|----------------|------------------------------------------------------|
| 1. Code Reusability | Write common code for multiple object types.     |
| 2. Extensibility    | Add new classes without changing existing code.  |
| 3. Clean Code       | Avoids long conditional statements.              |
| 4. Dynamic Behavior | Decisions are made at runtime.                   |
| 5. Flexibility      | Same interface, different implementations.       |
| 6. Scalability      | Suitable for large projects and teams.           |
| 7. Abstraction      | Hides implementation details.                    |
"""


# ================================================
# Summary:
# - Polymorphism simplifies code and enhances flexibility.
# - Reduces duplication, encourages reusability, and improves scalability.
# - Makes large-scale systems modular and maintainable.
# - Enables dynamic behavior and consistent interface design.
# ================================================
