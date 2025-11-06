# ================================================
# File: 03_Method_Overriding.py
# Topic: Method Overriding in Python
# ================================================

"""
In Object-Oriented Programming (OOP), **Method Overriding** allows a subclass
(child class) to provide a specific implementation of a method that is already
defined in its parent class (superclass).

When a subclass defines a method with the same **name**, **parameters**, and
**return type** as the method in the parent class, the **child class method overrides**
the parent class method.

This is a key feature of **Polymorphism** — it allows one interface to be used
for different data types or classes.
"""

# ------------------------------------------------
# 1️⃣ Basic Example of Method Overriding
# ------------------------------------------------

class Parent:
    def show(self):
        print("This is the show() method of the Parent class")

class Child(Parent):
    # Overriding the parent's show() method
    def show(self):
        print("This is the show() method of the Child class")

# Usage
obj1 = Parent()
obj2 = Child()

obj1.show()  # Output: This is the show() method of the Parent class
obj2.show()  # Output: This is the show() method of the Child class


# ------------------------------------------------
# 2️⃣ Why Use Method Overriding?
# ------------------------------------------------
"""
Method overriding allows a subclass to modify or completely change
the behavior of a method that it inherits from the parent class.

✅ It enhances code flexibility and reusability.
✅ It enables polymorphic behavior — the same method name can behave differently
   depending on the object that calls it.
"""


# ------------------------------------------------
# 3️⃣ Using super() to Call the Parent Method
# ------------------------------------------------
"""
If you still want to use the parent class method inside the overridden method,
you can use the **super()** function. It allows you to call methods from the parent class.
"""

class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    def sound(self):
        super().sound()  # Call the parent class method
        print("Dog barks")

# Usage
d = Dog()
d.sound()
# Output:
# Animals make sounds
# Dog barks


# ------------------------------------------------
# 4️⃣ Example: Overriding in Real-Life Scenario
# ------------------------------------------------

class BankAccount:
    def interest_rate(self):
        return 5  # Default interest rate in percentage

class SavingsAccount(BankAccount):
    def interest_rate(self):
        return 7  # Higher interest rate for savings account

class CurrentAccount(BankAccount):
    def interest_rate(self):
        return 4  # Lower interest rate for current account

# Usage
savings = SavingsAccount()
current = CurrentAccount()

print("Savings Account Interest Rate:", savings.interest_rate())  # Output: 7
print("Current Account Interest Rate:", current.interest_rate())  # Output: 4


# ------------------------------------------------
# 5️⃣ Example: Method Overriding with Additional Functionality
# ------------------------------------------------
"""
A child class can override a method but also **extend its functionality**
by calling the parent version first, then adding more behavior.
"""

class Vehicle:
    def start(self):
        print("Starting vehicle...")

class Car(Vehicle):
    def start(self):
        super().start()  # Call parent class method
        print("Car engine started successfully")

# Usage
c = Car()
c.start()
# Output:
# Starting vehicle...
# Car engine started successfully


# ------------------------------------------------
# 6️⃣ Polymorphism through Method Overriding
# ------------------------------------------------
"""
When different subclasses override the same method from a parent class,
you can call that method on any subclass object, and Python automatically
invokes the correct version — this is **runtime polymorphism**.
"""

class Shape:
    def area(self):
        print("Calculating area...")

class Circle(Shape):
    def area(self):
        print("Area of Circle = πr²")

class Rectangle(Shape):
    def area(self):
        print("Area of Rectangle = length × breadth")

shapes = [Circle(), Rectangle()]

for shape in shapes:
    shape.area()

# Output:
# Area of Circle = πr²
# Area of Rectangle = length × breadth


# ------------------------------------------------
# 7️⃣ Rules for Method Overriding
# ------------------------------------------------
"""
✔ The method must have the same name as in the parent class.
✔ The number of parameters must be the same.
✔ It occurs between two classes that have a parent-child relationship (inheritance).
✔ The child class method replaces (overrides) the parent class version when called.
"""


# ------------------------------------------------
# 8️⃣ Method Overriding vs Method Overloading
# ------------------------------------------------
"""
| Feature                  | Method Overriding                      | Method Overloading (Simulated)          |
|---------------------------|----------------------------------------|----------------------------------------|
| Definition                | Same method name in parent & child     | Same method name, different parameters |
| Inheritance Required      | Yes                                    | No                                     |
| Execution Time            | Runtime (Dynamic Polymorphism)         | Compile-time (Static-like)             |
| Python Support            | Fully Supported                        | Simulated using default/*args          |
"""


# ------------------------------------------------
# 9️⃣ Practical Example: Overriding Built-in Methods
# ------------------------------------------------
"""
You can override built-in methods like __str__, __len__, etc.,
to customize object behavior.
"""

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        # Overriding built-in __str__ method
        return f"Book Title: {self.title}, Pages: {self.pages}"

book = Book("Python Mastery", 450)
print(book)  # Output: Book Title: Python Mastery, Pages: 450


# ================================================
# Summary:
# - Method Overriding → Subclass redefines a method from its superclass.
# - Achieved through inheritance.
# - super() can be used to access the parent class version.
# - Enables polymorphism (different behaviors for the same method name).
# - Used extensively in real-world OOP design.
# ================================================
