# ================================================
# File: 04_Practical_Example_Encapsulation.py
# Topic: Encapsulation in Python (Practical Example)
# ================================================

"""
In Object-Oriented Programming (OOP), **encapsulation** is one of the core
principles. It refers to the **bundling of data (variables)** and the **methods
that operate on that data** into a single unit — typically a class.

Encapsulation also involves **restricting direct access** to an object's internal
state, protecting it from unintended interference and misuse. This is achieved
using **access modifiers** like public, protected, and private members.

Encapsulation ensures:
- Controlled access to class data
- Data integrity and validation
- Better code maintainability and flexibility
"""

# ------------------------------------------------
# 1️⃣ Concept of Encapsulation
# ------------------------------------------------
# - The internal data of a class should not be directly accessible from outside.
# - Instead, access should be provided through well-defined interfaces 
#   (methods like getters, setters, or other controlled functions).
#
# In Python:
# - Public members: Accessible from anywhere
# - Protected members: Accessible within class and subclasses
# - Private members: Hidden from outside the class (name-mangled)


# ------------------------------------------------
# 2️⃣ Basic Example of Encapsulation
# ------------------------------------------------

class Student:
    def __init__(self, name, marks):
        self.__name = name        # Private attribute
        self.__marks = marks      # Private attribute

    # Getter method for name
    def get_name(self):
        return self.__name

    # Setter method for name
    def set_name(self, name):
        if len(name) > 0:
            self.__name = name
        else:
            print("Name cannot be empty.")

    # Getter method for marks
    def get_marks(self):
        return self.__marks

    # Setter method for marks with validation
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Marks must be between 0 and 100.")

    def display_info(self):
        print(f"Name: {self.__name}, Marks: {self.__marks}")

# Usage
s1 = Student("Hamna", 92)
s1.display_info()

# Trying to access private data directly
# print(s1.__marks)  # AttributeError

# Access through getter and setter
print("Current Marks:", s1.get_marks())
s1.set_marks(98)
s1.display_info()
s1.set_marks(150)   # Invalid marks, validation in action


# ------------------------------------------------
# 3️⃣ Practical Example: Bank Account with Encapsulation
# ------------------------------------------------
# A bank account system is an ideal real-world example of encapsulation.
# Sensitive data like account balance should not be directly accessible or modifiable.
# Instead, controlled methods like deposit() and withdraw() should handle it.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner          # Private data
        self.__balance = balance      # Private data

    # Getter for balance (read-only)
    @property
    def balance(self):
        return self.__balance

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Withdraw method
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.__balance}")

    # Display account info
    def show_account_info(self):
        print(f"Account Owner: {self.__owner}")
        print(f"Current Balance: {self.__balance}")

# Usage
acc = BankAccount("Ali", 5000)
acc.show_account_info()

acc.deposit(2000)
acc.withdraw(1000)
acc.withdraw(7000)  # Invalid withdrawal

# Direct access to private variable (Not allowed)
# print(acc.__balance)   # AttributeError

# Access using name mangling (not recommended)
print("Access via name mangling:", acc._BankAccount__balance)


# ------------------------------------------------
# 4️⃣ Benefits of Encapsulation
# ------------------------------------------------
# 1. **Data Hiding:** Internal details are hidden; only necessary information is exposed.
# 2. **Improved Security:** Sensitive data cannot be directly modified from outside.
# 3. **Controlled Access:** You can control how data is read or modified.
# 4. **Code Flexibility:** Internal implementation can change without affecting external code.
# 5. **Maintenance:** Makes code easier to maintain, debug, and scale.


# ------------------------------------------------
# 5️⃣ Encapsulation with Properties (Pythonic Way)
# ------------------------------------------------
# Instead of writing explicit getter and setter methods, Python’s `@property`
# decorator allows defining properties for controlled attribute access.

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Salary must be positive.")

    def display(self):
        print(f"Employee: {self.__name}, Salary: {self.__salary}")

# Usage
emp = Employee("Sara", 60000)
emp.display()

emp.salary = 65000
emp.display()

emp.salary = -1000   # Invalid update (validation applied)


# ------------------------------------------------
# 6️⃣ Summary Table
# ------------------------------------------------
# | Concept           | Description                                               | Example Syntax         |
# |-------------------|-----------------------------------------------------------|-------------------------|
# | Public Member     | Accessible everywhere                                     | self.name              |
# | Protected Member  | Accessible in class and subclass (by convention)          | self._salary           |
# | Private Member    | Accessible only within class (name-mangled)               | self.__balance         |
# | Getter/Setter     | Methods to access/modify private data                     | get_x(), set_x()       |
# | @property         | Pythonic way to define getters/setters                    | @property, @x.setter   |


# ================================================
# Summary:
# Encapsulation → Binding data and methods while restricting direct access.
# - Protects data integrity and provides controlled interfaces.
# - Implemented using public, protected, and private access modifiers.
# - Achieved through getters, setters, and @property decorators.
# ================================================
