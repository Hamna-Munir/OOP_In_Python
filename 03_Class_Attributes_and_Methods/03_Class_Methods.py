# ================================================
# File: 03_Class_Methods.py
# Topic: Class Methods in Python
# ================================================

"""
In Object-Oriented Programming (OOP), **class methods** are methods that
operate on the **class itself** rather than on individual instances.

They are defined using the **@classmethod** decorator and take `cls` as
their first parameter instead of `self`.

- `self` → refers to the instance of the class.
- `cls`  → refers to the class itself.
"""

# ------------------------------------------------
# 1️⃣ Defining and Using Class Methods
# ------------------------------------------------

class Student:
    school_name = "ABC High School"   # Class variable

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @classmethod
    def get_school_name(cls):
        """Returns the name of the school (class-level data)."""
        return cls.school_name


# Usage
print(Student.get_school_name())  # Output: ABC High School

s1 = Student("Hamna", 95)
print(s1.get_school_name())       # Also valid: Output: ABC High School


# ------------------------------------------------
# 2️⃣ Modifying Class Variables using Class Methods
# ------------------------------------------------
# Class methods can be used to change class-level variables.

class Employee:
    company_name = "TechCorp"

    def __init__(self, name, role):
        self.name = name
        self.role = role

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name
        print(f"Company name changed to: {cls.company_name}")

# Usage
Employee.change_company("AI Innovations")
print(Employee.company_name)  # Output: AI Innovations


# ------------------------------------------------
# 3️⃣ Alternative Constructors using Class Methods
# ------------------------------------------------
# Class methods can also act as **alternative constructors**, providing
# different ways to create objects.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        """Alternative constructor to create Person using birth year."""
        from datetime import datetime
        current_year = datetime.now().year
        age = current_year - birth_year
        return cls(name, age)

# Usage
p1 = Person("Ali", 25)
p2 = Person.from_birth_year("Sara", 2000)

print(p1.name, p1.age)   # Output: Ali 25
print(p2.name, p2.age)   # Output: Sara 25 (if current year = 2025)


# ------------------------------------------------
# 4️⃣ Calling Class Methods
# ------------------------------------------------
# Class methods can be called using either:
# - The class name → preferred way
# - The instance name → also works

Employee.change_company("CodeLab")  # Using class name
emp = Employee("Hamza", "Developer")
emp.change_company("SmartSoft")     # Using instance (less common)


# ------------------------------------------------
# 5️⃣ Key Points
# ------------------------------------------------
# - Defined using the @classmethod decorator.
# - First parameter is always `cls` (refers to the class).
# - Can access and modify class variables.
# - Useful for creating factory/alternative constructors.
# - Can be called via class name or instance.


# ================================================
# Summary:
# Class methods → Operate on class-level data, not on individual instances.
# ================================================
