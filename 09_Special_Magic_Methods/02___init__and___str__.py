# ================================================================
# File: 02___init__and___str__.py
# Topic: The __init__() and __str__() Dunder Methods in Python
# ================================================================

"""
In Python, **__init__** and **__str__** are two of the most commonly used 
**dunder (magic) methods** in Object-Oriented Programming.

These methods play an essential role in how objects are **created** and **represented**.
"""

# ------------------------------------------------
# 1️⃣ The __init__() Method
# ------------------------------------------------
"""
Definition:
------------
The **__init__()** method is automatically called when a new object of a class is created.
It is known as the **constructor** in Python.

Purpose:
---------
- Used to initialize the object's attributes.
- Sets up the object’s initial state.
- Automatically executed after the object is created.

Syntax:
--------
    def __init__(self, parameters):
        # initialization code
"""

# Example 1: Basic use of __init__()

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print(f"Student {self.name} created successfully!")

# Object creation automatically calls __init__()
s1 = Student("Hamna", 95)
s2 = Student("Ali", 88)

# Output:
# Student Hamna created successfully!
# Student Ali created successfully!


# ------------------------------------------------
# 2️⃣ Using __init__() to Set Instance Variables
# ------------------------------------------------
"""
Every time an object is created, __init__() initializes its attributes.
These attributes are unique to each object.
"""

class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

# Creating multiple objects
emp1 = Employee("Sara", 60000, "Manager")
emp2 = Employee("Zain", 45000, "Developer")

print(emp1.name, emp1.salary, emp1.position)
print(emp2.name, emp2.salary, emp2.position)

# Output:
# Sara 60000 Manager
# Zain 45000 Developer


# ------------------------------------------------
# 3️⃣ The __str__() Method
# ------------------------------------------------
"""
Definition:
------------
The **__str__()** method defines the **string representation** of an object.
It is automatically called when we use `print()` or `str()` on an object.

Purpose:
---------
- Provides a human-readable description of the object.
- Improves the output readability instead of showing memory addresses.

Without __str__():
------------------
By default, printing an object displays something like:
<__main__.ClassName object at 0x000001B5D8A8E7F0>
"""

# Example 2: Without __str__()

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Corolla")
print(car1)
# Output (default): <__main__.Car object at 0x0000023E6A7B4D90>


# Example 3: With __str__()

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"Car(Brand: {self.brand}, Model: {self.model})"

car2 = Car("Honda", "Civic")
print(car2)
# Output: Car(Brand: Honda, Model: Civic)


# ------------------------------------------------
# 4️⃣ Combining __init__() and __str__() in One Class
# ------------------------------------------------
"""
Both methods are often used together:
- __init__() initializes the object.
- __str__() defines its readable representation.
"""

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"

book1 = Book("Python Programming", "John Doe", 500)
book2 = Book("Object-Oriented Design", "Alice Smith", 320)

print(book1)
print(book2)

# Output:
# 'Python Programming' by John Doe, 500 pages
# 'Object-Oriented Design' by Alice Smith, 320 pages


# ------------------------------------------------
# 5️⃣ Difference Between __str__() and __repr__()
# ------------------------------------------------
"""
Although both return string representations, they serve different purposes:

- __str__()  → For *end users* (readable, friendly output).
- __repr__() → For *developers* (debugging, unambiguous representation).

If __str__() is not defined, Python automatically uses __repr__() instead.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

book3 = Book("Clean Code", "Robert Martin")
print(book3)  # Uses __repr__ if __str__ is not defined
# Output: Book('Clean Code', 'Robert Martin')


# ------------------------------------------------
# 6️⃣ Key Points
# ------------------------------------------------
"""
✅ __init__() initializes the object's data when it is created.
✅ __str__() defines what should be shown when printing the object.
✅ Together, they make your class more readable and user-friendly.
✅ If __str__() is not defined, Python falls back to __repr__().
✅ Both are automatically invoked by Python.
"""


# ================================================================
# Summary:
# - __init__() → Constructor: Initializes object attributes.
# - __str__()  → String representation: Defines human-readable output.
# These two methods improve code readability and maintainability.
# ================================================================
