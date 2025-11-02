# ----------------------------------------------------------
# File Name: 05_Example_Class_Based_Program.py
# Topic: Example — Class-Based Program in Python
# ----------------------------------------------------------
# Author: Hamna Munir
# Repository: OOP-in-Python
# ----------------------------------------------------------

#    What is a Class-Based Program?

# ➤ A class-based program is one that is designed around **objects and classes**.  
# ➤ It uses the principles of **Object-Oriented Programming (OOP)** such as:
#    - Encapsulation (grouping data and methods)
#    - Reusability (via classes and inheritance)
#    - Abstraction (simplifying complex logic)
# ➤ In Python, a class-based approach helps write clean, organized, and modular code.


# ----------------------------------------------------------
#   Example 1: Simple Student Management Program
# ----------------------------------------------------------

class Student:
    """Represents a student with basic details and behavior."""

    school_name = "AI Learning Academy"  # Class variable shared by all students

    def __init__(self, name, age, course):
        self.name = name        # Instance variable
        self.age = age          # Instance variable
        self.course = course    # Instance variable

    def display_info(self):
        """Display student details."""
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print(f"School: {Student.school_name}")

    def is_adult(self):
        """Check if the student is an adult."""
        return self.age >= 18


# Creating student objects
student1 = Student("Hamna", 21, "Artificial Intelligence")
student2 = Student("Ayesha", 17, "Machine Learning")

# Displaying information
student1.display_info()
# Output:
# Student Name: Hamna
# Age: 21
# Course: Artificial Intelligence
# School: AI Learning Academy

print("\nIs Adult?", student1.is_adult())  # Output: True

print("\n------------------------------\n")

student2.display_info()
# Output:
# Student Name: Ayesha
# Age: 17
# Course: Machine Learning
# School: AI Learning Academy

print("\nIs Adult?", student2.is_adult())  # Output: False


# ----------------------------------------------------------
#   Example 2: Bank Account System
# ----------------------------------------------------------

class BankAccount:
    """Represents a simple bank account."""

    bank_name = "Secure Bank"

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money if sufficient balance is available."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Invalid or insufficient balance.")

    def check_balance(self):
        """Display current balance."""
        print(f"Account Holder: {self.account_holder}")
        print(f"Bank: {BankAccount.bank_name}")
        print(f"Current Balance: {self.balance}")


# Creating Bank Account Objects
account1 = BankAccount("Hamna", 5000)
account2 = BankAccount("Ayesha")

# Performing Operations
account1.deposit(2000)          # Output: 2000 deposited successfully.
account1.withdraw(1500)         # Output: 1500 withdrawn successfully.
account1.check_balance()
# Output:
# Account Holder: Hamna
# Bank: Secure Bank
# Current Balance: 5500

print("\n------------------------------\n")

account2.deposit(3000)
account2.withdraw(1000)
account2.check_balance()
# Output:
# Account Holder: Ayesha
# Bank: Secure Bank
# Current Balance: 2000


# ----------------------------------------------------------
#   Example 3: Product Management System
# ----------------------------------------------------------

class Product:
    """Represents a product with name, price, and stock."""

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        """Calculate total stock value."""
        return self.price * self.quantity

    def restock(self, amount):
        """Increase product stock."""
        if amount > 0:
            self.quantity += amount
            print(f"{amount} units added to {self.name} stock.")
        else:
            print("Invalid quantity for restocking.")

    def sell(self, amount):
        """Reduce product stock when sold."""
        if 0 < amount <= self.quantity:
            self.quantity -= amount
            print(f"{amount} {self.name}(s) sold successfully.")
        else:
            print("Invalid quantity or insufficient stock.")


# Example Usage
product1 = Product("Laptop", 120000, 5)
product1.sell(2)
product1.restock(3)
print("Total Stock Value:", product1.total_value())
# Output:
# 2 Laptop(s) sold successfully.
# 3 units added to Laptop stock.
# Total Stock Value: 720000


# ----------------------------------------------------------
#   Summary:
# ----------------------------------------------------------
# - Class-based programs organize code into reusable and logical structures.
# - Each class represents a real-world entity (e.g., Student, BankAccount, Product).
# - Methods define actions or behaviors associated with those entities.
# - Class variables are shared among all instances; instance variables are unique.
# - Using classes improves scalability, readability, and maintainability of code.
# ----------------------------------------------------------
