# ================================================
# File: 01_Instance_vs_Class_Variables.py
# Topic: Instance Variables vs Class Variables
# ================================================

"""
In Python Object-Oriented Programming, variables inside a class can be
classified into two main types:

1. **Instance Variables** — Belong to a specific object (instance).
2. **Class Variables** — Shared among all objects of the same class.
"""

# ------------------------------------------------
# 1️⃣ Instance Variables
# ------------------------------------------------
# - Defined inside the constructor (__init__) using `self`.
# - Each object (instance) has its own separate copy.
# - Changing one instance variable does not affect others.

class Student:
    def __init__(self, name, grade):
        self.name = name           # Instance variable
        self.grade = grade         # Instance variable

# Usage
s1 = Student("Hamna", "A")
s2 = Student("Ali", "B")

print(s1.name, s1.grade)   # Output: Hamna A
print(s2.name, s2.grade)   # Output: Ali B

# Changing one object’s instance variable
s2.grade = "A+"
print(s1.grade)  # Output: A (unchanged)
print(s2.grade)  # Output: A+


# ------------------------------------------------
# 2️⃣ Class Variables
# ------------------------------------------------
# - Declared inside the class but outside all methods.
# - Shared by all instances of the class.
# - Changing a class variable affects all objects (unless overridden).

class Employee:
    company_name = "TechCorp"   # Class variable

    def __init__(self, name, salary):
        self.name = name        # Instance variable
        self.salary = salary    # Instance variable

# Usage
emp1 = Employee("Sara", 50000)
emp2 = Employee("Ahmed", 60000)

print(emp1.company_name)  # Output: TechCorp
print(emp2.company_name)  # Output: TechCorp

# Changing the class variable
Employee.company_name = "NextGenTech"
print(emp1.company_name)  # Output: NextGenTech
print(emp2.company_name)  # Output: NextGenTech


# ------------------------------------------------
# 3️⃣ Difference Example
# ------------------------------------------------
class Dog:
    species = "Canine"   # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

dog1 = Dog("Buddy")
dog2 = Dog("Rocky")

print(dog1.species)  # Output: Canine
print(dog2.species)  # Output: Canine

# Modify class variable
Dog.species = "Domestic Dog"
print(dog1.species)  # Output: Domestic Dog
print(dog2.species)  # Output: Domestic Dog

# Modify instance variable (unique per object)
dog1.name = "Charlie"
print(dog1.name)  # Output: Charlie
print(dog2.name)  # Output: Rocky


# ------------------------------------------------
# 4️⃣ Key Points
# ------------------------------------------------
# - Instance variables: Defined inside __init__, unique per object.
# - Class variables: Defined at class level, shared by all objects.
# - Use `self.variable` for instance variables.
# - Use `ClassName.variable` for class variables.


# ================================================
# Summary:
# Instance variables → unique to each object.
# Class variables → shared across all objects.
# ================================================
