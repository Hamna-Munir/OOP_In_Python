# ================================================
# File: 04_Method_Overriding.py
# Topic: Method Overriding in Python
# ================================================

"""
**Method Overriding** is an important concept in Object-Oriented Programming (OOP)
that allows a child (derived) class to provide a new implementation for a method
that is already defined in its parent (base) class.

It enables a subclass to **customize or extend** the behavior of an inherited method
without modifying the parent class directly.

This supports **polymorphism**, where the same method name behaves differently 
based on the object that calls it.
"""

# ------------------------------------------------
# 1️⃣ What is Method Overriding?
# ------------------------------------------------
# Method overriding occurs when:
# - A child class defines a method with the **same name**, **same parameters**, and **same return type** as its parent class.
# - The method in the child class replaces the method from the parent class when called on a child object.
#
# Purpose:
# - To modify or extend the functionality of the parent method in the derived class.

# Example:
class Parent:
    def show(self):
        print("This is the Parent class method.")

class Child(Parent):
    def show(self):
        print("This is the Child class method (Overridden).")

# Usage
print("----- Basic Method Overriding -----")
obj = Child()
obj.show()    # Calls Child’s version instead of Parent’s


# ------------------------------------------------
# 2️⃣ Accessing Parent Class Method using super()
# ------------------------------------------------
# You can still access the parent class’s overridden method using the `super()` function.

class Animal:
    def make_sound(self):
        print("Animals make generic sounds.")

class Dog(Animal):
    def make_sound(self):
        print("Dog barks.")
        super().make_sound()  # Calling parent method

# Usage
print("\n----- Using super() with Method Overriding -----")
dog = Dog()
dog.make_sound()


# ------------------------------------------------
# 3️⃣ Real-World Example: Bank Account System
# ------------------------------------------------

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_info(self):
        print(f"Account Holder: {self.owner}")
        print(f"Current Balance: {self.balance}")

class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    # Overriding show_info()
    def show_info(self):
        super().show_info()  # Call parent’s version
        print(f"Interest Rate: {self.interest_rate}%")

# Usage
print("\n----- Real-World Example: Banking -----")
acc = SavingsAccount("Hamna", 50000, 5)
acc.show_info()


# ------------------------------------------------
# 4️⃣ Example: Overriding with Different Behavior
# ------------------------------------------------
# A subclass can redefine the logic entirely while keeping the same method name.

class Shape:
    def area(self):
        print("Area formula not defined for generic shapes.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area_value = 3.14 * self.radius * self.radius
        print(f"Area of Circle: {area_value}")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area_value = self.length * self.width
        print(f"Area of Rectangle: {area_value}")

# Usage
print("\n----- Overriding for Specific Shapes -----")
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    shape.area()    # Calls respective subclass method


# ------------------------------------------------
# 5️⃣ Overriding Built-in Methods
# ------------------------------------------------
# You can also override built-in or special methods like __str__(), __len__(), etc.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Overriding the built-in __str__() method
    def __str__(self):
        return f"Student Name: {self.name}, Marks: {self.marks}"

# Usage
print("\n----- Overriding Built-in Methods -----")
s1 = Student("Ali", 92)
print(s1)   # Automatically calls __str__()


# ------------------------------------------------
# 6️⃣ Rules of Method Overriding
# ------------------------------------------------
# ✅ The method name must be the same in both parent and child classes.
# ✅ The method must have the same number and type of parameters.
# ✅ The return type (if applicable) should be compatible.
# ✅ The overridden method should maintain logical consistency.
# ✅ You can still call the parent’s version using `super()` if needed.


# ------------------------------------------------
# 7️⃣ Method Overriding and Polymorphism
# ------------------------------------------------
# Method overriding enables **runtime polymorphism**, where the method that gets executed
# depends on the object type at runtime, not the reference type.

class Vehicle:
    def start(self):
        print("Starting a generic vehicle...")

class Car(Vehicle):
    def start(self):
        print("Starting a car...")

class Bike(Vehicle):
    def start(self):
        print("Starting a bike...")

# Usage
print("\n----- Polymorphism with Overriding -----")
vehicles = [Car(), Bike(), Vehicle()]
for v in vehicles:
    v.start()    # Method behavior changes depending on the object type


# ------------------------------------------------
# 8️⃣ Difference Between Overloading and Overriding
# ------------------------------------------------
# | Feature             | Overloading                          | Overriding                          |
# |---------------------|--------------------------------------|-------------------------------------|
# | Definition          | Same method name, different parameters | Same method name and parameters     |
# | Occurs In           | Same class                            | Different (Parent & Child) classes  |
# | Execution Time      | Compile-time (simulated in Python)     | Runtime                             |
# | Keyword Used        | Not applicable                        | super() can be used                 |
# | Purpose             | Increase flexibility                  | Modify inherited behavior           |


# ------------------------------------------------
# 9️⃣ Practical Example: E-Commerce Order System
# ------------------------------------------------

class Order:
    def calculate_total(self, price, quantity):
        total = price * quantity
        print(f"Base total (without discount): {total}")

class DiscountedOrder(Order):
    def calculate_total(self, price, quantity):
        total = price * quantity
        discount = total * 0.1
        total_after_discount = total - discount
        print(f"Total after 10% discount: {total_after_discount}")

# Usage
print("\n----- E-Commerce Example -----")
order = DiscountedOrder()
order.calculate_total(100, 3)


# ------------------------------------------------
# 🔟 Best Practices
# ------------------------------------------------
# - Use method overriding when the child class logically modifies parent behavior.
# - Always keep method signatures consistent.
# - Use `super()` to maintain and extend parent functionality.
# - Avoid unnecessary overriding that makes code harder to maintain.
# - Combine overriding with polymorphism for cleaner, more flexible code.


# ================================================
# Summary:
# - Method overriding → redefining parent methods in child classes.
# - Enables polymorphism and flexible behavior.
# - Use `super()` to call parent versions.
# - Keep method names and parameters consistent across classes.
# ================================================
