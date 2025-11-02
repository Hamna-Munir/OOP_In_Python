# ----------------------------------------------------------
# File Name: 04_Static_Methods.py
# Topic: Static Methods in Python
# ----------------------------------------------------------
# Author: Hamna Munir
# Repository: OOP-in-Python
# ----------------------------------------------------------

#    What is a Static Method in Python?

# ➤ A static method belongs to a class rather than an instance of the class.  
# ➤ It does not require access to instance variables (self) or class variables (cls).  
# ➤ It is used when some functionality logically belongs to the class, 
#    but does not need data from the class or its objects.  
# ➤ Declared using the @staticmethod decorator.  
# ➤ Static methods improve code **organization**, **readability**, and **reusability**.  


# ----------------------------------------------------------
#   Defining and Using Static Methods
# ----------------------------------------------------------

class MathOperations:
    @staticmethod
    def add(a, b):
        """Performs addition of two numbers."""
        return a + b

    @staticmethod
    def multiply(a, b):
        """Performs multiplication of two numbers."""
        return a * b


# Using static methods
print(MathOperations.add(5, 3))       # Output: 8
print(MathOperations.multiply(4, 6))  # Output: 24


# ----------------------------------------------------------
#   Difference Between Instance, Class, and Static Methods
# ----------------------------------------------------------
# Instance Method → Operates on object data (uses self)
# Class Method    → Operates on class data (uses cls)
# Static Method   → Operates independently (no self or cls)


class Example:
    company = "TechCorp"

    def __init__(self, name):
        self.name = name

    def instance_method(self):
        return f"Instance method called by {self.name}"

    @classmethod
    def class_method(cls):
        return f"Class method called. Company: {cls.company}"

    @staticmethod
    def static_method():
        return "Static method called. No access to instance or class data."


# Usage
obj = Example("Hamna")

print(obj.instance_method())   # Output: Instance method called by Hamna
print(Example.class_method())  # Output: Class method called. Company: TechCorp
print(Example.static_method()) # Output: Static method called. No access to instance or class data.


# ----------------------------------------------------------
#   When to Use Static Methods
# ----------------------------------------------------------
# ✔ When the function performs a general task (like calculations or checks).  
# ✔ When it does not depend on instance or class attributes.  
# ✔ When the functionality logically belongs to the class, not an instance.


# Example: Checking if a number is even or odd
class NumberCheck:
    @staticmethod
    def is_even(num):
        return num % 2 == 0


print(NumberCheck.is_even(10))  # Output: True
print(NumberCheck.is_even(7))   # Output: False


# ----------------------------------------------------------
#   Real-World Example: Using Static Methods for Validation
# ----------------------------------------------------------

class Validator:
    @staticmethod
    def is_valid_email(email):
        """Check if the email contains '@' and '.'."""
        return "@" in email and "." in email

    @staticmethod
    def is_valid_age(age):
        """Check if age is within a valid range."""
        return 0 < age < 120


# Usage
print(Validator.is_valid_email("hamna@example.com"))  # Output: True
print(Validator.is_valid_age(25))                     # Output: True
print(Validator.is_valid_age(-5))                     # Output: False


# ----------------------------------------------------------
#   Key Points
# ----------------------------------------------------------
# - Declared using @staticmethod decorator.
# - Does not take self or cls as parameters.
# - Cannot access or modify class or instance variables.
# - Best used for helper and utility functions.
# - Can be called using either class name or object name.


# ----------------------------------------------------------
#   Summary:
# ----------------------------------------------------------
# - Static methods belong to a class but work independently of class or object data.
# - They are ideal for tasks like calculations, validations, or data formatting.
# - They promote cleaner and more modular code organization.
# ----------------------------------------------------------
