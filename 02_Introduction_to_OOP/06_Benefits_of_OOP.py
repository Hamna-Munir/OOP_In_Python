# ================================================
# File: 06_Benefits_of_OOP.py
# Topic: Benefits of Object-Oriented Programming (OOP)
# ================================================

"""
Object-Oriented Programming (OOP) offers several advantages that make code
more organized, reusable, and easier to maintain. Below are the key benefits
of using OOP in Python.
"""

# 1️⃣ Code Reusability
# --------------------
# - Through inheritance, classes can reuse code from parent classes.
# - This reduces duplication and improves maintainability.
# - Example:
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand:", self.brand)

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show_info(self):
        print(f"{self.brand} - {self.model}")

# Usage
car = Car("Toyota", "Corolla")
car.show_info()  # Output: Toyota - Corolla


# 2️⃣ Data Encapsulation
# ----------------------
# - Data (attributes) and functions (methods) are bundled into a single unit (class).
# - Access to sensitive data can be restricted using private/protected attributes.
# - Example:
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# Usage
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500


# 3️⃣ Code Maintainability
# -------------------------
# - Changes made in one class do not affect other parts of the program.
# - Easier to debug and update because of modular structure.


# 4️⃣ Abstraction
# ----------------
# - Hides complex implementation details and exposes only necessary parts.
# - Example:
class CoffeeMachine:
    def __init__(self):
        pass

    def make_coffee(self):
        self.__boil_water()
        self.__brew_coffee()
        self.__pour_into_cup()
        print("☕ Coffee is ready!")

    def __boil_water(self):
        print("Boiling water...")

    def __brew_coffee(self):
        print("Brewing coffee...")

    def __pour_into_cup(self):
        print("Pouring into cup...")

# Usage
machine = CoffeeMachine()
machine.make_coffee()


# 5️⃣ Polymorphism
# ----------------
# - Allows objects of different classes to be treated as objects of a common base class.
# - Makes code more flexible and extensible.
# - Example:
class Bird:
    def speak(self):
        print("Some sound")

class Sparrow(Bird):
    def speak(self):
        print("Chirp")

class Parrot(Bird):
    def speak(self):
        print("Squawk")

# Usage
for bird in [Sparrow(), Parrot()]:
    bird.speak()


# 6️⃣ Inheritance and Extensibility
# ---------------------------------
# - New features can be added without modifying existing code.
# - Encourages code evolution and scalability.


# 7️⃣ Real-World Modeling
# ------------------------
# - OOP closely represents real-world entities (e.g., car, person, bank account).
# - Improves conceptual clarity and design.


# ================================================
# Summary:
# - OOP helps in building modular, maintainable, and scalable applications.
# - Main advantages: Reusability, Encapsulation, Abstraction, Polymorphism.
# ================================================
