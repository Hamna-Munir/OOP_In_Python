# ================================================
# File: 02_Instance_Methods.py
# Topic: Instance Methods in Python
# ================================================

"""
In Object-Oriented Programming (OOP), **instance methods** are the most common
type of methods defined inside a class.

They are used to perform operations using the **instance variables** of an object.
Each instance method takes `self` as its first parameter, which refers to the
current instance of the class.
"""

# ------------------------------------------------
# 1️⃣ Defining and Using Instance Methods
# ------------------------------------------------

class Student:
    def __init__(self, name, marks):
        self.name = name        # Instance variable
        self.marks = marks      # Instance variable

    # Instance Method
    def display_info(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

# Usage
s1 = Student("Hamna", 95)
s2 = Student("Ali", 88)

s1.display_info()   # Output: Name: Hamna, Marks: 95
s2.display_info()   # Output: Name: Ali, Marks: 88


# ------------------------------------------------
# 2️⃣ Modifying Instance Variables using Instance Methods
# ------------------------------------------------
# Instance methods can also modify or update instance variables.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"{self.name}'s updated salary: {self.salary}")

# Usage
emp = Employee("Sara", 50000)
emp.update_salary(55000)   # Output: Sara's updated salary: 55000


# ------------------------------------------------
# 3️⃣ Instance Methods with Parameters
# ------------------------------------------------
# You can pass additional arguments to instance methods besides `self`.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}. Remaining balance: {self.balance}")
        else:
            print("Insufficient funds!")

# Usage
acc1 = BankAccount("Ahmed", 1000)
acc1.deposit(500)
acc1.withdraw(300)
acc1.withdraw(2000)


# ------------------------------------------------
# 4️⃣ Accessing Instance Methods
# ------------------------------------------------
# Instance methods are called using the instance name followed by a dot (.)
# Example:  object_name.method_name()

# You can also call them using the class name, but you must pass the instance manually:
# ClassName.method_name(instance)

s1 = Student("Zara", 90)
Student.display_info(s1)   # Valid but less common


# ------------------------------------------------
# 5️⃣ Key Points
# ------------------------------------------------
# - Instance methods work with instance variables.
# - The first argument is always `self`.
# - They can access and modify the object’s data.
# - They are called using the object of the class.
# - Used for behaviors specific to individual objects.


# ================================================
# Summary:
# Instance methods → Operate on instance data (object-specific data)
# ================================================
