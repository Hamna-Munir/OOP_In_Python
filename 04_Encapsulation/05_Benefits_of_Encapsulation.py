# ================================================
# File: 05_Benefits_of_Encapsulation.py
# Topic: Benefits of Encapsulation in Python
# ================================================

"""
Encapsulation is a fundamental principle of Object-Oriented Programming (OOP) 
that focuses on **data protection** and **controlled access**. It ensures that 
the internal representation of an object is hidden from the outside world, and 
can only be accessed through well-defined interfaces (methods).

Encapsulation improves code **security**, **maintainability**, and **reusability** 
by preventing unintended interference with an object’s data.
"""

# ------------------------------------------------
# 1️⃣ What is Encapsulation?
# ------------------------------------------------
# Encapsulation is the process of combining **data (attributes)** and the 
# **methods that operate on that data** into a single unit — the class.
#
# The main idea is to:
# - Protect internal data from unauthorized access.
# - Allow controlled modification through getters and setters.
# - Hide implementation details and expose only necessary behavior.

class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    # Getter
    def get_marks(self):
        return self.__marks

    # Setter with validation
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks. Must be between 0 and 100.")

    def display(self):
        print(f"Name: {self.__name}, Marks: {self.__marks}")

# Usage
student = Student("Hamna", 90)
student.display()
student.set_marks(95)       # Valid update
student.display()
student.set_marks(120)      # Invalid update


# ------------------------------------------------
# 2️⃣ Core Benefits of Encapsulation
# ------------------------------------------------

# Benefit 1: Data Hiding
# ----------------------
# Encapsulation hides the internal data of a class to prevent direct access.
# This protects against accidental or malicious modifications.

class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance     # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. Remaining Balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

# Usage
account = BankAccount("Ali", 5000)
account.deposit(2000)
account.withdraw(1000)
print("Final Balance:", account.get_balance())

# Direct access is not allowed
# print(account.__balance)  # AttributeError


# Benefit 2: Data Validation and Control
# --------------------------------------
# Encapsulation allows enforcing rules and validation before data modification.

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

# Usage
emp = Employee("Sara", 60000)
print("Current Salary:", emp.salary)
emp.salary = 70000          # Valid update
emp.salary = -5000          # Invalid update


# Benefit 3: Code Maintainability and Flexibility
# -----------------------------------------------
# Encapsulation makes code easier to maintain and extend.
# Internal logic can change without affecting other parts of the program.

class Car:
    def __init__(self, brand, speed):
        self.__brand = brand
        self.__speed = speed

    def accelerate(self, value):
        self.__speed += value
        print(f"{self.__brand} accelerated to {self.__speed} km/h")

    def brake(self, value):
        self.__speed -= value
        if self.__speed < 0:
            self.__speed = 0
        print(f"{self.__brand} slowed down to {self.__speed} km/h")

# Usage
car = Car("Toyota", 50)
car.accelerate(30)
car.brake(60)
# Internal speed calculation is hidden and can be changed without breaking external code.


# Benefit 4: Improved Security
# ----------------------------
# Sensitive information can be secured and accessed only through authorized methods.

class UserAccount:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password   # Private variable

    def login(self, username, password):
        if self.__username == username and self.__password == password:
            print("Login successful.")
        else:
            print("Invalid credentials.")

# Usage
user = UserAccount("admin", "secure123")
user.login("admin", "secure123")   # Valid login
user.login("admin", "wrongpass")   # Invalid login


# ------------------------------------------------
# 3️⃣ Summary of Encapsulation Benefits
# ------------------------------------------------
# 1. **Data Hiding:** Internal details are not exposed publicly.
# 2. **Validation & Control:** Allows controlled data modification.
# 3. **Code Maintainability:** Internal changes do not affect other code.
# 4. **Reusability:** Encapsulated classes can be reused easily.
# 5. **Security:** Sensitive data is protected from direct access.


# ------------------------------------------------
# 4️⃣ Encapsulation in Real-World Applications
# ------------------------------------------------
# Encapsulation is widely used in:
# - Banking systems (to protect account details)
# - Authentication systems (to hide passwords)
# - Medical record management (to secure patient data)
# - Software APIs (to hide internal implementation from users)
# - Game development (to manage player stats and states safely)


# ------------------------------------------------
# 5️⃣ Key Takeaways
# ------------------------------------------------
# - Encapsulation binds data and methods together.
# - Direct access to private data is restricted.
# - Data should always be modified using controlled interfaces.
# - It improves reliability, security, and reduces dependencies between classes.


# ================================================
# Summary:
# Encapsulation enhances:
# - Data protection
# - Security and validation
# - Flexibility and maintainability
# It ensures that objects control their own data, making systems robust and reliable.
# ================================================
