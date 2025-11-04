# ================================================
# File: 01_Public_Private_Protected_Members.py
# Topic: Public, Private, and Protected Members in Python
# ================================================

"""
In Object-Oriented Programming (OOP), **data hiding** is an important concept.
It allows you to control how class members (attributes and methods) are accessed
and modified from outside the class.

In Python, data hiding is achieved through **naming conventions** using underscores.

There are three levels of access control for class members:
1️⃣ Public Members  
2️⃣ Protected Members  
3️⃣ Private Members
"""

# ------------------------------------------------
# 1️⃣ Public Members
# ------------------------------------------------
# Public members are accessible from anywhere — both inside and outside the class.
# They are the default type of members in Python.

class Student:
    def __init__(self, name, age):
        self.name = name        # Public member
        self.age = age          # Public member

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Usage
s1 = Student("Hamna", 21)
s1.display_info()          # ✅ Accessible
print(s1.name)             # ✅ Accessible outside the class
print(s1.age)              # ✅ Accessible outside the class


# ------------------------------------------------
# 2️⃣ Protected Members
# ------------------------------------------------
# Protected members are indicated by a **single underscore prefix (_)**.
# They should NOT be accessed directly outside the class,
# but they can be accessed by subclasses.

class Employee:
    def __init__(self, name, salary):
        self._salary = salary      # Protected member
        self.name = name

    def show_salary(self):
        print(f"{self.name}'s salary: {self._salary}")

# Subclass can access protected members
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_manager_info(self):
        print(f"Manager: {self.name}, Department: {self.department}, Salary: {self._salary}")

# Usage
emp = Employee("Ali", 60000)
emp.show_salary()
print(emp._salary)          # ⚠️ Technically accessible, but not recommended

mgr = Manager("Sara", 90000, "IT")
mgr.show_manager_info()     # ✅ Can access protected member from subclass


# ------------------------------------------------
# 3️⃣ Private Members
# ------------------------------------------------
# Private members are indicated by a **double underscore prefix (__)**.
# They cannot be accessed directly from outside the class or by subclasses.
# This helps achieve true encapsulation.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance     # Private member

    def deposit(self, amount):
        self.__balance += amount
        print(f"{self.owner} deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{self.owner} withdrew {amount}. Remaining balance: {self.__balance}")
        else:
            print("Insufficient funds!")

    def show_balance(self):
        print(f"{self.owner}'s current balance: {self.__balance}")

# Usage
acc = BankAccount("Zara", 5000)
acc.deposit(1500)
acc.withdraw(2000)
acc.show_balance()

# Trying to access private variable directly
# print(acc.__balance)       # ❌ AttributeError: 'BankAccount' object has no attribute '__balance'

# Accessing private variable using name mangling (Not recommended)
print(acc._BankAccount__balance)    # ⚠️ Possible but should be avoided


# ------------------------------------------------
# 4️⃣ Name Mangling in Python
# ------------------------------------------------
# Python internally changes the name of private members to include the class name.
# This process is called **name mangling**.
# Example:
# __balance → _BankAccount__balance
#
# It prevents accidental access but not intentional misuse.


# ------------------------------------------------
# 5️⃣ Summary of Access Modifiers
# ------------------------------------------------
# | Type        | Syntax     | Accessible Outside Class | Accessible in Subclass |
# |--------------|------------|---------------------------|------------------------|
# | Public       | var        | ✅ Yes                   | ✅ Yes                 |
# | Protected    | _var       | ⚠️ Yes (Not Recommended) | ✅ Yes                 |
# | Private      | __var      | ❌ No (Name Mangled)     | ❌ No                  |


# ================================================
# Summary:
# - Public members → Accessible everywhere
# - Protected members → Accessible within class & subclass (by convention)
# - Private members → Hidden from outside; accessible only within class
# ================================================
