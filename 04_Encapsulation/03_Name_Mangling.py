# ================================================
# File: 03_Name_Mangling.py
# Topic: Name Mangling in Python
# ================================================

"""
In Python, **name mangling** is a mechanism used to protect private class members 
from being accidentally accessed or overridden in subclasses.

When a class attribute name starts with **two underscores (__)**, Python 
automatically changes its name internally to include the class name.

This feature helps achieve **data hiding** and prevents **accidental access**, 
though it can still be accessed intentionally if needed.
"""

# ------------------------------------------------
# 1️⃣ What is Name Mangling?
# ------------------------------------------------
# When you define a variable with two leading underscores (e.g. `__balance`),
# Python internally renames it to `_ClassName__variable`.
#
# Example:
# Inside class BankAccount:
#   self.__balance → self._BankAccount__balance
#
# This makes it harder (but not impossible) to access the variable from outside.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance     # Private variable (will be name-mangled)

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.__balance}")

# Usage
acc = BankAccount("Hamna", 5000)
acc.show_balance()

# Trying to access private variable directly
# print(acc.__balance)        #  AttributeError: 'BankAccount' object has no attribute '__balance'

# Accessing through name mangling (not recommended)
print(acc._BankAccount__balance)     #  Possible, but discouraged


# ------------------------------------------------
# 2️⃣ Why Does Python Use Name Mangling?
# ------------------------------------------------
# Name mangling is used to:
# - Avoid accidental access to private attributes
# - Prevent subclasses from unintentionally overriding private attributes
# - Support encapsulation and data hiding


# ------------------------------------------------
# 3️⃣ Example: Subclass and Name Mangling
# ------------------------------------------------
# In inheritance, name mangling prevents the child class from accidentally
# overriding the parent’s private variables.

class Parent:
    def __init__(self):
        self.__secret = "Parent Secret"

    def reveal_secret(self):
        print("Parent secret:", self.__secret)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__secret = "Child Secret"

    def reveal_secret(self):
        # Accessing own private variable
        print("Child secret:", self.__secret)
        # Accessing parent's private variable via name mangling
        print("Accessing parent secret:", self._Parent__secret)

# Usage
child = Child()
child.reveal_secret()

# Trying to access private variable directly
# print(child.__secret)          #  AttributeError
print(child._Child__secret)       #  Accessible through name mangling


# ------------------------------------------------
# 4️⃣ Name Mangling Rules
# ------------------------------------------------
# - Starts with **two underscores (__)**
# - Does NOT end with two underscores (avoid __init__, __str__, etc.)
# - Python renames it internally to: `_ClassName__variable`
# - Can still be accessed manually (but not recommended)


# ------------------------------------------------
# 5️⃣ When to Use Name Mangling
# ------------------------------------------------
# ✅ Use for:
#   - Attributes that should not be accessed or overridden accidentally
#   - Preventing name conflicts in subclasses
#
# ⚠️ Avoid using it excessively — prefer single underscore (_) for “protected” members


# ================================================
# Summary:
# - Name mangling hides private members by renaming them internally.
# - Access via: _ClassName__variable
# - Protects data from accidental misuse, not from intentional access.
# ================================================
