# ================================================
# File: 03_Super_Function.py
# Topic: The super() Function in Python
# ================================================

"""
In Object-Oriented Programming (OOP), the **super()** function is used to call
methods and constructors of a parent (base) class from within a child (derived) class.

It is one of the most powerful tools in inheritance, allowing child classes to
reuse and extend the functionality of parent classes without rewriting code.

`super()` is especially useful in:
- Calling the parent class constructor (__init__)
- Accessing overridden methods in the parent class
- Working with multiple inheritance (following MRO)
"""

# ------------------------------------------------
# 1️⃣ What is super()?
# ------------------------------------------------
# The `super()` function returns a temporary object of the parent class that allows
# access to its methods and properties.
#
# Syntax:
#     super().method_name()
#
# You can use `super()` inside the child class to call methods defined in its parent class.


# ------------------------------------------------
# 2️⃣ Using super() to Call Parent Class Constructor
# ------------------------------------------------

class Parent:
    def __init__(self, name):
        self.name = name
        print("Parent __init__() called")

class Child(Parent):
    def __init__(self, name, age):
        # Calling the parent constructor
        super().__init__(name)
        self.age = age
        print("Child __init__() called")

# Usage
print("----- Using super() in Constructor -----")
c = Child("Hamna", 20)
print(f"Name: {c.name}, Age: {c.age}")


# ------------------------------------------------
# 3️⃣ Using super() to Call Overridden Methods
# ------------------------------------------------
# When a child class overrides a method from the parent class,
# `super()` can be used to call the parent’s version of that method.

class Animal:
    def sound(self):
        print("Animals make different sounds.")

class Dog(Animal):
    def sound(self):
        print("Dog barks.")
        # Call parent class method
        super().sound()

# Usage
print("\n----- Using super() in Method Overriding -----")
dog = Dog()
dog.sound()


# ------------------------------------------------
# 4️⃣ Real-World Example: Employee and Manager
# ------------------------------------------------

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def show_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")

class Manager(Employee):
    def __init__(self, name, emp_id, team_size):
        # Call parent constructor
        super().__init__(name, emp_id)
        self.team_size = team_size

    def show_info(self):
        # Extend parent method functionality
        super().show_info()
        print(f"Team Size: {self.team_size}")

# Usage
print("\n----- Real-World Example -----")
m = Manager("Sara", 102, 5)
m.show_info()


# ------------------------------------------------
# 5️⃣ Using super() with Multiple Inheritance
# ------------------------------------------------
# In multiple inheritance, `super()` works according to the **Method Resolution Order (MRO)**.
# It ensures that each parent class in the hierarchy is initialized only once and in the correct order.

class A:
    def __init__(self):
        print("Class A initialized")

class B(A):
    def __init__(self):
        super().__init__()
        print("Class B initialized")

class C(A):
    def __init__(self):
        super().__init__()
        print("Class C initialized")

class D(B, C):
    def __init__(self):
        super().__init__()   # Calls next in MRO
        print("Class D initialized")

# Usage
print("\n----- Multiple Inheritance with super() -----")
obj = D()

# Display the MRO (Method Resolution Order)
print("MRO:", D.mro())


# ------------------------------------------------
# 6️⃣ Why Use super()?
# ------------------------------------------------
# Advantages:
# - Avoids duplicate calls to base classes (especially in multiple inheritance)
# - Promotes reusability of parent methods
# - Simplifies maintenance by preventing hard-coded parent class names
# - Follows Python’s MRO automatically for consistent behavior


# ------------------------------------------------
# 7️⃣ Common Mistakes to Avoid
# ------------------------------------------------
# ❌ Forgetting to call super().__init__() when the parent requires initialization.
# ❌ Using the parent class name directly (e.g., Parent.__init__(self)) — breaks MRO.
# ✅ Always prefer `super()` over direct class references in inheritance.


# ------------------------------------------------
# 8️⃣ Practical Example: Banking System
# ------------------------------------------------

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def show_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def show_info(self):
        super().show_info()
        print(f"Interest Rate: {self.interest_rate}%")

# Usage
print("\n----- Banking Example -----")
acc = SavingsAccount(1001, 50000, 5)
acc.show_info()


# ------------------------------------------------
# 9️⃣ Best Practices
# ------------------------------------------------
# - Always use `super()` instead of directly calling the parent class name.
# - Call `super().__init__()` early in the child constructor to ensure proper initialization.
# - When working with multiple inheritance, rely on `super()` to follow MRO.
# - Keep your inheritance hierarchies simple and logical.


# ================================================
# Summary:
# - The `super()` function allows access to parent class methods and constructors.
# - It simplifies code reuse and supports multiple inheritance safely.
# - Python uses MRO to determine the order of execution for `super()`.
# - Always use `super()` for clean, maintainable, and extensible OOP code.
# ================================================
