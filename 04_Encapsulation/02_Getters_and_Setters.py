# ================================================
# File: 02_Getters_and_Setters.py
# Topic: Getters and Setters in Python
# ================================================

"""
In Object-Oriented Programming (OOP), **getters** and **setters** are methods 
used to access and modify private or protected data members of a class.

Python does not enforce strict data encapsulation, but it provides mechanisms 
to control access to attributes using getter and setter methods — or the 
`@property` decorator.

These methods help maintain data integrity and validation.
"""

# ------------------------------------------------
# 1️⃣ Getters and Setters using Regular Methods
# ------------------------------------------------
# These are traditional getter and setter methods defined explicitly in a class.

class Student:
    def __init__(self, name, marks):
        self.__name = name          # Private attribute
        self.__marks = marks        # Private attribute

    # Getter method
    def get_marks(self):
        return self.__marks

    # Setter method
    def set_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print(" Invalid marks! Must be between 0 and 100.")

# Usage
s1 = Student("Hamna", 85)
print("Current Marks:", s1.get_marks())   #  Access using getter

s1.set_marks(92)                          #  Update using setter
print("Updated Marks:", s1.get_marks())

s1.set_marks(150)                         #  Invalid marks


# ------------------------------------------------
# 2️⃣ Getters and Setters using @property Decorator
# ------------------------------------------------
# Python provides a cleaner way to define getters and setters using decorators.
# The `@property` decorator allows attribute access syntax while keeping 
# validation logic inside methods.

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    # Getter
    @property
    def salary(self):
        return self.__salary

    # Setter
    @salary.setter
    def salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print(" Salary must be positive.")

# Usage
emp = Employee("Sara", 50000)
print(f"Current Salary: {emp.salary}")   #  Calls getter

emp.salary = 60000                       #  Calls setter
print(f"Updated Salary: {emp.salary}")

emp.salary = -1000                       #  Invalid salary


# ------------------------------------------------
# 3️⃣ Using @property with Read-Only and Write-Only Attributes
# ------------------------------------------------
# - Read-Only: Define only a getter (no setter)
# - Write-Only: Define only a setter (no getter)

class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    # Read-Only property
    @property
    def balance(self):
        return self.__balance

    # Write-Only property
    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print(" Balance cannot be negative.")

# Usage
acc = BankAccount("Ali", 10000)
print(f"Initial Balance: {acc.balance}")   #  Read balance

acc.balance = 12000                        #  Update balance
print(f"Updated Balance: {acc.balance}")

acc.balance = -500                         #  Invalid balance


# ------------------------------------------------
# 4️⃣ Why Use Getters and Setters?
# ------------------------------------------------
# - To validate data before updating attributes
# - To make attributes read-only or write-only
# - To maintain control over internal data representation
# - To avoid breaking code when internal structure changes


# ------------------------------------------------
# 5️⃣ Key Points
# ------------------------------------------------
# - Use getters and setters to encapsulate and validate data.
# - Use `@property` for a clean and Pythonic approach.
# - Private attributes should always be accessed via these methods.
# - Avoid direct manipulation of private variables.


# ================================================
# Summary:
# Getters → Access private data  
# Setters → Modify private data  
# `@property` → Pythonic way to define getters and setters
# ================================================
